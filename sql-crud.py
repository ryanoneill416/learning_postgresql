from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from "chinook" db
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for the "Programmer" table
class FavPlace(base):
    __tablename__ = "FavouritePlaces"
    id = Column(Integer, primary_key=True)
    country = Column(String)
    nat_language = Column(String)
    population = Column(Integer)


# instead of connecting to db directly, we ask for a session
# create new instance of sessionmaker, then point to db
Session = sessionmaker(db)
# opens an actual session by calling the Session() 
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)


# creating records on our programmer table
my_house = FavPlace(
    country="Ireland",
    nat_language="English",
    population=3
)

paleokastritsa = FavPlace(
    country="Greece",
    nat_language="Greek",
    population=1242078
)

budapest = FavPlace(
    country="Hungary",
    nat_language="Hungarian",
    population=4234742
)

leeds = FavPlace(
    country="United Kingdom",
    nat_language="English",
    population=5384243
)

morroccoy = FavPlace(
    country="Venezuela",
    nat_language="Spanish",
    population=230076
)


# add each instance of our programmers to our session
session.add(my_house)
session.add(paleokastritsa)
session.add(budapest)
session.add(leeds)
session.add(morroccoy)


# commit our session to the database
# session.commit()


# updating a single record
# programmer = session.query(Programmer).filter_by(id=8).first()
# programmer.famous_for = "World President"


# # updating multiple records
# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined")
#         session.commit()


# deleting a single record
# fname = input("Enter first name: ")
# lname = input("Enter last name: ")
# programmer = session.query(Programmer).filter_by(first_name = fname, last_name= lname).first()
# # defensive programming
# if programmer is not None:
#     print("Programmer Found: ", programmer.first_name + " " + programmer.last_name)
#     confirmation = input("Are you sure you want to delete this record? (y/n) ")
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("Selected record deleted successfully")
#     else:
#         print("Selected record not deleted")
# else:
#     print("No matching records found")


# delete multiple records
# programmers = session.query(Programmer)
# for programmer in programmers:
#     session.delete(programmer)
#     session.commit()


# query the database to find all Programmers
favplaces = session.query(FavPlace)
for place in favplaces:
    print(
        place.id,
        place.country,
        place.nat_language,
        place.population,
        sep=" | "
    )