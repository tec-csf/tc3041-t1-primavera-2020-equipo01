from flask import Flask, jsonify, request, url_for
from flask_api import FlaskAPI, status, exceptions
from flaskext.mysql import MySQL

app = FlaskAPI(__name__)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'myflixdb'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

## conextion variables
conn = mysql.connect()
cur = conn.cursor()

"""
notes = {
    0: 'do the shopping',
    1: 'build the codez',
    2: 'paint the door',
}

def note_repr(key):
    return {
        'url': request.host_url.rstrip('/') + url_for('notes_detail', key=key),
        'text': notes[key]
    }


@app.route("/", methods=['GET', 'POST'])
def notes_list():
    if request.method == 'POST':
        print(request.data)
        note = str(request.data.get('text', ''))
        idx = max(notes.keys()) + 1
        notes[idx] = note
        return note_repr(idx), status.HTTP_201_CREATED

    # request.method == 'GET'
    return [note_repr(idx) for idx in sorted(notes.keys())]

@app.route("/<int:key>/", methods=['GET', 'PUT', 'DELETE'])
def notes_detail(key):

    if request.method == 'PUT':
        note = str(request.data.get('text', ''))
        notes[key] = note
        return note_repr(key)

    elif request.method == 'DELETE':
        notes.pop(key, None)
        return '', status.HTTP_204_NO_CONTENT

    # request.method == 'GET'
    if key not in notes:
        raise exceptions.NotFound()
    return note_repr(key)

"""


@app.route("/", methods=['GET', 'POST'])
def index():
    # request.method == 'GET'
    return {'flask-api': ''}

### colegio end points
@app.route('/colegio',  methods=['GET', 'POST', 'PUT'])
def get_colegios():
    if request.method == 'GET':
        cur.execute('select * from Colegio')
        r = [dict((cur.description[i][0], value)
                for i, value in enumerate(row)) for row in cur.fetchall()]
        return {'colegios' : r}

    if request.method == 'POST':
        cur.execute(request.data.get('query', ''))
        r = [dict((cur.description[i][0], value)
                for i, value in enumerate(row)) for row in cur.fetchall()]
        return {'colegios' : r}

    #Put method for insert

@app.route('/colegio/<int:key>/',  methods=['GET', 'PUT', 'DELETE'])
def get_colegio(key):
    if request.method == 'GET':
        cur.execute('SELECT * FROM Colegio WHERE num=%s',(key))
        r = [dict((cur.description[i][0], value)
                for i, value in enumerate(row)) for row in cur.fetchall()]
        return {'colegio' : r}

    if request.method == 'DELETE':
        cur.execute("DELETE FROM Colegio WHERE num=%s", (key))
        conn.commit()
        return {'colegio' : 'borrado'}
    #Put method for update



### mesa end points
@app.route('/mesa',  methods=['GET', 'POST', 'PUT'])
def get_mesas():
    if request.method == 'GET':
        cur.execute('select * from Mesa')
        r = [dict((cur.description[i][0], value)
                for i, value in enumerate(row)) for row in cur.fetchall()]
        return {'mesas' : r}

    if request.method == 'POST':
        cur.execute(request.data.get('query', ''))
        r = [dict((cur.description[i][0], value)
                for i, value in enumerate(row)) for row in cur.fetchall()]
        return {'mesas' : r}

    #Put method for insert

@app.route('/mesa/<int:key>/',  methods=['GET', 'PUT', 'DELETE'])
def get_mesa(key):
    if request.method == 'GET':
        cur.execute('SELECT * FROM Mesa WHERE letraMesa=%s',(key))
        r = [dict((cur.description[i][0], value)
                for i, value in enumerate(row)) for row in cur.fetchall()]
        return {'mesa' : r}

    if request.method == 'DELETE':
        cur.execute("DELETE FROM Mesa WHERE letraMesa=%s", (key))
        conn.commit()
        return {'mesa' : 'borrado'}
    #Put method for update



### partido end points
@app.route('/partido',  methods=['GET', 'POST', 'PUT'])
def get_patridos():
    if request.method == 'GET':
        cur.execute('select * from Partido')
        r = [dict((cur.description[i][0], value)
                for i, value in enumerate(row)) for row in cur.fetchall()]
        return {'partidos' : r}

    if request.method == 'POST':
        cur.execute(request.data.get('query', ''))
        r = [dict((cur.description[i][0], value)
                for i, value in enumerate(row)) for row in cur.fetchall()]
        return {'partidos' : r}

    #Put method for insert

@app.route('/partido/<int:key>/',  methods=['GET', 'PUT', 'DELETE'])
def get_partido(key):
    if request.method == 'GET':
        cur.execute('SELECT * FROM Partido WHERE siglas=%s',(key))
        r = [dict((cur.description[i][0], value)
                for i, value in enumerate(row)) for row in cur.fetchall()]
        return {'partido' : r}

    if request.method == 'DELETE':
        cur.execute("DELETE FROM Partido WHERE siglas=%s", (key))
        conn.commit()
        return {'partido' : 'borrado'}
    #Put method for update
if __name__ == "__main__":
    app.run(debug=True)

