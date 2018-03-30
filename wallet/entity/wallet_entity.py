import uuid

class WalletEntity:

    def __init__(self):
        self.uuid = str(uuid.uuid4())

    # @property
    # def uuid(self):
    #     return self._uuid
    #
    # @uuid.setter
    # def uuid(self, uuid):
    #     self._uuid = uuid