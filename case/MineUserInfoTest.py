from case.pages.MineUserInfo import MineUserInfo
import minium
import base64


@minium.ddt_class(testNameFormat="%(name)s_%(index)s")
class MineUserInfoTest(MineUserInfo):

    @minium.ddt_case(
        minium.ddt_data("./img/test.png")
    )
    def test_001_uploadAvatar(self, filePath):
        """
        测试上传头像
        """
        ret = self.page.wait_for(self.getElementPath("头像"), max_timeout=10)
        self.assertTrue(ret, "头像存在")
        with open(filePath, "rb") as fd:
            c = fd.read()
            image_b64data = base64.b64encode(c).decode("utf8")
        self.logger.info("image_b64data: %s" % image_b64data)
        ret = self.app.mock_choose_image("1.png", image_b64data)
        # 点击头像
        self.getElement("头像").tap()
        self.assertTrue(ret, "上传头像成功")

    # 测试修改昵称
    @minium.ddt_case(
        minium.ddt_data(['测试昵称', True], name="正常文字"),
        minium.ddt_data(['-1234', True], name="负数"),
        minium.ddt_data(['', False], name="空"),
        minium.ddt_data([' ', True], name="空格"),
        minium.ddt_data([
            '11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111',
            True], name="超长文本"),
        minium.ddt_data(['!#$%^&*()_+=-[]}{;",.><=?/', True], name="特殊字符"),
        minium.ddt_data(['😀', True], name="表情"),
    )
    @minium.ddt_unpack
    def test_001_changeNickname(self, name="rhhstyh", ret=True):
        """
        测试修改昵称,无法单独触发修改昵称的函数，
        所以只能再触发一次上传头像的函数，以此来实现修改昵称
        """
        # 获取data中的 userInfo user_name
        nickName = self.page.data["userInfo"]["user_name"]
        self.logger.info("修改前的昵称：%s" % nickName)
        # 点击昵称
        el = self.getElement("昵称")
        # 修改昵称
        el.tap()
        self.page.wait_for(1)
        el.trigger("input", {"value": name})
        self.page.wait_for(1)

        self.app.mock_choose_image("1111", "11111")
        self.getElement("头像").tap()
        self.page.wait_for(2)
        self.getElement("清理缓存").tap()
        self.app.wait_util(0)
        self.page.wait_for(2)
        el = self.getElement("昵称")
        self.logger.info("修改后的昵称：%s" % el.value)
        bo = el.value == name
        self.assertEqual(bo, ret, "修改昵称成功")