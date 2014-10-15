
from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(120))
    autor = db.Column(db.String(120))
    editora = db.Column(db.String(100))
    categoria = db.Column(db.String(120))
    status = db.Column(db.String(20))
    quantidade = db.Column(db.Integer)
    descricao = db.Column(db.String(120))
    tipo = db.Column(db.String(20))

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3


class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    data_emprestimo = db.Column(db.String)
    data_devolucao = db.Column(db.String)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3
