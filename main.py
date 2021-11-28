# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import datetime
import time

from ApproverControl import ApproverControl
from UserControl import UserControl
from WebDriverApproverContorl import WebDriverApproverContorl
from WebDriverUserContorl import WebDriverUserContorl

UserConfigPath = 'Z:\\AutoScript\\start'
ApproverConfigPath = 'Z:\\AutoScript\\Approver'
WebURL = 'http://20.3.237.1:7001/fund-capital/standard/'


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    while True:
        ApproverConfigList = ApproverControl().getApproverConfigList(ApproverConfigPath)
        for Approver in ApproverConfigList:
            print(str(datetime.datetime.now()) + ' ' + str(Approver.__dict__) + ' start.')
            print(Approver.__dict__)
            WebDriverInstance = WebDriverApproverContorl()
            WebDriverInstance.setURL(WebURL)
            try:
                logStatus = WebDriverInstance.logWEB(Approver)
            except IndexError:
                break

            if logStatus:
                SubmitStatus = WebDriverInstance.AutoSubmit(Approver)
            else:
                pass

            print(SubmitStatus)
            if SubmitStatus:
                closeStatus = WebDriverInstance.closeWEB(User)
                print(str(datetime.datetime.now()) + ' ' + str(User.__dict__) + ' succeed.')
            else:
                pass



        UserConfigList = UserControl().getUserConfigList(UserConfigPath)

        for User in UserConfigList:
            print(str(datetime.datetime.now()) + ' ' + str(User.__dict__) + ' start.')
            print(User.__dict__)
            WebDriverInstance = WebDriverUserContorl()
            WebDriverInstance.setURL(WebURL)
            try:
                logStatus = WebDriverInstance.logWEB(User)
            except IndexError:
                break

            if logStatus:
                SubmitStatus = WebDriverInstance.AutoSubmit(User)
            else:
                pass

            print(SubmitStatus)
            if SubmitStatus:
                closeStatus = WebDriverInstance.closeWEB(User)
                print(str(datetime.datetime.now()) + ' ' + str(User.__dict__) + ' succeed.')
            else:
                pass

        time.sleep(900)  # 15 mins




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
