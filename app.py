import datetime
import sqlalchemy as sa 
from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy



# Create a flask object
app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


class Todo(db.Model):
    '''
        Initializes the database
    '''
    id = sa.Column(sa.Integer, primary_key=True)
    content = sa.Column(sa.String(500), nullable=False)
    date_created = sa.Column(sa.DateTime, default=datetime.date)

    def __repr__(self):
        '''
            Returns the task in a string format
        '''
        return '<Task %r>' % self.id

with app.app_context():
    db.create_all()
# URL mapping
@app.route('/')
def home(): 
    # how to use this in each column?
    tasks = Todo.query.order_by(Todo.date_created).all()
    return render_template('index.html', tasks=tasks)


@app.route('/move', methods=['POST'])
def move():
    pass


@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        # add happening here
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'


@app.route('/edit/<int:id>', methods=['POST'])
def edit(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'The task could not be updated'

    else:
        return render_template('update.html', task=task)


@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    deleted_task = Todo.query.get_or_404(id)

    try:
        db.session.delete(deleted_task)
        db.session.commit()
        return redirect('/')
    except:
        return 'The task could not be deleted'


# Main driver function 
if __name__ == '__main__':
 app.run(debug=True)