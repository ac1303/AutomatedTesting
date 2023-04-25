from case.pages.HomeIndex import HomeIndex
from minium import Callback
import minium


class HomeIndexTest(HomeIndex):

    @minium.skip(reason="确定跳转后存在一些问题，暂时跳过")
    def test_009_clickAction(self):
        """
        点击动作库
        """
        callback = Callback()  # 监听回调, 阻塞当前主线程
        # 监听showModal回调, 确认由弹窗弹出
        self.app.hook_wx_method("showModal", callback=callback.callback)

        ret = self.page.wait_for(self.getElementPath("动作库"), max_timeout=10)
        self.assertTrue(ret, "动作库存在")
        self.getElement("动作库").tap()
        self.page.wait_for(1)

        result = self.native.handle_modal("允许")
        self.app.release_hook_wx_method("showModal")
        # 无法通关回调判断弹窗是否被点击，所以只能通过判断handle_modal的返回值来判断
        self.assertIsNotNone(result, "点击弹窗成功")

    # 点击换礼品
    def test_001_clickGift(self):
        """
        点击换礼品，跳转礼品商城
        """
        ret = self.page.wait_for(self.elementXpath["换礼品"]["value"], max_timeout=10)
        self.assertTrue(ret, "换礼品存在")
        self.getElement("换礼品").tap()
        self.page.wait_for(1)
        ret = self.app.wait_for_page(self.route.get_page("礼品商城"))
        self.assertTrue(ret, "跳转礼品页面成功")

    # 点击送教材
    def test_001_clickSendBook(self):
        """
        点击送教材，弹出弹窗，点击复制
        """
        after = Callback()  # 监听回调, 阻塞当前主线程
        # hook setClipboardData 方法，监听是否被调用
        self.app.hook_wx_method("setClipboardData", after=after)
        self.assertTrue(self.page.wait_for(self.getElementPath("送教材"), max_timeout=10), "送教材存在")
        self.getElement("送教材").tap()
        self.page.wait_for(1)
        self.assertTrue(self.page.wait_for(self.getElementPath("复制"), max_timeout=10), "复制按钮存在")
        self.getElement("复制").tap()
        self.page.wait_for(1)
        # 判断是否触发了 setClipboardData 方法
        self.assertTrue(after.wait_called(timeout=10), "after called")
        self.app.release_hook_wx_method("setClipboardData")

    # 点击激活码
    def test_001_clickActivationCode(self):
        """
        点击激活码，跳转激活码页面
        """
        ret = self.page.wait_for(self.getElementPath("激活码"), max_timeout=10)
        self.assertTrue(ret, "激活码存在")
        self.getElement("激活码").tap()
        self.page.wait_for(1)

        ret = self.app.wait_for_page(self.route.get_page("激活码"))
        self.assertTrue(ret, "跳转激活码页面成功")

    # 点击健身小知识-查看更多
    def test_001_clickKnowledgeMore(self):
        """
        点击健身小知识-查看更多，跳转健身小知识页面
        """
        ret = self.page.wait_for(self.getElementPath("健身小知识-查看更多"), max_timeout=10)
        self.assertTrue(ret, "健身小知识-查看更多 存在")
        self.getElement("健身小知识-查看更多").tap()
        self.page.wait_for(1)

        ret = self.app.wait_for_page(self.route.get_page("视频教程"))
        self.assertTrue(ret, "跳转视频教程页面成功")

    # 点击健身小知识-视频列表
    def test_001_clickKnowledgeVideo(self):
        """
        点击健身小知识-视频列表，跳转视频播放页面
        """
        ret = self.page.wait_for(self.getElementPath("健身小知识-视频列表"), max_timeout=10)
        self.assertTrue(ret, "健身小知识-视频列表存在")
        self.getElement("健身小知识-视频列表")[0].tap()
        self.page.wait_for(1)

        ret = self.app.wait_for_page(self.route.get_page("视频详情"))
        self.assertTrue(ret, "跳转视频播放页面成功")
