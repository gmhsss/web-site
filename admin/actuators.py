from flask import Blueprint, request, render_template, redirect, url_for

operator = Blueprint("operator",__name__, template_folder="templates")

atuadores = {'Servo Motor': 0, 'Lampada': 1}

@operator.route('/register_actuators')
def register_actuators():
    return render_template("register_actuators.html")


@operator.route('/add_actuators', methods=['GET','POST'])
def add_actuators():
    global actuators
    if request.method == 'POST':
        atuador = request.form['atuador']
        value = request.form['value']
        atuadores[atuador] = value
    else:
        atuador = request.args.get('atuador', None)
        value = request.args.get('value', None)
        
    return render_template("actuators.html", atuadores=atuadores)


@operator.route('/actuators')
def actuators():
    return render_template("actuators.html", atuadores=atuadores)



@operator.route('/remove_actuator')
def remove_actuator():
    return render_template("remove_actuator.html", atuadores=atuadores)



@operator.route('/del_actuator', methods=['GET','POST'])
def del_actuator():
    global atuadores
    if request.method == 'POST':
        atuador = request.form['atuador']
        atuadores.pop(atuador)
    else:
        atuador = request.args.get('atuador', None)
        atuadores.pop(atuador)
    return render_template("actuators.html", atuadores=atuadores)