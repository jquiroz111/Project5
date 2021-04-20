from flask import Flask, jsonify, escape, request, Response
import random
import hashlib
import math

# instansiate the Flask object
app = Flask(__name__)

# the main route url route
@app.route('/')
def hello():
    return "Hello, Welcome to group project #5."

''' example
@app.route('/md5/<string>')
def json_response():
    resp = Response('{ "foo": "bar", "baz": "bat" }')
    resp.headers['Content-Type'] = 'application/json'
    return resp
'''
# Calculation for factorials
@app.route('/factoral/')
def factoral_response():
    n = int(input("enter a number:"))
    factorial = 1
    if (n == 0):
        print("The factorial of 0 is 1")
    else if (n < 0):
        print("Error, The input was not positive, please try again")
    else:
       for i in range(1,n + 1):
           factorial = factorial*i
       print("The factorial of number:",factorial)  
    '''@app.route('/fibonacci/')

def fibonacci_response():
    num = input('Input: ')
    return "Output: {resp}"
'''
    
@app.route('/is-prime/')
def prime_response():
    num = int(input('Input: '))
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                resp = False
                break
            else:
                resp = True
    else:
        resp = False
    
    return "{num} is Prime: {resp}"

# Posting to a Slack channel
def slack_message(text):
    from urllib import request, parse
    import json

    post = {"text": "{0}".format(text)}

    try:
        json_data = json.dumps(post)
        req = request.Request("https://hooks.slack.com/services/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",
                              data=json_data.encode('ascii'),
                              headers={'Content-Type': 'application/json'}) 
        resp = request.urlopen(req)
    except Exception as em:
        print("EXCEPTION: " + str(em))

slack_message('Howdy Slack Alert Here!')
