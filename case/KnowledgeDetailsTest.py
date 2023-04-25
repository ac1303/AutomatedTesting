from case.pages.KnowledgeDetails import KnowledgeDetails
import minium


@minium.ddt_class(testNameFormat="%(name)s_%(index)s")
class KnowledgeDetailsTest(KnowledgeDetails):

    @minium.ddt_case(
        minium.ddt_data(['1', True], name="正常"),
        minium.ddt_data(['', False], name="空"),
        minium.ddt_data(["     ", True], name="空格"),
        minium.ddt_data(['!@#$%^&*()_+}{":<>?}', True], name="特殊字符"),
        minium.ddt_data(['111111111111111111111111111111111111111111111111111111111111111111111111111111111', True],
                        name="超长文本"),
        minium.ddt_data(['😀', True], name="表情"),
    )
    @minium.ddt_unpack
    def test_inputPublicNotes(self, value, boo):
        self.getElement('笔记').click()
        self.page.wait_for(1)
        # 判断删除按钮是否存在
        ret = self.page.element_is_exists(self.getElementPath('删除'))
        if ret:
            self.getElement('删除').click()
            self.page.wait_for(1)
            self.native.handle_modal('确定')
            self.app.wait_util(0)
            self.page.wait_for(1)
        self.getElement('记笔记').click()
        self.page.wait_for(1)
        self.getElement('笔记内容').trigger('input', {'value': value})
        self.page.wait_for(1)
        self.getElement('保存').click()
        self.app.wait_util(0)
        self.page.wait_for(1)
        if boo:
            self.assertEqual(self.getElement('笔记内容-弹窗').inner_text, value, '笔记保存成功')
        else:
            self.assertNotEqual(self.getElement('笔记内容-弹窗').inner_text, value, '笔记保存成功')
