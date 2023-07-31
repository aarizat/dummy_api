from flask import Flask, make_response, render_template_string, jsonify
import csv
import io


app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template_string("""
        <html>
            <head>
                <meta charset="UTF-8">
            </head>
            <body style="display: flex; justify-content: center; align-items: center; height: 100vh; flex-direction: column;">
                <h1> Welcome! </h1>
                <p style="font-size: 1.5em;">Lost in the Internet? You're in the right place! &#x1F602;</p>
                <footer style="position: fixed; bottom: 0; width: 100%; text-align: center; padding: 20px;">
                    <p>By Andres Ariza &#x2764;</p>
                </footer>
            </body>
        </html>
    """)


@app.route('/csv-with-metadata', methods=['GET'])
def get_csv_with_metadata():
    si = io.StringIO()
    cw = csv.writer(si)
    cw.writerow(['List of users'])
    cw.writerow([])
    cw.writerow(['Created date:', '2023-07-27'])
    cw.writerow([])
    cw.writerow(['name', 'age', 'profession'])
    cw.writerow(['Joe', '34', 'engineer'])
    cw.writerow(['Mack', '45', 'Teacher'])
    cw.writerow(['Jose', '100', 'Retired'])
    cw.writerow(['Marlon', '45', 'Astronaut'])
    output = make_response(si.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=users.csv"
    output.headers["Content-type"] = "text/csv"
    return output


@app.route('/csv', methods=['GET'])
def get_csv_data():
    si = io.StringIO()
    cw = csv.writer(si)
    cw.writerow(['name', 'age', 'profession'])
    cw.writerow(['Joe', '34', 'engineer'])
    cw.writerow(['Mack', '45', 'Teacher'])
    cw.writerow(['Jose', '100', 'Retired'])
    cw.writerow(['Marlon', '45', 'Astronaut'])
    output = make_response(si.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=users.csv"
    output.headers["Content-type"] = "text/csv"
    return output


@app.route('/json', methods=['GET'])
def get_json_data():
    data = [
        {"name": "Joe", "age": 34, "profession": "engineer"},
        {"name": "Mack", "age": 45, "profession": "Teacher"},
        {"name": "Jose", "age": 100, "profession": "Retired"},
        {"name": "Marlon", "age": 45, "profession": "Astronaut"},
    ]
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=False)
