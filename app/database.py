import os

_db = None

async def connect_db():
    global _db
    print('No database configured')

async def disconnect_db():
    pass

def get_db():
    return _db