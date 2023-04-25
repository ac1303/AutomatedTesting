import base64
from case.pages.ClockIn import ClockIn
import minium


class ClockInTest(ClockIn):

    @minium.ddt_case(
        minium.ddt_data("./img/test.png")
    )
    def test_uploadImage(self, filePath="./img/test.png"):
        """
        测试上传打卡图片
        """
        img_url = self.getElement("上传图片").attribute("src")
        self.logger.info("img_url: %s" % img_url)
        with open(filePath, "rb") as fd:
            c = fd.read()
            image_b64data = base64.b64encode(c).decode("utf8")
        # self.logger.info("image_b64data: %s" % image_b64data)
        ret = self.app.mock_choose_image("1.png", image_b64data)
        # 点击头像
        self.getElement("上传图片").tap()
        self.native.handle_action_sheet("选择图片")
        self.assertTrue(ret, "mock_choose_image成功")
        self.app.wait_util(0)
        self.page.wait_for(1)
        new_img_url = self.getElement("上传图片").attribute("src")
        self.logger.info("new_img_url: %s" % new_img_url)
        self.assertNotEqual(img_url, new_img_url, "上传图片成功")
        self.getElement("删除图片").tap()
        self.app.wait_util(0)
        self.page.wait_for(1)
        del_img_url = self.getElement("上传图片").attribute("src")
        self.assertNotEqual(new_img_url, del_img_url, "删除图片成功")

    # 测试图片库
    def test_imageLibrary(self):
        el = self.getElement("图片库")[0]
        img_url = el.attribute("src")
        el.tap()
        self.app.wait_util(0)
        self.page.wait_for(1)
        self.assertTrue(self.app.wait_for_page(self.route.get_page("设置分享图")), "进入设置分享图成功")
        self.getElement("设置为打卡图片").tap()
        self.app.wait_util(0)
        self.page.wait_for(1)
        self.assertTrue(self.app.wait_for_page(self.route.get_page("打卡")), "进入打卡页面成功")
        new_img_url = self.getElement("上传图片").attribute("src")
        self.logger.info("new_img_url: %s" % new_img_url)
        self.assertNotEqual(img_url, new_img_url, "设置图片成功")