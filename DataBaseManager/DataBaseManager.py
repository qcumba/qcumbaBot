import uuid
from peewee import *

db = PostgresqlDatabase(
    'orgs',
    user='bot',
    password='vePu4r6AsX8',
    host='localhost',
)


class Address(Model):
    address_value = CharField()
    latitude = CharField(null=True)
    longitude = CharField(null=True)

    class Meta:
        database = db


class State(Model):
    status = CharField()
    registration_date = DateField(null=True)
    liquidation_date = DateField(default=None, null=True)

    class Meta:
        database = db


class Management(Model):
    name = CharField(null=True)
    post = CharField(null=True)

    class Meta:
        database = db


class Requisites(Model):
    inn = CharField()
    ogrn = CharField()
    opf = CharField()
    kpp = CharField(null=True)

    class Meta:
        database = db


class Org(Model):
    group_id = UUIDField()
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
        address = Address.create(
            address_value=org.address.address_value,
            latitude=org.address.latitude,
            longitude=org.address.longitude
        )
        state = State.create(
            status=org.state.status,
            registration_date=org.state.registration_date,
            liquidation_date=org.state.liquidation_date
        )
        management = Management.create(
            name=org.management.name,
            post=org.management.post
        )
        requisites = Requisites.create(
            inn=org.requisites.inn,
            ogrn=org.requisites.ogrn,
            opf=org.requisites.opf,
            kpp=org.requisites.kpp
        )
        org = Org.create(
            group_id=group_id,
            position=index,
            name=org.name,
            requisites=requisites,
            management=management,
            state=state,
            address=address
        )
        if index == 0:
            current_org_id = org.id

    return current_org_id


def get_org(id):
    result = Org.select().where(Org.id == id).get()
    next_result = Org.select().where((Org.group_id == result.group_id) & (Org.position == result.position + 1)).get()
    next_id = next_result.id
    return next_result, next_id
