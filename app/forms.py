# -*- coding:utf-8 -*-

from flask.ext.wtf import Form
from app.models import Book
from wtforms import StringField, BooleanField, TextAreaField, IntegerField, SelectField, DateField
from wtforms.validators import DataRequired, Length


class BookForm(Form):
    titulo = StringField('titulo', validators=[DataRequired()])
    autor = StringField('autor', validators=[DataRequired()])
    editora = StringField('editora', validators=[DataRequired()])
    categoria = StringField('categoria', validators=[DataRequired()])
    status = SelectField('status', validators=[DataRequired()], choices=[('', 'Selecione'),('sim', 'Sim'), ('nao', 'Nao')])
    quantidade = IntegerField('quantidade', validators=[DataRequired()])
    descricao = TextAreaField('descricao', validators=[DataRequired()])
    tipo = SelectField('tipo', validators=[DataRequired()], choices=[('', 'Selecione'),('manga', 'Manga'), ('livro', 'Livro'), ('hq', 'HQ')])


class LoadForm(Form):
    data_emprestimo = StringField('data_emprestimo', validators=[DataRequired()])
    data_devolucao = StringField('data_devolucao', validators=[DataRequired()])