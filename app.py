from flask import Flask , render_template

app = Flask(__name__)


@app.route("/student_dashboard")
@app.route("/student_dashboard/")
def student_dashboard():
    return render_template("student_dashboard.html")

@app.route("/student_dashboard/my-applications")
@app.route("/student_dashboard/my-applications/")
def student_my_applications():
    return render_template("student_my_applications.html")

@app.route("/student_dashboard/all-forms")
def student_all_forms():
    return render_template("student_all_forms.html")

@app.route("/student_dashboard/my-applications/pharmacy")
def student_form_pharmacy():
    return render_template("student_form_pharmacy.html")

@app.route("/student_dashboard/my-payments")
def student_my_payments():
    return render_template("student_my_payments.html")

@app.route("/student_dashboard/raise-query")
def student_raise_query():
    return render_template("student_raise_query.html")

if __name__ == "__main__":
    app.run(debug=True , host= "0.0.0.0" , port = 5000)