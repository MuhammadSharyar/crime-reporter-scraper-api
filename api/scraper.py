from requests_html import HTMLSession
import os

os.environ['URL'] = 'http://localhost:3000/'

class Scraper():

    def scrapedata(self):
        s = HTMLSession()
        r = s.get(os.environ['URL'])
        print(r.status_code)

        report_list = []

        reports = r.html.find('div.Home_card___LpL1')

        for re in reports:
            item = {
                'text': re.text.strip(),
            }
            report_list.append(item)

        return report_list




reports = Scraper()

reports.scrapedata()