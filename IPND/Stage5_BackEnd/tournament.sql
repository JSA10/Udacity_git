-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

--My notes: This file sets up the tables that make up my database structure

-- Remove any old databases
DROP DATABASE   IF EXISTS tournament;

-- Create database for the tournament
CREATE DATABASE tournament;

-- Connect to the new database
\c              tournament;

-- Double check for any tables or views that may exist
DROP TABLE      IF EXISTS players;
DROP TABLE      IF EXISTS matches;
DROP VIEW       IF EXISTS standings;

-- Create table for player ids and names.
-- Using PostgreSQL's serial format for the id and assign as primary key (single)
CREATE TABLE    players (
                id serial PRIMARY KEY,
                name text NOT NULL
);

-- Create table for games, use same primary key and add columns to assign the
-- wins and losses from each game to a player as a foreign key referencing primary
-- key from players table
CREATE TABLE    matches(
                id serial PRIMARY KEY,
                winner integer,
                loser integer,
                FOREIGN KEY(winner) REFERENCES players(id),
                FOREIGN KEY(loser) REFERENCES players(id)
);

-- Create view to show standings. Running joins without using the term, by
-- using foreign key of matches linked to primary key of players to count each
-- win next to the right player and also increment games played.
CREATE VIEW     standings AS
SELECT          players.id, players.name,
  (SELECT count(*) FROM matches WHERE matches.winner = players.id) as wins,
  (SELECT count(*) FROM matches WHERE players.id in (winner, loser)) as games
FROM players
GROUP BY players.id
ORDER BY wins DESC;
