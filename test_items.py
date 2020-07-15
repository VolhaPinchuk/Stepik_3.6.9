import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_is_on_the_page(browser):
    browser.get(link)
    button = browser.find_elements_by_css_selector("#add_to_basket_form > button")

    assert len(button) == 1 , "error"