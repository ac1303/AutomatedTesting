from case.base.Api import Api
from case.base.BaseCase import BaseCase


class CourseIndex(BaseCase):
    def __init__(self, methodName="CourseIndex"):
        super().__init__(methodName)
        self.elementXpath = {
            "课程分类列表": {
                "isList": True,
                "value": "/page/view/view/view[1]/u-tabs/view/view/scroll-view/view/view"
            },
            "搜索框": {
                "isList": False,
                "value": "/page/view/view/view[2]/view[1]"
            },
            "课程列表": {
                "isList": True,
                "value": "/page/view/view/view[3]/card[1]/view/view[2]/view"
            },
            "知识点": {
                "isList": False,
                "value": "/page/view/view/view[3]/view/view[1]"
            },
            "通关秘籍": {
                "isList": False,
                "value": "/page/view/view/view[3]/view/view[2]"
            },
            "章节练": {
                "isList": False,
                "value": "/page/view/view/view[3]/view/view[3]"
            },
            "模拟考": {
                "isList": False,
                "value": "/page/view/view/view[3]/view/view[4]"
            },
            "备考攻略": {
                "isList": True,
                "value": "/page/view/view/view[3]/card[2]/view/view[2]/view"
            },
            "打卡": {
                "isList": False,
                "value": "/page/view/view/view[3]/sign-in-icon/view/view"
            },
            "设置学习提醒": {
                "isList": False,
                "value": "/page/view/view/view[3]/sign-in-icon/view/sign-in-poup/view/view[2]/view[4]"
            },
        }

    def setUp(self):
        super().setUp()
        self.app.wait_util(0)
        self.page.wait_for(1)
        page = self.app.get_current_page()
        self.assertEqual(page, self.route.get_tabber("课程"), "进入课程首页")

    def goToCourseIndex(self):
        """
        进入课程首页
        :return: None
        """
        ret = self.mini.app.wait_for_page(self.route.get_tabber("课程"))
        self.app.wait_util(0)
        self.assertTrue(ret, "跳转课程首页成功")

    # 切换当前课程分类
    def switchCourseCategory(self, category=None):
        """category为None时，若当前索引为0，则切换到1，否则切换到0"""
        courseSubjectList = self.getElement("课程分类列表")
        if category is None:
            selectTabIndex = self.page.data["selectTabIndex"]
            if selectTabIndex == 0:
                courseSubjectList[1].tap()
            else:
                courseSubjectList[0].tap()

    #     TODO 等以后需要切换到其他分类时，再写

    def getCourseCurList(self):
        """
        获取当前课程列表
        :return: list
        """
        return self.page.data["courseCurList"]

#     增加观看时间
    def addWatchTime(self, time):
        """
        增加观看时间
        :param time:  增加的时间
        :return: None
        """
        # 先获取某个课程章节的id
        self.getElement("课程列表")[0].tap()
        self.app.wait_util(0)
        self.page.wait_for(1)
        ChapterId = self.page.data["courseInfo"]["catalog"][0]["id"]
        self.app.navigate_back(1)
        params = {
            "cid": ChapterId,
            "percentage": "0.1",
            "see_time": "1",
            "time": time,
            "rid": "0",
            "type": "1",
            "duration": "1",
        }
        api = Api(self)
        resp = api.request("视频打点", **params)
        self.logger.info("第一次视频打点返回结果: %s" % resp.json())
        # params["rid"] = resp.json()["data"]["rid"]
        # params["time"] = "60"
        # resp = api.request("视频打点", **params)
        # self.logger.info("第二次视频打点返回结果: %s" % resp.json())
        return resp

#     mock学习时长的接口,需要释放mock
    def mockStudyTime(self, time, signin: bool = False):
        self.app.restore_request()
        mock_resp = {"data":
            {
                "yx_times": time,
                "sd_times": "1200",
                "data": False,
                "sy_times": 1140,
                "code": 1 if signin else 0,
                "msg": "mock返回数据"
            },
            "statusCode": 200}
        mock_rule = {
            "url": "user/clocking",
        }
        self.app.mock_request(rule=mock_rule, success=mock_resp)

