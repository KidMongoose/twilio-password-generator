from flask import Flask, render_template, redirect, request, url_for, flash
from twilio.rest import Client
from forms import PasswordForm
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR SECRET KEY'
acct_sid = 'TWILIO ACCOUNT SID'
auth_token = 'TWILIO AUTH TOKEN'
client = Client(acct_sid, auth_token)



def generate_password(password_length):
    characters = '01234567890abcdefghijklmnopqrstuvwxyzABCDFEGHIJKLMNOPQRSTUVWXYZ_<!@>%^*(-)=+'
    pwd = ''.join(random.choice(characters) for _ in range(password_length))
    return pwd



@app.route('/', methods=['GET', 'POST'])
def index():
   form = PasswordForm()
   if form.validate_on_submit():
       return redirect(url_for('/sent'))
   return render_template('index.html', title='Password Generator', form = form)
   

@app.route('/sent', methods=['POST', 'GET'])
def sent():
   if request.method == 'POST':
       form = request.form
       passwd = generate_password(int(request.form['password_length_field']))
       message = client.messages.create(body='Hello from Password Generator. Your password is: \n{}'.format(passwd), from_='+17272059874', to="+{}".format(str(request.form['telephone_number_field'])))
       return render_template('sent.html', form = form)
   

if __name__ == '__main__':
   app.run()