import MetaTrader5 as mt5
import pandas as pd
# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)
 
# establish connection to the MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()
 
# connect to the trade account specifying a password and a server
authorized=mt5.login(65364552, password="8ftgzelu", server="MetaQuotes-Demo")
if authorized:
    account_info=mt5.account_info()
    if account_info!=None:
        # display trading account data 'as is'
        print(account_info)
        # display trading account data in the form of a dictionary
        print("Show account_info()._asdict():")
        account_info_dict = mt5.account_info()._asdict()
        for prop in account_info_dict:
            print("  {}={}".format(prop, account_info_dict[prop]))
        print()
 
        # convert the dictionary into DataFrame and print
        df=pd.DataFrame(list(account_info_dict.items()),columns=['property','value'])
        print("account_info() as dataframe:")
        print(df)
    print(mt5.version())
    # display info on the terminal settings and status
    terminal_info=mt5.terminal_info()
    if terminal_info!=None:
        # display the terminal data 'as is'
        print(terminal_info)
        # display data in the form of a list
        print("Show terminal_info()._asdict():")
        terminal_info_dict = mt5.terminal_info()._asdict()
        for prop in terminal_info_dict:
            print("  {}={}".format(prop, terminal_info_dict[prop]))
        print()
    # convert the dictionary into DataFrame and print
        df=pd.DataFrame(list(terminal_info_dict.items()),columns=['property','value'])
        print("terminal_info() as dataframe:")
        print(df)
else:
    print("failed to connect to trade account 25115284 with password=gqz0343lbdm, error code =",mt5.last_error())
 
# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()