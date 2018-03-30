from wallet.entity.wallet_entity import WalletEntity
import json
from wallet.service.wallet_service import WalletService
import pickle

wallet_service = WalletService()

def list(event, context):

    wallets = wallet_service.list()

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": pickle.dumps(WalletEntity())
    }

def create(event, context):

    wallet = WalletEntity()
    response = wallet_service.create(wallet)

    print(response)

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.JSONEncoder().encode({ "Created" : response})
    }
