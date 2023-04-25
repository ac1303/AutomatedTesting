import json

from case.base.Api import Api
from case.base.BaseCase import BaseCase


class PractiseIndex(BaseCase):
    def __init__(self, methodName="PractiseIndex"):
        super().__init__(methodName)
        self.elementXpath = {
            "课程类型": {
                "isList": False,
                "value": "/page/view/u-navbar/view/view[1]/view[2]/view[2]/view/view/picker"
            },
            "答题记录": {
                "isList": False,
                "value": "/page/view/view/view[1]/view[1]/view[1]"
            },
            "错题本": {
                "isList": False,
                "value": "/page/view/view/view[1]/view[2]/view[1]"
            },
            "正确率": {
                "isList": False,
                "value": "/page/view/view/view[1]/view[3]/view[1]"
            },
            "笔记夹": {
                "isList": False,
                "value": "/page/view/view/view[2]/view[4]/view[1]"
            },
        }

    def setUp(self):
        super().setUp()
        self.goToPractiseIndex()

    def goToPractiseIndex(self):
        self.app.switch_tab(self.route.get_tabber("练习"))
        ret = self.app.wait_for_page(self.route.get_tabber("练习"))
        self.app.wait_util(0)
        self.page.wait_for(1)
        self.assertTrue(ret, "进入练习页面成功")

    # 切换课程类型
    def changeCourseType(self, courseType: str = None):
        typeList = self.page.data["typeList"]
        picker = self.page.get_element("picker")
        picker.click()
        if courseType is not None:
            for i in range(len(typeList)):
                if typeList[i]["cname"] == courseType:
                    picker.click()
                    picker.pick(i)
        else:
            typeIndex = self.page.data["typeIndex"]
            if int(typeIndex) == 1:
                picker.pick(0)
            else:
                picker.pick(1)
        self.app.wait_util(0)
        self.page.wait_for(1)

    #     获取当前课程类型的id
    def getCourseTypeId(self):
        typeList = self.page.data["typeList"]
        typeIndex = self.page.data["typeIndex"]
        return typeList[typeIndex]["id"]

    # 记录已答题目数量
    def recordAnswerCount(self):
        api = Api(self)
        # 获取课程数据
        params = {
            "subject": self.getCourseTypeId(),
            "page": 1,
            "limit": 200
        }
        resp = api.request("答题记录", **params)
        answerList = json.loads(resp.text)
        self.logger.info("答题记录接口返回数据：%s" % answerList)
        answerCountMap = {}
        answerList = answerList["list"]
        for answer in answerList:
            # 判断pid是否存在，不存在将ans保存 pid为key，ans为value，若是存在则比较ans大小，取大的
            ans = int(answer["ans"])
            if answer["pid"] in answerCountMap:
                if answerCountMap[answer["pid"]] < ans:
                    answerCountMap[answer["pid"]] = ans
            else:
                answerCountMap[answer["pid"]] = ans
        # 对map中的所有value求和
        answerCount = 0
        for key in answerCountMap:
            answerCount += answerCountMap[key]
        return answerCount

    # 统计错题数量
    def recordErrorCount(self):
        api = Api(self)
        # 获取课程数据
        params = {
            "subject": self.getCourseTypeId(),
            "page": 1,
            "limit": 200
        }
        resp = api.request("错题记录", **params)
        resp = json.loads(resp.text)
        self.logger.info("错题记录接口返回数据：%s" % resp)
        dataList = resp["data"]["list"]
        count = 0
        for item in dataList:
            count += int(item["num"])
        return count



    # 获取统计数据
    def getStatisticsData(self, name):
        statisticsData = self.page.data["statisticsData"]
        data = {
            "已答题目": statisticsData["totalnum"],
            "所有题目": statisticsData["allnum"],
            "正确题目": statisticsData["rightnum"],
            "错误题目": statisticsData["errornum"],
            "正确率": statisticsData["correctrate"],
            "训练记录": statisticsData["planNum"],
        }
        return data[name]
