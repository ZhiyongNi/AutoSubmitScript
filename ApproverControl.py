import base64
import json
import os

from ApproverDict import ApproverDict
from UserDict import UserDict


class ApproverControl:

    @staticmethod
    def getApproverConfigList(path):
        ApproverFileList = []
        for home, dirs, files in os.walk(path):
            for filename in files:
                # 文件名列表，包含完整路径
                ApproverFileList.append(os.path.join(home, filename))
                # # 文件名列表，只包含文件名
        print(ApproverFileList)

        ApproverConfigList = []
        for ApproverFile in ApproverFileList:
            file = open(ApproverFile, 'r')
            JsonTmp = json.load(file)
            ApproverTmp = ApproverDict()
            ApproverTmp.UserName = JsonTmp['UserName']
            ApproverTmp.UserPassword = JsonTmp['UserPassword']
            # UserTmp.UserPassword = base64.decodestring(JsonTmp['UserPassword']).decode()
            ApproverTmp.PickProduct = JsonTmp['PickProduct']
            ApproverTmp.PickPortfolio = JsonTmp['PickPortfolio']
            ApproverTmp.RunningClock = JsonTmp['RunningClock']
            ApproverConfigList.append(ApproverTmp)

        return ApproverConfigList
