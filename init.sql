-- Active: 1713724896456@@127.0.0.1@5432@juliodatabase@public
-- Criar a tabela USERS
CREATE TABLE IF NOT EXISTS USERS (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    country VARCHAR(100),
    id_console INTEGER
);

-- Criar a tabela VIDEOGAMES
CREATE TABLE IF NOT EXISTS VIDEOGAMES (
    id_console SERIAL PRIMARY KEY,
    name VARCHAR(100),
    id_company INTEGER,
    release_date DATE
);

-- Criar a tabela GAMES
CREATE TABLE IF NOT EXISTS GAMES (
    id_game SERIAL PRIMARY KEY,
    title VARCHAR(100),
    genre VARCHAR(100),
    release_date DATE,
    id_console INTEGER
);

-- Criar a tabela COMPANY
CREATE TABLE IF NOT EXISTS COMPANY (
    id_company SERIAL PRIMARY KEY,
    name VARCHAR(100),
    country VARCHAR(100)
);