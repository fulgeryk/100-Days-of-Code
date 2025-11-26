from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[Length(min=5, message='Cafe name must be at least 5 characters long'), DataRequired()])
    location = StringField('Cafe Location from Google Maps (URL)', validators=[URL(require_tld=True, message='Invalid URL'), DataRequired()])
    open_time = StringField('Opening time eg 8AM', validators=[DataRequired()])
    close_time = StringField('Closing time eg 8PM', validators=[DataRequired()])
    coffee_rating = SelectField(
    label='Coffee rating',
    choices=[
        ('☕', '☕'),
        ('☕☕', '☕☕'),
        ('☕☕☕', '☕☕☕'),
        ('☕☕☕☕', '☕☕☕☕'),
        ('☕☕☕☕☕', '☕☕☕☕☕')
    ],
    validators=[DataRequired()]
    )
    wifi_strength = SelectField(
    label='WiFi strength',
    choices=[
        ('✘', '✘'),
        ('💪', '💪'),
        ('💪💪', '💪💪'),
        ('💪💪💪', '💪💪💪'),
        ('💪💪💪💪', '💪💪💪💪'),
        ('💪💪💪💪💪', '💪💪💪💪💪')
    ],
    validators=[DataRequired()]
    )
    power_outlet = SelectField(
    label='Power outlet availability',
    choices=[
        ('✘', '✘'),
        ('🔌', '🔌'),
        ('🔌🔌', '🔌🔌'),
        ('🔌🔌🔌', '🔌🔌🔌'),
        ('🔌🔌🔌🔌', '🔌🔌🔌🔌'),
        ('🔌🔌🔌🔌🔌', '🔌🔌🔌🔌🔌')
    ],
    validators=[DataRequired()]
    )
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods = ["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv', mode='a', newline="", encoding='utf-8') as csv_file:
                csv_file.write(f"\n{form.cafe.data},{form.location.data},{form.open_time.data},{form.close_time.data},{form.coffee_rating.data},{form.wifi_strength.data},{form.power_outlet.data}")
        with open('cafe-data.csv', newline="", encoding='utf-8') as csv_file:
            csv_data = csv.reader(csv_file)
            cafes = list(csv_data)

        return render_template('cafes.html', cafes=cafes)
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
