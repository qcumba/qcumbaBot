# coding=utf-8
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
        super(IndividualRequisites, self).__init__(inn, ogrn, opf_code)


class LegalRequisites(BasicRequisites):
    """
    Requisites for legal organizations
    """

    def __init__(self, inn, ogrn, opf_code, kpp, management):
        super(LegalRequisites, self).__init__(inn, ogrn, opf_code)
        self.kpp = kpp
        self.management = management


class Management(object):
    """
    Management post and name
    """

    def __init__(self, management):
        if management is not None:
            self.name = management['name']
            if management['post'] is not None:
                self.post = management['post']
            else:
                self.post = 'Директор'
