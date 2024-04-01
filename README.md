# Email Sending API Endpoint Documentation

This documentation provides detailed instructions on how to set up and use the Email Sending API Endpoint in your Django project. The API endpoint allows you to send emails using the Mailgun API service.

## Requirements

Before setting up the Email Sending API Endpoint, ensure you have the following prerequisites:

- Python (3.8 or higher)
- Django (3.2 or higher)
- Docker (for deployment)
- Mailgun account with API key and server name

## Installation

1. Clone the repository containing your Django project.

   ```bash
   git clone https://github.com/YounoussaBen/EmailAPI.git
   ```

2. Navigate to the project directory.

   ```bash
   cd EmailAPI
   ```

3. Install the project dependencies using pip.

   ```bash
   pip install -r requirements.txt
   ```

4. Create a copy of the `.env.example` file and name it `.env`.

   ```bash
   cp .env.example .env
   ```

5. Fill in the required environment variables in the `.env` file. Replace placeholders with appropriate values for your environment.

## Configuration

### Development Environment

For local development, ensure the following settings are configured:

- **`DEV_SECRET_KEY`**: Secret key for Django.
- **`DEV_ALLOWED_HOSTS`**: Comma-separated list of allowed hosts for development.

### Production Environment

For production deployment, configure the following settings:

- **`PROD_SECRET_KEY`**: Secret key for Django.
- **`PROD_ALLOWED_HOSTS`**: Domain name(s) for your production environment.

### Database Settings

Depending on your environment, configure the following database settings:

#### Development (SQLite)

- **`DB_ENGINE`**: Set to `django.db.backends.sqlite3`.
- No additional database configuration needed.

#### Production (PostgreSQL)

- **`DB_ENGINE`**: Set to `postgresql`.
- **`DB_NAME`**: Name of the PostgreSQL database.
- **`DB_USER`**: Username for the PostgreSQL database.
- **`DB_PASSWORD`**: Password for the PostgreSQL database.
- **`DB_HOST`**: Hostname for the PostgreSQL database server.
- **`DB_PORT`**: Port number for the PostgreSQL database server.

## Running the Application

### Local Development

To run the Django project locally, use the following command:

```bash
python manage.py runserver
```

The development server will start, and you can access the Email Sending API Endpoint at `http://localhost:8000/send-email/`.

### Production Deployment with Docker

To deploy the Django project in a production environment using Docker, follow these steps:

1. Build the Docker image:

   ```bash
   docker-compose build
   ```

2. Run the Docker containers:

   ```bash
   docker-compose up -d
   ```

The Django application will be accessible on port 7000. You can access the Email Sending API Endpoint at `http://localhost:7000/send-email/`.

## API Usage

To use the Email Sending API Endpoint, send a POST request to `/send-email/` with the following parameters:

- `from`: Sender's email address.
- `to`: List of recipient email addresses.
- `subject`: Email subject.
- `text`: Email body text.
- `attachments`: List of attachments (optional).

### Example Request

```json
{
  "from": "sender@example.com",
  "to": ["recipient1@example.com", "recipient2@example.com"],
  "subject": "Test Email",
  "text": "This is a test email sent using the Email Sending API Endpoint.",
  "attachments": [
    {
      "filename": "example.pdf",
      "content": "<base64_encoded_content>"
    }
  ]
}
```

Replace `<base64_encoded_content>` with the Base64-encoded content of the attachment file.

### Example Response

```json
{
  "message": "Email sent successfully"
}
```

If an error occurs during email sending, an appropriate error message will be returned along with the corresponding status code.

## Conclusion

This concludes the documentation for the Email Sending API Endpoint. Follow the provided instructions to set up, configure, and use the API endpoint in your Django project. If you encounter any issues or have questions, please refer to the project's documentation or reach out to the project maintainers for assistance.