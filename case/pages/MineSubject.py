from case.base.BaseCase import BaseCase


class MineSubject(BaseCase):
    def __init__(self, methodName="MineSubject"):
        super().__init__(methodName)
        self.elementXpath = {
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
        self.goToMineSubject()

    def goToMineSubject(self):
        """
        进入我的科目页面
        """
        params = {
            "id": 20,
        }
        self.app.navigate_to(self.route.get_page("选择科目"))
        self.app.wait_util(0)
        self.page.wait_for(1)
        ret = self.app.wait_for_page(self.route.get_page("选择科目"))
        self.assertTrue(ret, "跳转成功")
