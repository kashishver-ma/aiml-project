## Flask :

### Flask is a web application framework written in Python.

Flask is considered a "micro" web framework because it is lightweight and simple to use, with minimal dependencies

(unlike djangi with built-in auth and admin panel)

#### flask is built on top of two powerful libraries:

Werkzeug: A comprehensive WSGI web server library that helps manage the application's request and response cycles.

Jinja2: A templating engine that allows you to use dynamic HTML in your application

#### define routes with decorators that map URLs to Python functions.

#### steps:

1. create virtual env
   `python -m venv venv

2.activate it
`venv\scripts\activate`

#### routing :

route() decorator in Flask is used to bind a URL to a function

add_url_rule() which is a function of an application object that is also available to bind a URL with a function as in the above example, route() is used.

`def gfg():
return "abc"
add_url_rule('/','gfg',gfg)
`

app.add_url_rule(rule, endpoint=None, view_func=None, \*\*options)

rule : URL path (e.g., '/', '/about')
endpoint : unique name for this route (used internally and with url_for)
view_func : function it is connectd with

#### method 1

@app.route('/')
def index():
return "index"

#### Method 2

def gfg():
return 'geeksforgeeks'

app.add_url_rule('/gfg', 'g2g', gfg)

#### Dynamic route endpoints:

add variables in your web app

````@app.route('/greet/<name>')
 def greet(name):
    return "hi %s" % name ```


````

#### using POST method in route ()

it tell flask that :
“This route should accept POST requests (not just GET).”
