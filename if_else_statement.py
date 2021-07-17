mark = 50

if mark >= 80:
    print("You Got A+")
if 70 <= mark < 80:
    print("You Got A-")
elif 60 <= mark < 70:
    print("You Got B")
else:
    if 50 <= mark < 60:
        print("You Got C")
    else:
        print("You Failed")
