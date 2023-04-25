from case.pages.KnowledgeIndex import KnowledgeIndex


class KnowledgeIndexTest(KnowledgeIndex):

    # 测试点击知识点列表
    def test_clickKnowledgeList(self):
        self.getElement('知识点列表')[0].click()
        ret = self.app.wait_for_page(self.route.get_page('知识点详情'))
        self.app.wait_util(0)
        self.page.wait_for(1)
        self.assertTrue(ret, '进入知识点详情页面成功')

