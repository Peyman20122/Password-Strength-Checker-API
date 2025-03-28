# Password Strength Checker API

This project is a simple API built using **FastAPI** to check the strength of passwords and provide suggestions for stronger alternatives. The tool helps users assess the security of their passwords and encourages them to improve weak passwords by suggesting stronger ones.

## Features

- **Password Strength Check**: The input password is evaluated for length, the presence of numbers, uppercase letters, and special characters to determine its strength.
- **Strong Password Suggestion**: If the input password is weak, a strong random password is suggested.
- **SHA256 Hashing**: Passwords are hashed using **SHA256**, and it checks whether the input password matches any known weak passwords.

## Setup Instructions

### Prerequisites

1. Python 3.8 or higher
2. FastAPI
3. Uvicorn for running the server

### Install Dependencies

To install the required dependencies, first activate the virtual environment (if needed) and install the necessary packages:

```bash
# Create a virtual environment (if needed)
python -m venv venv
# Activate the virtual environment
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate  # For Windows

# Install the dependencies
pip install fastapi uvicorn
```

### Run the Server

Once the dependencies are installed, you can run the server using `uvicorn`:

```bash
uvicorn main:app --reload
```

After running the above command, the server will start and be available at `http://127.0.0.1:8000`.

### Usage

The API provides a single endpoint:

#### `GET /check-password/{password}`

This endpoint checks the strength of the provided password. It returns the strength level of the password, a suggested strong password, and a message with further instructions.

**Example request:**

```bash
GET http://127.0.0.1:8000/check-password/your_password_here
```

**Example response:**

```json
{
  "password": "your_password_here",
  "strength": "Weak",
  "suggested_password": "RandomStrongPassword123!",
  "message": "This password is weak and commonly used. Please choose a stronger one."
}
```

## Contributing

Feel free to fork the repository, create a branch, and submit pull requests for improvements. If you find any bugs or have suggestions, please open an issue.

## License

This project is open-source and available under the [MIT License](LICENSE).
