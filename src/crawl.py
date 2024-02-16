import datetime

import driver
import repository


class InsolScraper:

    def __init__(self, remote_web_driver_url: str) -> None:
        self.repo = repository.Repository()
        self.driver = driver.Driver(remote_web_driver_url)
        self.finished = False

    def startup(self):
        self.repo.open()
        self.driver.start()

    def close(self):
        if self.driver is not None:
            self.driver.close()
        if self.repo is not None:
            self.repo.close()

    def fetch_all(self):
        self.driver.fetch_for_date(datetime.date(2019, 10, 17))




if __name__ == "__main__":
    c = InsolScraper(remote_web_driver_url="http://192.168.0.2:4445/wd/hub")
    try:
        c.startup()
        c.fetch_all()
    finally:
        c.close()
