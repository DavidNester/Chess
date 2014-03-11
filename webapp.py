from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    board = ["rnbqkbnr", #8
             "pppppppp", #7
             "........", #6
             "........", #5
             "........", #4
             "........", #3
             "PPPPPPPP", #2
             "RNBQKBNR"]
    return render_template('chess_board.html', board=board)

if __name__ == "__main__":
    app.run(debug=True)
