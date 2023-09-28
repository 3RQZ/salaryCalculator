skillLevel = int(input('Insert your skill level: '))
hours = int(input('Insert hours worked: '))

hourRate = 0
overtimeRate = 0
salary = 0
salaryAfter = 0

medicalIns = ''
med = 0
dedMed = 0

dentalIns = ''
dental = 0
dedDent = 0


disabilityIns = ''
disability = 0
dedDis = 0

retirementPlan = ''
retirement = 0
dedRet = 0

while skillLevel > 3:
    skillLevel = int(input('Invalid skill level please insert your skill level again: '))

while skillLevel < 1:
    skillLevel = int(input('Invalid skill level please insert your skill level again: '))

while hours < 0:
    hours = int(input('Invalid number of hours please insert hours again: '))
if skillLevel == 1:
    hourRate = 30
    overtimeRate = 45
    if hours <= 40:
        salary = hours * hourRate
    elif hours > 40:
        salary = 40 * hourRate + (hours - 40) * overtimeRate

elif skillLevel == 2:
    hourRate = 40
    overtimeRate = 60
    if hours <= 40:
        salary = hours * hourRate
    elif hours > 40:
        salary = 40 * hourRate + (hours - 40) * overtimeRate

    medicalIns = input('Do you have want medical insurance (Y/N): ')
    dentalIns = input('Do you have want dental insurance (Y/N): ')
    disabilityIns = input('Do you have want disability insurance (Y/N): ')

    if medicalIns == 'y' or medicalIns == 'Y':
        med = 1
    elif medicalIns == 'n' or medicalIns == 'N':
        med = 2
    else:
        print('invalid input')

    if dentalIns == 'y' or dentalIns == 'Y':
        dental = 1
    elif dentalIns == 'n' or dentalIns == 'N':
        dental = 2
    else:
        print('invalid input')

    if disabilityIns == 'y' or disabilityIns == 'Y':
        disability = 1
    elif disabilityIns == 'n' or disabilityIns == 'N':
        disability = 2
    else:
        print('invalid input')

elif skillLevel == 3:
    hourRate = 50
    overtimeRate = 75
    if hours <= 40:
        salary = hours * hourRate
    elif hours > 40:
        salary = 40 * hourRate + (hours - 40) * overtimeRate

    medicalIns = input('Do you have want medical insurance (Y/N): ')
    dentalIns = input('Do you have want dental insurance (Y/N): ')
    disabilityIns = input('Do you have want disability insurance (Y/N): ')
    retirement = input('Do you have want retirement plan (Y/N): ')

    if medicalIns == 'y' or medicalIns == 'Y':
        med = 1
    elif medicalIns == 'n' or medicalIns == 'N':
        med = 2
    else:
        print('invalid input')

    if dentalIns == 'y' or dentalIns == 'Y':
        dental = 1
    elif dentalIns == 'n' or dentalIns == 'N':
        dental = 2
    else:
        print('invalid input')

    if disabilityIns == 'y' or disabilityIns == 'Y':
        disability = 1
    elif disabilityIns == 'n' or disabilityIns == 'N':
        disability = 2
    else:
        print('invalid input')

    if retirementPlan == 'y' or retirementPlan == 'Y':
        retirement = 1
    elif retirementPlan == 'n' or retirementPlan == 'N':
        retirement = 2
    else:
        print('invalid input')

if med == 1:
    dedMed = 60

if dental == 1:
    dedDent = 40

if disability == 1:
    dedDis = 25

if retirement == 1:
    dedRet = (salary*0.03)

deductions = dedMed + dedDis + dedRet + dedDent

salaryAfter = salary - deductions

print('hours worked is', hours)
print('hourly rate is', hourRate)
print('regular rate is', hourRate)
print('overtime pay is', overtimeRate)
print('total pay is', salary)
print('total deductions is', deductions)
print('the final payment with deductions is', salaryAfter)
