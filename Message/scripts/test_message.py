import time
import pytest
from base.base_driver import init_driver
from page.page import Page
class TestContact:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)
    def teardown(self):
        time.sleep(3)
        self.driver.quit()
    @pytest.mark.parametrize(("phone","text"),[("14512347895","张三，你好"),("18010121456","hello,hi")])
    def test_send_message(self,phone,text):
        self.page.message_list.click_new()
        self.page.new_message.input_recipients(phone)
        self.page.new_message.input_content(text)
        self.page.new_message.click_send()
    # def test_add_list(self):
    #     self.page.message_list.click_add_btn()
    #     self.page.message_list.input_names("zhangsan")
    #     self.page.message_list.input_phones("18000001111")