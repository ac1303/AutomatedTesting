from case.base.BaseCase import BaseCase


class Search(BaseCase):
    def __init__(self, methodName="Search"):
        super().__init__(methodName)
        self.elementXpath = {
            "搜索框": {
                "isList": False,
                "value": "/page/view/view[1]/view[1]/input"
            },
            "取消": {
                "isList": False,
                "value": "/page/view/view[1]/view[2]"
            },
            "删除全部搜索记录": {
                "isList": False,
                "value": "/page/view/search-history/view/view[1]/view[1]/image"
            },
            "搜索记录-标题": {
                "isList": False,
                "value": "/page/view/search-history/view/view[1]/view[1]/text"
            },
            "搜索记录": {
                "isList": True,
                "value": "/page/view/search-history/view/view[1]/view[2]/view"
            },
            "第一条搜索记录": {
                "isList": False,
                "value": "/page/view/search-history/view/view[1]/view[2]/view[1]/view"
            },
            "删除第一条搜索记录": {
                "isList": False,
                "value": "/page/view/search-history/view/view[1]/view[2]/view[1]/image"
            },
            "知识点": {
                "isList": False,
                "value": "/page/view/search-list/view/view[1]/u-tabs/view/view/scroll-view/view/view[1]"
            },
            "动作": {
                "isList": False,
                "value": "/page/view/search-list/view/view[1]/u-tabs/view/view/scroll-view/view/view[2]"
            },
            "视频": {
                "isList": False,
                "value": "/page/view/search-list/view/view[1]/u-tabs/view/view/scroll-view/view/view[3]"
            },
            "文章": {
                "isList": False,
                "value": "/page/view/search-list/view/view[1]/u-tabs/view/view/scroll-view/view/view[4]"
            },
            "课程": {
                "isList": False,
                "value": "/page/view/search-list/view/view[1]/u-tabs/view/view/scroll-view/view/view[5]"
            },
            "搜索结果列表": {
                "isList": True,
                "value": "/page/view/search-list/view/view[3]/view/view"
            }
        }

    def setUp(self):
        super().setUp()
        self.goToSearch()

    def goToSearch(self):
        """
        进入搜索页面
        :return: None
        """
        self.app.navigate_to(self.route.get_page("搜索页"))
        ret = self.app.wait_for_page(self.route.get_page("搜索页"))
        self.app.wait_util(0)
        self.page.wait_for(1)
        self.assertTrue(ret, "跳转搜索页面成功")
