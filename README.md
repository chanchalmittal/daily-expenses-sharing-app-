# Daily Expenses Sharing Application

## Overview

The Daily Expenses Sharing Application is a backend service designed to help users manage their daily expenses efficiently. It allows users to add expenses and split them among participants using three different methods: equal splits, exact amounts, and percentage-based splits. The application also generates downloadable balance sheets for easy expense tracking.

## Features

- **User Management**: 
  - Create user accounts with email, name, and mobile number.
  - Retrieve user details.

- **Expense Management**:
  - Add expenses with various splitting methods:
    - **Equal Split**: Split expenses equally among all participants.
    - **Exact Amount**: Specify the exact amount each participant owes.
    - **Percentage Split**: Specify the percentage each participant owes (percentages must total 100%).

- **Balance Sheet Generation**:
  - View individual and overall expenses.
  - Download balance sheets in a user-friendly format.

## Technologies Used

- Python
- FastAPI
- SQLAlchemy
- SQLite (or any other database of your choice)
- Pydantic
- Uvicorn

## Installations

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/chanchalmittal/daily-expenses-app.git
    cd daily-expenses-app
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment**:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Run the Application**:
    ```bash
    uvicorn app.main:app --reload
    ```

6. **Access the API**:
    Open your browser and navigate to `http://127.0.0.1:8000/docs` to view the API documentation and test the endpoints.

## API Endpoints

### User Endpoints

- **Create User**: `POST /users/`
- **Retrieve User Details**: `GET /users/{user_id}`

### Expense Endpoints

- **Add Expense**: `POST /expenses/`
- **Retrieve Individual User Expenses**: `GET /expenses/user/{user_id}`
- **Retrieve Overall Expenses**: `GET /expenses/`
- **Download Balance Sheet**: `GET /expenses/balance-sheet/`

## Data Validation

The application validates user inputs and ensures that:
- Email format is correct.
- Mobile number is valid.
- Percentages in the percentage split method add up to 100%.

## Running Tests

To run tests, use:
```bash
pytest
```

License
-------

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Author
------

[Chanchal Mittal](https://github.com/chanchalmittal)
