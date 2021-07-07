from configparser import ConfigParser


def config(filename='database.ini', section='postgresql'):
    # create a parser

    # get section, default to postgresql
    db = {}
    db['host'] = '89.234.193.42'
    db['database'] = 'pomiary'
    db['user'] = 'pws'
    db['password'] = 'sd42re;1!'

    return db