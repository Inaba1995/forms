from flask import render_template, redirect, request, url_for, flash, abort

from app import app

ancet = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        if title and content:
            ancet.append({'title': title, 'content': content})
            return redirect(url_for('index'))
    return render_template('index.html', ancet=ancet)