from flask import Flask 
from . import __init__
application=Flask(__init__)
if __name__=="__main__":
	application.run(5000,debug=True)
