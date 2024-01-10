import requests
from bs4 import BeautifulSoup

GOOGLE_SHEET_URL = "https://docs.google.com/forms/d/e/1FAIpQLSdcFQvqz_yfxxNH2_XAou5L1E_jMvh6LsVA2fmtxF_Is4AslA/viewform?usp=sf_link"

class RealEstateTracker:

    # TODO 1: IMPORT ZILLOW HTML DATA BY BEAUTIFUL SOUP
    def scrapping_html(self):
        zillow_data = requests.get("https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-124.05539193846109%2C%22east%22%3A-121.94052377439859%2C%22south%22%3A37.0718974078438%2C%22north%22%3A38.401150478116044%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A602349%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sort%22%3A%7B%22value%22%3A%22days%22%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A8%7D")
        soup = BeautifulSoup(zillow_data.text, 'html.parser')

        elements = soup.select("div", {'id': 'wrapper'})
        for element in elements:
            print(element.text)

tracker = RealEstateTracker()
tracker.scrapping_html()