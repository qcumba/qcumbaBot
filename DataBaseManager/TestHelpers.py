import string
import random
from OrgInfoGenerator.Domain import Organization
from OrgInfoGenerator.Domain import Requisites
from OrgInfoGenerator.Domain import State
from OrgInfoGenerator.Domain import Address
from OrgInfoGenerator.Domain import Management


def random_generator(size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))


def generate_random_org():

    requisites = Requisites.LegalRequisites(
        random_generator(),
        random_generator(),
        random_generator(),
        random_generator()
    )
    state = State.State({
        'status': 'ACTIVE',
        'registration_date': '677376000000'
    })
    address = Address.Address({
        'unrestricted_value': random_generator(),
        'data': {
            'geo_lat': random_generator(),
            'geo_lon': random_generator()
        }
    })
    management = Management.Management({
        'post': random_generator(),
        'name': random_generator()
    })
    org = Organization.LegalOrganization(
        random_generator(),
        requisites,
        state,
        address,
        management
    )
    return org