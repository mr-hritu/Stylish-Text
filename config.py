import os

class Config(object):

      BOT_TOKEN = os.environ.get("BOT_TOKEN", "6114945822:AAEWOTZuIjoE5GgEzmLn5_Qu8baDS4zAYmk")
      API_ID = int(os.environ.get("API_ID", 29616312))
      API_HASH = os.environ.get("API_HASH" , default="dd1a05ab4c47a5a037cc067cf4bded27")
      OWNER_ID = int(os.environ.get("OWNER_ID" , default="5190902724"))

