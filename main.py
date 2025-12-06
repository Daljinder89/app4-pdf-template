from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(False, 0)
df = pd.read_csv('topics.csv')

for index, row in df.iterrows():
    for i in range(row['Pages']):
        pdf.add_page()
        pdf.set_font(family='Arial', style='B', size=24)
        pdf.set_text_color(100,100,100)
        pdf.cell(w=0, h=12, txt=row["Topic"], align='L', ln=1)
        pdf.set_line_width(.35)
        pdf.line(10, 22, 200, 22)

        #footer
        pdf.ln(265)
        pdf.set_font(family='Arial', style='B', size=8)
        pdf.set_text_color(100,100,100)
        pdf.cell(w=0, h=10, txt=row["Topic"], align='R')


pdf.output('output.pdf')