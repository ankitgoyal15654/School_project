import json


def get_response(message='operation successful', data="No data found", code=200, success=True, error_path="no error"):
    """
       for sending response along with status codes in case of success
    """
    response = dict(data=data, code=code, success=success,
                    message=message, error_path=error_path)
    return response


def raise_exception(message='some problem occured', data="NA", code=500, success=False, error_path="not defined"):
    """
       for sending response along with status codes in case of failure
    """
    response = {
        "code": code,
        "message": message,
        "data": data,
        "success": success,
        "error_path": error_path
    }
    error = json.dumps(response)
    raise Exception(error)
