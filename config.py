import os

class Config(object):

      BOT_TOKEN = os.environ.get("BOT_TOKEN", "6300910303:AAGyg1ckI_SR2YVw_xlDIIIZ1C_qukWGjuw")
      API_ID = int(os.environ.get("API_ID", 5321008))
      API_HASH = os.environ.get("API_HASH" , default="8a633e8f5259a852ec85d4e8cfc31e67")
      OWNER_ID = int(os.environ.get("OWNER_ID" , default="5190902724"))