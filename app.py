import os
import pandas as pd
from sqlalchemy import create_engine
from config import post_pass
from flask import Flask, jsonify, request

engine = create_engine("sqlite:///database_queries.sqlite")


app = Flask(__name__)

@app.route("/")
def welcome():
    with open('Resources/index.html') as f:
        return f.read()
    

# @app.route("/database_queries.sql")
# def us_gas_price_region():
    
#     return jsonify(us_gas_price_region)


# @app.route("static/js/pro3.js")
# def map_js():
    
#     return(map_js)
    
# @app.route("static/css/style.css")
# def style():
    
#     return(style)

if __name__ == "__main__":
    app.run(debug=True)