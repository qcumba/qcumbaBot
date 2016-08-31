# coding=utf-8
class BasicRequisites(object):
    """
    Basic class for organization requisites
    """

    def __init__(self, inn, ogrn, opf_code):
        self.inn = inn
        self.ogrn = ogrn
        self.opf = opf_code


class IndividualRequisites(BasicRequisites):
    """
    Requisites for individual organizations
    """

    def __init__(self, inn, ogrn, opf_code):
        super(IndividualRequisites, self).__init__(inn, ogrn, opf_code)
        self.kpp = None


class LegalRequisites(BasicRequisites):
    """
    Requisites for legal organizations
    """

    def __init__(self, inn, ogrn, opf_code, kpp):
        super(LegalRequisites, self).__init__(inn, ogrn, opf_code)
        self.kpp = kpp
