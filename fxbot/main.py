
import MetaTrader5 as mt5


class FXTrader:
    def __init__(self, login, password, server):
        self.login = int(login)
        self.password = password
        self.server = server

    def init_mt5(self):
        if not mt5.initialize():
            print("initialize() failed, error code =", mt5.last_error())
            return False
        else:
            print("initialize() completed")
    
    def connect(self):
        authorized = mt5.login(self.login, password=self.password, server=self.server)
        if authorized:
            print(f"Connected to account #{self.login}")
            return True
        else:
            print(f"Failed to connect at account #{self.login}, error code: {mt5.last_error()}")
            return False

    def account_info(self):
        account_info_dict = mt5.account_info()._asdict()
        for prop in account_info_dict:
            print(f"{prop}={account_info_dict[prop]}")