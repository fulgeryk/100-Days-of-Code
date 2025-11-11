from flask import Flask, render_template
import random
import datetime
from agify import Agify
from genderize import Genderize
from npoint import Npoint
app = Flask(__name__)

age = Agify()
gender = Genderize()

@app.route("/")
def home():
    random_number = random.randint(1,10)
    current_year = datetime.date.today().year
    return render_template('index.html', num = random_number, year = current_year)

@app.route('/guess/<name>')
def check_user(name):
    check_age = age.find_age(name)
    check_gender = gender.find_gender(name)
    return render_template('guess.html', nume = name, age_to_return = check_age, gender_to_return = check_gender)

@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    new_posts = Npoint()
    all_posts = new_posts.get_info_npoint
    return render_template('blog.html', posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)