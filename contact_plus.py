import fileinput
import logging
from logging.handlers import RotatingFileHandler


def format_bl_contact():
    result = {}
    with fileinput.input('bl_contact.txt') as file:
        for f in file:
            f.replace(' ', '')
            d = f.split(',')
            member_id = d[0]
            telephone = d[1]

            if member_id in result:
                v = result[member_id]
                v.add(telephone)
            else:
                result[member_id] = {telephone}
    return result


def logger_info(path):
    handler = RotatingFileHandler(filename=path,
                                  mode='a',
                                  maxBytes=6000 * 1024 * 1024,
                                  backupCount=2,
                                  encoding='utf-8')

    formatter = logging.Formatter('')
    handler.setFormatter(formatter)
    handler.setLevel(logging.INFO)

    LOG = logging.getLogger()
    LOG.setLevel(logging.INFO)
    LOG.addHandler(handler)


def format_app_contact(path):
    result = {}
    with fileinput.input(path) as file:
        for f in file:
            f.replace(' ', '')
            data = f.split(',')
            version = data[0]
            application_id = data[1]
            member_id = data[2]
            telephone = data[3]
            key = f'{version}-{application_id}-{member_id}'
            if key in result:
                v = result[key]
                v.add(telephone)
            else:
                result[key] = {telephone}
    return result


def count(format_app, format_bl):
    for key, app_contact in format_app.items():
        data = key.split('-')
        version = data[0]
        application_id = data[1]
        member_id = data[2]
        for k, d in format_bl.items():
            if member_id != k:
                result = len(app_contact & d)
                if result:
                    logging.info(f'{version}, {application_id}, {member_id}, {k}, {result}')
        print(f'key: {key} is done')


def add_format_app(app_contact_list):
    with open('app_contact.txt', 'w+') as f:
        for app_contact in app_contact_list:
            with fileinput.input(app_contact) as file:
                for file_ in file:
                    f.write(file_)


def main():
    logger_info('loan_result.txt')
    # add_format_app(['app_contact.txt.1', 'app_contact.txt.2', 'app_contact.txt.3'])
    # format_app = format_app_contact('app_contact.txt')
    format_app = format_app_contact('loan_contact.txt')
    format_bl = format_bl_contact()
    count(format_app, format_bl)


if __name__ == '__main__':
    main()
