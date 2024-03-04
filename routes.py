from app import app
from flask import render_template, request, redirect
import forms


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/heyoo')
def testing():
    return render_template(
        "helloNew.html",
        name="ASDA",
    )


@app.route('/testing')
def testing2():
    return render_template(
        "testing.html",
    )


@app.route('/form', methods=['GET', 'POST'])
def formr():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        print(f"submitted is {form.title.data}")
        return render_template(
            "form.html",
            form=form,
            title=form.title.data
        )
    return render_template(
        'form.html',
        form=form,
    )
