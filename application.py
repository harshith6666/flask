from flask import Flask
import project
project = Flask(project)
project.run(port=5000,debug=True)