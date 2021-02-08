from flask import Flask,render_template

app = Flask(__name__)
posts = [
    {"title":"What is Lorem Ipsum?", "content":"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy"},
    {"title":"Where does it come from?", "content":"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy"},
    {"title":"Why do we use it?", "content":"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy"},
    {"title":"Where can I get some?", "content":"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy"}     
]

# @app.route("/")
# def index():
#     return {"Message":"Success","content":"Hello Flask"}

@app.route("/")
def index():
    return render_template("index.html",summary=posts)


@app.route("/about")
def about():
    return "About me"


