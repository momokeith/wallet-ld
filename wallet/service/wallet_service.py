from sqlalchemy import orm
from sqlalchemy import create_engine
from wallet.entity.wallet_entity import WalletEntity
from sqlalchemy.orm import mapper
from sqlalchemy import Table, MetaData, Column , String


class WalletService:

    def __init__(self):
        self._engine = create_engine('mysql+pymysql://naman2kmn:M0mo1986@db1.csx6zvsxgs36.eu-west-1.rds.amazonaws.com:3306/wallet')
        self._session = orm.Session(bind=self._engine)
        wallet = Table('wallet', MetaData(),
                       Column('uuid', String, primary_key=True)
                       )
        mapper(WalletEntity, wallet)

    def list(self):
        return self._session.query(WalletEntity).all()

    def create(self, wallet_entity):
        self._session.add(wallet_entity)
        return self._session.commit()

