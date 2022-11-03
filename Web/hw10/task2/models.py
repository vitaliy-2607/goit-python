from mongoengine import EmbeddedDocument, Document
from mongoengine.fields import BooleanField, DateTimeField, EmbeddedDocumentField, ListField, StringField, EmailField


class Person(Document):
    name = StringField(max_length=100, required=True)
    phone = StringField(max_length=20, required=True)
    email = EmailField()


    meta = {'indexes': [
        {'fields': ['$name', "$phone", "$email"],
         'default_language': 'english',
         'weights': {'name': 10, 'phone': 9, 'email': 8}
         }
    ]}
