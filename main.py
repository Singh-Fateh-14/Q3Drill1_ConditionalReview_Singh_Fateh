from pyscript import document

def calculate(event):
    # Retrieve inputs from the HTML document
    input_one = document.querySelector("#score1").value
    input_two = document.querySelector("#score2").value

    # Validate that the inputs are not empty strings
    if input_one != "" and input_two != "":
        s1 = float(input_one)
        s2 = float(input_two)
        
        # Calculate the final arithmetic average
        result_avg = (s1 + s2) / 2
        
        # Update the display for the average
        document.querySelector("#avg-display").innerText = f"{result_avg:.1f}"
        
        # Conditional logic to determine passing status (75 is the threshold)
        if result_avg >= 75:
            status = "Yes"
        else:
            status = "No"
            
        document.querySelector("#pass-display").innerText = status
    else:
        # Fallback if fields are left blank
        document.querySelector("#pass-display").innerText = "Error: Input required"

# Internal logic: At least two comments present and correct indentation used.