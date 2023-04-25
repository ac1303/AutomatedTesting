from case.base.BaseCase import BaseCase


class MineUserInfo(BaseCase):
    def __init__(self, methodName="MineUserInfo"):
        super().__init__(methodName)
        self.elementXpath = {
            "头像": {
                "isList": False,
                "value": "/page/view/view[1]/view[2]/button"
            },
            "昵称": {
                "isList": False,
                "value": "/page/view/view[2]/view[2]/input"
            },
            "返回": {
                "isList": False,
                "value": "/page/view/u-navbar/view/view[1]/view[2]/view[1]/view/u-icon/view/text"
            },
            "手机号": {
                "isList": False,
                "value": "/page/view/view[3]/view[2]"
            },
            "清理缓存": {
                "isList": False,
                "value": "/page/view/view[4]"
            }
        }

    def setUp(self):
        super().setUp()
        self.goToMineUserInfo()

    def goToMineUserInfo(self):
        """
        进入个人信息页面
        :return: None
        """
        self.app.navigate_to(self.route.get_page("我的资料"))
        ret = self.app.wait_for_page(self.route.get_page("我的资料"))
        self.app.wait_util(0)
        self.page.wait_for(1)
        self.assertTrue(ret, "跳转个人信息页面成功")




