from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Scraping:
    def __init__(self):
        # Set driver
        # self.s_driver = Service(ChromeDriverManager().install())
        self.options = Options()
        self.options.add_argument("--headless")
        self.options.add_argument("--no-sandbox")
        # # docker
        # self.driver = webdriver.Chrome("/usr/bin/chromedriver", options=self.options)
        # local
        self.driver = webdriver.Chrome(
            "/usr/local/bin/chromedriver", options=self.options
        )

        self.hrefs = []
        self.data = []

    def scraping(self, url: str = "https://nav.al/") -> list:
        self.hrefs = []

    def get_hrefs(self, url: str = "https://nav.al/") -> list:
        self.driver.get(url)
        self.hrefs = [
            self.driver.find_element(
                By.XPATH,
                "/html/body/div[1]/main/section/div/div[2]/div/div[2]/div[1]/div[1]/article[1]/div/header/h2/a",
            )
        ]
        print(f"hrefs: {self.hrefs}")
        # Move to hrefs and get data
        for href in self.hrefs:
            url = href.get_attribute("href")
            self.data.append(self.get_data(url))
        return self.data

    def get_data(self, href: str) -> dict:
        print(f"href: {href}")
        self.driver.get(href)
        data = {
            "content": self.driver.find_element(
                By.XPATH,
                "/html/body/div[1]/main/section/div/div/div/div/article/div/div[2]",
            ).text,
        }
        # print(f"data: {data}")
        return data

        # self.hrefs = self.driver.find(By.XPATH, "/html/body/div[1]/main/section/div/div[2]/div/div[2]/div[1]/div[1]/article[2]/div/header/h2/a")
        # self.hrefs = [self.driver.find(By.XPATH, f"/html/body/div[1]/main/section/div/div[2]/div/div[2]/div[1]/div[1]/article[{idx}]/div/header/h2/a") for idx in range(1, 11)]


if __name__ == "__main__":
    scraping = Scraping()
    scraping.get_hrefs()
