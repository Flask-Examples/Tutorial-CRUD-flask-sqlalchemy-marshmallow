"""blueprint Books."""

from flask import Blueprint, current_app, request, jsonify
from .model import Book
from .serealizer import BookSchema

bp_books = Blueprint('books', __name__)


@bp_books.route('/mostrar', methods=['GET'])
def mostrar():
    """Blueprint books mostrar."""
    bs = BookSchema(many=True)
    result = Book.query.all()
    return bs.jsonify(result), 200


@bp_books.route('/cadastrar', methods=['POST'])
def cadastrar():
    """Blueprint books cadastrar."""
    bs = BookSchema()
    book, error = bs.load(request.json)

    # import ipdb; ipdb.set_trace()

    current_app.db.session.add(book)
    current_app.db.session.commit()

    return bs.jsonify(book), 201


@bp_books.route('/deletar/<identificador>', methods=['GET'])
def deletar(identificador):
    """Blueprint books deletar."""
    Book.query.filter(Book.id == identificador).delete()

    current_app.db.session.commit()
    
    return jsonify('Deletado!!!!')


@bp_books.route('/modificar/<identificador>', methods=['POST'])
def modificar(identificador):
    """Blueprint books modificars."""
    bs = BookSchema()

    query = Book.query.filter(Book.id == identificador)
    query.update(request.json)
    
    current_app.db.session.commit()

    return bs.jsonify(query.first())
