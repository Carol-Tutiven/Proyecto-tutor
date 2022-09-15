from flask import Flask, render_template

app = Flask(__name__)

# Creating simple Routes


@app.route('/test')
def test():
    return "Home Page"


@app.route('/test/Neutrosofia/')
def Neutrosofia_test():
    return "Neutrosofia Page"


@app.route('/test/LogicaDifusa/')
def LogicaDifusa_test():
    return "LogicaDifusa Page"


@app.route('/test/RedesBayesianas/')
def RedesBayesianas_test():
    return "RedesBayesianas Page"


@app.route('/test/info/')
def info_test():
    return "Info Page"


@app.route('/test/InferenciaAprendizaje/')
def InferenciaAprendizaje_test():
    return "InferenciaAprendizaje Page"


@app.route('/test/Historia/')
def Historia_test():
    return "Historia Page"

@app.route('/test/ClasificadoresBayesianos/')
def ClasificadoresBayesianos_test():
    return "ClasificadoresBayesianos Page"

@app.route('/test/acercaProyecto/')
def acercaProyecto_test():
    return "acercaProyecto Page"

@app.route('/test/index/')
def index_test():
    return "index Page"

@app.route('/test/preguntaFrecuente/')
def preguntaFrecuente_test():
    return "preguntaFrecuente Page"

@app.route('/test/contacto/')
def contacto_test():
    return "contacto Page"

@app.route('/test/NeutrosofiaHistoria/')
def NeutrosofiaHistoria_test():
    return "NeutrosofiaHistoria Page"

@app.route('/test/LogicaNeutrosofica/')
def LogicaNeutrosofica_test():
    return "LogicaNeutrosofica Page"


# Routes to Render Something
@app.route('/')
def home():
    return render_template("home.html")


@app.route('/Neutrosofia', strict_slashes=False)
def Neutrosofia():
    return render_template("Neutrosofia.html")


@app.route('/LogicaDifusa', strict_slashes=False)
def LogicaDifusa():
    return render_template("LogicaDifusa.html")


@app.route('/RedesBayesianas', strict_slashes=False)
def RedesBayesianas():
    return render_template("RedesBayesianas.html")


@app.route('/info', strict_slashes=False)
def info():
    return render_template("info.html")


@app.route('/InferenciaAprendizaje', strict_slashes=False)
def InferenciaAprendizaje():
    return render_template("/RedesBayesian/InferenciaAprendizaje.html")


@app.route('/Historia', strict_slashes=False)
def Historia():
    return render_template("/RedesBayesian/Historia.html")


@app.route('/ClasificadoresBayesianos', strict_slashes=False)
def ClasificadoresBayesianos():
    return render_template("/RedesBayesian/ClasificadoresBayesianos.html")

@app.route('/acercaProyecto', strict_slashes=False)
def acercaProyecto():
    return render_template("acercaProyecto.html")

@app.route('/index', strict_slashes=False)
def index():
    return render_template("index.html")

@app.route('/preguntaFrecuente', strict_slashes=False)
def preguntaFrecuente():
    return render_template("preguntaFrecuente.html")

@app.route('/contacto', strict_slashes=False)
def contacto():
    return render_template("contacto.html")

@app.route('/NeutrosofiaHistoria', strict_slashes=False)
def NeutrosofiaHistoria():
    return render_template("/Neutrosofia/NeutrosofiaHistoria.html")

@app.route('/LogicaNeutrosofica', strict_slashes=False)
def LogicaNeutrosofica():
    return render_template("/Neutrosofia/LogicaNeutrosofica.html")

# Make sure this we are executing this file
if __name__ == '__main__':
    app.run(debug=True)
