from wtforms import Form, StringField, TextAreaField  # type: ignore


class PostForm(Form):
    title = StringField('Title')
    body = TextAreaField('Body')
