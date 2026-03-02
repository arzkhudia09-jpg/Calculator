import os
from flask import Flask, render_template, request
from definition import add, subtract, multiply, divide

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0


@app.after_request
def disable_cache(response):
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response


def get_css_version():
    css_path = os.path.join(app.root_path, "static", "style.css")
    try:
        return int(os.path.getmtime(css_path))
    except OSError:
        return 1


@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    error = None
    num1 = None
    num2 = None
    operation = ""

    if request.method == "POST":
        operation = request.form.get("operation", "")
        num1_raw = request.form.get("num1", "").strip()
        num2_raw = request.form.get("num2", "").strip()

        try:
            num1 = float(num1_raw)
            num2 = float(num2_raw)

            if operation == "+":
                result = add(num1, num2)
            elif operation == "-":
                result = subtract(num1, num2)
            elif operation == "*":
                result = multiply(num1, num2)
            elif operation == "/":
                result = divide(num1, num2)
            else:
                error = "Please choose a valid operation."

        except ValueError:
            error = "Please enter valid numbers."
        except Exception as e:
            error = str(e)

    return render_template(
        "index.html",
        result=result,
        error=error,
        num1=num1,
        num2=num2,
        operation=operation,
        css_version=get_css_version(),
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
