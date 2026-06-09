from selenium.webdriver.common.by import By
import pytest


@pytest.mark.usefixtures("setup_and_teardown")
class Testsearch:

    @pytest.mark.valid
    def test_validproduct(self):
        self.driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys("canon")

        self.driver.find_element(By.XPATH,
            "//button[@class='btn btn-default btn-lg']"
        ).click()

        pytest.assume(
            self.driver.find_element(
                By.XPATH,
                "//img[@title='Canon EOS 5D']"
            ).is_displayed(),
            "Canon product is not displayed"
        )

    def test_invalidproduct(self):
        self.driver.find_element(
            By.XPATH,
            "//input[@placeholder='Search']"
        ).send_keys("honda")

        self.driver.find_element(
            By.XPATH,
            "//button[@class='btn btn-default btn-lg']"
        ).click()

        actual_text = self.driver.find_element(
            By.XPATH,
            "//p[contains(text(),'There is no product that matches the search criter')]"
        ).text

        pytest.assume(
            actual_text == "There is no product that matches the search criteria.",
            "Invalid product message mismatch"
        )

    @pytest.mark.valid
    def test_noproduct(self):
        self.driver.find_element(
            By.XPATH,
            "//input[@placeholder='Search']"
        ).send_keys("")

        self.driver.find_element(
            By.XPATH,
            "//button[@class='btn btn-default btn-lg']"
        ).click()

        actual_text = self.driver.find_element(
            By.XPATH,
            "//p[contains(text(),'There is no product that matches the search criter')]"
        ).text

        pytest.assume(
            actual_text == "There is no product that matches the search criteria.",
            "No product search message mismatch"
        )