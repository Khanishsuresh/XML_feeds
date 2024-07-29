# XML Feeds


## Features

- Manage Employers and Jobs using Django models.
- Generate XML feeds dynamically for different job boards.
- Serve the generated XML files via HTTP endpoints.

## Requirements

- Python 3.x
- Django 3.x or higher

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/Khanishsuresh/XML_feeds.git
    cd XML_feeds
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the database:**

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser to access the Django admin interface:**

    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

## Usage

### Adding Employers and Jobs

1. Access the Django admin interface at `http://127.0.0.1:8000/admin`.
2. Add `Employer` and `Job` entries.

### Generating and Accessing XML Feeds

#### ZipRecruiter

- **Generate XML Feed:**
  
  Visit `http://127.0.0.1:8000/jobs/ziprecruiter_generate/` to generate the XML feed for ZipRecruiter.

- **Access XML Feed:**
  
  Visit `http://127.0.0.1:8000/jobs/ziprecruiter_feed/` to access the generated XML feed.

#### JobRapido

- **Generate XML Feed:**
  
  Visit `http://127.0.0.1:8000/jobs/jobrapido_generate/` to generate the XML feed for JobRapido.

- **Access XML Feed:**
  
  Visit `http://127.0.0.1:8000/jobs/jobrapido_feed/` to access the generated XML feed.

