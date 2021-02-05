from flask import render_template, Flask
from flask_mail import Mail, Message
from flask import request
import  smtplib




app = Flask(__name__)


@app.route("/")
def index():
   title = "Mihlali"
   return  render_template("index.html", title = title)

@app.route('/form', methods =["POST"])
def form():
   name = request.form.get("name")
   email= request.form.get("email")
   message = request.form.get("message")
   my_email = "momozamihlali@gmail.com"
   my_password = "khazimla"

   server= smtplib.SMTP("smtp.gmail.com", 587)
   server.starttls()
   server.login(my_email, my_password)
   server.sendmail(my_email, message,email)

   server.quit()

   if not name or not email or not message:
      error_statement = "All form fields required"
      return render_template(index.html, error_statement=error_statement,
                             name=name,
                             email=email,
                             message=message)
   index.append(f"{name}{email}{message}")
   return render_template(index.html)






