"""Small, reusable Selenium actions for page objects."""

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


DEFAULT_TIMEOUT = 10


def wait_until(driver, condition, timeout=DEFAULT_TIMEOUT):
    """Wait until a Selenium expected condition becomes true."""
    return WebDriverWait(driver, timeout).until(condition)


def visible_element(driver, locator, timeout=DEFAULT_TIMEOUT):
    """Return one element after it becomes visible."""
    return wait_until(driver, EC.visibility_of_element_located(locator), timeout)


def visible_elements(driver, locator, timeout=DEFAULT_TIMEOUT):
    """Return visible matching elements after they load."""
    return wait_until(
        driver, EC.visibility_of_all_elements_located(locator), timeout
    )


def visible_text(driver, locator, expected_text=None, timeout=DEFAULT_TIMEOUT):
    """Return visible element text, optionally waiting for exact text."""
    if expected_text is None:
        return visible_element(driver, locator, timeout).text

    def text_matches(browser):
        element = browser.find_element(*locator)
        if element.is_displayed() and element.text.strip() == expected_text:
            return element
        return False

    return wait_until(driver, text_matches, timeout).text.strip()


def click_when_ready(driver, locator, timeout=DEFAULT_TIMEOUT):
    """Click an element once Selenium considers it clickable."""
    element = wait_until(driver, EC.element_to_be_clickable(locator), timeout)
    element.click()


def click_element_when_ready(driver, element, timeout=DEFAULT_TIMEOUT):
    """Click an already located element when it is visible and enabled."""
    ready_element = wait_until(
        driver,
        lambda _driver: element
        if element.is_displayed() and element.is_enabled()
        else False,
        timeout,
    )
    ready_element.click()


def child_texts(driver, parent_locator, child_locator, timeout=DEFAULT_TIMEOUT):
    """Return text from a child element in each visible parent element."""
    parents = visible_elements(driver, parent_locator, timeout)
    return [parent.find_element(*child_locator).text for parent in parents]
