from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
#

@app.route("/test/<name>/")
def testname(name):
    return "Name is {}".format(name)
#

@app.route("/test2/<name>/")
def testname2(name):
    return "Name2 is {}".format(name)
#

@app.route("/test3/<name>/")
def testname3(name):
    import pdb;
    pdb.set_trace()
    foo = 3
    return "Name3 is {}".format(name)
#





if __name__ == '__main__':
    app.run(debug=True)