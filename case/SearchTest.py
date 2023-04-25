from case.pages.Search import Search
import minium


@minium.ddt_class(testNameFormat="%(name)s_%(index)s")
class SearchTest(Search):

    @minium.ddt_case(
        minium.ddt_data(['1', True], name="正常"),
        minium.ddt_data(['', False], name="空"),
        minium.ddt_data(["     ", True], name="空格"),
        minium.ddt_data(['!@#$%^&*()_+}{":<>?}', True], name="特殊字符"),
        minium.ddt_data(["1111111111111111111111111111111111111111111111111111111111111111111111111111111111", True],
                        name="超长文本"),
        minium.ddt_data(['😀', True], name="表情"),
    )
    @minium.ddt_unpack
    # 第一个参数为搜索框输入的内容，第二个参数为是否会有搜索结果
    def test_001_search(self, value, boo):
        """
        搜索内容测试，包括正常搜索、空搜索、空格搜索、特殊字符搜索、超长文本搜索、表情搜索
        """
        el = self.getElement("搜索框")
        el.tap()
        el.trigger("input", {"value": value})
        el.trigger("confirm", {"value": "66"})
        self.page.wait_for(1)
        self.assertEqual(self.page.data.searchParams.search, value, "搜索框内文字与输入一致")
        self.page.wait_for(1)
        # 判断有没有搜索结果 /page/view/search-list/view/view[1]/u-tabs/view/view/scroll-view/view
        ret = self.page.wait_for(self.getElementPath("知识点"), max_timeout=10)
        self.assertIs(ret, boo, "搜索结果")

    def test_001_Cancel(self):
        """
        点击取消按钮,跳转到首页
        """
        # 跳转到搜索页面
        self.getElement("取消").tap()
        self.page.wait_for(1)
        ret = self.app.wait_for_page(self.route.get_tabber("课程"))
        self.assertTrue(ret, "取消成功")

    # 测试删除一个搜索记录
    def test_002_deleteOnce(self):
        """
        测试删除一个搜索记录
        """
        self.page.wait_for(2)
        els = self.getElement("搜索记录")
        self.logger.info("搜索历史记录数为：%s" % len(els))
        self.capture(name="搜索历史记录")
        if len(els) <= 0:
            self.logger.warn("搜索历史记录为空")
            self.assertTrue(False, "搜索历史记录为空")
            return
        # 长按触发删除按钮
        els[0].long_press(5000)
        # 记录当前搜索记录的内容
        text = els[0].inner_text
        self.logger.info("搜索历史记录内容为：%s" % text)
        # 点击删除按钮 /page/view/search-history/view/view[2]/view[1]/image
        # 判断是否存在删除按钮
        ret = self.page.element_is_exists(self.getElementPath("删除第一条搜索记录"))
        self.assertTrue(ret, "存在删除按钮")
        self.getElement("删除第一条搜索记录").tap()
        self.page.wait_for(2)
        # 判断是否删除成功
        if len(els) - len(self.getElement("搜索记录")) == 1:
            self.logger.info("删除成功")
            return
        else:
            # 获取当前搜索记录的内容
            self.assertEqual(text, self.getElement("搜索记录")[0].inner_text, "删除成功")

    def test_003_deleteAll(self):
        """
        测试删除所有搜索记录
        """
        els = self.getElement("搜索记录")
        self.logger.info("搜索历史记录数为：%s" % len(els))
        self.capture(name="搜索历史记录")
        if len(els) <= 0:
            self.logger.warn("搜索历史记录为空")
            self.assertTrue(False, "搜索历史记录为空")
            return
        # 删除全部
        self.getElement("删除全部搜索记录").tap()
        self.page.wait_for(2)
        self.native.handle_modal("确定")
        self.page.wait_for(2)
        # 当搜索记录被清空后，位置会变化，变成搜索发现，所以需要判断一下
        if self.getElement("搜索记录-标题").inner_text == "搜索发现":
            self.assertTrue(True, "删除成功")
            return
        # 判断是否删除成功
        self.assertEqual(len(self.getElement("搜索记录")), 0, "删除成功")
