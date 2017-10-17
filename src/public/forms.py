

from flask_wtf import Form
from wtforms.fields import BooleanField, TextField, PasswordField, DateTimeField, IntegerField,SelectField, FloatField
from wtforms.validators import EqualTo, Email, InputRequired, Length, re

from ..data.models import User, LogUser, Zbozi
from ..fields import Predicate

def email_is_available(email):
    if not email:
        return True
    return not User.find_by_email(email)

def username_is_available(username):
    if not username:
        return True
    return not User.find_by_username(username)

def safe_characters(s):
    " Only letters (a-z) and  numbers are allowed for usernames and passwords. Based off Google username validator "
    if not s:
        return True
    return re.match(r'^[\w]+$', s) is not None


class LogUserForm(Form):

    jmeno = TextField('Choose your username', validators=[
        Predicate(safe_characters, message="Please use only letters (a-z) and numbers"),
        Length(min=6, max=30, message="Please use between 6 and 30 characters"),
        InputRequired(message="You can't leave this empty")
    ])
    prijmeni = TextField('Choose your username', validators=[
        Predicate(safe_characters, message="Please use only letters (a-z) and numbers"),
        Length(min=6, max=30, message="Please use between 6 and 30 characters"),
        InputRequired(message="You can't leave this empty")
    ])
    pohlavi = BooleanField('Pohlavi')

class secti(Form):
    hodnota1 = IntegerField("vlozHodnotu1", validators=[InputRequired(message="vyzadovano")])
    hodnota2 = IntegerField("vlozHodnotu2", validators=[InputRequired(message="vyzadovano")])
class masoform(Form):
    typ=SelectField('Typ', choices=[(1, "Hovezi"), (2, "Veprove")], default=2)

class zboziform(Form):
    nazev = TextField('Nazev zbozi', validators=[
        Predicate(safe_characters, message="Please use only letters (a-z) and numbers"),
        Length(min=2, max=30, message="Please use between 1 and 30 characters"),
        InputRequired(message="You can't leave this empty")
    ])
    cena = FloatField("vloz cenu", validators=[InputRequired(message="vyzadovano")])
    vyrazen = BooleanField('Vyrazen')
    kusu = IntegerField("pocet kusu", validators=[InputRequired(message="vyzadovano")])

class ukolform(Form):
    jmeno = TextField('Vloz jmeno', validators=[
        Predicate(safe_characters, message="Please use only letters (a-z) and numbers"),
        Length(min=2, max=30, message="Please use between 1 and 30 characters"),
        InputRequired(message="You can't leave this empty")
    ])
    prijmeni = TextField('Prijmeni', validators=[
        Predicate(safe_characters, message="Please use only letters (a-z) and numbers"),
        Length(min=2, max=30, message="Please use between 1 and 30 characters"),
        InputRequired(message="You can't leave this empty")
    ])
    datum = TextField('Datum narozeni [dd(d)mm(m)yyyy(y)]', validators=[
        Predicate(safe_characters, message="Please use only letters (a-z) and numbers"),
        Length(min=2, max=30, message="Please use between 1 and 30 characters"),
        InputRequired(message="You can't leave this empty")
    ])


