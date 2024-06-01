from app import db

class Product(db.Model):
    __tablename__ = 'products'

    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    avaialability = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'{self.pid}, {self.name}, {self.description}, {self.avaialability}'
    