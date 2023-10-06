import os

class Config(object):

      BOT_TOKEN = os.environ.get("BOT_TOKEN", "6509245930:AAHTXGs2mE-kQFuG30QI5wwovkgBp7LK7sQ")
      API_ID = int(os.environ.get("API_ID", 5321008))
      API_HASH = os.environ.get("API_HASH" , default="8a633e8f5259a852ec85d4e8cfc31e67")
      OWNER_ID = int(os.environ.get("OWNER_ID" , default="5190902724"))