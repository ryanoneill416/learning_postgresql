from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# executing the instructions from our localhost "chinook" db
db = create_engine("postgresql:///chinook")

meta = MetaData(db)

# create variable for "Artist" table
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

# create variable for "Album" table
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)

# create variable for "Track" table
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)

# making the connection
with db.connect() as connection:

    # Query 1 - select all records from "Artist"
    # select_query = artist_table.select()

    # Query 2 - select only "Name" from "Artist"
    # select_query = artist_table.select().with_only_columns([artist_table.c.Name])

    # Query 3 - select only 'Queen' from "Artist"
    # select_query = artist_table.select().where(artist_table.c.Name == "Queen")

    # Query 4 - select only "ArtistId" 51 from "Artist"
    # select_query = artist_table.select().where(artist_table.c.ArtistId == 51)

    # Query 5 - select albums with ArtistId of 51
    select_query = album_table.select().where(album_table.c.ArtistId == 51)

    # Query 6 - select tracks where "Composer" is "Queen"
    select_query = track_table.select().where(track_table.c.Composer == "Queen")

    results = connection.execute(select_query)
    for result in results:
        print(result)