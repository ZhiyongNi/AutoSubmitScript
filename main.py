# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import datetime
import time

from UserControl import UserControl
from WebDriverContorl import WebDriverContorl

UserConfigPath = 'Z:\\AutoScript\\start'
WebURL = 'http://20.3.237.1:7001/fund-capital/standard/'


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    while True:
        UserConfigList = UserControl().getUserConfigList(UserConfigPath)

        for User in UserConfigList:
            print(str(datetime.datetime.now()) + ' ' + str(User.__dict__) + ' start.')
            print(User.__dict__)
            WebDriverInstance = WebDriverContorl()
            WebDriverInstance.setURL(WebURL)
            try:
                logStatus = WebDriverInstance.logWEB(User)
            except IndexError:
                break

            if logStatus:
                SubmitStatus = WebDriverInstance.AutoSubmit(User)
            else:
                pass

            if SubmitStatus:
                closeStatus = WebDriverInstance.closeWEB(User)
                print(str(datetime.datetime.now()) + ' ' + str(User.__dict__) + ' succeed.')
            else:
                pass

        time.sleep(900)  # 15 mins
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
