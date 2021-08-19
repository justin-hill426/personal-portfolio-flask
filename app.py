from flask import render_template, url_for, request, redirect
from models import db, Project, app
import datetime
import random


@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)


@app.route('/projects/new', methods=['GET', 'POST'])
def new_project():
    projects = Project.query.all()
    if request.form:
        new_project = Project(
            title=request.form['title'],
            completion_date=clean_date(request.form['date']),
            description=request.form['desc'],
            skills=request.form['skills'],
            github=request.form['github'])
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('projectform.html', projects=projects)


@app.route('/projects/<id>/edit', methods=['GET', 'POST'])
def edit_project(id):
    projects = Project.query.all()
    project = Project.query.get_or_404(id)
    if request.form:
        project.title = request.form['title']
        project.completion_date = clean_date(request.form['date'])
        project.description = request.form['desc']
        project.skills = request.form['skills']
        project.github = request.form['github']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template(
        'editproject.html', project=project, projects=projects)


@app.route('/projects/<id>/delete')
def delete_project(id):
    projects = Project.query.all()
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('index'), projects=projects)


@app.route('/about')
def about():
    projects = Project.query.all()
    return render_template('about.html', projects=projects)


def clean_date(date_str):
    split_date = date_str.split('-')
    year = int(split_date[0])
    month = int(split_date[1])
    return datetime.date(year, month, random.randint(1, 28))


@app.errorhandler(404)
def not_found(error):
    projects = Project.query.all()
    return render_template('404.html', msg=error, projects=projects), 404


@app.route('/projects/<id>')
def detail(id):
    projects = Project.query.all()
    project = Project.query.get_or_404(id)
    return render_template('detail.html', project=project, projects=projects)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')
