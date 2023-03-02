from main import FXTrader
from utils import fxaccount,fxpassword,fxserver

bot = FXTrader(login=fxaccount, password=fxpassword, server=fxserver)

bot.init_mt5()
bot.connect()
