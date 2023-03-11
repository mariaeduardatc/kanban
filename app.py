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
        - id: each task will have an unique id
        - content: a text containing the description of the task
        - tag: a tag to indicate the nature of the task
        - status: used to determine in which section of the kanban the task should be (used on the move of tasks)
        - date_created: used to order tasks
    '''
    id = sa.Column(sa.Integer, primary_key=True)
    content = sa.Column(sa.String(500), nullable=False)
    tag= sa.Column(sa.String(500), nullable=False)
    status = sa.Column(sa.Integer, default=0)
    date_created = sa.Column(sa.DateTime, default=datetime.date.today())

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
    # the kanban sections will be sublists inside tasks 
    tasks = []
    for i in range(4):
        tasks.append(Todo.query.order_by(Todo.date_created).filter(Todo.status == i).all())
    return render_template('index.html', tasks=tasks)


# route for when we add tasks
@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        # get the content and tag submitted by the form on the HTML
        task_content = request.form['content']
        tag_content = request.form['tag']
        new_task = Todo(content=task_content, tag=tag_content)

        # submission of info to the database
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            return 'There was an issue adding your task'


# route for when we delete tasks
@app.route('/delete/<int:id>')
def delete(id):
    deleted_task = Todo.query.get_or_404(id)

    # submission of info to the database (deletion in the database)
    try: 
        db.session.delete(deleted_task)
        db.session.commit()
        return redirect('/')
    except:
        return 'The task could not be deleted'
    

# route for when we move tasks to the right    
@app.route('/next/<int:id>')
def next(id):
    next_task = Todo.query.get_or_404(id)
 
    try: 
        # moving the task from one sublist to another in tasks
        next_task.status += 1
        db.session.commit()
        return redirect('/')
    except:
        return 'The task could not be moved'


# route for when we move tasks to the left
@app.route('/previous/<int:id>')
def previous(id):
    next_task = Todo.query.get_or_404(id)

    try: 
        # moving the task from one sublist to another in tasks
        next_task.status -= 1
        db.session.commit()
        return redirect('/')
    except:
        return 'The task could not be moved'
    

# Main driver function 
if __name__ == '__main__':
    app.run(debug=True)