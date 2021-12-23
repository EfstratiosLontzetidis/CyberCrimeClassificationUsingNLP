from CaseTransformToOWL import case_to_owl
from CharacteristicsToCrimes import map_characteristics_to_crimes

# Efstratios Lontzetidis dissertation for MSc Information Security and Digital Forensics
# This tool give the user the option to pick if he wants to see the cyber crimes listing with their characteristics
# (using NLP and the existing literature) or import his cases
# and transform them to owl individuals with their data properties (characteristics).

while True:
    user_input=input("If you want to see the mapped characteristics to cyber crimes type 1. If you want to import your cases and reveal their cyber crime category type 2:")
    print("\n")
    if (user_input=="1"):
        map_characteristics_to_crimes()
        break
    elif (user_input=="2"):
        case_to_owl("./descriptions/cases")
        break
    else:
        print("Unexpected input, please try again.")
        print("\n")