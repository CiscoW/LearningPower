from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class UserBehavior(object):
    def __init__(self, browser=None):
        self.browser = browser

    def open_browser(self):
        """
        默认使用Chrome浏览器
        :return:
        """
        if self.browser is None:
            self.browser = webdriver.Chrome()

    def browser_get(self, url):
        """
        模拟浏览器访问url
        :param url:
        :return:
        """
        if self.browser is None:
            self.open_browser()

        self.browser.get(url)

    def open_window_handle(self, url=""):
        self.browser.execute_script('window.open("%s");' % url)
        return self.get_window_handles()[-1]

    def get_current_window_handle(self):
        return self.browser.current_window_handle

    def get_window_handles(self):
        return self.browser.window_handles

    def switch_to_window(self, handle):
        self.browser.switch_to_window(handle)

    def maximize_window(self):
        self.browser.maximize_window()

    def page_source(self):
        return self.browser.page_source

    def save_screen_shot(self, name):
        self.browser.save_screenshot(name)

    def wait_until(self, timeout, by_strategies, by_strategies_name):
        return WebDriverWait(self.browser, timeout).until(
            expected_conditions.presence_of_element_located((by_strategies, by_strategies_name)))

    def click_button(self, by_id=None, by_name=None, by_css_selector=None, by_xpath=None, timeout=None):
        if timeout:
            if by_id:
                self.wait_until(timeout, By.ID, by_id).click()
                return
            if by_name:
                self.wait_until(timeout, By.NAME, by_name).click()
                return
            if by_css_selector:
                self.wait_until(timeout, By.CSS_SELECTOR, by_css_selector).click()
                return
            if by_xpath:
                self.wait_until(timeout, By.XPATH, by_xpath).click()
                return
        else:
            if by_id:
                self.browser.find_element_by_id(by_id).click()
                return
            if by_name:
                self.browser.find_element_by_name(by_name).click()
                return
            if by_css_selector:
                self.browser.find_element_by_css_selector(by_css_selector).click()
                return
            if by_xpath:
                self.browser.find_element_by_xpath(by_xpath).click()
                return

    def clicks(self, by_id=None, by_name=None, by_css_selector=None, by_xpath=None):
        if by_id:
            ids = self.browser.find_elements_by_id(by_id)
            for _id in ids:
                yield _id.click()

        if by_name:
            names = self.browser.find_elements_by_name(by_name)
            for _name in names:
                yield _name.click()

        if by_css_selector:
            css_selectors = self.browser.find_elements_by_css_selector(by_css_selector).click()
            for _css_selector in css_selectors:
                yield _css_selector.click()

        if by_xpath:
            xpaths = self.browser.find_elements_by_xpath(by_xpath).click()
            for _xpath in xpaths:
                yield _xpath.click()

    def send_keys(self, value, by_id=None, by_name=None, by_css_selector=None, by_xpath=None, timeout=None):
        if timeout:
            if by_id:
                self.wait_until(timeout, By.ID, by_id).send_keys(value)
                return
            if by_name:
                self.wait_until(timeout, By.NAME, by_name).send_keys(value)
                return
            if by_css_selector:
                self.wait_until(timeout, By.CSS_SELECTOR, by_css_selector).send_keys(value)
                return
            if by_xpath:
                self.wait_until(timeout, By.XPATH, by_xpath).send_keys(value)
                return
        else:
            if by_id:
                self.browser.find_element_by_id(by_id).send_keys(value)
                return
            if by_name:
                self.browser.find_element_by_name(by_name).send_keys(value)
                return
            if by_css_selector:
                self.browser.find_element_by_css_selector(by_css_selector).send_keys(value)
                return
            if by_xpath:
                self.browser.find_element_by_xpath(by_xpath).send_keys(value)
                return

    def scroll(self, size):
        js = "var q=document.documentElement.scrollTop=" + str(size)
        self.browser.execute_script(js)

    def scroll_bottom(self):
        js = "window.scrollTo(0, document.body.scrollHeight)"
        self.browser.execute_script(js)

    def close_current_window(self):
        self.browser.close()

    def close_browser(self):
        self.browser.quit()


if __name__ == '__main__':
    user_behavior = UserBehavior()
    user_behavior.browser_get(
        "https://pc.xuexi.cn/points/login.html?ref=https://www.xuexi.cn/")
    import time

    time.sleep(5)

    print(user_behavior.page_source())
