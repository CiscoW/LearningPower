import time
# from study import ReadArticle
from study import Login
from study import LongTimeReadArticle
from userbehavior import UserBehavior
from config import *

user_behavior = UserBehavior()


# user_behavior.browser_get(URL)
# user_behavior.maximize_window()

def login():
    user_behavior.browser_get(LOGIN)
    user_behavior.maximize_window()

    _login = Login(user_behavior)
    _login.save_screen_shot()
    _login.show_code()


# 阅读文章赚积分
def read_article_earn_credits():
    read_article = LongTimeReadArticle(user_behavior=user_behavior)
    articles = read_article.clicks(by_id=READ_ARTICLE_ID)
    num = 0

    for _ in articles:
        num += 1
        read_article.switch_to_window(read_article.get_current_window_handle())
        for size in range(0, 10000, 100):
            time.sleep(READ_ARTICLE_TIME / READ_ARTICLE_NUM / 100)
            read_article.scroll(size)
        read_article.scroll_bottom()
        read_article.close_current_window()
        read_article.switch_to_window(read_article.get_current_window_handle())
        if num >= READ_ARTICLE_NUM:
            read_article.close_current_window()
            break


if __name__ == '__main__':
    login()

    read_article_earn_credits()
