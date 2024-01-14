# Study Connect - Django Project Readme

## Overview

Welcome to Study Connect, a Django project designed to facilitate collaboration among students by providing a platform for connecting in rooms and discussing specific topics. This readme file will guide you through the setup process and provide an overview of the project structure.

## Features

- **Room Creation:** Users can create virtual rooms dedicated to specific topics or subjects.
- **Joining Rooms:** Students can join existing rooms to participate in discussions.
- **Discussion Threads:** Each room has discussion threads for users to post questions, share resources, and engage in conversations.
- **User Authentication:** Secure user authentication system to ensure that only registered users can create and join rooms.

## Getting Started

Follow these steps to set up the Study Connect project on your local machine:

### Prerequisites

- Python (3.6 or higher)
- Django
- Pipenv (optional but recommended)

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Syriamme/StudyConnect.git
   ```

2. Change into the project directory:

   ```bash
   cd study-connect
   ```

3. Create a virtual environment (using Pipenv):

   ```bash
   pipenv install
   ```

   Activate the virtual environment:

   ```bash
   pipenv shell
   ```

4. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

6. Create a superuser account:

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to create a superuser account, which you can use to log in and manage the Django admin interface.

7. Run the development server:

   ```bash
   python manage.py runserver
   ```

   The development server will be available at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

8. Access the admin interface:

   Visit [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) and log in with the superuser credentials you created earlier.

## Project Structure

The project structure follows Django conventions. Here are some key directories and files:

- **studyconnect/:** The main project directory containing settings, URLs, and other configurations.
- **rooms/:** The app responsible for handling room-related functionality.
- **templates/:** HTML templates for rendering views.
- **static/:** Static files such as stylesheets, JavaScript, and images.
- **media/:** Uploads and user-generated content.
- **requirements.txt:** Project dependencies.

## Contributing

If you'd like to contribute to Study Connect, please follow the [contribution guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Thanks to the Django community for providing an excellent web framework.
- Inspiration for Study Connect came from the need for an online platform to facilitate student collaboration.

Feel free to reach out if you have any questions or encounter issues! Happy studying!