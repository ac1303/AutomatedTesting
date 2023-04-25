# minireport outputs outputs
# minitest -s suite.json -c config.json -g
# python -m http.server 12345 -d outputs

# minitest -m case.homepage_test --case test_07_open_live_sale -c config.json -g #运行执行class文件中的指定用例test_07_open_live_sale

# minitest -s suite.json -c config.json -g   #按照suite配置去执行用例

# if __name__ == "__main__":
#     import unittest
#     test_dir = './test_case'
#     discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')
#     result = unittest.TextTestRunner().run(discover)
    # 修改默认执行路径
