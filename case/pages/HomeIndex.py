from case.base.BaseCase import BaseCase


class HomeIndex(BaseCase):
    def __init__(self, methodName="HomeIndex"):
        super().__init__(methodName)
        self.elementXpath = {
            "搜索框": {
                "isList": False,
                "value": "/page/scroll-view/view/view[1]/view/view/input"
            },
            "动作库": {
                "isList": False,
                "value": "/page/scroll-view/view/view[4]/view[1]"
            },
            "换礼品": {
                "isList": False,
                "value": "/page/scroll-view/view/view[4]/view[2]"
            },
            "送教材": {
                "isList": False,
                "value": "/page/scroll-view/view/view[4]/view[3]"
            },
            "复制": {
                "isList": False,
                "value": "/page/scroll-view/view/customer-service/view/u-popup[2]/view/view/view["
                         "1]/scroll-view/view/view[2]/text[2]"
            },
            "激活码": {
                "isList": False,
                "value": "/page/scroll-view/view/view[4]/view[4]"
            },
            "特色课程": {
                "isList": False,
                "value": "/page/scroll-view/view/view[5]/view[2]/view"
            },
            "健身小知识-查看更多": {
                "isList": False,
                "value": "/page/scroll-view/view/view[6]/view/view"
            },
            "健身小知识-视频列表": {
                "isList": True,
                "value": "/page/scroll-view/view/view[6]/scroll-view/view"
            }
        }

    def setUp(self):
        super().setUp()
        self.goToHome()

    def goToHome(self):
        # 进入首页
        self.app.switch_tab(self.route.get_tabber("首页"))
        ret = self.app.wait_for_page(self.route.get_tabber("首页"))
        self.app.wait_util(0)
        self.page.wait_for(1)
        self.assertTrue(ret, "跳转首页成功")
