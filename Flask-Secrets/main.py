from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, InputRequired, Email, Length
from flask_bootstrap import Bootstrap

class LogInForm(FlaskForm):
    email = EmailField(
        label='Email',
        validators=[DataRequired(), Email(check_deliverability=True)],
        render_kw={'style': 'width: 30ch'}
    )
    password = PasswordField(
        label='Password',
        validators=[InputRequired(), Length(min=6)],
        render_kw={'style': 'width: 40ch'}
    )
    submit = SubmitField(label='Log In', render_kw={'btn-primary': 'True'})

app = Flask(__name__)

bootstrap = Bootstrap5(app)

app.secret_key = "bro345wtf69"

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LogInForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=login_form)

if __name__ == '__main__':
    app.run(debug=True)
