from flask import render_template, redirect, request, url_for

from app import app

posts = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        city = request.form['city']
        hobby = request.form['hobby']
        age = request.form['age']
        if name and city and hobby and age:
            posts.append({'name': name, 'city': city, 'hobby': hobby, 'age': age})
            return redirect(url_for('index'))
    return render_template('form.html', posts=posts)