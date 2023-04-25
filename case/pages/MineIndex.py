from case.base.BaseCase import BaseCase
from case.pages.MineSubject import MineSubject


class MineIndex(BaseCase):
    def __init__(self, methodName="MineIndex"):
        super().__init__(methodName)
        self.elementXpath = {
            "昵称": {
                "isList": False,
                "value": "/page/view/view[1]/view/view/view[1]/view[1]"
            },
            "打卡次数": {
                "isList": False,
                "value": "/page/view/view[2]/view[1]"
            },
            "学分总计": {
                "isList": False,
                "value": "/page/view/view[2]/view[2]"
            },
            "累计时长": {
                "isList": False,
                "value": "/page/view/view[2]/view[3]"
            },
            "当前科目": {
                "isList": False,
                "value": "/page/view/view[3]"
            },
            "我的收藏": {
                "isList": False,
                "value": "/page/view/view[4]/view[2]/view[1]"
            },
            "我的购买": {
                "isList": False,
                "value": "/page/view/view[4]/view[2]/view[2]"
            },
            "兑换记录": {
                "isList": False,
                "value": "/page/view/view[4]/view[2]/view[3]"
            },
            "我的勋章": {
                "isList": False,
                "value": "/page/view/view[4]/view[2]/view[4]"
            },
            "我的证书": {
                "isList": False,
                "value": "/page/view/view[4]/view[2]/view[5]"
            },
            "学习提醒": {
                "isList": False,
                "value": "/page/view/view[4]/view[2]/view[8]"
            },
            # 以下时选择科目页面的元素
            "ACE-CPT": {
                "isList": False,
                "value": "/page/view/view[1]/view[2]/view"
            },
            "NSCA-CPT": {
                "isList": False,
                "value": "/page/view/view[2]/view[2]/view[1]"
            },
        }

    def setUp(self):
        super().setUp()
        self.goToMineIndex()

    def goToMineIndex(self):
        """
        进入我的首页
        :return: None
        """
        self.app.switch_tab(self.route.get_tabber("我的"))
        ret = self.app.wait_for_page(self.route.get_tabber("我的"))
        self.app.wait_util(0)
        self.page.wait_for(1)
        self.assertTrue(ret, "跳转我的首页成功")

    def getSubjectId(self):
        """
        获取当前科目的id
        :return: 科目id
        """
        return self.page.data["userInfo"]["subject"]

    def getSubjectName(self):
        """
        获取当前科目的名称
        :return: 科目名称
        """
        return self.page.data["userInfo"]["subject_name"]

    def switchSubject(self):
        """
        切换科目
        :return: None
        """
        subName = self.getSubjectName()
        self.getElement("当前科目").tap()
        self.app.wait_util(0)
        self.page.wait_for(1)
        ret = self.app.wait_for_page(self.route.get_page("选择科目"))
        self.assertTrue(ret, "跳转成功")
        if subName == "ACE-CPT":
            self.getElement("NSCA-CPT").tap()
        else:
            self.getElement("ACE-CPT").tap()
        self.app.wait_util(0)
        self.page.wait_for(1)
        self.app.navigate_back()
        self.app.wait_util(0)
        self.page.wait_for(1)


