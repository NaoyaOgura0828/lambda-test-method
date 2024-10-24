import json


def create_response_body(event):
    """
    Creates a response body containing information from the incoming event.

    Args:
        event (dict): The event dictionary containing API Gateway request data.

    Returns:
        dict: A dictionary containing the path, HTTP method, and body of the request.
        If any of these keys are missing, default values are provided ('N/A' for path and method,
        and 'No body' for the body).
    """
    path = event.get('path', 'N/A')
    method = event.get('httpMethod', 'N/A')
    body = event.get('body', 'No body')

    response_body = {
        'path': path,
        'method': method,
        'body': body
    }

    return response_body


def lambda_handler(event, context):
    """
    AWS Lambda function handler that processes API Gateway events and returns a response.

    Args:
        event (dict): The event dictionary containing API Gateway request data.
        context (object): The context in which the Lambda function is called (unused in this case).

    Returns:
        dict: A dictionary representing the HTTP response. It contains the status code
        and a JSON-encoded body with either the extracted request details or an error message
        if an exception occurs during processing.
    """
    try:
        response_body = create_response_body(event)
        status_code = 200
    except Exception as error:
        response_body = {'error': str(error)}
        status_code = 500

    return {
        'statusCode': status_code,
        'body': json.dumps(response_body)
    }
