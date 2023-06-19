#!/usr/bin/python3
"""Prints the first State object from the database hbtn_0e_6_usa"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python3 script_name.py db_username db_password db_name state_name")
        sys.exit(1)

    db_username = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine(f'mysql+mysqldb://{db_username}:{db_password}@localhost:3306/{db_name}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    instance = session.query(State).filter_by(name=state_name).first()
    if instance:
        print(instance.id)
    else:
        print("State not found")
