"""
Docs at: https://flask-script.readthedocs.io/en/latest/
The Flask-Script extension provides support for writing external scripts in Flask.
This includes running a development server, a customised Python shell, scripts to
set up your database, cronjobs, and other command-line tasks that belong outside
the web application itself.

Flask-Script works in a similar way to Flask itself. You define and add commands
that can be called from the command line to a Manager instance:
"""
# Create a python module to run your script commands in.  Here we'll call it manage.py

from flask_script import Manager, Command

from myapp import app
# In manage.py file, instantiate Manager class, which tracks commands and how
# they are called from command line.

# Manager class requires single arg: a flask instance
manager = Manager(app)

# ADDING COMMANDS TO THE MANAGER:
# Example 1:
# Add a command using command decorator of Manager instance
@manager.command
def hello():
    print "hello"
"""
To test, run the following from command line:
python manage.py hello
> hello
"""

# Example 2:
# Add a command by subclassing Command:
class Goodbye(Command):
    "prints goodbye world"
    # Command class must define a run method
    def run(self):
        print "goodbye world"
# add command to manager: (command line invocation string, subclass of command)
manager.add_command('goodbye', Goodbye())
"""
To test, run the following from command line:
python manage.py goodbye
> goodbye world
"""


if __name__ == "__main__":
    # Calling manager.run() prepares your Manager instance to receive input from the command line.
    manager.run()

"""
Once you define your script commands, you can then run them on the command line:
python manage.py hello
> hello
"""
