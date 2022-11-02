import csv
from fpdf import FPDF

with open('test.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0

    # L = landscape
    pdf = FPDF('L', 'mm', "A4")
    pdf.add_font("Georgia", '', './Georgia.ttf', uni=True)
    pdf.add_font("Georgia_bold", '', './georgia-grassetto.ttf', uni=True)
    pdf.set_left_margin(40)
    pdf.set_right_margin(40)

    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f"{line_count}. - {row[0]}")
            pdf.add_page()
            # pdf.image('background-image_big.png', 0, 0, 297, 210)
            pdf.image('background-image.png', 0, 0, 297, 210)
            first_line = "Certificate of Achievement"
            second_line = "for"
            third_line = row[0]
            if int(row[2]) >= 80:
                forth_line = f"Passed with merit {row[1]} level for {row[2]} %."
                forth_2line = f"Your result is good enough to pass {row[1]} test. Congratulation!"
            elif int(row[2]) >= 50:
                forth_line = f"Passed {row[1]} level for {row[2]} %."
                forth_2line = f"Congratulation! You have everything correct."
            else:
                forth_line = f"For taking part in {row[1]} course."
                forth_2line = f"This percentage is not enough to pass {row[1]} test. Minimum for passing is 70 %."

            fifth_line = "V Moravském Krumlově dne 25. 6. 2022."
            logo = pdf.image('logo.png', 180, 145)

            # certificate
            pdf.set_font("Georgia", size=52)
            pdf.cell(0, 50, txt=" ", ln=1, align='C')
            pdf.cell(0, 10, txt=first_line, ln=1, align='C')

            # for
            pdf.set_font("Georgia", size=25)
            pdf.cell(0, 25, txt=second_line, ln=1, align='C')

            # name
            pdf.set_font("Georgia_bold", size=60)
            pdf.set_text_color(150, 39, 66)
            pdf.cell(0, 10, txt=third_line, ln=1, align='C')

            #other
            pdf.set_font("Georgia", size=25)
            pdf.set_text_color(1, 1, 1)
            pdf.cell(0, 10, txt=" ", ln=1, align='C')
            pdf.cell(0, 10, txt=forth_line, ln=1, align='C')
            # pdf.cell(0, 5, txt=forth_2line, ln=1, align='C')
            pdf.set_font("Georgia", size=20)
            pdf.cell(0, 15, txt=" ", ln=1, align='C')
            pdf.cell(0, 10, txt=fifth_line, ln=1, align='L')

            line_count += 1
    print(f'Processed {line_count} lines, first line is not name - processed names {line_count-1}.')

#----------------------------------------

# save the pdf with name .pdf
import datetime
pdf.output(f"test_{datetime.datetime.now().hour}_{datetime.datetime.now().minute}_{datetime.datetime.now().second}.pdf")
