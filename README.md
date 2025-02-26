# SQLAlchemy ORM Project
This project demonstrates the use of SQLAlchemy ORM for database interactions in a Python application.


## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Database Configuration](#database-configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)


## Introduction
This project implements a basic authentication system (registration and login) using SQLAlchemy ORM to interact with a MySQL database. It demonstrates how to create data models, perform database operations, and manage user sessions securely, with password encryption using SHA256.



## Installation
To install the necessary dependencies, run the following command:
```bash
pip install -r requirements.txt
```


## Database Configuration
1.  Create a `.env` file in the project's root directory.
2.  Populate the environment variables with your MySQL database credentials:

    ```
    USER=your_mysql_username
    PASSWORD=your_mysql_password
    HOST=your_mysql_host
    PORT=3306
    DB=your_mysql_database
    ```

    * Replace `your_mysql_username`, `your_mysql_password`, `your_mysql_host`, and `your_mysql_database` with your actual MySQL connection details.
    * The default MySQL port is 3306, but it may vary in your setup.
3.  Ensure that the `.env` file is listed in your `.gitignore` to prevent exposing your credentials.


## Usage
To run the application, use the following command:
```bash
python main.py
```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.