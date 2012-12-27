#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask, jsonify, request
import commands
import hashlib
# import urllib

host = "127.0.0.1"
port = "5002"

app = Flask(__name__)

@app.route("/")
def index():
    return "This is gepuro's api."

@app.route("/hello")
def hello():
    response = {"hello":"world"}
    return jsonify(response)

@app.route("/plot")
def plot():
    x = request.args.get("x", "").encode("utf-8")
    y = request.args.get("y", "").encode("utf-8")
    
    xlab = request.args.get("xlab", "x").encode("utf-8")
    ylab = request.args.get("ylab", "y").encode("utf-8")
    main = request.args.get("main", " ").encode("utf-8")
    grid = request.args.get("grid", "0").encode("utf-8")
    type_ = request.args.get("type", "p").encode("utf-8")
    
    filename = hashlib.sha256(x + y + xlab + ylab + main + grid + type_).hexdigest()

    x = x.split(",")
    y = y.split(",")
    f = open("./data/"+filename,"w")
    for i in range(len(x)):
        f.write(x[i]+","+y[i]+"\n")
    f.close()
    
    option = "\t".join([filename,xlab,ylab,main,grid,type_])
    commands.getoutput("echo '" + option + "' | Rscript sampuzu.R")
    return open("./graph/"+filename+".png").read()

if __name__ == "__main__":
    app.run(host=host, port=int(port))
