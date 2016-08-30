import uuid


class BasicOrganization(object):
    """
    Basic class for organization
    """

    def __init__(self, full_name, requisites, state, address):
        self.name = full_name
        self.requisites = requisites
        self.state = state
        self.address = address


class LegalOrganization(BasicOrganization):
    """
    Info about legal organization
    """

    def __init__(self, full_name, requisites, state, address, management):
        super(LegalOrganization, self).__init__(full_name, requisites, state, address)
        self.jur = True
        self.management = management


class IndividualOrganization(BasicOrganization):
    """
    Info about individual organization
    """

    def __init__(self, full_name, requisites, state, address):
        super(IndividualOrganization, self).__init__(full_name, requisites, state, address)
        self.jur = False
