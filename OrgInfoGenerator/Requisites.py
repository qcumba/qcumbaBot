class BasicRequisites(object):
    """
    Basic class for organization requisites
    """

    def __init__(self, inn, ogrn, opf_code):
        self.inn = inn
        self.ogrn = ogrn
        self.opf_code = opf_code


class IndividualRequisites(BasicRequisites):
    """
    Requisites for individual organizations
    """

    def __init__(self, inn, ogrn, opf_code):
        self.inn = inn
        self.ogrn = ogrn
        self.opf_code = opf_code


class LegalRequisites(BasicRequisites):
    """
    Requisites for legal organizations
    """

    def __init__(self, inn, ogrn, opf_code, kpp):
        self.inn = inn
        self.ogrn = ogrn
        self.opf_code = opf_code
        self.kpp = kpp
