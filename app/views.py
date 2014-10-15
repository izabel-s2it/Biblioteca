from flask import render_template, flash, redirect, session, url_for, request, g
from app import app, db
from forms import BookForm, LoadForm
from models import Book, Loan
import datetime,time


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    form = BookForm()
    if form.validate_on_submit():
        book = Book(titulo=request.form['titulo'], autor=request.form['autor'], editora=request.form['editora'], categoria=request.form['categoria'], tipo=request.form['tipo'], status=request.form['status'], quantidade=request.form['quantidade'], descricao=request.form['descricao'])
        db.session.add(book)
        flash('Livro inserido com sucesso!!')
        db.session.commit()
        return redirect(url_for('cadastro'))

    return render_template('cadastro.html', form=form)


@app.route('/lista')
def lista():
    book = Book.query.all()
    if book is None:
        flash('Empty')
        return redirect(url_for('index'))
    return render_template('lista.html', book=book)

@app.route('/edita/<id>', methods=['GET', 'POST'])
def edita(id):
    book_list = Book.query.filter_by(id=id).first()
    form = BookForm()
    form.titulo.data = book_list.titulo
    form.autor.data = book_list.autor
    form.editora.data = book_list.editora
    form.categoria.data = book_list.categoria
    form.tipo.data = book_list.tipo
    form.status.data = book_list.status
    form.quantidade.data = book_list.quantidade
    form.descricao.data = book_list.descricao
    if form.validate_on_submit():
        #book = Book(titulo=request.form['titulo'], autor=request.form['autor'], editora=request.form['editora'], categoria=request.form['categoria'], tipo=request.form['tipo'], status=request.form['status'], quantidade=request.form['quantidade'], descricao=request.form['descricao'], id=id)
        db.session.execute("UPDATE Book SET titulo = '"+request.form['titulo']+"', autor = '"+request.form['autor']+"', editora = '"+request.form['editora']+"', categoria = '"+request.form['categoria']+"', tipo = '"+request.form['tipo']+"', status = '"+request.form['status']+"', quantidade = '"+request.form['quantidade']+"', descricao = '"+request.form['descricao']+"' where id = '"+id+"'")
        flash('Livro editado com sucesso!!')
        db.session.commit()
        return redirect(url_for('lista'))

    return render_template('cadastro.html', form=form, book_list=book_list)


@app.route('/emprestimo', methods=['GET', 'POST'])
def emprestimo():
    book = Book.query.all()
    form = LoadForm()
    if form.data_devolucao.data:
        loan = Loan(book_id=request.form['titulos'], data_emprestimo=request.form['data_emprestimo'], data_devolucao=request.form['data_devolucao'])
        db.session.add(loan)
        flash('Emprestimo inserido com sucesso!!')
        db.session.commit()
        return redirect(url_for('emprestimo'))
    else:
        print('ahhhhh')

    return render_template('emprestimo.html', book=book, form=form)

@app.route('/lista_emprestimo')
def lista_emprestimo():
    loan = Loan.query.all()
    if loan is None:
        flash('Empty')
        return redirect(url_for('index'))
    return render_template('lista_emprestimo.html', loan=loan)