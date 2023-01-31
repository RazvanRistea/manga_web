import logging

import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.top_bars.top_menu_bar import TopMenuBar
import time
from helper_enums.help_enums import Enums, ValueEnums
from api_core.microservices.apibase.assertions.userAssertions import BaseAssertions

baseAssertions = BaseAssertions()


class RegistrationPage(TopMenuBar):
    """ Login Page """
    PAGE_TITLE = (By.XPATH, "//*[@id=\"__next\"]/div[1]/div/div/div/div/div[2]/div/div[2]/h5")
    FIRST_NAME = (By.XPATH, "//*[@id=\"__next\"]/div[1]/div/div/div/div/div[2]/div/form/div[1]/div/div[1]/input")
    LAST_NAME = (By.XPATH, "//*[@id=\"__next\"]/div[1]/div/div/div/div/div[2]/div/form/div[1]/div/div[2]/input")
    PASSWORD = (By.XPATH, "//*[@id=\"__next\"]/div[1]/div/div/div/div/div[2]/div/form/div[2]/div/input")
    EMAIL = (By.XPATH, "//*[@id=\"__next\"]/div[1]/div/div/div/div/div[2]/div/form/div[1]/input")
    PHONE = (By.XPATH, "//*[@id=\"__next\"]/div[1]/div/div/div/div/div[2]/div/form/div[3]/div[2]/input")
    COUNTRYCODE_DROPDOWN = (By.XPATH, "//*[@id=\"__next\"]/div[1]/div/div/div/div/div[2]/div/form/div[3]/div["
                                      "1]/div/div/button")
    DATEOFBIRTH = (By.XPATH, "//*[@id=\"__next\"]/div[1]/div/div/div/div/div[2]/div/form/div[6]/div[1]/div/div/input")
    STREET = (By.XPATH, "//*[@id=\"__next\"]/div[1]/div/div/div/div/div[2]/div/form/div[4]/input")
    CITY = (By.XPATH, "//*[@id=\"__next\"]/div[1]/div/div/div/div/div[2]/div/form/div[5]/div/div[1]/input")
    POSTCODE = (By.XPATH, "//*[@id=\"__next\"]/div[1]/div/div/div/div/div[2]/div/form/div[5]/div/div[2]/input")
    GENDER = (By.XPATH, "//*[@id=\"__next\"]/div[1]/div/div/div/div/div[2]/div/form/div[3]/div/div/div[1]/input")
    AGREE_ALL = (By.XPATH, "//*[@id=\"__next\"]/div[1]/div/div/div/div/div[2]/div/form/div[7]/div/div")
    SMS_CODE = (By.XPATH, "//*[@id=\"__next\"]/div[1]/div/div/div/div/div[2]/div/form/div[5]/div[1]/div")
    AGREE_TERMS = (By.XPATH, "//*[@id=\"signupModal\"]/div/div[2]/section/form/div/div[8]/fieldset/div[1]/label/span["
                             "1]/span[1]")
    AGREE_COOKIE = (By.XPATH, "//*[@id=\"signupModal\"]/div/div[2]/section/form/div/div[8]/fieldset/div["
                              "2]/label/span[1]/span[1]")
    AGREE_OFFERS = (By.XPATH, "//*[@id=\"__next\"]/div[1]/div/div/div/div/div[2]/div/form/div[8]/div/div")
    SEND_SMS = (By.XPATH, "//*[@id=\"__next\"]/div[1]/div/div/div/div/div[2]/div/form/div[5]/div[2]/button")
    CONTINUE_BTN_STEP_1 = (By.XPATH, "//*[@id=\"signupModal\"]/div/div[2]/section/button")
    CONTINUE_BTN_STEP_2 = (By.XPATH, "//*[@id=\"__next\"]/div[1]/div/div/div/div/div[2]/div/form/div[9]/button")

    VERIFY_SMS_BTN = (By.XPATH, "//*[@id=\"__next\"]/div[1]/div/div/div/div/div[2]/div/form/div[5]/div[2]/button")

    EMAIL_WARNING = (By.XPATH, "//*[@id=\"__next\"]/div[1]/div/div/div/div/div[2]/div/form/div[1]/p")
    PASSWORD_WARNING = (By.XPATH, "//*[@id=\"__next\"]/div[1]/div/div/div/div/div[2]/div/form/div[2]/ul/p")
    LAST_NAME_WARNING = (By.XPATH, "//*[@id=\"signupModal\"]/div/div[2]/section/form/div/div[1]/div/p")
    FIRST_NAME_WARNING = (By.XPATH, "//*[@id=\"signupModal\"]/div/div[2]/section/form/div/div[1]/div/p")
    STREET_WARNING = (By.XPATH, "//*[@id=\"__next\"]/div[1]/div/div/div/div/div[2]/div/form/div[4]/p")
    CITY_WARNING = (By.XPATH, "//*[@id=\"__next\"]/div[1]/div/div/div/div/div[2]/div/form/div[5]/div/div[1]/p")
    POSTCODE_WARNING = (By.XPATH, "//*[@id=\"__next\"]/div[1]/div/div/div/div/div[2]/div/form/div[5]/div/div[2]/p")
    BIRTHDATE_WARNING = (By.XPATH, "//*[@id=\"signupModal\"]/div/div[2]/section/form/div/div[3]/div/p")

    REGISTER_DEPOSIT_AND_PLAY = (By.XPATH, "//*[@id=\"signupModal\"]/div/div[1]/div[1]/div[2]")
    PAY_AND_PLAY_AMOUNT = (By.XPATH, "//*[@id=\"amount\"]")
    START_PLAYING = (By.XPATH, "// *[ @ id = \"signupModal\"] / div / div[2] / div / section / div[2] / button")

    BANKS_IFRAME = (By.XPATH, "//*[@id=\"deposit\"]")
    NORDEA_BANK = (By.XPATH, "//*[@id=\"app\"]/div[1]/div/div[2]/div/ul/div[1]/div/div[2]")

    JATKA_BUTTON = (By.XPATH, "//*[@id=\"app\"]/div[1]/div/div[2]/div[2]/div/button")
    LAST_JAKTA_BUTTON = (By.XPATH, "//*[@id=\"app\"]/div[2]/div[2]/div/div/div[2]/div/div[2]/div[4]/button")
    CONTINUE_PNP = (By.XPATH, "//*[@id=\"app\"]/div[1]/div/div[2]/div[2]/div/button")
    LOGIN_ID = (By.XPATH, "//*[@id=\"app\"]/div[1]/div/div[2]/div[1]/div/div/div")
    ONE_TIME_CODE = (By.XPATH, "//*[@id=\"app\"]/div[1]/div/div[2]/div[1]/div[1]/div/div/h3")
    ONE_TIME_CODE_BOX = (By.XPATH, "//*[@id=\"app\"]/div[1]/div/div[2]/div[1]/div[2]/div/div/input")

    CHECKING_ACCOUNT = (By.XPATH, "//*[@id=\"app\"]/div[1]/div/div[2]/div/div[2]/div/ul/div[1]/div/div[1]/div/div["
                                  "1]/span[1]")
    EMAIL_PAY_N_PLAY = (By.XPATH, "//*[@id=\"emailPayNPlay\"]")
    PASSWORD_PAY_N_PLAY = (By.XPATH, "//*[@id=\"passwordPayNPlay\"]")
    PHONE_PAY_N_PLAY = (By.XPATH, "//*[@id=\"phoneBodyPayNPlay\"]")
    AGREE_ALL_PAY_N_PLAY = (By.XPATH, "//*[@id=\"signupModal\"]/div/div[2]/div/section/form/div/div[5]/fieldset/label")

    REGISTER_PAY_N_PLAY = (By.XPATH, "//*[@id=\"signupModal\"]/div/div[2]/div/section/div[2]/button")

    COUNTRYCODE_DICT = {'Japan': 63, 'France': 43, 'Thailand': 121}

    def __init__(self, driver):

        super().__init__(driver)

    logger = logging.getLogger(__name__)

    @allure.step("Register to website with required data from the new user data dictionary - step 1.")
    def register_step_1(self, newUserData, browser):

        """Initialise the variables that need for this step."""

        email = newUserData.email
        password = newUserData.password
        phone = newUserData.phone
        countryCode = newUserData.countryCode

        self.fill_text(self.EMAIL, email)
        self.fill_text(self.PASSWORD, password)

        if countryCode is not None:
            self.click(self.COUNTRYCODE_DROPDOWN)
            COUNTRY_CODE = self.get_country(countryCode)
            self.get_element(COUNTRY_CODE)
            self.click(COUNTRY_CODE)

        self.fill_text(self.PHONE, phone)

        if self.is_elem_enabled(self.SEND_SMS):
            self.click(self.SEND_SMS)
            time.sleep(5)
            self.wait_for_element(self.SMS_CODE, max_retries=10)
            self.click(self.SMS_CODE)
            self.type_with_keys(self.SMS_CODE, ValueEnums.SMS_CODE.value)
            self.click(self.VERIFY_SMS_BTN)

    @allure.step("Register to website and verify that missing or incorrect fields have warnings - step 1.")
    def register_step_1_invalid_data(self):

        self.fill_text(self.EMAIL, ValueEnums.BOGUS_VALUE.value)
        self.delete_with_keys(self.EMAIL, len(str(ValueEnums.BOGUS_VALUE.value)))
        self.fill_text(self.PASSWORD, ValueEnums.BOGUS_VALUE.value)

        self.click(self.PHONE)

        self.is_warning_visible(self.EMAIL_WARNING)
        self.is_warning_visible(self.EMAIL_WARNING)
        self.is_warning_visible(self.PASSWORD_WARNING)
        self.delete_with_keys(self.PASSWORD, len(str(ValueEnums.BOGUS_VALUE.value)))
        status = self.is_elem_enabled(self.SEND_SMS)
        baseAssertions.assertEquals(False, status)

    @allure.step("Register to website with required data from the new user data dictionary - step 2.")
    def register_step_2(self, newUserData, agreements=None):

        """Initialise the variables that need for this step."""
        dateOfBirth = newUserData.dateOfBirth
        postCode = newUserData.postCode
        city = newUserData.city
        street = newUserData.street
        firstName = newUserData.firstName
        lastName = newUserData.lastName

        self.fill_text(self.FIRST_NAME, firstName)
        self.fill_text(self.LAST_NAME, lastName)
        self.click(self.GENDER)
        self.fill_text(self.STREET, street)
        self.fill_text(self.CITY, city)
        self.fill_text(self.POSTCODE, postCode)
        self.click(self.DATEOFBIRTH)
        self.fill_text(self.DATEOFBIRTH, dateOfBirth)
        self.scroll_down()
        if agreements is None:
            self.click(self.AGREE_ALL)
        else:
            self.click_agreements(agreements)

        if self.is_elem_enabled(self.CONTINUE_BTN_STEP_2):
            self.click(self.CONTINUE_BTN_STEP_2)

    @allure.step("Register to website and verify that missing or incorrect fields have warnings - step 2.")
    def register_step_2_invalid_data(self):

        self.click(self.STREET)
        self.fill_text(self.STREET, ValueEnums.INVALID_DATA.value)
        self.delete_with_keys(self.STREET, len(str(ValueEnums.INVALID_DATA.value)))
        self.fill_text(self.POSTCODE, ValueEnums.INVALID_DATA.value)
        self.delete_with_keys(self.POSTCODE, len(str(ValueEnums.INVALID_DATA.value)))
        self.fill_text(self.CITY, ValueEnums.INVALID_DATA.value)
        self.delete_with_keys(self.DATEOFBIRTH, len(str(ValueEnums.INVALID_DATA.value)))

        self.is_warning_visible(self.STREET_WARNING)
        self.is_warning_visible(self.POSTCODE_WARNING)

        status = self.is_elem_enabled(self.CONTINUE_BTN_STEP_2)
        baseAssertions.assertEquals(False, status)

    @allure.step("Get page title")
    def get_page_title(self):
        return self.get_text(self.PAGE_TITLE)

    @allure.step("Clicking country from drop down.")
    def get_country(self, countryCode):
        country_list_number = self.COUNTRYCODE_DICT.get(countryCode)
        COUNTRY_CODE = (By.XPATH, "// *[ @ id = \"__next\"] / div[1] / div / div / div / div / div[2] / div / "
                                  "form / div[3] / div[1] / div / div[2] " \
                                  "/ div / div / div[" + str(country_list_number) + "]")
        return COUNTRY_CODE

    @allure.step("Clicking agreements.")
    def click_agreements(self, agreement_combination):

        type_dict = {'termsAndConditions': self.AGREE_TERMS,
                     'cookiePolicy': self.AGREE_COOKIE,
                     'agreeAll': self.AGREE_ALL,
                     'offers': self.AGREE_OFFERS}

        for agr_type in agreement_combination.split(" "):
            self.click(type_dict.get(agr_type))
            time.sleep(0.5)

    def select_for_mobile(self):
        self.click(self.CONTINUE_BTN_STEP_1)
        time.sleep(1)
        self.click(self.CONTINUE_BTN_STEP_1)

    @allure.step("Checking if continue button is enabled.")
    def is_continue_button_enabled(self):
        return self.is_elem_enabled(self.CONTINUE_BTN_STEP_2)

    @allure.step("Check that field warning is displayed {element}")
    def is_warning_visible(self, element):
        status = self.is_elem_displayed(element)
        baseAssertions.assertEquals(True, status)
