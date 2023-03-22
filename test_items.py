import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_should_check_basket(browser):

    browser.get(link)
    input1 = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    text_basket = input1.text
    print(f"'Это текст на кнопке:' {text_basket}")
    assert "Añadir al carrito" == text_basket, 'Код теста написан неверно'

