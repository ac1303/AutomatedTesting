from case.base.Api import Api
from case.base.BaseCase import BaseCase


class MyCourseIndex(BaseCase):
    def __init__(self, methodName="MyCourseIndex"):
        super().__init__(methodName)
        self.elementXpath = {
            "学习日历": {
                "isList": False,
                "value": "/page/view/view/view[2]/view[1]"
            },
            "学习排名": {
                "isList": False,
                "value": "/page/view/view/view[2]/view[2]"
            },
            "本周排行": {
                "isList": False,
                "value": "/page/view/view/view[2]/view[2]/view[1]/text"
            },
            "课程列表": {
                "isList": True,
                "value": "/page/view/view/view[4]/view"
            },
            "继续学习": {
                "isList": False,
                "value": "/page/view/view/view[3]/view[2]/view[2]"
            },
            "上次观看": {
                "isList": False,
                "value": "/page/view/view/view[3]/view[2]/view[1]/view"
            },
            "激活课程": {
                "isList": False,
                "value": "/page/view/view/view[1]/view"
            }
        }

    def setUp(self):
        super().setUp()
        self.goToMyCourseIndex()

    def goToMyCourseIndex(self):
        """
        进入我的课程首页
        :return: None
        """
        self.app.navigate_to(self.route.get_page("我的课程"))
        ret = self.app.wait_for_page(self.route.get_page("我的课程"))
        self.app.wait_util(0)
        self.page.wait_for(1)
        self.assertTrue(ret, "跳转我的课程首页成功")

    # 获取上次观看的课程
    def get_last_course(self):
        history = self.page.data["myCourseInfo"]["history"]
        # {
        #     "cid": 189,
        #     "cpid": 679,
        #     "name": "第一课：课程介绍",
        # }
        return history["cid"]

    # 课程列表
    def get_course_list(self):
        return self.page.data["myCourseInfo"]["course_list"]

    # 切换
    def switch_course(self):
        cid = self.get_last_course()
        course_list = self.get_course_list()
        # 跳转的课程id
        jump_cid = 0
        for course in course_list:
            if course["id"] != cid:
                jump_cid = course["id"]
                break
        if jump_cid == 0:
            self.logger.warn("没有可跳转的课程")
            return
        self.app.navigate_to(self.route.get_page("课程详情"), {"cid": int(jump_cid)})
        self.app.wait_for_page(self.route.get_page("课程详情"))
        self.app.wait_util(0)
        self.page.wait_for(1)
        catalog = self.page.data["courseInfo"]["catalog"][0]
        params = {
            "cid": int(jump_cid),
            "cpid": catalog["id"],
            "vtime": catalog["is_see"],
        }
        self.app.navigate_to(self.route.get_page("课程详情-章节"), params)
        self.page.wait_for(1)
        self.app.wait_for_page(self.route.get_page("课程详情-章节"))
        self.app.wait_util(0)
        self.page.wait_for(2)
        currentVideo = self.page.data["currentVideo"]
        api = Api(self)
        params = {
            "cid": int(currentVideo["id"]),  # 课程id
            "percentage": 4,  # 观看百分比
            "see_time": int(currentVideo["see_time"]),  # 观看时长
            "time": 1,  # 本次打点持续时间
            "rid": 0,  # 打点id，第一次打点为0
            "type": 1,  # ？未知，默认为1
            "duration": int(currentVideo["duration"]),  # 视频总时长
        }
        api.request("视频打点", **params)
        self.app.navigate_back(2)
