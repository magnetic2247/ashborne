#!/usr/bin/python3
import backend.requests as r
import flask, json

"""
Studli by Adrien Genevieve and Benji Wong
"""

# Server
app = flask.Flask(__name__)

"""Frontend"""
# Index
@app.route("/")
def read():
    # Get Tables
    options = r.table("Options")
    eleves = r.table("Eleves")
    profs = r.table()

    # Render index
    return flask.render_template("read.html", options=options, eleves=eleves, profs=profs)

@app.route("/write")
def write():
    # Get mode and convert into int, avoiding ValueError
    try: mode = int(flask.request.args.get('mode'))
    except: mode = 0

    # Render write page
    return flask.render_template("write.html", mode=mode)

"""API Reads"""
# Table
@app.route("/table/<dbname>")
def api(dbname):
    data = r.table(dbname)
    return flask.render_template("display.html", keys=data[0].keys(), table=data, title=dbname)

# Students following a certain option
@app.route("/students/per_option/<id>")
def per_option(id):
    data = r.students_per_option(id)
    keys = ["Identifiant", "Nom", "Prénom", "Date de Naissance", "Option"]
    return flask.render_template("display.html", keys=keys, table=data, title="Élève dans l'option "+id)

# Students following a certain subject
@app.route("/students/per_subject/<subject>")
def per_subject(subject):
    data = r.students_per_subject(subject)
    keys = ["Identifiant", "Nom", "Prénom", "Date de Naissance", "Option"]
    return flask.render_template("display.html", keys=keys, table=data, title="Élève suivant la matière "+subject)

# Student's teacher
@app.route("/teachers/per_student/<student_id>")
def teacher(student_id):
    data = r.teacher_from_student(student_id)
    keys = ["Prénom", "Nom"]
    return flask.render_template("display.html", keys=keys, table=data, title="Professeur de l'élève "+student_id)


"""API Writes"""
# New Student
@app.route("/students/add/", methods=["POST"])
def add_stud():
    # Get form
    response = flask.request.form
    first = flask.escape(response["first"])
    last = flask.escape(response["last"].upper())
    option = flask.escape(response["option"])
    date = flask.escape(response["dnd"])
    print("DATERECEIVED", date)
    year, month, day = date.split("-")
    
    # Insert new student
    r.new_student(first, last, day, month, year, option)

    # Redirect Back to Home
    return flask.redirect("/")

# New Teacher
@app.route("/teachers/add/", methods=["POST"])
def add_teach():
    r.new_teacher(flask.escape(flask.request.form["first"]), flask.escape(flask.request.form["last"].upper()))
    # Redirect Back to Home
    return flask.redirect("/")

# New Option
@app.route("/options/add/", methods=["POST"])
def add_option():
    r.new_option(flask.escape(flask.request.form["id"]), flask.escape(flask.request.form["teacher"]), flask.escape(flask.request.form["subject"]))
    # Redirect Back to Home
    return flask.redirect("/")

# Kill Student
@app.route("/students/kill/", methods=["POST"])
def kill():
    r.kill_student(flask.escape(flask.request.form["id"]))
    # Redirect Back to Home
    return flask.redirect("/")

# Update Teacher
@app.route("/teachers/update/", methods=["POST"])
def update():
    r.update_teacher(flask.escape(flask.request.form["id"]), flask.escape(flask.request.form["first"]), flask.escape(flask.request.form["last"].upper()))
    # Redirect Back to Home
    return flask.redirect("/")


# Run Server if ran as script
if __name__ == "__main__":
    app.run(port=8080)


