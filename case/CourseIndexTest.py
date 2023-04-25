import minium
from case.base.Api import Api
from case.pages.CourseIndex import CourseIndex
import hashlib


@minium.ddt_class(testNameFormat="%(name)s_%(index)s")
class CourseIndexTest(CourseIndex):

    #     测试课程分类列表
    def test_001_courseCategoryList(self):
        """
        测试课程分类列表
        :return: None
        """
        # 获取当前 courseCurList
        courseCurList = self.getCourseCurList()
        # courseCurList转换为字符串，计算md5
        md5_last = hashlib.md5()
        md5_last.update(str(courseCurList).encode("utf-8"))
        md5_last = md5_last.hexdigest()
        self.logger.info("md5_last: %s" % md5_last)
        # 切换课程分类
        courseCategoryList = self.getElement("课程分类列表")
        self.assertTrue(len(courseCategoryList) > 0, "课程分类列表长度大于0")
        self.switchCourseCategory()
        self.app.wait_util(0)
        self.page.wait_for(1)
        # 获取新的 courseCurList
        courseCurList = self.getCourseCurList()
        md5_now = hashlib.md5()
        md5_now.update(str(courseCurList).encode("utf-8"))
        md5_now = md5_now.hexdigest()
        self.logger.info("md5_now: %s" % md5_now)
        # 判断md5是否相同
        self.assertNotEqual(md5_last, md5_now, "切换课程分类成功")

    @minium.ddt_case(
        minium.ddt_data(['搜索框', "搜索页", "跳转搜索页面成功"], name="搜索框"),
        minium.ddt_data(['知识点', "知识点", "跳转知识点页面成功"], name="知识点"),
        minium.ddt_data(['通关秘籍', "通关秘籍", "跳转通关秘籍页面成功"], name="通关秘籍"),
        minium.ddt_data(['章节练', "章节练", "跳转章节练页面成功"], name="章节练"),
        minium.ddt_data(['模拟考', "模拟考", "跳转模拟考页面成功"], name="模拟考"),
    )
    @minium.ddt_unpack
    def test_001_goToOtherPage(self, element, page, msg):
        """
        测试跳转到其他页面
        :param element: 控件
        :param page: 页面
        :param msg: 提示消息
        :return: None
        """
        self.getElement(element).tap()
        self.app.wait_util(0)
        self.assertTrue(self.app.wait_for_page(self.route.get_page(page)), msg)

    # 模拟打卡
    def test_002_simulateClockIn(self):
        """
        模拟打卡
        :return: None
        """
        self.mockStudyTime(300)
        self.page.wait_for(3)
        self.getElement("打卡").tap()
        # 根据当前还在不在课程页面判断打卡功能是否正常
        page = self.app.get_current_page()
        self.assertEqual(page, self.route.get_tabber("课程"), "打卡功能正常")

        self.mockStudyTime(1140)
        self.page.wait_for(3)
        self.getElement("打卡").tap()
        page = self.app.get_current_page()
        self.assertEqual(page, self.route.get_tabber("课程"), "打卡功能正常")

        self.mockStudyTime(1200, True)
        self.page.wait_for(3)
        self.getElement("打卡").tap()
        ret = self.app.wait_for_page(self.route.get_page("打卡"))
        self.assertTrue(ret, "打卡功能正常")
        self.app.restore_request()
