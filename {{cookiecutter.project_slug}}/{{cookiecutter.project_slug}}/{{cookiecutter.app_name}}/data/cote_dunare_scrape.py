import bs4 as bs
import re, datetime
from urllib.request import Request, urlopen
import psycopg2

req = Request('https://www.afdj.ro/ro/cotele-dunarii', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

soup = bs.BeautifulSoup(webpage, 'lxml')
table = soup.find('table')
table_rows = table.find_all('tr')
for tr in table_rows[2:3]:
    td = tr.find_all('td')
    row = [i.text for i in td]
    oras = row[0].strip()
    km = int(row[1])
    nivelul_apei = int(''.join(list(filter(str.isdigit, row[2]))))
    variatia = int(row[3])
    temp_masurata = float(re.findall(r"[+-]? *(?:\d+(?:\,\d*)?|\,\d+)(?:[eE][+-]?\d+)?", row[4].strip())[0].replace(',', '.'))
    data_actualizare = datetime.datetime.strptime(row[5].strip(), '%d/%m/%Y').date()

    print(oras, km, nivelul_apei, variatia, temp_masurata, data_actualizare)
    # print(type(data_actualizare))
    try:
        connection = psycopg2.connect(user = "bogdan",
                                      password = "bogdan",
                                      host = "127.0.0.1",
                                      port = "5432",
                                      database = "{{cookiecutter.project_slug}}")
        cursor = connection.cursor()
        postgres_insert_query = """INSERT INTO public."DDMap_cotedunare"(oras, km, nivelul_apei, variatia, temp_masurata, data_actualizare) VALUES (%s, %s, %s, %s, %s, %s);"""
        record_to_insert = (oras, km, nivelul_apei, variatia, temp_masurata, data_actualizare)
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into DDMap_cotedunare table")
    except (Exception, psycopg2.Error) as error:
        if (connection):
            print("Failed to insert record into DDMap_cotedunare table", error)
    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")