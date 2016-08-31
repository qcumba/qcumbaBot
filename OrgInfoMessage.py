# -*- coding: utf-8 -*-
from emoji import emojize


def make_org_info_message(org_element):
    params_requisites = {
        'inn': '<b>' + org_element.requisites.inn + '</b>',
        'ogrn': '<b>' + org_element.requisites.ogrn + '</b>'
    }
    requisites = u'ИНН\\ОГРН:\n {inn}\\{ogrn}\n'
    if hasattr(org_element.requisites, 'kpp') and org_element.requisites.kpp is not None:
        params_requisites['kpp'] = org_element.requisites.kpp
        requisites += u'КПП:\n {kpp}\n'
    if hasattr(org_element, 'management') and hasattr(org_element.management, 'name'):
        params_requisites['post'] = org_element.management.post,
        params_requisites['name'] = '<b>' + org_element.management.name + '</b>'
        requisites += org_element.management.post + ':\n{name}\n'
    requisites = requisites.format(**params_requisites)

    params = {
        'full_name': '<b>' + org_element.name + '</b>',
        'requisites': requisites,
        'opf': '<b>' + org_element.requisites.opf + '</b>',
        'registration_date': '<b>' + org_element.state.registration_date.strftime("%d-%m-%Y") + '</b>',
        'status': '<b>' + org_element.state.status + '</b>'
    }
    message = u'Наименование:\n {full_name}\n' \
              u'{requisites}Код ОПФ:\n {opf}\n' \
              u'Дата регистрации:\n {registration_date}' \
              u'\nСтатус:\n {status}\n'.format(**params)

    return emojize(':bank:', use_aliases=True) + message
