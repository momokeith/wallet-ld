from wallet import WalletEntity
import json

def list(event, context):

    wallet = WalletEntity

    payload = {
        "uuid" : str(wallet.uuid)
    }

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.JSONEncoder().encode(payload)
    }

def create(event, context):
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.JSONEncoder().encode({ "Created" : 1})
    }
