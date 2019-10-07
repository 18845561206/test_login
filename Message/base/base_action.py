from selenium.webdriver.support.wait import WebDriverWait
class BaseAction:
    def __init__(self,driver):
        self.driver = driver
    def find_element(self,feature,timeout=10,poll=1):
        feature_by,feature_value = feature
        element = WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_element(feature_by,feature_value))
        return  element
    def find_elements(self,feature,timeout=10,poll=1):
        feature_by,feature_value = feature
        elements = WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_element(feature_by,feature_value))
        return  elements
    def click(self,feature):
        self.find_element(feature).click()
    def input(self,feature,text):
        self.find_element(feature).send_keys(text)