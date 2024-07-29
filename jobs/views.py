import os
from django.conf import settings
from django.http import HttpResponse
from .models import Job
from datetime import datetime, timedelta
from django.shortcuts import render
from typing import List

def home(request):
    jobs = Job.objects.all()
    return render(request, 'job_list.html', {'jobs': jobs})

def generate_xml_for_ziprecruiter(jobs: List[Job]) -> str:
    xml = '<?xml version="1.0" encoding="UTF-8"?>'
    xml += '<source>'
    xml += '<publisher>untappped</publisher>'
    xml += '<publisherurl>http://www.untappped.com</publisherurl>'
    current_time = datetime.now().strftime('%Y-%m-%dT%H:%M:%S%z')
    xml += f'<last-build-date>{current_time}</last-build-date>'

    for job in jobs:
        xml += '<job>'
        xml += f'<title><![CDATA[{job.title}]]></title>'
        xml += f'<date><![CDATA[{job.postdate.strftime("%Y-%m-%d %H:%M:%S %z")}]]></date>'
        xml += f'<referencenumber><![CDATA[{job.jobid}]]></referencenumber>'
        xml += f'<url><![CDATA[https://untappped/singlejob/{job.jobid}]]></url>'
        xml += f'<company><![CDATA[{job.eid.companyname}]]></company>'
        xml += f'<city><![CDATA[{job.eid.city}]]></city>'
        xml += f'<state><![CDATA[{job.eid.location}]]></state>'
        xml += f'<country><![CDATA[{job.eid.location}]]></country>'
        xml += f'<postalcode><![CDATA[{job.eid.pincode}]]></postalcode>'
        xml += f'<salary><![CDATA[{job.basicpay}]]></salary>'
        xml += f'<email><![CDATA[{job.eid.email}]]></email>'
        xml += f'<description><![CDATA[{job.jobdesc}]]></description>'
        xml += f'<jobtype><![CDATA[{job.jobtype}]]></jobtype>'
        xml += '</job>'

    xml += '</source>'
    return xml

def generate_xml_for_jobrapido(jobs: List[Job]) -> str:
    xml = '<?xml version="1.0" encoding="UTF-8"?>'
    xml += '<source>'
    xml += '<jobs>'

    for job in jobs:
        xml += '<job>'
        xml += f'<title><![CDATA[{job.title}]]></title>'
        xml += f'<location><![CDATA[{job.eid.city}]]></location>'
        xml += f'<state><![CDATA[{job.eid.location}]]></state>'
        xml += f'<country><![CDATA[{job.eid.location}]]></country>'
        xml += f'<postalcode><![CDATA[{job.eid.pincode}]]></postalcode>'
        xml += f'<company><![CDATA[{job.eid.companyname}]]></company>'
        xml += f'<website><![CDATA[{job.eid.website}]]></website>'
        xml += f'<publishdate><![CDATA[{job.postdate.strftime("%d/%m/%Y")}]]></publishdate>'
        xml += f'<expirydate><![CDATA[{(job.postdate + timedelta(days=60)).strftime("%d/%m/%Y")}]]></expirydate>'
        xml += f'<url><![CDATA[https://untappped/singlejob/{job.jobid}]]></url>'
        xml += f'<email><![CDATA[{job.eid.email}]]></email>'
        xml += f'<description><![CDATA[{job.jobdesc}]]></description>'
        xml += f'<reference_id><![CDATA[{job.jobid}]]></reference_id>'
        xml += f'<salary><![CDATA[{job.basicpay}]]></salary>'
        xml += f'<education><![CDATA[Bachelors]]></education>'
        xml += f'<jobtype><![CDATA[{job.jobtype}]]></jobtype>'
        xml += f'<category><![CDATA[Category1]]></category>'
        xml += f'<experience><![CDATA[5+ years]]></experience>'
        xml += '</job>'

    xml += '</jobs>'
    xml += '</source>'
    return xml

def save_xml_to_file(xml: str, file_name: str):
    file_path = os.path.join(settings.MEDIA_ROOT, file_name)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(xml)

    return file_path

def ziprecruiter_generate(request):
    jobs: List[Job] = Job.objects.filter(eid__companyname='ZipRecruiter')  # Replace with actual company name
    xml = generate_xml_for_ziprecruiter(jobs)
    save_xml_to_file(xml, 'ziprecruiter.xml')
    return HttpResponse("ZipRecruiter XML generation has been completed.")

def ziprecruiter_feed(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'ziprecruiter.xml')

    if not os.path.isfile(file_path):
        return HttpResponse("File not found.", status=404)

    with open(file_path, 'r', encoding='utf-8') as f:
        xml = f.read()

    response = HttpResponse(xml.encode('utf-8'), content_type='application/xml')
    response['Content-Disposition'] = 'inline; filename="ziprecruiter.xml"'
    return response

def jobrapido_generate(request):
    jobs: List[Job] = Job.objects.filter(eid__companyname='JobRapido')  # Replace with actual company name
    xml = generate_xml_for_jobrapido(jobs)
    save_xml_to_file(xml, 'jobrapido.xml')
    return HttpResponse("JobRapido XML generation has been completed.")

def jobrapido_feed(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'jobrapido.xml')

    if not os.path.isfile(file_path):
        return HttpResponse("File not found.", status=404)

    with open(file_path, 'r', encoding='utf-8') as f:
        xml = f.read()

    response = HttpResponse(xml.encode('utf-8'), content_type='application/xml')
    response['Content-Disposition'] = 'inline; filename="jobrapido.xml"'
    return response
