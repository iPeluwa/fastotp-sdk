import requests
from enums import TokenType

class FastOTPClient:
    """
    A client for interacting with the FastOTP service.

    Parameters:
    - api_key (str): Your API key for authenticating requests.
    """

    def __init__(self, api_key):
        """
        Initialize the FastOTPClient.

        Args:
        - api_key (str): Your API key for authenticating requests.
        """
        self.base_url = "https://api.fastotp.co"
        self.headers = {
            "x-api-key": api_key,
            "Content-Type": "application/json"
        }

    def generate_otp(self, token_type=TokenType.NUMERIC, token_length=4, validity=5, delivery=None, identifier=None):
        """
        Generate a One-Time Password (OTP) using the FastOTP service.

        Args:
        - token_type (TokenType): Type of OTP to generate. Defaults to TokenType.NUMERIC.
        - token_length (int): Length of the generated OTP. Default is 4.
        - validity (int): Validity period of the OTP in minutes. Default is 5 minutes.
        - delivery (dict): Delivery options for the OTP.
        - identifier (str): Unique identifier tied to the token.

        Returns:
        - dict: The generated OTP details.
        """
        url = f"{self.base_url}/generate"
        payload = {
            "type": token_type.value,
            "token_length": token_length,
            "validity": validity,
            "delivery": delivery,
            "identifier": identifier
        }

        response = self._make_request("POST", url, payload)
        return self._handle_response(response)

    def validate_otp(self, identifier, token):
        """
        Validate a One-Time Password (OTP) using the FastOTP service.

        Args:
        - identifier (str): Unique identifier tied to the token.
        - token (str): The OTP to validate.

        Returns:
        - dict: The validation result.
        """
        url = f"{self.base_url}/validate"
        payload = {
            "identifier": identifier,
            "token": token
        }

        response = self._make_request("POST", url, payload)
        return self._handle_response(response)

    def get_otp_details(self, otp_id):
        """
        Get details of a generated One-Time Password (OTP) using its ID.

        Args:
        - otp_id (str): The ID of the OTP.

        Returns:
        - dict: The OTP details.
        """
        url = f"{self.base_url}/{otp_id}"
        response = self._make_request("GET", url)
        return self._handle_response(response)

    def _make_request(self, method, url, data=None):
        """
        Make an HTTP request to the FastOTP API.

        Args:
        - method (str): HTTP method (e.g., "POST", "GET").
        - url (str): The URL for the API endpoint.
        - data (dict): The payload for the request.

        Returns:
        - requests.Response: The HTTP response.
        """
        try:
            response = requests.request(method, url, json=data, headers=self.headers)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            print(f"Error making {method} request to {url}: {e}")
            raise

    def _handle_response(self, response):
        """
        Handle the HTTP response from the FastOTP API.

        Args:
        - response (requests.Response): The HTTP response.

        Returns:
        - dict: The JSON content of the response.
        """
        try:
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error handling response: {e}")
            raise
