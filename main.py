from js import document
import js

def compute_average(e):
    # Get input values from the HTML inputs
    score1 = document.getElementById("score1").value
    score2 = document.getElementById("score2").value

    # Convert input values to numbers
    try:
        num1 = float(score1)
        num2 = float(score2)
    except ValueError:
        document.getElementById("result").innerHTML = "Please enter valid numbers."
        return

    # Check if the scores are within the valid range
    if num1 >= 0 and num1 <= 100 and num2 >= 0 and num2 <= 100:
        average = (num1 + num2) / 2

        # Check if the average is passing or failing
        if average >= 75:
            document.getElementById("result").innerHTML = f"Average: {average:.2f} <br>✅ Passed"
        else:
            document.getElementById("result").innerHTML = f"Average: {average:.2f} <br>❌ Failed"
    else:
        document.getElementById("result").innerHTML = "Please enter scores between 0 and 100."

js.window.compute_average = compute_average


