import encrypt
import decrypt
import json

def lambda_handler(event, context):
    # TODO implement
    print("Hello from Lambda")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!' + event[''])
    }