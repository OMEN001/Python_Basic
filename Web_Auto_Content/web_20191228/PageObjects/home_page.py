from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:

    # 我的帐号  元素
    my_user_name = (By.XPATH,'//a[contains(text(),"我的帐户")]')

    def __init__(self,driver:WebDriver):
        self.driver = driver

    # 用户名是否存在
    def user_is_existed(self):
        """

        Return:
        """
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located(self.my_user_name))
        except:
            return False
        else:
            return True


    # 点击第一个抢投标
    def click_first_bid(self):
        pass

