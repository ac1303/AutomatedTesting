from case.pages.MineIndex import MineIndex
import minium


@minium.ddt_class(testNameFormat="%(name)s_%(index)s")
class MineIndexTest(MineIndex):

    # 测试跳转其他页面
    @minium.ddt_case(
        minium.ddt_data(["昵称", "我的资料"], name="我的资料"),
        minium.ddt_data(["打卡次数", "打卡日历"], name="打卡次数"),
        minium.ddt_data(["学分总计", "礼品商城"], name="学分总计"),
        minium.ddt_data(["累计时长", "排行榜"], name="累计时长"),
        minium.ddt_data(["我的收藏", "我的收藏"], name="我的收藏"),
        minium.ddt_data(["我的购买", "我的购买"], name="我的购买"),
        minium.ddt_data(["兑换记录", "我的礼品"], name="兑换记录"),
        minium.ddt_data(["我的勋章", "我的勋章"], name="我的勋章"),
        minium.ddt_data(["我的证书", "我的证书"], name="我的证书"),
        minium.ddt_data(["学习提醒", "学习提醒"], name="学习提醒"),
    )
    @minium.ddt_unpack
    def test_001_goToOtherPage(self, element, page):
        """
        测试跳转其他页面
        :param element: 控件元素
        :param page: 跳转页面
        :return: None
        """
        self.getElement(element).tap()
        self.app.wait_util(0)
        self.page.wait_for(1)
        ret = self.app.wait_for_page(self.route.get_page(page))
        self.assertTrue(ret, "跳转成功")

    # 测试切换科目
    def test_001_switchSubject(self):
        """
        测试切换科目
        :return: None
        """
        subjectId = self.getSubjectId()
        self.switchSubject()
        newSubjectId = self.getSubjectId()
        self.assertNotEqual(subjectId, newSubjectId, "切换科目成功")



