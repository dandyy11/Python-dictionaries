"""
Process the JSON file named school_data.json. Display only those schools 
that are part of the ACC, Big 12, Big Ten, and SEC divisons.

Copy that info here:

"NCAA/NAIA conference number football (IC2020)","372","American Athletic Conference"
"NCAA/NAIA conference number football (IC2020)","108","Big Twelve Conference"
"NCAA/NAIA conference number football (IC2020)","107","Big Ten Conference"
"NCAA/NAIA conference number football (IC2020)","130","Southeastern Conference"


Display report for all universities that have a graduation rate for Women over 90%
Display report for all universities that have a total price for in-state students living off campus over $60,000



"""
import json

# Use the full path to the file
infile = open('e:/AdvancedPython/AdvPython/mydictionaries/school_data.json', 'r')
schools = json.load(infile)

# Check type of schools data
print(type(schools))

# List of conference numbers for ACC, Big 12, Big Ten, SEC
conference_schools = [372, 108, 107, 130]

# Report 1 - Schools in ACC, Big 12, Big Ten, SEC divisions
print("\nSchools in ACC, Big 12, Big Ten, SEC divisions:")
for school in schools:
    if 'NCAA' in school:
        if school['NCAA'].get('NAIA conference number football (IC2020)') in conference_schools:
            print(school['instnm'])

# Report 2 - Schools with graduation rate for women over 90%
print("\nSchools with graduation rate for women over 90%:")
for school in schools:
    if 'Graduation rate  women (DRVGR2020)' in school and school['Graduation rate  women (DRVGR2020)'] is not None:
        if school['Graduation rate  women (DRVGR2020)'] > 90:
            print(school['instnm'])


# Report 3 - Schools with total price for in-state students living off-campus over $60,000
print("\nSchools with total price for in-state students living off-campus over $60,000:")
for school in schools:
    if 'Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)' in school:
        if school['Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)'] is not None:
            if school['Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)'] > 60000:
                print(school['instnm'])

# Close the file
infile.close()
