"""
Process the JSON file named school_data.json. Display only those schools 
that are part of the AAC, Big 12, Big Ten, and SEC divisons.

Copy that info here:

"NCAA/NAIA conference number football (IC2020)","372","American Athletic Conference"
"NCAA/NAIA conference number football (IC2020)","108","Big Twelve Conference"
"NCAA/NAIA conference number football (IC2020)","107","Big Ten Conference"
"NCAA/NAIA conference number football (IC2020)","130","Southeastern Conference"


Display report for all universities that have a graduation rate for Women over 75%
Display report for all universities that have a total price for in-state students living off campus over $50,000

"""

import json

infile = open('school_data.json', 'r')

schoolList = json.load(infile)

# print(type(schoolList))
# print(schoolList[1])

confList = [372,108,107,130]

#if key in confList:

for i in schoolList:
    if i['NCAA']['NAIA conference number football (IC2020)'] in confList:
        if i['Graduation rate  women (DRVGR2020)'] > 75:
            print(f'University: {i['instnm']}')
            print(f'Graduation Rate for Women: {i['Graduation rate  women (DRVGR2020)']}%\n\n')

print(f'----------------------------------------\n\n')

for i in schoolList:
    if i['NCAA']['NAIA conference number football (IC2020)'] in confList:
        if i['Total price for in-state students living on campus 2020-21 (DRVIC2020)'] > 50000:
            print(f'University: {i['instnm']}')
            print(f'Total price for in-state students living off campus: ${i['Total price for in-state students living on campus 2020-21 (DRVIC2020)']:,.2f}\n\n')





