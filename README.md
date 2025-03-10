# Flask Text Summarization Web App using BART

This web application allows users to input text, which is then summarized using the BART (Bidirectional and Auto-Regressive Transformers) model. The app runs on Docker with Gunicorn as the server for production-ready performance.

## Features

- **Text Summarization**: Input text is processed and summarized using the BART model.
- **Simple User Interface**: A clean, chat-like interface for users to interact with the app.
- **Dockerized Environment**: The application runs in a containerized environment using Docker for easy deployment.
- **Gunicorn Server**: Production-grade server using Gunicorn for efficient request handling.

## Technologies Used

- **Flask**: A lightweight WSGI web framework for Python to build the backend.
- **BART Model**: A transformer model for abstractive text summarization.
- **Docker**: Containerization for easy deployment and scaling.
- **Gunicorn**: A WSGI HTTP server for running the Flask app in production.
- **Jinja2**: Templating engine used for rendering HTML pages.

## Setup Instructions

### Prerequisites

- Docker installed on your machine.
- Python 3.9+ installed.

### Clone the Repository

```bash
git clone https://github.com/BencivenniFilippo/AI-Summarizer-Web-App.git
cd AI-Summarizer-Web-App