from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import InvalidSessionIdException
from typing import List
from urllib3.exceptions import ReadTimeoutError
from selenium.webdriver.support.wait import WebDriverWait

import remote_gateway
import insolvency


class Driver:

    def __init__(self, remote_web_driver_url: str) -> None:
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--ignore-ssl-errors=yes')
        self.options.add_argument('--ignore-certificate-errors')

        self.remote_web_driver_url = remote_web_driver_url
        self.driver = None
        self.next_sleep_time = 0

        self.gateway = remote_gateway.RemoteGateway(retryable_errors=[ReadTimeoutError],
                                                    accepted_errors=[NoSuchElementException,
                                                                     StaleElementReferenceException],
                                                    error_handlers=[(InvalidSessionIdException, self.restart)])

    def restart(self):
        self.close()
        self.start()

    def start(self):
        self.driver = webdriver.Remote(
            command_executor=self.remote_web_driver_url,
            options=self.options
        )
        self.driver.maximize_window()

    def close(self):
        if self.driver is not None:
            self.driver.close()
            self.driver.quit()

    def extract_details(self) -> List[insolvency.Insolvency]:
        return []  # TODO get elements and extract data

    def fetch_for_date(self, date) -> List[insolvency.Insolvency]:
        self.load_results(date)
        return self.extract_details()

    def load_results(self, date):
        suchen_btn = "frm_suche:cbt_suchen"
        date_str = date.strftime('%m%d%Y')
        print(f"fetching for {date_str}")
        self.gateway.crawl_call(lambda: self.driver.get("https://neu.insolvenzbekanntmachungen.de/ap/suche.jsf"))
        self.gateway.crawl_call(lambda: self.driver.find_element(By.ID, "frm_suche:ldi_datumVon:datumHtml5")
                                .send_keys(date.strftime('%m%d%Y')))
        self.gateway.crawl_call(lambda: self.driver.find_element(By.ID, "frm_suche:ldi_datumBis:datumHtml5")
                                .send_keys(date_str))
        self.gateway.crawl_call(lambda: self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);"))
        self.gateway.crawl_call(lambda: self.driver.find_element(By.ID, suchen_btn)
                                .click())
        self.gateway.crawl_call(lambda: WebDriverWait(driver=self.driver, timeout=10 * 60).until(
            lambda d: d.execute_script('return document.readyState') == 'complete'))



