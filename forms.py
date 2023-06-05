from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField, EmailField, TextAreaField
from wtforms.validators import DataRequired

class NewProduct(FlaskForm):
    '''
    Create the form to be used to add a new product
    '''
    name = StringField(label="Name", validators=[DataRequired()])
    Price = StringField(label="Price", validators=[DataRequired()])
    desc = StringField(label="Description", validators=[DataRequired()])
    category = StringField(label="Category", validators=[DataRequired()])
    size = StringField(label="Size", validators=[DataRequired()])
    image = FileField(label="Image", validators=[DataRequired()])
    submit = SubmitField(label="Add Product", validators=[DataRequired()])


class ContactUs(FlaskForm):
    '''
    Create a the contact us form
    Name
    Email
    Subject
    Message
    '''
    name = StringField(label="Name")
    email = EmailField(label="Email")
    subject = StringField(label="Subject")
    message = TextAreaField(label="Message")
    submit = SubmitField(label="Send")

    
