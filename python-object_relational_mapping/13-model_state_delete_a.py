#!/usr/bin/python3
"""
popo
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """
    popo
    """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db_url = f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}"
    engine = create_engine(db_url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states_to_delete = (
        session.query(State)
        .filter(State.name.like('%a%'))
        .all()
    )

    for state in states_to_delete:
        session.delete(state)

    session.commit()
