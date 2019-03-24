import time
# from study import ReadArticle
from study import Login
from study import LongTimeReadArticle
from study import LongTimeWatchVideo
from userbehavior import UserBehavior
from config import *

user_behavior = UserBehavior()


# user_behavior.browser_get(URL)
# user_behavior.maximize_window()

def login():
    user_behavior.browser_get(LOGIN)

    _login = Login(user_behavior)
    _login.get_code()
    user_behavior.maximize_window()


# 阅读文章赚积分
def read_article_earn_credits():
    read_article = LongTimeReadArticle(user_behavior=user_behavior)
    articles = read_article.clicks(by_id=READ_ARTICLE_ID)
    num = 0

    for _ in articles:
        num += 1
        # 暂停三秒防止无法切换到新的页签
        time.sleep(3)
        read_article.switch_to_window(read_article.get_current_window_handle())
        # 赚篇数积分 # 5秒一篇 共6篇
        if num <= 6:
            for size in range(0, 1000, 200):
                time.sleep(1)
                read_article.scroll(size)
            read_article.scroll_bottom()
            read_article.close_current_window()
            read_article.switch_to_window(read_article.get_current_window_handle())
            continue

        # 长时间阅读赚取积分 4分钟一篇文章 共8篇
        for size in range(0, 10000, 100):
            time.sleep(4 * 60 / 100)
            read_article.scroll(size)
        read_article.scroll_bottom()
        read_article.close_current_window()
        read_article.switch_to_window(read_article.get_current_window_handle())
        if num >= READ_ARTICLE_NUM:
            read_article.close_current_window()
            read_article.switch_to_window(read_article.get_current_window_handle())
            break


# 观看视频转积分
def watch_video_earn_credits():
    watch_video = LongTimeWatchVideo(user_behavior=user_behavior)
    videos = watch_video.clicks(by_id=WATCH_VIDEO_ID)
    # 强行睡眠5秒
    time.sleep(5)
    num = 0
    for _ in videos:
        # 暂停三秒防止无法切换到新的页签
        time.sleep(3)
        watch_video.switch_to_window(watch_video.get_current_window_handle())
        num += 1
        time_length = 0
        # 观看6个视频、每个视频观看10秒
        if num <= 6:
            while True:
                time.sleep(1)
                time_length += 1
                if time_length >= 10:
                    break
            watch_video.close_current_window()
            watch_video.switch_to_window(watch_video.get_current_window_handle())
            continue

        # 观看10个视频、每个观看时长5分钟
        while True:
            if watch_video.was_over():
                watch_video.refresh()
            else:
                time_length += 1

            if time_length >= 5 * 60:
                break
        watch_video.close_current_window()
        watch_video.switch_to_window(watch_video.get_current_window_handle())

        if num >= WATCH_VIDEO_NUM:
            watch_video.close_current_window()
            break


if __name__ == '__main__':
    login()
    read_article_earn_credits()
    watch_video_earn_credits()
    user_behavior.close_browser()
