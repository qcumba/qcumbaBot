from sqlalchemy import Table, Column, Integer, String, ForeignKey
from Connector import connect


def create_tables(con, meta):
    orgs_common = Table('orgs_common', meta,
                        Column('id', String, primary_key=True),
                        Column('group_id', String),
                        Column('position', Integer),
                        Column('name', String),
                        Column('requisites', String, ForeignKey('requisites.id')),
                        Column('management', String, ForeignKey('managements.id')),
                        Column('state', String, ForeignKey('states.id')),
                        Column('address', String, ForeignKey('addresses.id'))
                        )
    requisites = Table('requisites', meta,
                       Column('id', String, primary_key=True),
                       Column('inn', String),
                       Column('ogrn', String),
                       Column('opf', String),
                       Column('kpp', String)
                       )
    managements = Table('managements', meta,
                        Column('id', String, primary_key=True),
                        Column('name', String),
                        Column('post', String)
                        )
    states = Table('states', meta,
                   Column('id', String, primary_key=True),
                   Column('status', String),
                   Column('registration_date', String),
                   Column('liquidation_date', String)
                   )
    addresses = Table('addresses', meta,
                      Column('id', String, primary_key=True),
                      Column('address_value', String),
                      Column('latitude', String),
                      Column('longitude', String)
                      )

    # Create the above tables
    meta.create_all(con)

con, meta = connect('bot', 'vePu4r6AsX8', 'orgs')
create_tables(con, meta)
