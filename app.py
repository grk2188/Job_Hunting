from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'San Francisco',
    'salary': '$120,000'
}, {
    'id': 2,
    'title': 'Front-end Engineer',
    'location': 'San Jose',
    'salary': '$140,000'
}, {
    'id': 3,
    'title': 'Data Engineer',
    'location': 'Seattle',
    
}, {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'Seattle',
    'salary': '$160,000'
}]


@app.route('/')
def home():
  return render_template('home.html', jobs=JOBS)

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
