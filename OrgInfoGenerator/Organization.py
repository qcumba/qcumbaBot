import uuid


class BasicOrganization(object):
    """
    Basic class for organization
    """

    def __init__(self, full_name, requisites, status):
        self.id = uuid.uuid4()
        self.full_name = full_name
        self.requisites = requisites
        self.status = status


class LegalOrganization(BasicOrganization):
    """
    Info about legal organization
    """

    def __init__(self, full_name, requisites, status, address):
        super(LegalOrganization, self).__init__(full_name, requisites, status)
        self.address = address
        self.jur = True


class IndividualOrganization(BasicOrganization):
    """
    Info about individual organization
    """

    def __init__(self, full_name, requisites, status, address):
        super(IndividualOrganization, self).__init__(full_name, requisites, status)
        self.address = address
        self.jur = False
