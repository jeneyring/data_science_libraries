#Read only credentials
host = '157.230.209.171'
username = 'jemison_1756'
user = username
password = 'iy6zLR1hBf4ZwPGsfz8wkW6iEl4Imvui'

def get_db_url(db_name):
    url = f'mysql+pymysql://{user}:{password}@{host}/{db_name}'
    return url
    

