import sqlite3
import datetime




con = sqlite3.connect('Symbols.db')



def create_symbol_table(symbol): 

    cur = conn.cursor()
    cur.execute(f'''CREATE TABLE {symbol}
               symbol text, open_time text,close real,volume real ''')

     



def show_tables(con):
    con = sqlite3.connect('database.sqlite')
    cursor = con.cursor()
    cursor.execute('SELECT name from sqlite_master where type= "table"')
    print(cursor.fetchall())
    con.close()


def show_columns():
    con = sqlite3.connect('database.sqlite')
    cursor = con.execute('select * from bar')
    # instead of cursor.description:
    row = cursor.fetchone()
    names = row.keys()


def select_all():

    con = sqlite3.connect('database.sqlite')
    cursor = con.cursor()

    result = cursor.execute('SELECT Datetime,Country,League,HomeTeam,AwayTeam,FTR FROM football_data')

    for row in result:
        print(row)
    con.close()

def add_data_from_api():
    pass


def add_several_rows():
    n = input('Combien de ligne voulez vous ajouter ? : ')
    list_to_insert = []

    for e in range(0,int(n)):

        con = sqlite3.connect('database.sqlite')
        cursor = con.cursor()

        print(f'Pour la ligne {e+1} : ')
        date_match = input('Merci de rentrer la data du match ( JJ/MM/AAAA ): ')
        date_match = datetime.datetime.strptime(date_match, '%d/%m/%Y')

        div = input('Merci de rentrer le pays du match : ')

        country = input('Merci de rentrer la ligue du match : ')
        home_team = input("Merci de rentrer la l'équipes à domicile : ")
        away_team = input("Merci de rentrer la l'équipes à l'extérieur : ")
        result = input('Merci de rentrer le résultat : ')
        tuple = (date_match,div,country,home_team,away_team,result)
        list_to_insert.append(tuple)

    cursor.executemany("insert into football_data (Datetime,Country,League,HomeTeam,AwayTeam,FTR) VALUES (?,?,?,?,?,?)", list_to_insert)
    print(f'Les {n} lignes ont été ajoutées ! ')

def delete_row():

    con = sqlite3.connect('database.sqlite')
    cursor = con.cursor()

    condition = input('Quel est votre condition pour supprimer des lignes ? :')
    cursor.execute("DELETE FROM football_data WHERE (?)", condition)
    print('les lignes ont bien été supprimées')



def make_request():
    request = input('Quelle requête souhaitez vous effectuer ? ')
    con = sqlite3.connect('database.sqlite')
    cursor = con.cursor()

    try:
        result = cursor.execute(request)
        for e in result:
            print(e)

    except :
        print('Erreur avec votre requête')
        pass



def table_to_df():
    con = sqlite3.connect('database.sqlite')
    table = input("Quelle table voulez vous afficher sous forme de DF ? ")
    df = pd.read_sql(f'SELECT * FROM {table}',con)
    print(df)
    con.close()

def show_columns():
    cursor = connection.execute('select * from bar')
    # instead of cursor.description:
    row = cursor.fetchone()
    names = row.keys()

def joke():
    print("Clément est con")
