#!/usr/bin/python3
import json
import backend.db as db

# Database Object
database = db.Database("backend/db.sqlite")

"""API Reads"""
# Read table
def table(table="Profs"):
    return database.query(f"SELECT * FROM {table}")

# Students following a certain option
def students_per_option(option_id):
    return database.query("select * from Eleves where id_option=?", (option_id,))

# Students following a certain subject
def students_per_subject(subject):
    return database.query("select Eleves.* from Eleves inner join Options on Eleves.id_option=Options.id_option where Options.matiere_option like ?", (subject,))

# Teacher teaching the option a student follows
def teacher_from_student(student_id):
    return database.query("select Profs.pre_prof, Profs.nom_prof from Profs inner join Options on Profs.id_prof=Options.id_prof where Options.id_option=(select id_option from Eleves where id_eleve=?);", (student_id,))

"""API Writes"""
# Add New Teacher
def new_teacher(first_name, last_name):
    teacher_id = last_name[:2] + first_name[:2]
    database.query("insert into Profs (id_prof, nom_prof, pre_prof) values (?,?,?)", (teacher_id, last_name, first_name))
    return "ok"

# Add new option
def new_option(option_id, teacher_id, subject):
    database.query("insert into Options (id_option, id_prof, matiere_option) values (?,?,?)", (option_id, teacher_id, subject))
    return "ok"

# Add new students
def new_student(first_name, last_name, dnd_date, dnd_month, dnd_year, option_id):
    student_id = last_name[:2] + first_name[:2] + str(dnd_month) + str(dnd_year)[2:]
    dnd = str(dnd_date)+"/"+str(dnd_month)+"/"+str(dnd_year)
    database.query(
        "insert into Eleves (id_eleve, nom_eleve, pre_eleve, dnd_eleve, id_option) values (?,?,?,?,?)",
        (student_id, last_name, first_name, dnd, option_id)
    )
    return "ok"

# Kill Student
def kill_student(student_id):
    database.query("delete from Eleves where id_eleve=?", (student_id,))
    return "ok"

# Update Teacher's name
def update_teacher(teacher_id, first_name, last_name):
    database.query("update Profs set nom_prof=?, pre_prof=? where id_prof=?", (last_name, first_name, teacher_id))
    return "ok"
