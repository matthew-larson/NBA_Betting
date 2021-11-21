from datetime import datetime
from scrapy import Request, Spider

from basketball_reference.items import BR_StandingsItem
from basketball_reference.item_loaders import BR_StandingsItemLoader


class BR_StandingsSpider(Spider):
    name = "BR_standings_spider"
    allowed_domains = ["basketball-reference.com"]

    current_datetime = datetime.now()
    current_day = current_datetime.strftime("%d")
    current_month = current_datetime.strftime("%m")
    current_year = current_datetime.strftime("%Y")

    # Start of scraping and working backwards in time.
    start_day = 15
    start_month = 11
    start_year = 2021

    start_urls = [
        f"https://www.basketball-reference.com/friv/standings.fcgi?month={start_month}&day={start_day}&year={start_year}&lg_id=NBA"
    ]

    def parse(self, response):
        date = response.xpath('//span[@class="button2 index"]/text()').get()

        for table in ["e", "w"]:
            for row in response.xpath(
                f'//table[@id="standings_{table}"]/tbody/tr'
            ):
                loader = BR_StandingsItemLoader(
                    item=BR_StandingsItem(), selector=row
                )
                loader.add_xpath("team", "th[@data-stat='team_name']/a/text()")
                loader.add_value("date", date)
                loader.add_xpath("wins", "td[@data-stat='wins']/text()")
                loader.add_xpath("losses", "td[@data-stat='losses']/text()")
                loader.add_xpath(
                    "win_perc", "td[@data-stat='win_loss_pct']/text()"
                )
                loader.add_xpath(
                    "points_scored_per_game",
                    "td[@data-stat='pts_per_g']/text()",
                )
                loader.add_xpath(
                    "points_allowed_per_game",
                    "td[@data-stat='opp_pts_per_g']/text()",
                )
                loader.add_xpath(
                    "expected_wins", "td[@data-stat='wins_pyth']/text()"
                )
                loader.add_xpath(
                    "expected_losses", "td[@data-stat='losses_pyth']/text()"
                )

                # add missing fields
                item = loader.load_item()
                fields = [
                    f
                    for f in [
                        "team",
                        "date",
                        "wins",
                        "losses",
                        "win_perc",
                        "points_scored_per_game",
                        "points_allowed_per_game",
                        "expected_wins",
                        "expected_losses",
                    ]
                    if f not in item
                ]

                for f in fields:
                    item[f] = None

                yield item

        active_date = datetime.strptime(
            response.xpath('//span[@class="button2 index"]/text()').get(),
            "%B %d, %Y",
        )
        previous_date = datetime.strptime(
            response.xpath('//a[@class="button2 prev"]/text()').get(),
            "%B %d, %Y",
        )
        stop_date = datetime.strptime("October 12, 2006", "%B %d, %Y")

        # scrape previous date if before stop date
        if active_date > stop_date:
            month = previous_date.month
            day = previous_date.day
            year = previous_date.year

            url = f"https://www.basketball-reference.com/friv/standings.fcgi?month={month}&day={day}&year={year}"

            yield Request(url, callback=self.parse)
