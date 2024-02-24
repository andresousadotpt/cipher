import cipher
import util
import json


def lambda_handler(event, context):
    action = event['queryStringParameters']['action']

    if action == 'encrypt':
        body = util.verify_field("body", event)
        if body.get("statusCode") == 400:
            return body

        encrypted = cipher.encrypt(body["secret_key"].encode(), body["data"].encode())
        return {
            'statusCode': 200,
            'body': json.dumps({'message': encrypted})
        }
    elif action == 'decrypt':
        body = util.verify_field("body", event)
        if body.get("statusCode") == 400:
            return body

        try:
            decrypted = cipher.decrypt(body["secret_key"].encode(), body["data"].encode())
            return {
                'statusCode': 200,
                'body': json.dumps({'message': decrypted.decode()})
            }
        except Exception:
            return {
                'statusCode': 400,
                'body': json.dumps("An error occurred during decryption. Please check your input.")
            }
    elif action == 'hello':
        return {
            'statusCode': 400,
            'body': json.dumps("Hello this is in good condition :)")
        }
    else:
        return {
            'statusCode': 200,
            'body': json.dumps("Invalid action. Please use 'encrypt' or 'decrypt' as action. " + event)
        }