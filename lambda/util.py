import json


def verify_field(field: str, json_body):
    if field in json_body:
        return json.loads(json_body[field])

    return {
        'statusCode': 400,
        'body': json.dumps(f"Invalid request. Please provide a ${field}.")
    }
