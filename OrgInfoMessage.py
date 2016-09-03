# -*- coding: utf-8 -*-
from emoji import emojize


def make_org_info_message(org_element):
    if org_element.requisites.inn is None:
        inn_message = 'Ликвидирован'
    else:
        inn_message = org_element.requisites.inn
    params_requisites = {
        'inn': '<b>' + inn_message + '</b>',
        'ogrn': '<b>' + org_element.requisites.ogrn + '</b>'
    }

    if org_element.state.registration_date is not None:
        reg_date = org_element.state.registration_date.strftime("%d-%m-%Y")
    else:
        reg_date = 'Отсутствует информация'
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
        'registration_date': '<b>' + reg_date + '</b>',
        'status': '<b>' + org_element.state.status + '</b>'
    }
    message = u'Наименование:\n {full_name}\n' \
              u'{requisites}Код ОПФ:\n {opf}\n' \
              u'Дата регистрации:\n {registration_date}' \
              u'\nСтатус:\n {status}\n'.format(**params)

    return emojize(':bank:', use_aliases=True) + message
