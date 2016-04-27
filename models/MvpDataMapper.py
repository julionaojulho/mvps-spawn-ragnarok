import pickle

from models.Mvp import Mvp

with open('mvps.db', 'rb') as file:
    _db = pickle.load(file)  # type: dict(Mvp)


def save(mvp):
    """
    Persists a Mvp object to the database.

    Args:
        mvp (Mvp): Mvp object to be persisted.

    """
    _db[(mvp.name, mvp.map)] = mvp

    with open('mvps.db', 'wb') as output:
        pickle.dump(_db, output)


def get(mvp_name):
    return _db[mvp_name]
