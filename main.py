from flask import Flask, render_template, request, abort, Response, redirect, url_for
import random
import requests
import urllib.parse
import xml.etree.ElementTree as ET
import main
app = Flask(__name__)

@app.route("/")
def index():
  return "MarkovAPI"

app.run(host="0.0.0.0",port=80)
