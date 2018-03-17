from wallet import WalletEntity
import json

def handle(event, context):

    wallet = WalletEntity

    payload = {
        "uuid" : str(wallet.uuid)
    }

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.JSONEncoder().encode(payload)
    }
