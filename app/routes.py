from app import app
from flask import render_template, request, redirect, url_for, flash

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form.get('user_input', '').strip()
    if user_input:
        return redirect(f'/{user_input}')
    return redirect(url_for('home'))

@app.route('/intro')
def intro():
    return render_template('intro.html')

@app.route('/<path:input>')
def dynamic_page(input):
    flash("Helaas, dit werkt niet.")
    return redirect(url_for('home'))

@app.route('/fjordverdriet')
def fjordverdriet():
    return render_template('fjordverdriet.html')

@app.route('/vanillejenever')
def vanillejenever():
    return render_template('vanillejenever.html')

@app.route('/feestverdriet')
def feestverdriet():
    return render_template('feestverdriet.html')

@app.route('/seks')
def seks():
    return render_template('seks.html')

@app.route('/lesbian')
def lesbian():
    return render_template('lesbian.html')

@app.route('/fotosynthese')
def fotosynthese():
    return render_template('fotosynthese.html')

@app.route('/koas')
def koas():
    return render_template('koas.html')

@app.route('/nicole&erica')
def nicole_erica():
    return render_template('nicole&erica.html')

@app.route('/aksiedentje')
def aksiedentje():
    return render_template('aksiedentje.html')

@app.route('/troela')
def troela():
    return render_template('troela.html')