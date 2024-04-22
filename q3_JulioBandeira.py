import psycopg2

connect_to_database = lambda: psycopg2.connect(
    host="localhost",
    user="juliousername",
    password="juliopassword",
    database="juliodatabase"
)

# Metodos de insert


insert_user = lambda user_id, user_name, user_country, console_id: (
    "INSERT INTO USERS (id, name, country, id_console) VALUES (%s, %s, %s, %s)",
    (user_id, user_name, user_country, console_id)
)

insert_videogame = lambda console_id, game_name, company_id, release_date: (
    "INSERT INTO VIDEOGAMES (id_console, name, id_company, release_date) VALUES (%s, %s, %s, %s)",
    (console_id, game_name, company_id, release_date)
)

insert_game = lambda game_id, game_title, game_genre, game_release_date, console_id: (
    "INSERT INTO GAMES (id_game, title, genre, release_date, id_console) VALUES (%s, %s, %s, %s, %s)",
    (game_id, game_title, game_genre, game_release_date, console_id)
)

insert_company = lambda company_id, company_name, company_country: (
    "INSERT INTO COMPANY (id_company, name, country) VALUES (%s, %s, %s)",
    (company_id, company_name, company_country)
)

# Metodos de Get all

get_all_users = lambda: (
    "SELECT * FROM USERS",
    ()
)

get_all_videogames = lambda: (
    "SELECT * FROM VIDEOGAMES",
    ()
)

get_all_games = lambda: (
    "SELECT * FROM GAMES",
    ()
)

get_all_companies = lambda: (
    "SELECT * FROM COMPANY",
    ()
)

# Metodos de remover

remove_user = lambda user_id: (
    "DELETE FROM USERS WHERE id = %s",
    (user_id,)
)


remove_videogame = lambda game_id: (
    "DELETE FROM VIDEOGAMES WHERE id_console = %s",
    (game_id,)
)


remove_game = lambda game_id: (
    "DELETE FROM GAMES WHERE id_game = %s",
    (game_id,)
)

remove_company = lambda company_id: (
    "DELETE FROM COMPANY WHERE id_company = %s",
    (company_id,)
)


# Executar e buscar os resultados

execute_query = lambda query, values: (
    cursor.execute(query, values)
)

fetch_results = lambda: (
    cursor.fetchall()
)

# Casos de uso

connection = connect_to_database()
cursor = connection.cursor()


# Insert a user
execute_query(*insert_user(8, 'John Doe', 'USA', 1))

# Insert a videogame
execute_query(*insert_videogame(14, 'Game Name', 1, '2022-01-01'))

# Insert a game
execute_query(*insert_game(32, 'Super Mario', 'Platformer', '1985-09-13', 1))

# Insert a company
execute_query(*insert_company(44, 'Nintendo', 'Japan'))



connection.commit()

execute_query(*get_all_users())
users = fetch_results()
print("Usuários:")
for user in users:
    print(user)

execute_query(*get_all_videogames())
videogames = fetch_results()
print("Videogames:")
for videogame in videogames:
    print(videogame)

execute_query(*get_all_games())
games = fetch_results()
print("Jogos:")
for game in games:
    print(game)

execute_query(*get_all_companies())
companies = fetch_results()
print("Empresas:")
for company in companies:
    print(company)

cursor.close()
connection.close()