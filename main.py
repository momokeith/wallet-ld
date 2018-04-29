from wallet.entity.wallet_entity import WalletEntity
from wallet.entity.wallet_entity import JsonEncoder
from wallet.service.wallet_service import WalletService
import json

wallet_service = WalletService()

def list(event, context):

    wallets = wallet_service.list()

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(wallets,cls=JsonEncoder)
    }


def create(event, context):

    request_body = json.JSONDecoder().decode(event['body'])
    wallet = WalletEntity(request_body['user_id'])
    wallet = wallet_service.create(wallet)

    return {
        "statusCode": 201,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(wallet,cls=JsonEncoder)
    }

def delete(event, context):
    try:
        wallet = wallet_service.delete(event['pathParameters']['uuid'])
        return {
            "statusCode": 202,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(wallet, cls=JsonEncoder)
        }
    except Exception as e:
        return {
            "statusCode": 404,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({
                "message": "{0}".format(e)

            })
        }


