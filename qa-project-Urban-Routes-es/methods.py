import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import data
import locators
from sms_code import retrieve_phone_code



## ============================== Metodos Pagina ============================================ ##

class UrbanRoutes:


    def __init__(self,driver):
        self.driver = driver

## ============================== Establecer Ruta ============================================ ##
    def set_from(self, from_address):
        WebDriverWait(self.driver,5).until(expected_conditions.element_to_be_clickable((By.ID,'from')))
        self.driver.find_element(*locators.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*locators.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*locators.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*locators.to_field).get_property('value')

    def set_route(self,from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

## ============================== Establecer Parametros de Viaje ============================================ ##

    def ask_for_taxi_button(self):
        self.driver.find_element(*locators.taxi_button).click()

    def set_comfort_fare(self):
        self.driver.find_element(*locators.comfort_tariff).click()


## ============================== Rellenar Teléfono y Código ============================================ ##
    def phone_modal_info(self):
        self.driver.find_element(*locators.phone_container).click()

    def fill_phone_requirements(self):
        self.driver.find_element(*locators.phone_field_modal).click()
        self.driver.find_element(*locators.phone_input).send_keys(data.phone_number)
        self.driver.find_element(*locators.phone_submit_button).click()

    def fill_phone_code(self):
        codigo = retrieve_phone_code(self.driver)
        self.driver.find_element(*locators.code_modal_container).click()
        self.driver.find_element(*locators.code_modal_field).send_keys(codigo)
        self.driver.find_element(*locators.confirm_code).click()

    def assure_phone_number_after_code(self):
        return self.driver.find_element(*locators.phone_check).text

## ============================== Rellenar Metodo de Pago ============================================ ##
    def select_payment_info(self):
        element = self.driver.find_element(*locators.payment_method)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def fill_payment_info(self):
        self.driver.find_element(*locators.card_number_field).send_keys(data.card_number)
        self.driver.find_element(*locators.card_number_code_field).send_keys(data.card_code)
        self.driver.find_element(*locators.card_number_field).click()
        self.driver.find_element(*locators.confirm_card_button).click()
        self.driver.find_element(*locators.close_card_modal).click()

## ============================== Recuperar los datos de la tarjeta ingresada ============================================ ##
    def get_card_number(self):
        return self.driver.find_element(*locators.card_number_field).get_property('value')
    def return_card_code(self):
        return self.driver.find_element(*locators.card_number_code_field).get_property('value')


## ============================== Agregar mensaje para el conductor ============================================ ##
    def comment_for_driver(self):
        self.driver.find_element(*locators.comment_selector).click()
        self.driver.find_element(*locators.comment_placer).send_keys(data.message_for_driver)

    def check_driver_comment(self):
        return self.driver.find_element(*locators.comment_placer).get_property('value')

## ============================== Ajustar Configuraciones de Viaje ============================================ ##
    def define_ride_settings(self):
        amenities = self.driver.find_element(*locators.amenities)
        self.driver.execute_script("arguments[0].scrollIntoView();", amenities)

    def click_on_radio_button(self):
        self.driver.find_element(*locators.radio_button).click()

## ============================== Agregar Helado para el viaje ============================================ ##
    def is_ice_cream_counter_zeroed(self):
        return self.driver.find_element(*locators.ice_cream_counter).text

    def add_yummy_ice_cream(self):
        counter = self.driver.find_element(*locators.yummy_ice_cream)
        self.driver.execute_script("arguments[0].scrollIntoView();", counter)
        for _ in range(2):
            counter.click()

    def did_you_add_yummy_ice_cream(self):
        return self.driver.find_element(*locators.ice_cream_counter).text

## ============================== Confirmar Configuraciones de Viaje ============================================ ##
    def confirm_and_look_for_taxi(self):
        self.driver.find_element(*locators.confirm_button).click()

    def show_driver_info(self):
        return self.driver.find_element(*locators.order_header_title).text





