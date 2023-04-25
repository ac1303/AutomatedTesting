from case.base.BaseCase import BaseCase


class KnowledgeIndex(BaseCase):
    def __init__(self, methodName='KnowledgeIndex'):
        super().__init__(methodName)
        self.elementXpath = {
            "知识点列表": {
                "isList": True,
                "value": "/page/view/view/view",
            }
        }

    def setUp(self):
        super().setUp()
        self.goToKnowledgeIndex()

    def goToKnowledgeIndex(self):
        params = {
            'id': 2,
            'cname': 'NSCA-CPT'
        }
        self.app.navigate_to(self.route.get_page('知识点'),params=params)
        ret = self.app.wait_for_page(self.route.get_page('知识点'))
        self.app.wait_util(0)
        self.page.wait_for(1)
        self.assertTrue(ret, '进入知识点页面成功')
