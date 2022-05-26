from flask import Flask, render_template

app = Flask(__name__)

# @app.route("/libro/<int:id_libro>/")
# def mostrar_libro(id_libro):
#     return "mostrando el libro {}".format(id_libro)

@app.route("/libros/libro/")
@app.route("/libros/libro/<int:id_libro>/")
def form_libro(id_libro = None):
    return render_template("libros/form_libro.html",id_libro=id_libro)
@app.route("/libro/<int:id_libro>/")
def mostrar_libro(id_libro):
    return render_template("ver_libro.html", id_libro=id_libro)
    
# libros:[]
# @app.route('/')

# def principal():
#     return "{} libros".format(len(libros))

# def index():
#     # return 'hola prro'
#     cursos = ['JQUERY','PYTHON','C#','JAVA','JS']
#     data = {
#         'titulo' : 'Index',
#         'Bienvenida' : '!Saludos!',
#         'cursos': cursos,
#         'numero_cursos' : len(cursos)
#     }
#     return render_template('index.html' , data=data)

if __name__ == '__main__':
    app.run(debug=True,port=5000)