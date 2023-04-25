import minium
from Route import Route
from pathlib import Path
import json


class BaseCase(minium.MiniTest):
    """测试用例基类"""
    def __init__(self, methodName):
        """
        这个methodName，必传，不传就报错

        官方文档的解释：
        Create an instance of the class that will use the named test
           method when executed. Raises a ValueError if the instance does
           not have a method with the specified name.

        :param methodName:
        """
        super().__init__(methodName)
        self.route = Route()
        self.elementXpath = {}

    @classmethod
    def setUpClass(cls):
        super(BaseCase, cls).setUpClass()
        output_dir = Path(cls.CONFIG.outputs)
        cls.logger.warning("output_dir: %s", output_dir)
        if not output_dir.is_dir():
            output_dir.mkdir()

    @classmethod
    def tearDownClass(cls):
        super(BaseCase, cls).tearDownClass()
        # cls.app.go_home()

    def setUp(self):
        # 开始获取性能数据
        self.app.get_perf_time(entry_types=['render', 'script', 'navigation', 'loadPackage'])
        # 获取 CPU 内存 数据，每隔1秒获取一次
        self.native.start_get_perf(1)
        ret = self.app.wait_for_page(self.route.get_tabber("课程"))
        self.app.wait_util(0)
        self.assertTrue(ret, "进入课程")

    def tearDown(self):
        # 结束获取性能数据
        perf_data = self.app.stop_get_perf_time()
        perf_data = json.dumps(perf_data)
        #  结束 获取 CPU 内存 数据
        data = self.native.stop_get_perf()
        data = json.dumps(data)
        """暂时没保存这些数据，等后续处理"""
        output = self.test_config.case_output
        # 将性能数据perf_data保存到output目录下的perf.log文件中
        f = open(output + "/perf.log", "a")
        f.write(perf_data)
        f.close()
        # 将CPU 内存数据保存到output目录下的cpu.log文件中
        f = open(output + "/cpu.log", "a")
        f.write(data)
        f.close()

        # perf_data = json.dumps(perf_data)
        # 保存性能数据

    def getElement(self, key: str):
        if key not in self.elementXpath:
            raise KeyError("不存在这个控件")
        if self.elementXpath[key]["isList"]:
            return self.page.get_elements(self.elementXpath[key]["value"])
        else:
            return self.page.get_element(self.elementXpath[key]["value"])

    def getElementPath(self, key: str):
        if key not in self.elementXpath:
            raise KeyError("不存在这个控件")
        return self.elementXpath[key]["value"]
