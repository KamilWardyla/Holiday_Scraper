from apscheduler.schedulers.background import BlockingScheduler
from HolidayScraper.holiday_scraper import WebScraper


def scheduler_job():
    sched = BlockingScheduler()

    @sched.scheduled_job('interval', minutes=1)
    def fun():
        web = WebScraper()
        print(web.get_last_list())
        print(web.web_scraper_last_minuter())
        print(web.web_scraper_fly4free())
        print(web.web_scraper_wakacyjni_piraci())

    sched.start()


scheduler_job()
