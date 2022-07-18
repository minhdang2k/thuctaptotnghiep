# Flask- Mail Tutorial
# File & Directories (Creating vitual environment is optional)
# Frontend HTML File Setup (Press "! + Tab" to get boilerplate HTML)
# This block of code í setting up Flask-Mail to send emails (mail server, port, sender's email, etc)
from flask import Flask, render_template, request
from flask_mail import Mail, Message
import os

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'minhdang2804@gmail.com'
app.config['MAIL_PASSWORD'] = 'ziiktromsincuchg' # 'Nhập mật khẩu ứng dụng'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)



@app.route('/home', methods= ['GET', 'POST'])
@app.route('/', methods= ['GET', 'POST'])
def home():
    if request.method == 'POST':
        msg = Message("Bao cao thu 4", sender='minhdang2804@gmail.com', recipients=['vutruong5438@gmail.com', 'thopn95@gmail.com'])
        msg.body = "Em Minh chao 2 anh dep trai bang flask"
        mail.send(msg)
        return "Sent email"
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)