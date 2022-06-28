## This is app.py file

from flask  import Flask

app=Flask(__name__)

@app.route("/" , methods=['GET', 'POST'])
def index():
    return "Starting Machin Learning Project"

if __name__=="__main__":
    app.run(debug=True)