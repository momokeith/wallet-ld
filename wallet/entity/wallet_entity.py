import uuid
import json

class WalletEntity(object):

    def __init__(self, user_id = None , uuid = str(uuid.uuid4()) ):
        self.uuid = uuid
        self.user_id = user_id


class JsonEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, WalletEntity):
            return self.encode_entity(o)
        else:
            if isinstance(o,list):
                wallets = []
                for wallet in o:
                    wallets.append(self.encode_entity(wallet))
                return wallets

    def encode_entity(self, wallet):
        return {
            'uuid': wallet.uuid,
            'user_id': wallet.user_id
        }