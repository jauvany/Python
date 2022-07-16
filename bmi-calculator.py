#BMI Calculator from scratch @jauvany

w = int(input())
h = float(input())

fh = h ** 2
bmi = w / fh
if bmi < 18.5:
  print("Underweight")
else: 
  if (bmi >= 18.5) and (bmi < 25):
    print("Normal")
  else: 
    if (bmi >= 25) and (bmi < 30): 
      print("Overweight ")
    else:
      if bmi > 30:   
        print("Obesity")

