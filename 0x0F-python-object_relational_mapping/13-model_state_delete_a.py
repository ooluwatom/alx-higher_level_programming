#!/usr/bin/python3
""" Script to list all state objects using SQLalchemy module """

if __name__ == '__main__':

    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm.session import sessionmaker, Session
    from model_state import Base, State

    username = argv[1]
    password = argv[2]
    db_name = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name))

    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(State).filter(State.name.like('%a%')).\
        delete(synchronize_session=False)

    session.commit()
