import hashlib
import minium
from case.pages.PractiseIndex import PractiseIndex


@minium.ddt_class(testNameFormat="%(name)s_%(index)s")
class PractiseIndexTest(PractiseIndex):

    # 测试切换课程类型
    def test_001_changeCourseType(self):
        # 获取课程数据
        dataList = self.page.data["dataList"]
        # 计算课程数据的md5值
        md5 = hashlib.md5()
        md5.update(str(dataList).encode("utf-8"))
        md5Value = md5.hexdigest()
        # 切换课程类型
        self.changeCourseType()
        self.app.wait_util(0)
        self.page.wait_for(1)
        # # 获取切换后的课程数据
        dataList = self.page.data["dataList"]
        # 计算切换后的课程数据的md5值
        md5 = hashlib.md5()
        md5.update(str(dataList).encode("utf-8"))
        md5Value2 = md5.hexdigest()
        # 判断两个md5值是否相等
        self.assertNotEqual(md5Value, md5Value2, "切换课程类型成功")

    # 测试答题数量
    def test_001_answerCount(self):
        # 获取答题记录接口返回的答题数量
        count = self.recordAnswerCount()
        self.logger.info("答题记录接口返回的答题数量：%s" % count)
        # 获取页面上的答题数量
        totalnum = self.getStatisticsData("已答题目")
        self.logger.info("页面上的答题数量：%s" % totalnum)
        self.assertEqual(count, totalnum, "答题数量正确")

    # 测试错题数量
    def test_001_errorCount(self):
        count = self.recordErrorCount()
        self.logger.info("错题记录接口返回的错题数量：%s" % count)
        # 获取页面上的答题数量
        errornum = self.getStatisticsData("错误题目")
        self.logger.info("页面上的错题数量：%s" % errornum)
        self.assertEqual(count, errornum, "错题数量正确")

    # 测试答题正确率
    def test_001_answerRate(self):
        # 获取页面上的正确率
        rate2 = self.getStatisticsData("正确率")
        self.logger.info("页面上的正确率：%s" % rate2)

        totalnum = self.getStatisticsData("已答题目")
        errornum = self.getStatisticsData("错误题目")
        if totalnum == 0:
            self.assertEqual(rate2, 0, "正确率正确")
            return
        # 计算正确率,保留两位小数,四舍五入
        rate = round((totalnum - errornum) / totalnum, 2)
        self.logger.info("正确率：%s" % rate)
        self.assertEqual(rate, rate2, "正确率正确")

    # 测试跳转
    @minium.ddt_case(
        minium.ddt_data(["答题记录", "答题记录"], name="答题记录"),
        minium.ddt_data(["错题本", "错题本"], name="错题记录"),
        minium.ddt_data(["正确率", "成绩单"], name="正确率"),
        minium.ddt_data(["笔记夹", "笔记夹"], name="笔记夹"),
    )
    @minium.ddt_unpack
    def test_001_goToOtherPage(self, element, page):
        self.getElement(element).tap()
        self.app.wait_util(0)
        self.page.wait_for(1)
        ret = self.app.wait_for_page(self.route.get_page(page))
        self.assertTrue(ret, "跳转成功")

