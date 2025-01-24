from flask import Blueprint, render_template, current_app, request, flash, session, redirect, url_for
from markupsafe import Markup
from .grafic1 import PlotPie
from .grafic2 import PlotHistogram
from .grafic3 import PlotBar

views = Blueprint('views', __name__)

@views.route('/', methods=['GET'])
def mainWindow():
    t = current_app.mongo.db.project.find()
    htmlPie = Markup(PlotPie())
    htmlHistogram = Markup(PlotHistogram())
    htmlBar = Markup(PlotBar())
    return render_template('index.html', htmlPie=htmlPie,
                            htmlHistogram=htmlHistogram, htmlBar=htmlBar)

@views.route('/', methods=['POST'])
def mainWindowSearch():
    print(request.method)
    
    items = current_app.mongo.db.project.find()
    title = request.form['universityName']
    if title == '':
        mainWindow()
    elif title == ' ':
        return render_template('page2.html', items=items)
    else:
        items = current_app.mongo.db.project.find({
            'Name': {'$regex': title, '$options': 'i'}
        })

        return render_template('page2.html', items=items)

@views.route('/page2', methods=['GET'])
def page2():
    items = current_app.mongo.db.project.find()

    # Фильтр по уровню образования
    education_level = request.args.get('education_level')
    if education_level:
        items = current_app.mongo.db.project.find({
            'Education level': {'$regex': education_level, '$options': 'i'}
        })

    # Фильтр по минимальному проходному баллу
    min_score = request.args.get('min_score')
    if min_score:
        items = current_app.mongo.db.project.find({
            'Lowest score budget (total)': {'$gte': float(min_score)}
        })

    # Фильтр по средней стоимости обучения
    max_cost = request.args.get('max_cost')
    if max_cost:
        items = current_app.mongo.db.project.find({
            'Average cost (₽)': {'$lte': int(max_cost)}
        })

    # Фильтр по специальностям (ищем в строке)
    specialty = request.args.get('specialty')
    if specialty:
        items = current_app.mongo.db.project.find({
            'Specialties': {'$regex': specialty, '$options': 'i'}
        })

    return render_template('page2.html', items=items)