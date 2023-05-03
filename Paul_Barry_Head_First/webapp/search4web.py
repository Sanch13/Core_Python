from flask import Flask, render_template, request, session
# session - global dict which save state web-app.
# technology of state creation in Flask on top of a web without a state
from markupsafe import escape
from dbcm import UseDatabase
from checker import check_logged_in

app = Flask(__name__)

app.secret_key = "My_secret_key"    # key to init cookie

# We need four params to connect to the DB
app.config["dbconfig"] = {"host": "127.0.0.1",  # Database IP address to connect
                          "user": "sanch",  # user to connect the DB
                          "password": "vektor1302",  # Password of the user
                          "database": "vsearchlogDB"}  # Name of the Database


def search4letters(phrase: str, letters: str = "aeiou") -> set:
    """Return set letters from <letters> found in current phrase """
    return set(letters).intersection(phrase)


def log_request(req: "flask_request", res: str) -> None:
    """Write data into vsearch.log"""
    with open("vsearch.log", "a") as file:
        print(req.form, req.remote_addr, req.user_agent, res, file=file, sep=' | ')


# def save_to_db_log_request(req: "flask_request", res: str) -> None:
#     """Save data into DB"""
#     import mysql.connector  # driver mysql
#     # use driver mysql --> mysql.connector we connect to the DB with four params->(dbconfig)
#     conn = mysql.connector.connect(**app.config.get("dbconfig"))  # Create a connect with DataBase
#     # and save link in the conn
#     cursor = conn.cursor()  # create cursor-object. It helps us to do SQL-commands to the DB.
#     _SQL = """insert into log
#     (phrase, letters, ip, browser_string, results)
#     values
#     (%s, %s, %s, %s, %s )"""  # create sql template for write data for column
#     cursor.execute(_SQL, (req.form.get("phrase"),
#                           req.form.get("letters"),
#                           req.remote_addr,
#                           str(req.user_agent),
#                           res))  # write data to the columns
#     conn.commit()  # write to the DB immediately
#     cursor.close()  # close the cursor-object.
#     conn.close()  # close the connection with DB

def save_data_to_the_db_use_class(req: "flask_request", res: str) -> None:
    """Save data with use class"""
    with UseDatabase(app.config.get("dbconfig")) as cursor:
        _SQL = """insert into log
        (phrase, letters, ip, browser_string, results)
        values
        (%s, %s, %s, %s, %s )"""  # create sql template for write data for column
        cursor.execute(_SQL,
                       (req.form.get("phrase"),
                        req.form.get("letters"),
                        req.remote_addr,
                        str(req.user_agent),
                        res)
                       )  # write data to the columns


@app.route("/search4", methods=["POST"])
def do_search() -> "html":
    """Return result  """
    phrase = request.form.get("phrase")
    letters = request.form.get("letters")
    result = str(search4letters(phrase=phrase, letters=letters))
    # log_request(req=request, res=result)
    # save_to_db_log_request(req=request, res=result)
    save_data_to_the_db_use_class(req=request, res=result)
    return render_template("results.html",
                           the_title="Hello RESULT",
                           the_result=result,
                           the_phrase=phrase,
                           the_letters=letters, )


@app.route("/")
@app.route("/entry")
def entry_page() -> "html":
    return render_template("entry.html", the_title="Hello FLASK")


@app.route("/viewlog")
@check_logged_in  # check login user?
def view_the_log() -> "html":
    """Display log from DB"""
    # content = []
    # with open("vsearch.log") as file:
    #     for line in file:
    #         content.append([])
    #         for item in line.split("|"):
    #             content[-1].append(escape(item))
    # titles = ("Form DATA", "Remote addr", "User_agent", "Results")
    with UseDatabase(app.config.get("dbconfig")) as cursor:
        _SQL = """select phrase, letters, ip, browser_string, results from log"""
        cursor.execute(_SQL)  # read data from the table log
        content = cursor.fetchall()  # get all the records from mysql
    titles = ("phrase", "letters", "Remote addr", "User_agent", "Results")
    return render_template("viewlog.html",
                           the_title="Viewlog",
                           the_row_titles=titles,
                           the_data=content)


@app.route("/login")
def do_login() -> str:
    """Login user in the system"""
    session["logged_in"] = True     # create logged_in for the user
    return "You are now logged in"


@app.route("/logout")
def do_logout() -> str:
    """Logout user in the system"""
    session.pop("logged_in", False)    # delete logged_in of the user
    return "You are now logged out"


if __name__ == '__main__':
    app.run(debug=True)
