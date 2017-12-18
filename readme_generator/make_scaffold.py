"""Module to create README.md file with basic scaffold, using markdown_generator."""
import markdown_generator as mg
import os

# from gather_data import models, apps, tests, basic_data
# data necessary = ['Project Title']
os.system('rm README.md')
os.system('touch README.md')

if __name__ == '__main__':
    with open('README.md', 'w') as f:
        w = mg.Writer(f)
        w.write_heading('Project Title', 1)
        w.write_hrule()

        # Description and Key Features
        w.writeline('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')
        key_features = mg.List()
        key_features.append('Feature #1')
        key_features.append('Feature #2')
        key_features.append('Feature #3')
        w.write(key_features)

        w.write_heading('Getting Started', 3)

        # GETTING STARTED: Installation requirements
        w.write_heading(mg.emphasis('Prerequisites'), 5)
        prereqs = mg.List()
        prereqs.append(mg.link('https://www.python.org/downloads/', 'python (3.6+)'))
        prereqs.append(mg.link('https://pip.pypa.io/en/stable/', 'pip'))
        prereqs.append(mg.link('https://git-scm.com/', 'git'))
        w.write(prereqs)

        # GETTING STARTED: Cloning/VE Instructions
        w.write_heading(mg.emphasis('Installation'), 5)
        w.writeline('First, clone the project repo from Github. Then, change directories into the cloned repository, create a new virtual environment, and install the repo\'s requirements into your VE. To accomplish this, execute these commands:')
        w.writeline()
        w.writeline('`$ git clone https://github.com/chelseadole/write-me.git`')
        w.writeline('`$ cd write-me`')
        w.writeline()
        w.writeline('Now now that you\'ve cloned your repo and changed directories into the project, create a virtual environment, and download the project\'s requirements into your VE.')
        w.writeline()
        w.writeline('`$ python3 -m venv ENV`')
        w.writeline('`$ source ENV/bin/activate`')
        w.writeline('`$ pip install -r requirements.txt`')

        # GETTING STARTED: Serving the App
        w.write_heading(mg.emphasis('Serving Locally'), 5)
        w.writeline('Once you have cloned the application and installed the requirements, you can serve the project on your local machine. Once you have executed this command, open your browser, and go to `http://localhost:8000/`')
        w.writeline('`$ ./manage.py runserver`')

        # TESTS: Running
        w.write_heading('Test Suite', 3)
        w.write_heading(mg.emphasis('Running Tests'), 5)
        w.writeline('This application uses pytest as a testing suite. To run tests, run:')
        w.writeline()
        w.writeline('`$ pytest`')
        w.writeline()
        w.writeline('To view test coverage, run:')
        w.writeline()
        w.writeline('`$ pytest --cov`')
