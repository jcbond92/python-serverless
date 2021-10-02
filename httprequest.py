import requests

# API: https://dukengn.github.io/Dog-facts-API/


def handler(event, context):

    r = requests.get(
        "https://dog-facts-api.herokuapp.com/api/v1/resources/dogs?number=3")

    response = {
        "statusCode": 200,
        "body": r.json()
    }

    return response
