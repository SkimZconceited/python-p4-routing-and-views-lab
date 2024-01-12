#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# @app.route('/print/<string:parameter>')
# def print_route(parameter):
#     print('hello')
#     return f'<h2>print {parameter}</h2>'

# @app.route('/print/hello')
# def print_text():
#     return f'hello'

@app.route('/print/<string:route>')
def print_string(route):
    print(route)
    return route

@app.route('/math/<int:value1>/%/<int:value2>')
def math_modulo(value1, value2):
    print(value1%value2)
    return f'{value1%value2}', 200

@app.route('/math/<int:value1>/div/<int:value2>')
def math_divide(value1, value2):
    print(value1/value2)
    return f'{value1/value2}', 200

@app.route('/math/<int:value1>/*/<int:value2>')
def math_multiply(value1, value2):
    print(value1*value2)
    return f'{value1*value2}', 200

@app.route('/math/<int:value1>/-/<int:value2>')
def math_substract(value1, value2):
    print(value1-value2)
    return f'{value1-value2}', 200

@app.route('/math/<int:value1>/+/<int:value2>')
def math_add(value1, value2):
    print(value1+value2)
    return f'{value1+value2}', 200

@app.route('/count/<int:parameter>')
def count_range_10(parameter):
    count = ''.join(str(no)+'\n' for no in range(0, parameter))
    return count ,200

if __name__ == '__main__':
    app.run(port = 5555, debug=True)