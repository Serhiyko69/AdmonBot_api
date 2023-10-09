import pymongo
import configparser
import certifi
ca = certifi.where()

config = configparser.ConfigParser()
config.read('config.ini')

mongo_user = config.get('DB', 'admin')
mongodb_pass = config.get('DB', 'password')
mong_domain = config.get('DB', 'domain')

client = pymongo.MongoClient(
    f"mongodb+srv://{mongo_user}:{mongodb_pass}@cluster0.{mong_domain}.mongodb.net/?retryWrites=true&w=majority",  tlsCAFile=ca)

my_db = client['cities']
collection = my_db['cities_bot']

TOKEN = config.get('BOT', 'token')
GROUP_ID = config.get('BOT', 'grop_id')