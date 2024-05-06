# Vendor Management System

## Overview

The Vendor Management System is a comprehensive application designed to facilitate vendor management. The system allows you to handle vendor performance, purchase orders, and other crucial data through a set of RESTful APIs.

## Installation & Run Tests

Follow these steps to install and set up the Vendor Management System:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/naveens800/vendor_management_system.git
2. **Navigate to the Project Directory:Enter the project directory to proceed with further steps.**
    ```bash
    cd vendor_management_system

3. **Create a virtual environment to keep your dependencies isolated.**
    ```bash
    python3 -m venv <env_name>

4. **Activate the virtual environment using the command below:**

 > Linux/macOS:
     > source <env_name>/bin/activate

> Windows:
    > <env_name>\Scripts\activate

6. Once the virtual environment is activated, install the required dependencies.
    ```bash
      pip install -r requirements.txt

7. Apply the migrations to set up the necessary database tables.
    ```bash
    python manage.py migrate
8. Verify the functionality by running tests. You have two options:
  Standard Test Execution:
   ```bash
   python manage.py test #python manage.py test --parallel
      
9. Load sample data to populate the application with predefined information.
    ```bash
    python manage.py load_data sample_data.json
11. Finally, start the Django development server to begin using the application.
    ```bash
    python manage.py runserver


## Refer [DOCS.md](.DOCS.md) for API Documentation
  ### Use any api testing tool like postman/insomnia to run apis
