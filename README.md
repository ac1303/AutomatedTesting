# 四大证备考神器自动化测试

## 待完成页面
- [ ] 章节练
- [ ] 模拟考
- [ ] 学习提醒
- [ ] 我的收藏
- [ ] 我的礼品


## 使用说明

### 1. 执行全部测试用例

```shell
minitest -s suite.json -c config.json -g
```

### 2. 执行单个测试用例
xxxx为测试用例名称
```shell
minitest -m case.xxxx -c config.json -g
```

### 3. 执行单个测试用例的单个步骤
xxxx为测试用例名称，yyyy为步骤名称
```shell
minitest -m case.xxxx --case yyyy -c config.json -g
```

### 4. 查看测试报告
```shell
python -m http.server 12345 -d outputs
```

## 项目结构

```shell
.
├── README.md
├── config.json # 配置文件
├── suite.json # 测试用例集
├── case # 测试用例存放路径
    ├── base # 测试基类,一些公共方法会存放在这里
    ├── page # 页面对象,每个页面一个文件,每个页面的元素和操作都会存放在这里
    ├── xxxTest.py # 测试用例文件
├── outputs # 测试日志和生成的测试报告
    ├── xxxxx 
```
## minitest 命令行参数说明

- -h, --help: 使用帮助。
- -v, --version: 查看 minium 的版本。
- -p PATH/--path PATH: 用例所在的文件夹，默认当前路径。
- -m MODULE_PATH, --module MODULE_PATH: 用例的包名或者文件名
- --case CASE_NAME: test_开头的用例名
- -s SUITE, --suite SUITE:测试计划文件

## [miniTest官方文档](https://minitest.weixin.qq.com/#/minium/Python/framework/Minitest)
