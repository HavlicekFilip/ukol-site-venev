"""
Logic for dashboard related routes
"""
from flask import Blueprint, render_template, flash,redirect,url_for
from .forms import LogUserForm, secti,masoform,zboziform,ukolform
from ..data.database import db
from ..data.models import LogUser
from ..data.models import Zbozi
from ..data.models import Ukol


blueprint = Blueprint('public', __name__)

@blueprint.route('/', methods=['GET'])
def index():
    return render_template('public/index.tmpl')

@blueprint.route('/loguserinput',methods=['GET', 'POST'])
def InsertLogUser():
    form = LogUserForm()
    if form.validate_on_submit():
        LogUser.create(**form.data)
    return render_template("public/LogUser.tmpl", form=form)

@blueprint.route('/loguserlist',methods=['GET'])
def ListuserLog():
    pole = db.session.query(LogUser).all()
    return render_template("public/listuser.tmpl",data = pole)

@blueprint.route('/secti', methods=['GET','POST'])
def scitani():
    form = secti()
    if form.validate_on_submit():
        return render_template('public/vystup.tmpl',hod1=form.hodnota1.data,hod2=form.hodnota2.data,suma=form.hodnota1.data+form.hodnota2.data)
    return render_template('public/secti.tmpl', form=form)

@blueprint.route('/maso', methods=['GET','POST'])
def masof():
    form = masoform()
    if form.validate_on_submit():
        return render_template('public/masovystup.tmpl',hod1=form.hodnota1.data,hod2=form.hodnota2.data,suma=form.hodnota1.data+form.hodnota2.data)
    return render_template('public/maso.tmpl', form=form)

@blueprint.route('/zbozi', methods=['GET','POST'])
def Formular():
    form = zboziform()
    if form.validate_on_submit():
        Zbozi.create(**form.data)
        flash("Ulozeno",category="INFO")
    return render_template('public/zboziform.tmpl', form=form)

@blueprint.route('/vystupzbozi', methods=['GET'])
def ZboziList():
    pole = db.session.query(Zbozi).all()
    return render_template('public/vystupzbozi.tmpl', pole=pole)

@blueprint.route('/smazZbozi/<id>', methods=['GET'])
def FormularDel(id):
    iddel = db.session.query(Zbozi).filter_by(id=id).first()
    Zbozi.delete(iddel)
    return redirect(url_for('public.ZboziList'))

@blueprint.route('/ukol', methods=['GET','POST'])
def Formularukol():
    form = ukolform()
    if form.validate_on_submit():
        Ukol.create(**form.data)
        flash("Ulozeno",category="INFO")
    return render_template('public/ukolform.tmpl', form=form)

@blueprint.route('/vystupukol', methods=['GET'])
def UkolList():
    pole = db.session.query(Ukol).all()
    return render_template('public/vystupukol.tmpl', pole=pole)

@blueprint.route('/smazUkol/<id>', methods=['GET'])
def UkolDel(id):
    iddel = db.session.query(Ukol).filter_by(id=id).first()
    Ukol.delete(iddel)
    return redirect(url_for('public.UkolList'))