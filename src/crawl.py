import datetime

import driver
import repository


class InsolScraper:
    WAIT_DAYS_BEFORE_SCRAPE = 10

    def __init__(self, remote_web_driver_url: str) -> None:
        self.repo = repository.Repository()
        self.driver = driver.Driver(remote_web_driver_url)
        self.finished = False

    def startup(self):
        self.repo.open()
        self.driver.start()
        self.finished = False

    def close(self):
        if self.driver is not None:
            self.driver.close()
        if self.repo is not None:
            self.repo.close()

    def fetch_all(self):
        dates = self.repo.scraped_dates()
        wanted_dates = self.wanted_dates()
        dates_to_scrape: set = wanted_dates.difference(dates)
        while len(dates_to_scrape) > 0:
            print(f"Dates to go: {len(dates_to_scrape)}")
            next_date = dates_to_scrape.pop()
            print(f"fetching for {next_date}")
            results = self.driver.fetch_for_date(next_date)
            if len(results) == 1000:
                print("1000 results found")
            elif len(results) == 0:
                print("No Insolvencies found")
            self.repo.insert_data(results, next_date)
        self.finished = True

    def wanted_dates(self):
        end_date = datetime.date.today() - datetime.timedelta(days=self.WAIT_DAYS_BEFORE_SCRAPE)
        start_date = datetime.date(2000,1,1)
        date = end_date
        wanted_dates = set()
        while date != start_date:
            date = date - datetime.timedelta(days=1)
            wanted_dates.add(date)
        return wanted_dates

