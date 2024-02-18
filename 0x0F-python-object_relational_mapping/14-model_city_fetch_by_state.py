#!/usr/bin/python3
"""
that prints all City objects from the database hbtn_0e_14_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".
            format(argv[1], argv[2], argv[3]),
            pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    cities = session.query(City, State).filter(State.id == City.state_id).all()

    for state, city in cities:
        print(f"{city.name}: ({city.id}) {state.name}")

    session.commit()
