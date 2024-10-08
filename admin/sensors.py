from flask import Blueprint, request, render_template, redirect, url_for

detector = Blueprint("detector",__name__, template_folder="templates")

sensores = {'Sensor de Umidade': 1,'Sensor de Temperatura':1, 'Sensor de Luminosidade':1}

@detector.route('/register_sensors')
def register_sensor():
    return render_template("register_sensors.html")


@detector.route('/add_sensors', methods=['GET','POST'])
def add_sensors():
    global sensores
    if request.method == 'POST':
        sensor = request.form['sensor']
        estado = request.form['estado']
        sensores[sensor] = estado
    else:
        sensor = request.args.get('sensor', None)
        estado = request.args.get('estado', None)
        
    return render_template("sensors.html", sensores=sensores)
    


@detector.route('/sensors')
def sensors():
    return render_template("sensors.html", sensores=sensores)


@detector.route('/remove_sensor')
def remove_sensor():
    return render_template("remove_sensor.html", sensores=sensores)



@detector.route('/del_sensor', methods=['GET','POST'])
def del_sensor():
    global sensores
    if request.method == 'POST':
        sensor = request.form['sensor']
        sensores.pop(sensor)
    else:
        sensor = request.args.get('sensor', None)
        sensores.pop(sensor)
    return render_template("sensors.html", sensores=sensores)