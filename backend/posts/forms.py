from wtforms import Form, StringField, TextAreaField  # type: ignore
from wtforms.validators import InputRequired, Length


class PostForm(Form):
    title = StringField("Title", [InputRequired(), Length(max=140)])
    body = TextAreaField("Body", [InputRequired()])
    tags = StringField("Tags")
