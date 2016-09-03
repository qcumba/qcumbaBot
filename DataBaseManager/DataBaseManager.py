import uuid
from peewee import *
from Settings import Settings

DB_NAME = Settings.get_setting_value('db_name')
DB_USER_NAME = Settings.get_setting_value('db_user_name')
DB_PASSWORD = Settings.get_setting_value('db_password')
DB_HOST = Settings.get_setting_value('db_host')

db = PostgresqlDatabase(
    DB_NAME,
    user=DB_USER_NAME,
    password=DB_PASSWORD,
    host=DB_HOST,
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
    next_org_id = None
    for index, org in enumerate(orgs):
        try:
            if hasattr(org, 'address'):
                address = Address.create(
                    address_value=org.address.address_value,
                    latitude=org.address.latitude,
                    longitude=org.address.longitude
                )
            else:
                address = None
            state = State.create(
                status=org.state.status,
                registration_date=org.state.registration_date,
                liquidation_date=org.state.liquidation_date
            )
            if hasattr(org, 'management') and hasattr(org.management, 'name'):
                management = Management.create(
                    name=org.management.name,
                    post=org.management.post
                )
            else:
                management = None
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
            if index == 1:
                next_org_id = org.id
        except Exception as ex:
            raise

    return next_org_id


def get_org(org_id):
    current_org = Org.select().where(Org.id == org_id).get()
    count = Org.select().where(Org.group_id == current_org.group_id).count()
    position = current_org.position
    if position > 0:
        previous_org = Org.select().where(
            (Org.group_id == current_org.group_id) & (Org.position == position - 1)
        ).get()
    else:
        previous_org = None

    if position < count - 1:
        next_org = Org.select().where(
            (Org.group_id == current_org.group_id) & (Org.position == position + 1)
        ).get()
    else:
        next_org = None

    return current_org, previous_org, next_org


def get_org_by_position(position, group_id):
    result = Org.select().where(
        (Org.group_id == group_id) & (Org.position == position)
    ).get()
    return result
