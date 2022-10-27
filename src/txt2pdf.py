from fpdf import FPDF


class Txt2Pdf:
    def __init__(self) -> None:
        self.pdf = FPDF()

    def txt2pdf(self, data: str) -> None:
        data = data.encode("latin-1", "ignore").decode("latin-1")
        self.pdf.set_font("Arial", size=12)
        self.pdf.add_page()
        self.pdf.multi_cell(0, 5, txt=data)
        self.pdf.output("test.pdf")


if __name__ == "__main__":
    txt2pdf = Txt2Pdf()
    txt2pdf.txt2pdf("Hello World")
