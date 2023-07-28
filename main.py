from flask import Flask, make_response
import csv
import io


app = Flask(__name__)

@app.route('/dummy_data', methods=['GET'])
def get_data():
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


if __name__ == '__main__':
    app.run(debug=False)
