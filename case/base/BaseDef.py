from case.base.BaseCase import BaseCase


# 向上滚动
def scrollUp(mini: BaseCase, px, time=1000):
    mini.page.scroll_to(mini.page.scroll_y + px, time)


# 向下滚动
def scrollDown(mini: BaseCase, px, time=1000):
    mini.page.scroll_to(mini.page.scroll_y - px, time)


# 封装一个获取Storage的方法
def getStorage(mini: BaseCase, key):
    ret = mini.app.call_wx_method("getStorageSync", key)
    return ret["result"]["result"]


# 封装一个获取当前用户信息的方法
def getUserInfo(mini: BaseCase):
    return getStorage(mini, "userInfo")

