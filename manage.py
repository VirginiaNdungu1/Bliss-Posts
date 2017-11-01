from app import create_app, db
from flask_script import Manager, Server
from app.models import Role, User, Category, Post, Comment
from flask_migrate import Migrate, MigrateCommand


app = create_app('development')

# app = create_app('test')

# app = create_app('production')
'''
Create app instance
How?

Call the create_app function
pass in the onfiguration_options keys - 'development', 'test'
'''
# Initialise flask class instances
manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('server', Server)
# create new manager command and pass in the MigrateCommand class
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role, Category=Category, Post=Post, Comment=Comment)


if __name__ == '__main__':
    manager.run()
