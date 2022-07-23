from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.task import Task
from utils.db import db

task = Blueprint("task", __name__)


@task.route("/")
def index():
    task = Task.query.all()
    return render_template("index.html", task=task)


@task.route("/new", methods=["POST"])
def add():
    if request.method == "POST":

        # receive data from the form
        tittle = request.form["tittle"]
        description = request.form["description"]
        priority = request.form["priority"]

        # create a new Task object
        new_Task = Task(tittle, description, priority)

        # save the object into the database
        db.session.add(new_Task)
        db.session.commit()

        flash("Task added successfully!")

        return redirect(url_for("task.index"))


@task.route("/update/<string:id>", methods=["GET", "POST"])
def update(id):
    # get Task by Id
    print(id)
    task = Task.query.get(id)

    if request.method == "POST":
        task.tittle = request.form["tittle"]
        task.description = request.form["description"]
        task.priority = request.form["priority"]

        db.session.commit()

        flash("Task updated successfully!")

        return redirect(url_for("task.index"))

    return render_template("update.html", task=task)


@task.route("/delete/<id>", methods=["GET"])
def delete(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()

    flash("Task deleted successfully!")

    return redirect(url_for("task.index"))


@task.route("/about")
def about():
    return render_template("about.html")
