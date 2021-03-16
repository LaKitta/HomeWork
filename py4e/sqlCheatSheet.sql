# junction table - course & user
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;


CREATE TABLE User(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Course(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE
);

CREATE TABLE Member(
    user_id INTEGER,
    course_id INTEGER,
    role INTEGER,
    PRIMARY KEY (user_id, course_id)
);

SELECT User.name, Course.title, Member.role
FROM Member JOIN Course JOIN User
ON Member.user_id = User.id AND Member.course_id = Course.id
LIMIT 50;

# itunes track

DROP TABLE IF EXISTS Artists;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;

CREATE TABLE Artists(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Album(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    album TEXT UNIQUE
);

CREATE TABLE Genre(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    genre TEXT UNIQUE
);

CREATE TABLE Track(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT,
    artist_id INTEGER,
    album_id INTEGER,
    genre_id INTEGER,
    len INTEGER,
    rating INTEGER,
    count INTEGER
);

SELECT Track.title, Album.album, Genre.genre, Track.len, Track.rating, Track.count
FROM Track JOIN Artists JOIN Album JOIN Genre
ON Track.album_id = Album.id AND Track.genre_id = Genre.id
ORDER BY Track.count
LIMIT 100;

# spider.sqlite

DROP TABLE IF EXISTS Pages;
DROP TABLE IF EXISTS Links;
DROP TABLE IF EXISTS Webs;

CREATE TABLE IF NOT EXISTS Pages (
    id INTEGER PRIMARY KEY, 
    url TEXT UNIQUE, 
    html TEXT,
    error INTEGER, 
    old_rank REAL, 
    new_rank REAL
    );

CREATE TABLE IF NOT EXISTS Links (
    from_id INTEGER, 
    to_id INTEGER, 
    UNIQUE(from_id, to_id)
    );

CREATE TABLE IF NOT EXISTS Webs (
    url TEXT UNIQUE
    );