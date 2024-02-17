import crawl
import time
import os

wd_url = os.environ.get('wd_url')
c = crawl.InsolScraper(remote_web_driver_url=wd_url)

while True:
    try:
        c.startup()
        c.fetch_all()
    except Exception as e:
        print(f"unexpected error\n{e}")
    finally:
        c.close()
    if c.finished:
        seconds_in_day = 24 * 60 * 60
        print("crawler got all. Sleeping for one day.")
        time.sleep(seconds_in_day)
    else:
        print("Some error interupted. Trying again in 5 mins.")
        time.sleep(5 * 60)