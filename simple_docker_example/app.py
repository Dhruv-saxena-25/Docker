from flask import Flask, render_template_string, request

app = Flask(__name__)

# HTML Template using Jinja2 syntax
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Multiplication Table</title>
</head>
<body>
    <h2>Enter a Number to Generate its Multiplication Table</h2>
    <form method="post">
        <input type="number" name="number" required>
        <input type="submit" value="Generate Table">
    </form>

    {% if table %}
        <h3>Multiplication Table for {{ number }}</h3>
        <ul>
            {% for line in table %}
                <li>{{ line }}</li>
            {% endfor %}
        </ul>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    table = []
    number = None
    if request.method == 'POST':
        try:
            number = int(request.form['number'])
            table = [f"{number} x {i} = {number * i}" for i in range(1, 11)]
        except ValueError:
            table = ["Invalid input. Please enter a valid number."]
    return render_template_string(HTML_TEMPLATE, table=table, number=number)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)


## To build docker image 
## --> docker build -t  <user_name>/image name .

## To RUN docker image
## docker run -p <port_you_want_to_run>:<given_port_inside_code> <image_name>