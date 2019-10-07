from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class NewMessagePage(BaseAction):
    recipients_edit_text = By.ID,"com.android.mms:id/recipients_editor"
    content_edit_text = By.ID,"com.android.mms:id/embedded_text_editor"
    send_button = By.XPATH,"//*[@content-desc='发送']"

    def input_recipients(self,text):
        self.input(self.recipients_edit_text,text)
    def input_content(self,text):
        self.input(self.content_edit_text,text)
    def click_send(self):
        self.click(self.send_button)
