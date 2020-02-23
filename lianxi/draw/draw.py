data = [
(2019, 2.2,  3.2, 1.2),
(2019, 2.2,  4.2, 0.2),
(2019, 2.0,  5.0, 0.0),
(2019, 1.8,  6.8, 0.0),
(2019, 1.8,  6.8, 0.0),
(2020, 1.9,  7.9, 0.0),
(2020, 2.1,  9.1, 0.0),
(2020, 2.2,  9.2, 0.0),
(2020, 2.3, 10.3, 0.0),
(2020, 2.5, 11.5, 0.0),
(2020, 2.6, 11.6, 0.0),
(2020, 2.5, 12.5, 0.0),
(2020, 2.3, 12.3, 0.0),
(2020, 2.0, 12.0, 0.0),
(2020, 1.9, 11.9, 0.0),
(2020, 1.7, 11.7, 0.0),
(2020, 1.6, 11.6, 0.0),
(2021, 1.5, 11.5, 0.0),
(2021, 1.3, 11.3, 0.0),
(2021, 1.2, 11.2, 0.0),
(2021, 1.1, 11.1, 0.0),
(2021, 1.0, 11.0, 0.0),
(2021, 0.9, 10.9, 0.0),
(2021, 0.9, 10.9, 0.0),
(2021, 0.8, 10.8, 0.0),
(2021, 0.7, 10.7, 0.0),
(2021, 0.7, 10.7, 0.0),
(2021, 0.6, 10.6, 0.0),
(2021, 0.5, 10.5, 0.0),
(2022, 0.5, 10.5, 0.0),
(2022, 0.4, 10.4, 0.0),
(2022, 0.4, 10.4, 0.0),
(2022, 0.4, 10.4, 0.0),
(2022, 0.3, 10.3, 0.0),
(2022, 0.3, 10.3, 0.0),
(2022, 0.3, 10.3, 0.0),
(2022, 0.2, 10.2, 0.0),
(2022, 0.2, 10.2, 0.0),
(2022, 0.2, 10.2, 0.0),
(2022, 0.2, 10.2, 0.0),
(2022, 0.2, 10.2, 0.0)
]

for data_i in data:
    print(data_i)
    print(' ')

#from reportlab.graphics.shaps import Drawing, String
#from reportlab.graphics import renderPDF
import reportlab

#d = Drawing(100, 100)
#s = String(50, 50, 'Hello World!', textAnchor='middle')
#d.add(s)

#renderPDF.drawToFile(d, 'hello.pdf', 'A simple PDF file')

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate
from reportlab.lib import colors

Style=getSampleStyleSheet()

bt = Style['Normal']     #字体的样式
# bt.fontName='song'    #使用的字体
bt.fontSize=14            #字号
bt.wordWrap = 'CJK'    #该属性支持自动换行，'CJK'是中文模式换行，用于英文中会截断单词造成阅读困难，可改为'Normal'
bt.firstLineIndent = 32  #该属性支持第一行开头空格
bt.leading = 20             #该属性是设置行距

ct=Style['Normal']
# ct.fontName='song'
ct.fontSize=12
ct.alignment=1             #居中

ct.textColor = colors.red

t = Paragraph('hello',bt)
pdf=SimpleDocTemplate('ppff.pdf')
pdf.multiBuild([t])


