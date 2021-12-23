from sklearn.feature_extraction.text import TfidfVectorizer
import os

def read_text_file(file_path):
    with open(file_path, 'r',encoding=("UTF-8")) as f:
        return f.read()

def map_characteristics_to_crimes():
    print("The following cyber crimes are associated with their respective characteristics using NLP techniques (comparing similarity of documents) on the descriptions of the existing literature\n")
    characteristics_prefix=["./descriptions/characteristics/offender","./descriptions/characteristics/access violation","./descriptions/characteristics/victim","./descriptions/characteristics/target","./descriptions/characteristics/harm"]
    crimes_prefix="./descriptions/crimes"
    filestochecksimilarity = []
    # for each crime find its characteristics
    for file in os.listdir(crimes_prefix):
        # Check whether file is in text format or not
        file_path = crimes_prefix+"/"+file
        # call read text file function
        crime_name=file.replace(".txt","")
        print("Crime: " + crime_name)
        crime=read_text_file(file_path)
        print("*********************************")
        counter=0
        for obj in characteristics_prefix:
            if counter==0:
                print("Offender")
            elif counter==1:
                print("Access Violation")
            elif counter==2:
                print("Victim")
            elif counter==3:
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
                    print(characteristic_name)
                filestochecksimilarity.clear()
            filestochecksimilarity.clear()
            counter+=1
