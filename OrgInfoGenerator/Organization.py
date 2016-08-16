class BasicOrganization(object):
    """
    Basic class for organization
    """

    def __init__(self, full_name, requisites, status):
        self.full_name = full_name
        self.requisites = requisites
        self.status = status


class LegalOrganization(BasicOrganization):
    """
    Info about legal organization
    """

    def __init__(self, full_name, requisites, status, address):
        self.full_name = full_name
        self.requisites = requisites
        self.status = status
        self.address = address
        self.jur = True


class IndividualOrganization(BasicOrganization):
    """
    Info about individual organization
    """

    def __init__(self, full_name, requisites, status, address):
        self.full_name = full_name
        self.requisites = requisites
        self.status = status
        self.address = address
        self.jur = False
