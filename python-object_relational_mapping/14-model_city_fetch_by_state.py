#!/usr/bin/python3
"""
Cities
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_city import City
from model_state import State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        argv[1], argv[2], argv[3]
        ), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    rows = session.query(City, State).filter(
            City.state_id == State.id
            ).order_by(City.id)
    [print("{}: ({}) {}".format(
        state.name, city.id, city.name
        )) for city, state in rows]
