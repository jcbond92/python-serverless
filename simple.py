import json


def handler(event, context):
    body = {
        "message": "This response is from a serverless python function. Hello!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
