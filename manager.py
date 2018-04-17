

from flask_script import Manager

from App import craeat_app

app = craeat_app('develop')


manager=Manager(app=app)

if __name__ == '__main__':
    manager.run()
