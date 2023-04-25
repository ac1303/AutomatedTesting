class Route:
    """
    小程序的页面路由，统一配置管理
    """
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.pages = {
            "tabber": {
                "首页": "/pages/Home/index",
                "课程": "/pages/Course/index",
                "练习": "/pages/Practise/index",
                "我的": "/pages/Mine/index",
            },
            "搜索页": "/pages/Template/search/index",
            "礼品商城": "/pages/Template/shop/shop",
            "课程详情": "/pages/Template/courseDetails/courseDetails",
            "课程详情-章节": "/pages/Course/courseVideo",
            "视频教程": "/pages/Video/index",
            "视频详情": "/pages/Video/videoDetails",
            "备考必读": "/pages/Template/articleDetails/articleDetails",
            "激活码": "/pages/Template/activation/activation",
            "激活课程": "/pages/Template/activation/courseActive",
            "我的课程": "/pages/Template/myCourse/index",
            "打卡日历": "/pages/Template/clockInCalendar/clockInCalendar",
            "排行榜": "/pages/Template/chapter/ranking",

            "知识点": "/pages/Template/knowledge/index",
            "知识点详情": "/pages/Template/knowledge/details",
            "记笔记": "/pages/Template/knowledge/notes",
            "通关秘籍": "/pages/Template/customsClearance/customsClearance",
            "章节练": "/pages/Template/chapter/index",
            "模拟考": "/pages/Template/chapter/index",

            "打卡": "/pages/Template/clockIn/clockIn",
            "设置分享图": "/pages/Template/clockIn/clockImg",

            "答题记录": "/pages/Template/example/list",
            "错题本": "/pages/Template/example/list",
            "成绩单": "/pages/Template/transcript/index",
            "笔记夹": "/pages/Template/example/notesFolder",
            "随心练": "/pages/Template/chapter/answer",

            "我的资料": "/pages/Mine/userInfo",
            "我的收藏": "/pages/Mine/collection",
            "我的购买": "/pages/Mine/buy",
            "我的礼品": "/pages/Mine/gift",
            "我的勋章": "/pages/Mine/medal",
            "我的证书": "/pages/Template/mineSec/myCert",
            "学习提醒": "/pages/Template/clockInCalendar/setRemind",
            "选择科目": "/pages/Mine/subject",

        }

    def get_page(self, page_name):
        return self.pages[page_name]

    def get_tabber(self, tabber_name):
        return self.pages["tabber"][tabber_name]


