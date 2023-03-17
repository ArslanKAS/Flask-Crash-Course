from flask import Flask

app = Flask(__name__)

# ----------------------------- Custom Decorators ----------------------------------
def make_bold(user_function):
    def wrapper(*args, **kwargs): # In order to decorate any function, we need to consider its parameters too. Thus *args, **kwargs used
        value = user_function(*args, **kwargs) # Function that the user has will be called first
        return f'<b>{value}</b>' # Result of function returned to Wrapper
    return wrapper # Result of Wrapper returned to Decorator

def make_italic(user_function):
    def wrapper(*args, **kwargs): 
        value = user_function(*args, **kwargs)
        return f'<em>{value}</em>' 
    return wrapper 

def make_underline(user_function):
    def wrapper(*args, **kwargs): 
        value = user_function(*args, **kwargs)
        return f'<u>{value}</u>' 
    return wrapper 
# -------------------------------------------------------------------------------



@app.route("/") # This decorator points to Homepage
@make_bold
@make_italic
@make_underline
def hello_world():
    return "Hello, World!"

@app.route("/say") # This decorator points to a sub-page
def saying():
    return "I'm just saying"

@app.route("/<name>") # This decorator takes variables from user that are on URL
def names(name):
    return f"I'm just saying your {name}"

@app.route("/<name>/<int:age>") # This decorator takes variables with respective datatypes explicitly
def myurl(name, age):
    return f"Your name is {name} and your age is {age}"


if __name__ == "__main__":
    # app.run automatically configues the server settings
    app.run(debug=True) # debug auto-reloads the page