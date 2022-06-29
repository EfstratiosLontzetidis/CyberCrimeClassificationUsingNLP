from CaseTransformToOWL import case_to_owl
from CharacteristicsToCrimes import map_characteristics_to_crimes
from JaccardTransformCase import case_to_owl_jaccard
from EuclideanTransformCase import case_to_owl_euclidean
import time, tracemalloc

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
        location_input=input("Input the location of the cases. Press enter for default location (./descriptions/cases) :")
        if location_input == "":
            location="./descriptions/cases"
        else:
            location=location_input
        algorithm_input=input("Input the preferred algorithm for similarity comparisons. 1) Cosine Similarity 2) Jaccard Similarity 3) Euclidean Distance . Default: Cosine Similarity: ")
        if algorithm_input == "1":
            start_time = time.time()
            tracemalloc.start()
            case_to_owl(location)
            print("Peak memory: " + str(tracemalloc.get_traced_memory()[1]))
            print("Seconds to run: %s" % (time.time() - start_time))
            tracemalloc.stop()
        elif algorithm_input == "2":
            start_time = time.time()
            tracemalloc.start()
            case_to_owl_jaccard(location)
            print("Peak memory: " + str(tracemalloc.get_traced_memory()[1]))
            print("Seconds to run: %s" % (time.time() - start_time))
            tracemalloc.stop()
        elif algorithm_input=="3":
            start_time = time.time()
            tracemalloc.start()
            case_to_owl_euclidean(location)
            print("Peak memory: " + str(tracemalloc.get_traced_memory()[1]))
            print("Seconds to run: %s" % (time.time() - start_time))
            tracemalloc.stop()
        else:
            start_time = time.time()
            tracemalloc.start()
            case_to_owl(location)
            print("Peak memory: " + str(tracemalloc.get_traced_memory()[1]))
            print("Seconds to run: %s" % (time.time() - start_time))
            tracemalloc.stop()
        break
    else:
        print("Unexpected input, please try again.")
        print("\n")