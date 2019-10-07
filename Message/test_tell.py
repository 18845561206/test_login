# 导模块
import time
from appium import webdriver
# 创建一个字典，包装相应的启动参数
desired_caps = dict()
# 需要连接的手机的平台(不限制大小写)
desired_caps['platformName'] = 'Android'
# 需要连接的手机的版本号(比如 5.2.1 的版本可以填写 5.2.1 或 5.2 或 5 ，以此类推)
desired_caps['platformVersion'] = '9'
# 需要连接的手机的设备号(andoird平台下，可以随便写，但是不能不写)
desired_caps['deviceName'] = '5JP0218302000833'
# 需要启动的程序的包名
desired_caps['appPackage'] = 'com.android.contacts'
# 需要启动的程序的界面名
desired_caps['appActivity'] = '.activities.DialtactsActivity'
#设置手机不重置
desired_caps['noReset'] = True
#设置可以输入中文
# desired_caps['unicodeKeyboard'] = True
# desired_caps['resetKeyboard'] = True
# 连接appium服务器
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.ImageView").click()
driver.find_element_by_xpath("	//android.widget.FrameLayout[@content-desc='1']/android.widget.RelativeLayout/android.widget.TextView").click()
driver.find_element_by_xpath("	//android.widget.FrameLayout[@content-desc='0']/android.widget.RelativeLayout/android.widget.TextView").click()
driver.find_element_by_xpath("	//android.widget.FrameLayout[@content-desc='0']/android.widget.RelativeLayout/android.widget.TextView").click()
driver.find_element_by_xpath("	//android.widget.FrameLayout[@content-desc='8']/android.widget.RelativeLayout/android.widget.TextView").click()
driver.find_element_by_xpath("	//android.widget.FrameLayout[@content-desc='9']/android.widget.RelativeLayout/android.widget.TextView").click()
time.sleep(3)
# 退出
driver.quit()