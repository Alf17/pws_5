from datetime import datetime
# import psycopg2
import serial
# from .config import config

ser = serial.Serial('/dev/ttyACM1', 115200)


# def connect():
#     """ Connect to the PostgreSQL database server """
#     conn = None
#     try:
#         # read connection parameters
#         params = config()
#
#         # connect to the PostgreSQL server
#         print('Connecting to the PostgreSQL database...')
#         conn = psycopg2.connect(**params)
#
#         # create a cursor
#         cur = conn.cursor()
#
#         # execute a statement
#         print('PostgreSQL database version:')
#         cur.execute('SELECT version()')
#
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         pass
#
#     return cur, conn
#
#
# def write_data(cur, conn, dane):
#     czas_pomiaru = str(datetime.now())
#     id_urzadzenia_pomiarowego_id = dane[0].split(' ')[1].rstrip(':').strip()
#     wielkosc_pomiarowa_id = 2
#     pomiar = dane[1].rstrip(',')
#     if float(pomiar) > -999.0:
#         sql = f"""INSERT INTO pomiary_pomiar (pomiar, wielkosc_pomiarowa_id, id_urzadzenia_pomiarowego_id, czas_pomiaru)
#         VALUES ({pomiar}, {wielkosc_pomiarowa_id}, {id_urzadzenia_pomiarowego_id}, '{czas_pomiaru}');"""
#         print(sql)
#         file_name = datetime.now().strftime("%Y-%m-%d") + '.txt'
#         f = open(file_name, "a+")
#         f.write(sql + '\n')
#         f.close()
#         try:
#             ret = cur.execute(sql)
#             conn.commit()
#             print(ret)
#         except (Exception, psycopg2.Error) as error:
#             print(error)
#
#         wielkosc_pomiarowa_id = 1
#         pomiar = dane[2]
#         sql = f"""INSERT INTO pomiary_pomiar (pomiar, wielkosc_pomiarowa_id, id_urzadzenia_pomiarowego_id, czas_pomiaru)
#         VALUES ({pomiar}, {wielkosc_pomiarowa_id}, {id_urzadzenia_pomiarowego_id}, '{czas_pomiaru}');"""
#         print(sql)
#         f = open(file_name, "a+")
#         f.write(sql + '\n')
#         f.close()
#         try:
#             ret = cur.execute(sql)
#             conn.commit()
#             print(ret)
#         except (Exception, psycopg2.Error) as error:
#             print(error)
#             try:
#                 conn.close()
#             except:
#                 pass


if __name__ == '__main__':
    # cur, conn = connect()
    print("[ START ]")
    while True:
        linia = ser.readline().decode('utf-8')
        if linia != '':
            try:
                dane = linia.strip().split('\t')
                if 'UP' in dane[0]:
                    print(dane)
                    # write_data(cur, conn, dane)
            except:
                print('Blad')
