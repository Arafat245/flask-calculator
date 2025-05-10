# app.py
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def form():
    return render_template("form.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    try:
        x = float(request.form["input_number"])
        result = x ** 2  # example logic
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
