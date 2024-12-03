from guizero import *

app = App(title= "hello world")
title = Text(app, text= "make AI helpful for everyone")
text1 = Text(app, text= "donec magna orci, molestie a enim a, dapibus tincidunt nulla. Mauris nunc ligula, tincidunt")
picture = Picture(app, image="rizzler.png", width=500, height=600)
text2 = Text(app, text="donec magna orci, molestie a enim a, dapibus tinci")
text3 = Text(app, text="VTV.vn - Hơn nửa năm qua, hàng loạt đại án tham nhũng trong nhiều cấp, nhiều ngành, nhiều lĩnh vực đã bị phanh phui, điều tra, xử lý kiên quyết. 27 cán bộ thuộc diện Bộ Chính trị, Ban Bí thư quản lý bị kỷ luật từ đầu năm")
 


app.display()