"""Serealizer."""

from flask_marshmallow import Marshmallow
from .model import Book


ma = Marshmallow()

def configure(app):
    """Init serializer."""
    ma.init_app(app)


class BookSchema(ma.ModelSchema):
    """Create serializer."""
    class Meta():
        """Create serializer."""
        model = Book
