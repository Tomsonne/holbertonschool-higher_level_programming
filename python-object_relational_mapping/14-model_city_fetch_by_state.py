#!/usr/bin/python3
"""
popo
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    """"
    popo
    """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db_url = f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}"
    engine = create_engine(db_url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    results = (
        session.query(State.name, City.id, City.name)
        .join(City, State.id == City.state_id)
        .order_by(City.id)
        .all()
    )

    for state_name, city_id, city_name in results:
        print(f"{state_name}: ({city_id}) {city_name}")
