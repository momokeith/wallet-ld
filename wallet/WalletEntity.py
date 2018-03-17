import uuid

class WalletEntity:

    def __init__(self):
        self.uuid = uuid.uuid4()

    @property
    def uuid(self):
        return self.uuid

    @uuid.setter
    def uuid(self, uuid):
        self.uuid = uuid