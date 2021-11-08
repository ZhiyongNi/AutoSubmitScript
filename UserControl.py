import base64
import json
import os

from UserDict import UserDict


class UserControl:

    @staticmethod
    def getUserConfigList(path):
        UserFileList = []
        for home, dirs, files in os.walk(path):
            for filename in files:
                # 文件名列表，包含完整路径
                UserFileList.append(os.path.join(home, filename))
                # # 文件名列表，只包含文件名
        print(UserFileList)

        UserConfigList = []
        for UserFile in UserFileList:
            file = open(UserFile, 'r')
            JsonTmp = json.load(file)
            UserTmp = UserDict()
            UserTmp.UserName = JsonTmp['UserName']
            UserTmp.UserPassword = JsonTmp['UserPassword']
            # UserTmp.UserPassword = base64.decodestring(JsonTmp['UserPassword']).decode()
            UserTmp.PickProduct = JsonTmp['PickProduct']
            UserTmp.PickPortfolio = JsonTmp['PickPortfolio']
            UserTmp.RunningClock = JsonTmp['RunningClock']
            UserConfigList.append(UserTmp)

        return UserConfigList
