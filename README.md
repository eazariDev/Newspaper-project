# Newspaper Project

## Description

The Newspaper Project is a Django-based platform designed for news aggregation. This project serves as a basic foundation for building scalable news aggregation applications, with a focus on simplicity and scalability. It leverages Django's built-in tools for user authentication and article management.
This platform is ideal for developers who wish to build a news portal or integrate it as a news management backend in other projects.

## Core Features

- **Article Management**: Create, read, update, and delete news articles.
- **User Authentication**: Secure user registration and login system.
- **Responsive Design**: Built with Bootstrap.

## Project Structure

The project’s structure is as follows:

```bash
Newspaper-project/
├── accounts/                # User authentication views and models
├── articles/                # Models and views for managing articles
├── django_project/          # Core Django project settings and configurations
├── pages/                   # Static pages like home, about, and contact
├── static/                  # Static files (CSS, JavaScript, images)
├── templates/               # HTML templates for rendering views
├── manage.py                # Django project management utility
├── requirements.txt         # Python dependencies
└── Procfile                 # Deployment instructions for Heroku
```

## Key Techniques Used
1. Django Framework: The project leverages Django to manage routing, views, and user authentication. Django's MVT (Model-View-Template) architecture helps separate concerns and scale the application effectively.

2. Django Authentication: User authentication is handled using Django's built-in authentication system. This allows for secure user login, registration, and session management. More details on Django's authentication system can be found in the official documentation.

3. Bootstrap: Bootstrap is used to ensure the website is responsive and works well on mobile devices by default. It provides a robust grid system, UI components, and utility classes.

4. Static and Media Management: Django is configured to serve static files (like CSS and JavaScript) and media files (like images and documents) in an efficient manner. This is essential for projects that involve large amounts of dynamic content.

6. Gunicorn: In production environments, this project uses Gunicorn as the WSGI HTTP server to serve the Django application, providing better performance and scalability.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/eazariDev/Newspaper-project.git
   cd Newspaper-project 
    ```
2. Set Up a Virtual Environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3. Install Dependencies:
   ```bash
   pip install -r requirements.txt 
    ```
4. Apply Migrations:
   ```bash
   python manage.py migrate
    ```
5. Run the Development Server:
   ```bash
   python manage.py runserver
    ```

After completing these steps, you can access the application at http://127.0.0.1:8000/ and the admin panel at http://127.0.0.1:8000/admin/ .

## Contributing
Feel free to contribute to the development of this project. Whether you're improving functionality, adding new features, or fixing bugs, your input is welcome.

If you encounter issues, please open an issue on the GitHub issue tracker. Clearly describe the problem and provide any relevant examples.
