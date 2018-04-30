from sqlalchemy import orm
from sqlalchemy import create_engine
from wallet.entity.wallet_entity import WalletEntity
from sqlalchemy.orm import mapper
from sqlalchemy import Table, MetaData, Column , String
import os


class WalletService:

    def __init__(self):
        self._engine = create_engine('mysql+pymysql://%s:%s@%s/wallet' %(os.environ['DB_USERNAME'],os.environ['DB_PASSWORD'],os.environ['DB_ENDPOINT_ADDRESS']))
        self._session = orm.Session(bind=self._engine)
        wallet = Table('wallet', MetaData(),
                       Column('uuid', String, primary_key=True),
                       Column('user_id')
                       )
        mapper(WalletEntity, wallet)

    def list(self):
        return self._session.query(WalletEntity).all()

    def create(self, wallet_entity):
        self._session.add(wallet_entity)
        self._session.commit()
        return wallet_entity

