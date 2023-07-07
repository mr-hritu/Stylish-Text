import os

class Config(object):

      BOT_TOKEN = os.environ.get("BOT_TOKEN", "6300910303:AAGyg1ckI_SR2YVw_xlDIIIZ1C_qukWGjuw")
      API_ID = int(os.environ.get("API_ID", 29616312))
      API_HASH = os.environ.get("API_HASH" , default="dd1a05ab4c47a5a037cc067cf4bded27")
      OWNER_ID = int(os.environ.get("OWNER_ID" , default="6262157003"))