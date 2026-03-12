from flask import Blueprint, render_template

main_routes = Blueprint('main', __name__)

@main_routes.route('/')
def home():
    return render_template('index.html')

@main_routes.route('/projects')
def projects():
    return render_template('projects.html')

@main_routes.route('/joinus')
def joinus():
    return render_template('joinus.html')

@main_routes.route('/faq')
def faq():
    return render_template('faq.html')

@main_routes.route('/subteams')
def subteams():
    return render_template('subteams.html')


