from bottle import default_app, route, get, post, template, request, redirect
import sqlite3
import task1_database
from task2_dataset_database import get_task2_items, add_task2_item, delete_task2_item, update_task2_item
from task3_peewee_database import get_task3_items, add_task3_item, delete_task3_item, update_task3_item

connection = sqlite3.connect("task1_shopping_list.db")

@route('/')
def home():
    return template("main.tpl")

#Task1 Starts

@route('/task1/list/')
def get_task1_list():
    items = task1_database.get_items()
    return template("task1_shopping_list.tpl", name="pvkalyan13", shopping_list=items)

@post('/task1/add/')
def post_task1_add():
    description = request.forms.get("description")
    task1_database.add_item(description)
    redirect('/task1/list/')

@route("/task1/delete/<id>")
def get_task1_delete(id):
    task1_database.delete_item(id)
    redirect('/task1/list/')

@get("/task1/edit/<id>")
def get_task1_edit(id):
    items = task1_database.get_items(id)
    if len(items) != 1:
        redirect('/task1/list/')
    item_id, description = items[0]['id'], items[0]['desc']
    assert item_id == int(id)
    return template("task1_edit_item.tpl", id=id, description=description)

@post("/task1/edit/<id>")
def post_task1_edit(id):
    description = request.forms.get("description")
    task1_database.update_item(id, description)
    redirect('/task1/list/')

#Task1 Ends

#Task2 Starts

@route('/task2/list/')
def get_task2_list():
    items = get_task2_items()
    return template("task2_shopping_list.tpl", name="pvkalyan13", shopping_list=items)

@post('/task2/add/')
def post_task2_add():
    description = request.forms.get("description")
    add_task2_item(description)
    redirect('/task2/list/')

@route("/task2/delete/<id>")
def get_task2_delete(id):
    delete_task2_item(id)
    redirect('/task2/list/')

@get("/task2/edit/<id>")
def get_task2_edit(id):
    items = get_task2_items(id)
    if len(items) != 1:
        redirect('/task2/list/')
    item_id, description = items[0]['id'], items[0]['description']
    assert item_id == int(id)
    return template("task2_edit_item.tpl", id=id, description=description)

@post("/task2/edit/<id>")
def post_task2_edit(id):
    description = request.forms.get("description")
    update_task2_item(id, description)
    redirect('/task2/list/')
#Task2 Ends

#Task3 Starts

@route('/task3/list/')
def get_task3_list():
    items = get_task3_items()
    return template("task3_shopping_list.tpl", name="pvkalyan13", shopping_list=items)

@post('/task3/add/')
def post_task3_add():
    description = request.forms.get("description")
    try:
        quantity = int(quantity)
    except:
        quantity = 1
    add_task3_item(description)
    redirect('/task3/list/')

@route("/task3/delete/<id>")
def get_task3_delete(id):
    delete_task3_item(id)
    redirect('/task3/list/')

@get("/task3/edit/<id>")
def get_task3_edit(id):
    items = get_task3_items(id)
    if len(items) != 1:
        redirect('/task3/list')
    item_id, description = items[0]['id'], items[0]['description']
    assert item_id == int(id)
    return template("task3_edit_item.tpl", id=id, description=description)

@post("/task3/edit/<id>")
def post_task3_edit(id):
    description = request.forms.get("description")
    update_task3_item(id, description)
    redirect('/task3/list/')
#Task3 Ends
application = default_app()