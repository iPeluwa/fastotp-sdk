# FastOtp

The FastOTP Wrapper SDK is designed to simplify the integration and usage of the FastOTP service in Python applications. FastOTP is a service that provides functionality for generating, validating, and delivering One-Time Passwords (OTPs) through various channels.

## Purpose

The purpose of PyResponse is to simplify the process of generating success and error responses in web applications. It provides two main functions, `create_success_response()` and `create_error_response()`, which can be used to generate standardized response structures.

## Installation

To install PyResponse, you can use pip:

```bash
pip install fastotp
```

## Usage

Fastotp can be used with different web frameworks, including Django, FastAPI, and Flask. Here's how you can use Fastotp in each framework:

### # Example usage

```python
from fastotp_sdk.client import FastOTPClient, TokenType
```

## Initialize FastOTP client

```python
api_key = "your_api_key"
fastotp_sdk = FastOTPClient(api_key)
```

## Generate OTP

```python
generated_otp = fastotp_sdk.generate_otp(token_type=TokenType.NUMERIC, token_length=6, validity=10)
print("Generated OTP:", generated_otp)
```

## Validate OTP

```python
validation_result = fastotp_sdk.validate_otp(identifier="example_identifier", token="123456")
print("Validation Result:", validation_result)
```

## Get OTP Details

```python
otp_details = fastotp_sdk.get_otp_details(otp_id="123")
print("OTP Details:", otp_details)
```

### Vanilla Python

```python
from pyresponse.response import create_success_response, create_error_response


def main():
    # Example usage of PyResponse
    name = input("Enter your name: ")
    age = input("Enter your age: ")

    try:
        age = int(age)
        if age >= 18:
            message = "Success"
            data = {'name': name, 'age': age}
            success_response = create_success_response(
                data=data, message=message, status_code=200)
            print(success_response.data)  # Access the response data
            # Access the response status code
            print(success_response.status_code)
        else:
            message = "Error: Age must be 18 or older."
            error_response = create_error_response(
                message=message, status_code=400)
            print(error_response.data)  # Access the response data
            # Access the response status code
            print(error_response.status_code)

    except ValueError:
        message = "Error: Invalid age entered."
        error_response = create_error_response(
            message=message, status_code=400)
        print(error_response.data)  # Access the response data
        print(error_response.status_code)  # Access the response status code


if __name__ == '__main__':
    main()

```

### Django

1. Install PyResponse using pip as shown in the installation section.
2. Import the necessary functions from PyResponse in your Django views or API handlers.
3. Use the `create_success_response()` and `create_error_response()` functions to generate the desired responses.

```python
# In your views or models
from fastotp_sdk.client import FastOTPClient, TokenType

api_key = "your_api_key"
fastotp_sdk = FastOTPClient(api_key)

# Generate OTP
generated_otp = fastotp_sdk.generate_otp(token_type=TokenType.NUMERIC, token_length=6, validity=10)

# Use generated_otp as needed in your Django application

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
