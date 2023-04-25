import requests
from case.base.BaseCase import BaseCase
from case.base.BaseDef import getUserInfo


class Api:
    def __init__(self, mini: BaseCase):
        self.mini = mini
        self.baseUrl = "https://certt.froglesson.com"
        self.ApiMap = {
            "用户信息": {
                "url": "/user/info",
                "method": "POST",
                "params": []
            },
            "视频打点": {
                "url": "/course/doneChapter",
                "method": "GET",
                "params": ["cid", "percentage", "see_time", "time", "rid", "type", "duration"]
                # cid 课程id
                # percentage 观看百分比
                # see_time 观看时长
                # time 本次打点持续时间
                # rid 打点id，第一次打点为0
                # type ？未知，默认为1
                # duration 视频总时长
            },
            "答题记录": {
                "url": "/user/answer",
                "method": "GET",
                "params": ["subject", "page", "limit"]
                # subject 科目id
                # page 页码
                # limit 每页条数
            },
            "错题记录": {
                "url": "/practice/mistakes",
                "method": "GET",
                "params": ["subject", "page", "limit"]
                # subject 科目id
                # page 页码
                # limit 每页条数
            }
        }

    def request(self, apiName, **params):
        """
        针对该项目，统一封装请求方法
        :param apiName:  api名称
        :param params:  请求参数
        :return:  requests.Response
        """
        api = self.ApiMap[apiName]
        url = self.baseUrl + api["url"]
        userInfo = getUserInfo(self.mini)
        # 获取参数
        data = {}
        for key in api["params"]:
            data[key] = params[key]
        # 添加用户信息
        # 在请求参数中统一添加unionid，openid，uid
        data["unionid"] = userInfo["unionid"]
        data["openid"] = userInfo["openid"]
        data["uid"] = userInfo["uid"]
        # 发起请求，判断是Post还是Get
        if api["method"] == "GET":
            resp = requests.get(url, params=data)
        else:
            resp = requests.post(url, data=data)
        # self.mini.logger.info("请求参数: %s" % data)
        # self.mini.logger.info("请求地址: %s" % url)
        # self.mini.logger.info("请求结果: %s" % resp.text)
        return resp
