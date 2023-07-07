import os

class Config(object):

      BOT_TOKEN = os.environ.get("BOT_TOKEN", "6300910303:AAGyg1ckI_SR2YVw_xlDIIIZ1C_qukWGjuw")
      API_ID = int(os.environ.get("API_ID", 28888037))
      API_HASH = os.environ.get("API_HASH" , default="9fbe164b5591df05fbd8577e3b1d6d21")
      OWNER_ID = int(os.environ.get("OWNER_ID" , default="5190902724"))