"""
In a file called shirtificate.py, implement a program that prompts
the user for their name and outputs, using fpdf2, a CS50 shirtificate
in a file called shirtificate.pdf similar to this one for John Harvard,
with these specifications:

    The orientation of the PDF should be Portrait.
    The format of the PDF should be A4, which is 210mm wide by 297mm tall.
    The top of the PDF should say “CS50 Shirtificate” as text, centered horizontally.
    The shirt’s image should be centered horizontally.
    The user’s name should be on top of the shirt, in white text.

All other details we leave to you. You’re even welcome to add borders,
colors, and lines. Your shirtificate needn’t match John Harvard’s precisely.
And no need to wrap long names across multiple lines.

Before writing any code, do read through fpdf2’s tutorial to learn how to use it.
Then skim fpdf2’s API (application programming interface) to see all of its functions
and parameters therefor.

No need to submit any PDFs with your code. But, if you would like, you’re welcome
but not expected) to share a shirtificate with your name on it in any of CS50’s communities!


"""

#install FPDF via "pip install fpdf2"
from fpdf import FPDF

#subclass for FPDF to include a header
#py-pdf.github.io/fpdf2/Tutorial.html#tuto-2-header-footer-page-break-and-image
class PDF(FPDF):
    def header(self):
        # Performing a line break:
        self.ln(20)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", size=50)
        # Moving cursor to the right:
        self.cell(80, 10)
        # Printing title:
        self.cell(50, 10, "CS50 Shirtificate", border=0, align="C")
        # Performing a line break:
        self.ln(20)


def main():
    name = input("Name: ").strip() + " took CS50"

    #sets up PDF
    pdf = PDF()
    pdf = PDF(orientation="P", unit="mm", format="A4")
    pdf.set_margin(0) #removes margin per https://py-pdf.github.io/fpdf2/Margins.html
    pdf.add_page()

    #adds shirt image
    pdf.image("shirtificate.png", x=1, y=60)

    #sets shirt name
    pdf.set_font("helvetica", size = 30)
    pdf.set_text_color(255, 255, 255)
    pdf.ln(100)
    pdf.cell(0, 10, name, center=True, align='C')

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()