from flask import Flask, render_template, jsonify

app = Flask(__name__)


JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Tunis, Tunisia',
    'salary': '2500 dt'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Sousse, Tunisia',
    'salary': '3000 dt'
  },
  {
    'id': 3,
    'title': 'Devops Engineer',
    'location': 'Nice, France',
    'salary': '2800 $'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'US',
    'salary': '4000 £'
  }
]


@app.route("/")
def hello_word():
  return render_template('home.html', jobs=JOBS, company_name='Meniara')

@app.route("/api/jobs")
def list_job():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)