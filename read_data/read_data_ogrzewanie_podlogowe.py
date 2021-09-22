from datetime import datetime
import psycopg2
import serial
# from .config import config

ser1 = serial.Serial('/dev/ttyACM1', 115200)


def connect():
    """ Connect to the PostgreSQL database server """
    try:
        conn = psycopg2.connect(user="pws_17",
                                  password="pws_17",
                                  host="192.168.7.105",
                                #   host="178.183.96.38",
                                  port="5432",
                                  database="pws_17")

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        pass

    return cur, conn


def write_data(cur, conn, dane):
    czas_pomiaru = str(datetime.now())
    sql = f"""INSERT INTO pomiary_result (result, measurind_point_id, meazurand_type_id, sensor_id, date_time)
    VALUES ({float(dane[1].split(':')[1].strip())}, {int(dane[0].split(':')[1].strip()) + 1}, 1, 2, '{czas_pomiaru}');"""
    print(sql)
    file_name = datetime.now().strftime("%Y-%m-%d") + '.txt'
    f = open(file_name, "a+")
    f.write(sql + '\n')
    f.close()
    try:
        ret = cur.execute(sql)
        conn.commit()
        print(ret)
    except (Exception, psycopg2.Error) as error:
        print(error)

    sql = f"""INSERT INTO pomiary_result (result, measurind_point_id, meazurand_type_id, sensor_id, date_time)
    VALUES ({float(dane[2].split(':')[1].strip())}, {int(dane[0].split(':')[1].strip()) + 1}, 2, 2, '{czas_pomiaru}');"""
    print(sql)
    f = open(file_name, "a+")
    f.write(sql + '\n')
    f.close()
    try:
        ret = cur.execute(sql)
        conn.commit()
        print(ret)
    except (Exception, psycopg2.Error) as error:
        print(error)
        try:
            conn.close()
        except:
            pass


if __name__ == '__main__':
    # cur, conn = connect()
    print("[ START ]")
    cur, con = connect()
    print("data base")
    print(cur, con)
    while True:
        linia0 = ser1.readline().decode('utf-8')
        if linia0 != '':
            try:
                # print(f"Linia: {linia0}")
                dane = linia0.strip().split('_')
                print(dane)
                if len(dane) == 4:
                    write_data(cur=cur, conn=con, dane=dane)
            except:
                print('Blad port 0')
