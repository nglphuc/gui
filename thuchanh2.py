from guizero import *
from random import choice
# def random_hinh():
#     hinhanh = ["anh/anh1.png", "anh/anh2.png", "anh/anh3.png", "anh/anh4.png"]
#     anh = choice(hinhanh)

app = App(title= "random pic")
button = PushButton(app, text= "Click")
pic1 = Picture(app, "anh/anh1.png")
app.display()