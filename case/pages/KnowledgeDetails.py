from case.base.BaseCase import BaseCase


class KnowledgeDetails(BaseCase):
    def __init__(self, methodName='KnowledgeDetails'):
        super().__init__(methodName)
        self.elementXpath = {
            "笔记": {
                "isList": False,
                "value": "/page/view/add-notes-to-pdf/view/view"
            },
            "记笔记": {
                "isList": False,
                "value": "/page/view/view[2]/poup-chating/view/view[2]/scroll-view/view/view[2]/view[1]/view/view[2]/view[2]"
            },
            "笔记内容": {
                "isList": False,
                "value": "/page/view/view[1]/textarea"
            },
            "笔记内容-弹窗": {
                "isList": False,
                "value": "/page/view/view[2]/poup-chating/view/view[2]/scroll-view/view/view[2]/view[2]/chating/view/scroll-view/view/view/view[2]/view[2]"
            },
            "保存": {
                "isList": False,
                "value": "/page/view/view[3]"
            },
            "公开": {
                "isList": False,
                "value": "/page/view/view[2]/view"
            },
            "删除": {
                "isList": False,
                "value": "/page/view/view[2]/poup-chating/view/view[2]/scroll-view/view/view[2]/view[1]/view/view[1]/view[2]/image[2]"
            },
        }

    def setUp(self):
        super().setUp()
        self.goToKnowledgeDetails()

    def goToKnowledgeDetails(self):
        #     id=37&page=1&limit=20&cid=2
        params = {
            'id': 37,
            'page': 1,
            'limit': 20,
            'cid': 2
        }
        self.app.navigate_to(self.route.get_page('知识点详情'), params=params)
        ret = self.app.wait_for_page(self.route.get_page('知识点详情'))
        self.app.wait_util(0)
        self.page.wait_for(1)
        self.assertTrue(ret, '进入知识点详情页面成功')
