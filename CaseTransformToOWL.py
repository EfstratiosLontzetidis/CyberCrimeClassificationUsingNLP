from owlready2 import *
from sklearn.feature_extraction.text import TfidfVectorizer
import os

def read_text_file(file_path):
    with open(file_path, 'r',encoding=("UTF-8")) as f:
        return f.read()
# load ontology
crime = get_ontology("file://CyberCrimeOntology.owl").load()

characteristics_prefix=["./descriptions/characteristics/offender","./descriptions/characteristics/access violation","./descriptions/characteristics/victim","./descriptions/characteristics/target","./descriptions/characteristics/harm"]
cases_prefix="./descriptions/cases"

print("Starting to read cases from folder "+ cases_prefix)
filestochecksimilarity = []
# for each crime find its characteristics
for file in os.listdir(cases_prefix):
    # Check whether file is in text format or not
    file_path = cases_prefix+"/"+file
    # call read text file function
    case_name=file.replace(".txt","")
    print("CASE NAME: "+case_name)
    new_case = Thing(name=str(case_name), namespace=crime)
    case=read_text_file(file_path)
    print("*********************************")
    print("CΗARACTERISTICS: ")
    print("+++++++++++++++++++++++++++++++++")
    counter=0
    for obj in characteristics_prefix:
        if counter == 0:
            print("Offender")
        elif counter == 1:
            print("Access Violation")
        elif counter == 2:
            print("Victim")
        elif counter == 3:
            print("Target")
        else:
            print("Harm")
        print("=============================")
        for file2 in os.listdir(obj):
            file2_path = obj + "/" + file2
            filestochecksimilarity.append(file_path)
            filestochecksimilarity.append(file2_path)
            characteristic_name=file2.replace(".txt","")
            characteristic=read_text_file(file2_path)
            documents = [open(f,encoding="UTF-8").read() for f in filestochecksimilarity]
            tfidf = TfidfVectorizer(min_df=1, stop_words="english").fit_transform(documents)
            pairwise_similarity = tfidf * tfidf.T
            if (pairwise_similarity[0,1]>0.5):
                if counter == 0:
                    if characteristic_name=="abusive user":
                        new_case.hasOffender = ['Abusive User']
                    elif characteristic_name=="cyber bully":
                        new_case.hasOffender = ['Cyber Bully']
                    elif characteristic_name=="cyber fighter":
                        new_case.hasOffender = ['Cyber Fighter']
                    elif characteristic_name=="cyber terrorist":
                        new_case.hasOffender = ['Cyber Terrorist']
                    elif characteristic_name=="entities as offenders":
                        new_case.hasOffender = ['Entities as Offenders']
                    elif characteristic_name=="hacktivist":
                        new_case.hasOffender = ['Hacktivist']
                    elif characteristic_name=="insider":
                        new_case.hasOffender = ['Insider']
                    elif characteristic_name=="online social hacker":
                        new_case.hasOffender = ['Online Social Hacker']
                    elif characteristic_name=="script kiddie":
                        new_case.hasOffender = ['Script Kiddie']
                    elif characteristic_name=="sexually deviant user":
                        new_case.hasOffender = ['Sexually Deviant User']
                    elif characteristic_name=="cyber criminal":
                        new_case.hasOffender = ['Cyber Criminal']
                elif counter == 1:
                    if characteristic_name=="physical tampering":
                        new_case.hasAccessViolation = ['Physical Tampering']
                    elif characteristic_name=="local computer access":
                        new_case.hasAccessViolation = ['Local Computer Access']
                    elif characteristic_name=="remote computer access":
                        new_case.hasAccessViolation = ['Remote Computer Access']
                elif counter == 2:
                    if characteristic_name=="company":
                        new_case.hasVictim = ['Company']
                    elif characteristic_name=="country":
                        new_case.hasVictim = ['Country']
                    elif characteristic_name=="individual":
                        new_case.hasVictim = ['Individual']
                elif counter == 3:
                    if characteristic_name == "physical abuse":
                        new_case.hasTarget = ['Physical Abuse']
                    elif characteristic_name == "emotional abuse":
                        new_case.hasTarget = ['Emotional Abuse']
                    elif characteristic_name == "ict abuse":
                        new_case.hasTarget = ['ICT Abuse']
                    elif characteristic_name == "infrastructure ict abuse":
                        new_case.hasTarget = ['infrastructure ICT Abuse']
                    elif characteristic_name == "sexual abuse":
                        new_case.hasTarget = ['Sexual Abuse']
                    elif characteristic_name == "social abuse":
                        new_case.hasTarget = ['Social Abuse']
                    elif characteristic_name == "financial abuse":
                        new_case.hasTarget = ['Financial Abuse']
                else:
                    if characteristic_name == "inchoate harm":
                        new_case.hasHarm = ['Inchoate Harm']
                    elif characteristic_name == "individual harm":
                        new_case.hasHarm = ['Individual Harm']
                    elif characteristic_name == "direct systemic harm":
                        new_case.hasHarm = ['Direct Systemic Harm']
                    elif characteristic_name == "generalized individual harm":
                        new_case.hasHarm = ['Generalized Individual Harm']
                    elif characteristic_name == "aggregated individual harm":
                        new_case.hasHarm = ['Aggregated Individual Harm']
                print(characteristic_name)
            print("''''''''''''''''''''''''''''''''''''''''''''''''''''''")
            filestochecksimilarity.clear()
        filestochecksimilarity.clear()
        counter+=1

crime.save("Cyber_crime_ontology_with_new_crime_cases.owl")

