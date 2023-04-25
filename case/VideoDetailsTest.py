from case.pages.VideoDetails import VideoDetails


class VideoDetailsTest(VideoDetails):

    def test_001_collect(self):
        """
        测试收藏
        """
        # 获取收藏按钮
        collect = self.getElement("收藏")
        is_collect = self.getElement("收藏文本").inner_text == "收藏"
        # 点击收藏
        collect.tap()
        self.app.wait_util(0)
        self.page.wait_for(2)
        txt = self.getElement("收藏文本").inner_text
        if is_collect:
            # 判断是否收藏成功
            self.assertTrue(txt == "已收藏", "收藏成功")
        else:
            # 判断是否取消收藏成功
            self.assertTrue(txt == "收藏", "取消收藏成功")
