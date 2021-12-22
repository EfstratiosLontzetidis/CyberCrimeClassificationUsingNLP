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

print("Starting to read cases from folder "+cases_prefix)
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
            # no need to normalize, since Vectorizer will return normalized tf-idf
            pairwise_similarity = tfidf * tfidf.T
            if (pairwise_similarity[0,1]>0.5):
                if counter == 0:
                    # need enrichment
                    new_case.hasOffender = ['Abusive User']
                elif counter == 1:
                    # need enrichment
                    new_case.hasAccessViolation = ['Physical Tampering']
                elif counter == 2:
                    # need enrichment
                    new_case.hasVictim = ['Company']
                elif counter == 3:
                    # need enrichment
                    new_case.hasTarget = ['Physical Abuse']
                else:
                    # need enrichment
                    new_case.hasHarm = ['Inchoate Harm']
                print("=============================")
                print(characteristic_name)
            filestochecksimilarity.clear()
        filestochecksimilarity.clear()
        counter+=1

crime.save("Cyber_crime_ontology_with_new_crime_cases.owl")

