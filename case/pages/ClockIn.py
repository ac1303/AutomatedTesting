from case.base.BaseCase import BaseCase


class ClockIn(BaseCase):
    def __init__(self, methodName="ClockIn"):
        super().__init__(methodName)
        self.elementXpath = {
            "上传图片": {
                "isList": False,
                "value": "/page/view/view/view[1]/view[3]/view/image"
            },
            "删除图片": {
                "isList": False,
                "value": "/page/view/view/view[1]/view[3]/view/view"
            },
            "生成分享图": {
                "isList": False,
                "value": "/page/view/view/view[3]/view"
            },
            "分享打卡": {
                "isList": False,
                "value": "/page/view/view/view[3]/button"
            },
            "图片库": {
                "isList": True,
                "value": "/page/view/view/view[2]/view[2]/view"
            },
            "设置为打卡图片": {
                "isList": False,
                "value": "/page/view/view[2]"
            },

        }

    def setUp(self):
        super().setUp()
        self.goToClockInPage()

    def goToClockInPage(self):
        self.app.navigate_to(self.route.get_page("打卡"))
        self.app.wait_util(0)
        self.page.wait_for(1)
        ret = self.app.wait_for_page(self.route.get_page("打卡"))
        self.assertTrue(ret, "进入打卡页面成功")

