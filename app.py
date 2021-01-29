from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    # load current count
    with open("count.txt", 'r') as f:
        count = int(f.read())
    f.close()

    count+=1

    # overwrite the count
    f = open('count.txt', 'w')
    f.write(str(count))
    f.close()

    # render html with count variable

    return render_template('index.html', count = count)

if __name__ == "__main__":
    app.run(debug=True)