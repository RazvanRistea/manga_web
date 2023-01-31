import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from api_core.microservices.apibase.assertions.userAssertions import BaseAssertions

baseAssertions = BaseAssertions()


class AboutPage(BasePage):
    """ About page - The first page that appears when navigating to base URL"""
    LOGIN_LINK = (By.XPATH, '//*[@id="__next"]/div[2]/div/div[1]/section[2]/button[1]')
    REGISTER_LINK = (By.XPATH, '//*[@id="__next"]/div[2]/div/div[1]/section[2]/button[2]')
    COOKIE_POP_UP_OK_BUTTON = (By.XPATH, '//*[@id="__next"]/div[3]/div[4]/div[2]/button[2]')

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Click Login link")
    def click_login_link(self):
        self.click(self.LOGIN_LINK)

    @allure.step("I click on the registration button.")
    def click_register_link(self):
        self.click(self.REGISTER_LINK)

    @allure.step("I click on the OK cookies button pop up to close it.")
    def click_cookie_pop_up_ok_btn(self):
        pass
        # BasePage.click(self, self.COOKIE_POP_UP_OK_BUTTON)

    @allure.step("Checking if user is not logged in.")
    def user_is_not_logged_in(self):
        status = self.is_elem_enabled(self.REGISTER_LINK)
        baseAssertions.assertEquals(True, status)
