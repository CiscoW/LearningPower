import cv2 as cv
import time


class Study(object):
    def __init__(self, user_behavior):
        self.user_behavior = user_behavior

    def implicitly_wait(self, time_out):
        self.user_behavior.implicitly_wait(time_out)

    def refresh(self):
        self.user_behavior.refresh()

    def visit(self, by_id=None, by_name=None, by_css_selector=None, by_xpath=None, timeout=None):
        self.user_behavior.click_button(by_id, by_name, by_css_selector, by_xpath, timeout)

    def open_window_handle(self, url):
        self.user_behavior.open_window_handle(url)

    def get_current_window_handle(self):
        return self.user_behavior.get_window_handles()[-1]

    def switch_to_window(self, handle):
        self.user_behavior.switch_to_window(handle)

    def scroll(self, size):
        self.user_behavior.scroll(size)

    def scroll_bottom(self):
        self.user_behavior.scroll_bottom()

    def page_source(self):
        return self.user_behavior.page_source()

    def close_current_window(self):
        self.user_behavior.close_current_window()

    def close_browser(self):
        self.user_behavior.close_browser()

    def clicks(self, by_id=None, by_name=None, by_css_selector=None, by_xpath=None):
        for _ in self.user_behavior.clicks(by_id, by_name, by_css_selector, by_xpath):
            yield


class ReadArticle(Study):
    BY_CSS_SELECTOR = "#C5a9pgqwm4s400 > div > div > ul:nth-child(3) > li:nth-child(1) > a"

    def __init__(self, user_behavior, study_and_research=BY_CSS_SELECTOR):
        super(ReadArticle, self).__init__(user_behavior)
        self.visit(by_css_selector=study_and_research)
        self.switch_to_window(self.get_current_window_handle())


class LongTimeReadArticle(ReadArticle):
    pass


class WatchVideo(Study):
    FIRST_CHANNEL_URL = 'https://www.xuexi.cn/4426aa87b0b64ac671c96379a3a8bd26/db086044562a57b441c24f2af1c8e101.html'

    def __init__(self, user_behavior, url=FIRST_CHANNEL_URL):
        super(WatchVideo, self).__init__(user_behavior)
        self.open_window_handle(url)
        self.switch_to_window(self.get_current_window_handle())

    def was_over(self):
        p1 = self.page_source()
        time.sleep(1)
        p2 = self.page_source()

        if p1 == p2:
            return True
        else:
            return False


class LongTimeWatchVideo(WatchVideo):
    pass


class Login(object):
    NAME = "login.png"
    CODE_HEIGHT = slice(60, 350)
    CODE_WIDTH = slice(500, 850)
    # BY_XPATH = '//*[@id="C8putwnd60vk00"]'
    WINDOW_WIDTH, WINDOW_HEIGHT = (1365, 737)

    SCROLL_SIZE = 900

    def __init__(self, user_behavior):
        self.user_behavior = user_behavior

    def get_current_window_handle(self):
        return self.user_behavior.get_window_handles()[-1]

    def save_screen_shot(self, name=NAME, scroll_size=SCROLL_SIZE):
        self.user_behavior.scroll(scroll_size)
        self.user_behavior.save_screen_shot(name)

    def show_code(self, name=NAME):
        img = cv.imread(name, 1)
        code = img[self.CODE_HEIGHT, self.CODE_WIDTH]
        cv.namedWindow(name)
        cv.imshow(name, code)
        cv.waitKey()
        cv.destroyAllWindows()

    # def click_login(self, by_xpath=BY_XPATH):
    #     self.user_behavior.click_button(by_xpath=by_xpath)
    #     self.user_behavior.switch_to_window(self.get_current_window_handle())

    def get_code(self):
        self.user_behavior.set_window_size(self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        self.save_screen_shot()
        self.show_code()


if __name__ == '__main__':
    from userbehavior import UserBehavior

    # _user_behavior = UserBehavior()
    # _user_behavior.browser_get("https://pc.xuexi.cn/points/login.html?ref=https://www.xuexi.cn/")
    # login = Login(_user_behavior)
    # login.get_code()

    _user_behavior = UserBehavior()
    _user_behavior.browser_get("https://baidu.com")

    watch_video = WatchVideo(_user_behavior)

    videos = watch_video.clicks(by_id="Ck3ln2wlyg3k00")
    time.sleep(5)
    for _ in videos:
        watch_video.switch_to_window(watch_video.get_current_window_handle())

        while True:

            if watch_video.was_over():
                print("播放完毕")
                break
            else:
                print("正在播放")

        watch_video.close_current_window()
        watch_video.switch_to_window(watch_video.get_current_window_handle())
