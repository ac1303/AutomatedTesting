from case.base.BaseCase import BaseCase


class ActivationCode(BaseCase):
    def __init__(self, methodName="ActivationCode"):
        super().__init__(methodName)
        self.elementXpath = {
            "激活码输入框": {
                "isList": False,
                "value": "/page/view/view[1]/input"
            },
            "立即激活": {
                "isList": False,
                "value": "/page/view/view[2]"
            },
            "激活记录": {
                # 激活记录是一个列表，但是需要从第二个view开始，第一个view是标题
                "isList": True,
                "value": "/page/view/view[3]/view"
            },
        }

    def setUp(self):
        super().setUp()
        self.goToActivationCode()

    def goToActivationCode(self):
        # 进入激活码页面
        self.mini.app.navigate_to(self.route.get_page("激活码页"))
        ret = self.mini.app.wait_for_page(self.route.get_page("激活码页"))
        self.app.wait_util(0)
        self.mini.assertTrue(ret, "跳转激活码页面成功")
