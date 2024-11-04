# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()

height1=float(height)
weight2=int(weight)
BmI=weight2/(height1 * height1)
bmi=int(BmI)
print(bmi)