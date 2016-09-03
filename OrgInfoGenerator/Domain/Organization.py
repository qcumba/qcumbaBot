import uuid


class BasicOrganization(object):
    """
    Basic class for organization
    """

    def __init__(self, full_name, requisites, state, address=None):
        self.name = full_name
        self.requisites = requisites
        self.state = state
        if address is not None:
            self.address = address


class LegalOrganization(BasicOrganization):
    """
    Info about legal organization
    """

    def __init__(self, full_name, requisites, state, management, address=None):
        super(LegalOrganization, self).__init__(full_name, requisites, state, address)
        self.jur = True
        self.management = management


class IndividualOrganization(BasicOrganization):
    """
    Info about individual organization
    """

    def __init__(self, full_name, requisites, state, address=None):
        super(IndividualOrganization, self).__init__(full_name, requisites, state, address)
        self.jur = False
