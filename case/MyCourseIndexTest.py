import json

from case.base.Api import Api
from case.pages.MyCourseIndex import MyCourseIndex


class MyCourseIndexTest(MyCourseIndex):

    # 测试前往打卡日历
    def test_001_goToCalendar(self):
        self.getElement("学习日历").tap()
        ret = self.app.wait_for_page(self.route.get_page("打卡日历"))
        self.assertTrue(ret, "跳转我的课程首页成功")

    # 测试前往学习排名页面
    def test_001_goToStudyRank(self):
        # 获取排名
        rank = self.getElement("本周排行").inner_text
        self.getElement("学习排名").tap()
        ret = self.app.wait_for_page(self.route.get_page("排行榜"))
        self.assertTrue(ret, "跳转排行榜成功")
        #         如果排名是前十名，则再判断用户名是否一致
        if int(rank) <= 10:
            # 获取用户昵称
            api = Api(self)
            resp = api.request("用户信息")
            userInfo = json.loads(resp.text)
            self.app.wait_util(0)
            self.page.wait_for(1)
            # 获取排名
            showTimeRanklist = self.page.data["showTimeRanklist"]
            self.logger.info("排名为：%s" % rank)
            self.logger.info("用户名为：%s" % userInfo["user"]["user_name"])
            self.logger.info("排名昵称为：%s" % showTimeRanklist[int(rank) - 1]["user_name"])
            self.assertEqual(showTimeRanklist[int(rank) - 1]["user_name"], userInfo["user"]["user_name"], "排名正确")

    # 测试继续学习
    def test_001_continueStudy(self):
        cid = self.get_last_course()
        self.getElement("继续学习").tap()
        self.app.wait_util(0)
        self.page.wait_for(1)
        self.assertEqual(self.page.data["courseId"], cid, "跳转课程成功")
        self.app.navigate_back()
        self.app.wait_util(0)
        self.page.wait_for(1)
        #         测试更新上次观看的课程
        last = self.getElement("上次观看").inner_text
        self.switch_course()
        self.app.wait_util(0)
        self.page.wait_for(1)
        new = self.getElement("上次观看").inner_text
        self.assertNotEqual(last, new, "更新上次观看的课程成功")
        self.page.wait_for(100)

    # 测试前往激活课程
    def test_001_goToActiveCourse(self):
        self.getElement("激活课程").tap()
        ret = self.app.wait_for_page(self.route.get_page("激活课程"))
        self.assertTrue(ret, "跳转激活课程成功")
