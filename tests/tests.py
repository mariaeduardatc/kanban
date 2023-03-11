import unittest
import os
from app import app, db, Todo


TEST_DB = 'test.db'
# create a database on the root of the file
basedir = os.path.abspath(os.path.dirname(__file__))


class TestTask(unittest.TestCase):
    def setUp(self):
        '''
            This function sets up the needed configurations for all the tests.
            It is called automatically for each test case.
            Will raise an error in case of any problems with the test.  

            Parameter
            ---------
            None

            Returns
            -------
            None
        '''
        self.flaskApp = app
        self.flaskApp.config['TESTING'] = True       
        self.flaskApp.config['WTF_CSRF_ENABLED'] = False
        self.flaskApp.config['DEBUG'] = False 
        self.flaskApp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
            os.path.join(basedir, TEST_DB)
        self.app = self.flaskApp.test_client()
        with self.flaskApp.app_context():
            db.drop_all()
            db.create_all()
        self.assertEqual(self.flaskApp.debug, False)

    def tearDown(self):
        '''
            The execution of this method is contingent upon the successful completion of the setUp() method, 
            irrespective of the result of the test method.

            Parameter
            ---------
            None

            Returns
            -------
            None
        '''
        pass

    def test_tasks(self):
        '''
            Function with all the different tests for the Kanban:
            - add task
            - move task (next, previous)
            - delete task

            Parameter
            ---------
            None

            Returns
            -------
            None
        '''

        # to test the 'add' of tasks we mock inputs to test what is being put in the database
        self.app.post(
            '/add',
            data=dict(content='test content', tag='testTag'),
            follow_redirects=True
        )
    

        # here we mock the task id, get it with Todo and assert if the status match
        self.app.get(
            "/next/1",
            follow_redirects=True
        )
        task = Todo.query.one()
        self.assertEqual(task.status, 1)

        # here we mock the task id, get it with Todo and assert if the status match
        self.app.get(
            "/previous/1",
            follow_redirects=True
        )
        task = Todo.query.one()
        self.assertEqual(task.status, 0)

        # here we mock the task id, get it with Todo and check if the task still exists
        self.app.get(
            "/delete/1",
            follow_redirects=True
        )
        try:
            task = Todo.query.one()
            raise Exception('The task still exists')
        except:
            pass

print(TestTask.__doc__)
