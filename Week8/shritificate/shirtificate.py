from fpdf import FPDF

def create_shirt(name):

    pdf = FPDF()
    pdf.add_page()
    # Rendering logo:
    pdf.image("shirtificate.png", x="C", y=75 , w=200)
    # Setting font: helvetica bold 15
    pdf.set_font("helvetica", "B", 50)
    # Printing title:
    pdf.cell(text="CS50 Shirtificate", center=True, align="C", h=75)

    # set frot
    pdf.set_font(size=25)
    # set color to white
    pdf.set_text_color(255,255,255)
    # Print the shirt top text
    pdf.cell(text=f"{name} took CS50", center=True, align="C", h=275)
    pdf.set_margin(0)

    pdf.output("shirtificate.pdf")


def get_name():
    return input("Name: ")

def main():
    name = get_name()
    create_shirt(name)



if __name__ == "__main__":
    main()
