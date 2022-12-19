from flask import Flask
import random

from numpy import number
import random

random_number = random.randint(0,9)
print(random_number)

app = Flask(__name__)
print(random.__name__)
print(__name__)
@app.route('/')
def hello_world():
    return '<h1>guess the number 0 to 9</h1>'
@app.route('/<int:number>')
def guess_number(number):
    if  number>random_number:
        return '<h2 style="color:red">Number is to high chosie low number</h2>\
                <img src="https://logos.flamingtext.com/Word-Logos/high-design-china-name.png">'
    elif number<random_number:
        return  "<h2 style='color:yellow'>Number is to low chosie low number</h2>\
                <img src='https://www.creativefabrica.com/wp-content/uploads/2022/01/30/Low-word-aesthetic-retro-text-design-Graphics-6633320.jpg'>"   
    else:
        return "<h2 style='color:green'>you win</h2>\
                <img src='https://ak.picdn.net/shutterstock/videos/34233727/thumb/1.jpg'>"  
if __name__=="__main__":
    app.run(debug=True)            
