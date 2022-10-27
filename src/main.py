from scraping import Scraping
from txt2pdf import Txt2Pdf


class Main:
    def __init__(self) -> None:
        self.scraping = Scraping()
        self.txt2pdf = Txt2Pdf()

    def main(self) -> None:
        data = self.scraping.get_hrefs()
        self.txt2pdf.txt2pdf(data[0]["content"])


if __name__ == "__main__":
    main = Main()
    main.main()
