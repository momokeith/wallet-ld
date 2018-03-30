from sqlalchemy import Table, MetaData, Column , String

wallet = Table( 'wallet',MetaData(),
                Column('uuid',String,primary_key=True)
)