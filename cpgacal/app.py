from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    cgpa = None
    if request.method == 'POST':
        try:
            # Retrieve lists of grades and credits from the form
            grades = request.form.getlist('grade')
            credits = request.form.getlist('credit')

            total_points = 0
            total_credits = 0

            for g, c in zip(grades, credits):
                if g and c:
                    total_points += float(g) * float(c)
                    total_credits += float(c)

            if total_credits > 0:
                cgpa = round(total_points / total_credits, 2)
        except ValueError:
            cgpa = "Error: Please enter valid numbers."

    return render_template('index.html', cgpa=cgpa)

if __name__ == '__main__':
    app.run(debug=True)