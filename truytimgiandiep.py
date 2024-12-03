from guizero import *
from  random import *

list1 = []

def add():
    list1.append(input_box.value)
    print(list1)
    input_box.value = ""

def choose_name():
     
    name = choice(list1)
    name_text.value = name

app = App(title= "truy tìm gián điệp")
text = Text(app, text="Nhấn nút để tìm")
button = PushButton(app, choose_name, text="Tìm")
nut = PushButton(app, add, text="thim")
nut.bg = "purple"

button.bg = "pink"
input_box = TextBox(app)
name_text = Text(app, text="")

app.display()