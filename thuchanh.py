from guizero import *
from random import *
def matkhau():
    kitu = ["12e", "skd", "3m2","t0l"]
    a = choice(kitu)
    b = choice(kitu)
    c = choice(kitu)

    mkhau = a + b + c
    

app = App(title= "password")
button = PushButton(app, matkhau, text="Ấn để tạo mật khẩu")
mkhau = Text(app, text="")

app.display()