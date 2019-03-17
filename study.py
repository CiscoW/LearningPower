import cv2 as cv


class Study(object):
    def __init__(self, user_behavior):
        self.user_behavior = user_behavior

    def visit(self, by_id=None, by_name=None, by_css_selector=None, by_xpath=None, timeout=None):
        self.user_behavior.click_button(by_id, by_name, by_css_selector, by_xpath, timeout)

    def get_current_window_handle(self):
        return self.user_behavior.get_window_handles()[-1]

    def switch_to_window(self, handle):
        self.user_behavior.switch_to_window(handle)

    def scroll(self, size):
        self.user_behavior.scroll(size)

    def scroll_bottom(self):
        self.user_behavior.scroll_bottom()

    def close_current_window(self):
        self.user_behavior.close_current_window()

    def close_browser(self):
        self.user_behavior.close_browser()


class ReadArticle(Study):
    BY_CSS_SELECTOR = "#C5a9pgqwm4s400 > div > div > ul:nth-child(3) > li:nth-child(1) > a"

    def __init__(self, user_behavior, study_and_research=BY_CSS_SELECTOR):
        super(ReadArticle, self).__init__(user_behavior)
        self.visit(by_css_selector=study_and_research)
        self.switch_to_window(self.get_current_window_handle())

    def clicks(self, by_id=None, by_name=None, by_css_selector=None, by_xpath=None):
        for _ in self.user_behavior.clicks(by_id, by_name, by_css_selector, by_xpath):
            yield


class LongTimeReadArticle(ReadArticle):
    pass


class WatchVideo(Study):
    pass


class LongTimeWatchVideo(Study):
    pass


class Login(object):
    NAME = "login.png"
    CODE_HEIGHT = slice(60, 350)
    CODE_WIDTH = slice(500, 850)
    BY_XPATH = '//*[@id="C8putwnd60vk00"]'

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

    def click_login(self, by_xpath=BY_XPATH):
        self.user_behavior.click_button(by_xpath=by_xpath)
        self.user_behavior.switch_to_window(self.get_current_window_handle())


if __name__ == '__main__':
    from userbehavior import UserBehavior

    user_behavior = UserBehavior()
    user_behavior.browser_get("https://pc.xuexi.cn/points/login.html?ref=https://www.xuexi.cn/")
    user_behavior.maximize_window()
    login = Login(user_behavior)
    # login.click_login()
    login.save_screen_shot()
    login.show_code()
