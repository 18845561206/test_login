from selenium.webdriver.common.by import By

from base.base_action import BaseAction

# com.android.contacts/.activities.PeopleActivity
class MessageListPage(BaseAction):
    new_message_btn = By.ID, "com.android.mms:id/action_compose_new"
    def click_new(self):
        self.click(self.new_message_btn)


    #
    # add_btn = By.ID,"com.android.contacts:id/create_contact_button"
    # input_name = By.XPATH,"//*[@text='姓名']"
    # input_phone = By.XPATH, "//*[@text='电话']"
    # def click_add_btn(self):
    #     self.click(self.add_btn)
    # def input_names(self,text):
    #     self.input(self.input_name,text)
    # def input_phones(self,text):
    #     self.input(self.input_phone,text)


