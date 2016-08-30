import uuid
from peewee import *

db = PostgresqlDatabase(
    'orgs',
    user='bot',
    password='vePu4r6AsX8',
    host='localhost',
)


class Address(Model):
    id = UUIDField(primary_key=True)
    address_value = CharField()
    latitude = CharField(null=True)
    longitude = CharField(null=True)

    class Meta:
        database = db


class State(Model):
    id = UUIDField(primary_key=True)
    status = CharField()
    registration_date = DateField(null=True)
    liquidation_date = DateField(null=True)

    class Meta:
        database = db


class Management(Model):
    id = UUIDField(primary_key=True)
    name = CharField(null=True)
    post = CharField(null=True)

    class Meta:
        database = db


class Requisites(Model):
    id = UUIDField(primary_key=True)
    inn = CharField()
    ogrn = CharField()
    opf = CharField()
    kpp = CharField(null=True)

    class Meta:
        database = db


class Org(Model):
    id = CharField()
    group_id = CharField()
    position = IntegerField()
    name = CharField()
    requisites = ForeignKeyField(Requisites, null=True)
    management = ForeignKeyField(Management, null=True)
    state = ForeignKeyField(State, null=True)
    address = ForeignKeyField(Address, null=True)

    class Meta:
        database = db


# Address.create_table()
# State.create_table()
# Management.create_table()
# Requisites.create_table()
# Org.create_table()

def insert_org_list(orgs):
    group_id = uuid.uuid4()

    for index, org in enumerate(orgs):
        Address.create(
            id=uuid.uuid4(),
            address_value=org.address.address_value,
            latitude=org.address.latitude,
            longitude=org.address.longitude
        )
        State.create(
            id=uuid.uuid4(),
            status=org.state.status,
            registration_date=org.state.registration_date,
            liquidation_date=org.state.liquidation_date
        )
        Management.create(
            id=uuid.uuid4(),
            name=org.management.name,
            post=org.management.post
        )
        Requisites.create(
            id=uuid.uuid4(),
            inn=org.requisites.inn,
            ogrn=org.requisites.ogrn,
            opf=org.requisites.opf,
            kpp=org.requisites.kpp
        )
        Org.create(
            id=org.id,
            group_id=group_id,
            position=index,
            name=org.full_name,
            requisites=Requisites,
            management=Management,
            state=State,
            address=Address
        )
