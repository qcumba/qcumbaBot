# -*- coding: utf-8 -*-


def make_org_info_message(org_element):
    if org_element.jur:
        params = {
            'inn': '<b>' + org_element.requisites.inn + '</b>',
            'ogrn': '<b>' + org_element.requisites.ogrn + '</b>',
            'kpp': '<b>' + org_element.requisites.kpp + '</b>',
            'post': org_element.requisites.management.post,
            'name': '<b>' + org_element.requisites.management.name + '</b>',
        }
        requisites = u'ИНН\\ОГРН:\n {inn}\\{ogrn}\nКПП:\n {kpp}\n{post}:\n{name}\n'.format(**params)
    else:
        params = {
            'inn': '<b>' + org_element.requisites.inn + '</b>',
            'ogrn': '<b>' + org_element.requisites.ogrn + '</b>'
        }
        requisites = u'ИНН\\ОГРН:\n {inn}\\{ogrn}'.format(**params)
    params = {
        'full_name': '<b>' + org_element.full_name + '</b>',
        'requisites': requisites,
        'opf_code': '<b>' + org_element.requisites.opf_code + '</b>',
        'registration_date': '<b>' + org_element.status.registration_date + '</b>',
        'status': '<b>' + org_element.status.status + '</b>'
    }
    message = u'Наименование:\n {full_name}\n' \
              u'{requisites}Код ОПФ:\n {opf_code}\n' \
              u'Дата регистрации:\n {registration_date}' \
              u'\nСтатус:\n {status}\n'.format(**params)

    return message
