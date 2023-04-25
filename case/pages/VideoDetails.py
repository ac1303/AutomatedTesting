from case.base.BaseCase import BaseCase


class VideoDetails(BaseCase):
    def __init__(self, methodName="VideoDetails"):
        super().__init__(methodName)
        self.elementXpath = {
            "输入框": {
                "isList": False,
                "value": "/page/view/view[2]/view[last()-1]/view[2]/view[1]/input"
            },
            "评论": {
                "isList": False,
                "value": "/page/view/view[2]/view[last()-1]/view[2]/view[2]"
            },
            "收藏": {
                "isList": False,
                "value": "/page/view/view[2]/view[1]/view[4]/view/view"
            },
            "收藏文本": {
                "isList": False,
                "value": "/page/view/view[2]/view[1]/view[4]/view/view/text"
            },
            "观看次数": {
                "isList": False,
                "value": "/page/view/view[2]/view[1]/view[2]/view[2]"
            },
            "播放": {
                "isList": False,
                "value": "/page/view/view[1]/view/player/view/video/view[5]/view/view"
            },
            "评论列表": {
                "isList": True,
                "value": "/page/view/view[2]/view[4]/view/chating/view/scroll-view/view"
            }
        }

    def setUp(self):
        super().setUp()
        self.goToVideoDetails()

    def goToVideoDetails(self):
        self.app.switch_tab(self.route.get_tabber("首页"))
        self.app.wait_util(0)
        self.page.wait_for(1)
        page = self.app.get_current_page()
        fitnessTipsList = page.data["fitnessTipsList"]
        self.fitnessTipsList = fitnessTipsList
        # 判断self.fitnessTipsList是否为空
        if self.fitnessTipsList:
            # 获取第一个视频跳转地址
            url = self.fitnessTipsList[0].get("link")
            # 进行跳转
            self.app.navigate_to("/" + url)
            self.app.wait_for_page(self.route.get_page("视频详情"))
            self.page.wait_for(2)
        else:
            self.logger.warn("无法跳转到视频详情页，因为 fitnessTipsList is None")

