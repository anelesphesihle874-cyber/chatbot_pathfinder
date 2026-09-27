from flask import Flask, render_template, request, redirect, flash, jsonify, url_for, session
import secrets
from pathfinderdatabase import db, Learners, Programmes, other_Programmes
from model import general_response
from werkzeug.security import check_password_hash, generate_password_hash

chatBot = Flask(__name__)

# Generate a secret key
sec = secrets.token_hex(32)

# Give the secret key to Flask
chatBot.config["SECRET_KEY"] = sec

chatBot.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pathfinderdatabase.db"
chatBot.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(chatBot)

with chatBot.app_context():
    db.create_all()

# with chatBot.app_context():
#     Learners.__table__.drop(db.engine, checkfirst=True)

# with chatBot.app_context():
#     Programmes_requirements.__table__.drop(db.engine, checkfirst=True)


@chatBot.route("/")
def Home():
    return render_template("base.html")

@chatBot.route("/inner_base")
def inner_base():
    return render_template("inner_base.html")

@chatBot.route("/chatbx")
def chat():
    return render_template("chatbx.html")

@chatBot.route("/SignIn")
def SignIn():
    return render_template("SignIn.html")

@chatBot.route("/SignUp")
def SignUp():
    return render_template("SignUp.html")

@chatBot.route("/add_nurse_prog")
def nurse_prog():
    return render_template("add_nurse.html")



@chatBot.route("/add_nurse", methods= ["POST", "GET"])
def add_nurse():
    
    if "POST":
        name_of_prog = request.form["name_of_prog"].lower().strip()
        mathematics = request.form["mathematics"]
        life_science = request.form["life_Science"]
        english = request.form["english"]
        math_lit = request.form["math_lit"]
        req_points = request.form["req_points"]

        if not name_of_prog and not mathematics and not life_science and not english and not math_lit and not req_points:
            flash("your input are empty", "danger")
            return redirect("")
        
        try:
            int(req_points)
        except:
            flash("Enter an integer value", "danger")
            return redirect("/")

        exist=Programmes.query.filter_by(name_of_prog=name_of_prog).first()
        if exist:
            flash("This programme already exist in a database", "danger")
            return redirect("/")
        
        new_prog = Programmes(
            name_of_prog=name_of_prog,
            mathematics=mathematics,
            life_science=life_science,
            english=english,
            math_lit = math_lit,
            req_points=req_points
        )

        if new_prog:
            db.session.add(new_prog)
            db.session.commit()

            flash("Successfully submitted", "success")
            
            return redirect("/")
        else:
            KeyError("data was not submittedto the database")
            flash("Not successful", "danger")
            return redirect("/")


@chatBot.route("/signin", methods=["POST", "GET"])
def signin():

    # If user is just opening the sign-in page
    if request.method == "GET":
        return render_template("signin.html")

    # Get information from the form
    email = request.form["email"]
    password = request.form["password"]

    # Find learner in database
    existing_learner = Learners.query.filter_by(email=email).first()

    # Check login details
    if existing_learner and check_password_hash(
        existing_learner.password,
        password
    ):
        return redirect(url_for("chat"))



    # Login failed
    print("Username or password incorrect")

    return redirect(url_for("SignIn"))

@chatBot.route("/signup", methods=["POST", "GET"])
def signup():
    email=request.form["email"]
    password = request.form["password"]
    phone_no=request.form["phone_no"]
    name = request.form["name"]

    new_user=Learners(
        name= name,
        phone_no=phone_no,
        password=generate_password_hash(password),
        email=email
    )

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('SignIn'))

@chatBot.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("SignIn"))






@chatBot.route("/add_programme", methods=["POST"])
def add_programme():

    if "POST":
        name_of_prog = request.form["name_of_prog"].lower().strip()
        mathematics = request.form["mathematics"]
        physx = request.form["physx"]
        english = request.form["english"]
        req_points = request.form["req_points"]

        if not name_of_prog and not mathematics and not physx and not english and not req_points:
            flash("your input are empty", "danger")
            return redirect("/")
        
        try:
            int(req_points)
        except:
            flash("Enter an integer value", "danger")
            return redirect("/")

        exist=Programmes.query.filter_by(name_of_prog=name_of_prog).first()
        if exist:
            flash("This programme already exist in a database", "danger")
            return redirect("/")
        
        new_prog = Programmes(
            name_of_prog=name_of_prog,
            mathematics=mathematics,
            physx=physx,
            english=english,
            req_points=req_points
        )

        if new_prog:
            db.session.add(new_prog)
            db.session.commit()

            flash("Successfully submitted", "success")
            
            return redirect("/")
        else:
            KeyError("data was not submittedto the database")
            flash("Not successful", "danger")
            return redirect("/")

@chatBot.route("/add_programmes")
def add_prog():
    return render_template("add_programme.html")

@chatBot.route("/response", methods = ["POST", "GET"])
def ask_chatbot():
    

    data = request.get_json()
    user_message = data.get("user_message")

    
    response = general_response(user_message)

    return jsonify({
        "response": response
    })
        

        

        
    

if __name__ == "__main__":
    chatBot.run(debug=True)