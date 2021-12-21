import nltk
from owlready2 import *
from nltk import *
from nltk import bigrams, trigrams

def nlp_most_words_in_description(filename):
    # input abusive user description from file
    with open(filename, "r") as myfile:
        case = myfile.read()

    # tokenization
    tokens = nltk.word_tokenize(case)
    # stopwords and special characters
    wordlist = nltk.corpus.stopwords.words("english")
    wordlist2 = [",", ".", "’", ":", "“", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "''", "``", "'", "The"]
    # to calculate frequency of words
    fdist = FreqDist()
    # stemming if needed
    pst = PorterStemmer()
    # remove useless tokens
    new = []
    # if needed to switch to bigrams or trigrams
    bigrams = nltk.bigrams(list(tokens))
    trigrams = nltk.trigrams(list(tokens))
    # remove unnecessary words & special chars
    for words in tokens:
        # frequency
        flag = True
        for x in wordlist:
            if x == words or words in wordlist2:
                flag = False
                break
        if flag == True:
            # new.append(words)
            new.append(pst.stem(words))

    for x in new:
        fdist[x] += 1

    listtoreturn = []
    for x in fdist.most_common(15):
        listtoreturn.append(x[0])

    return listtoreturn

crime = get_ontology("file://CyberCrimeOntology.owl").load()

# wordlists for each crime characteristic

# offender characteristics

abusive_user_list = nlp_most_words_in_description("./descriptions/characteristics/offender/abusive user.txt")
cyber_bully_list = ['bully', 'cyber-bully', 'cyber bully']
cyber_criminal_list = ['criminal', 'cyber criminal', 'cyber-criminal']
cyber_fighter_list = ['fighter']
cyber_terrorist_list = ['terrorism', 'terrorist']
hacktivist_list = ['hacktivist', 'political', 'politics']
insider_list = ['insider', 'malicious employee', 'employee']
online_social_hacker_list = ['social hacker', 'online social hacker']
script_kiddie_list = ['kiddie', 'script kiddie']
sexually_deviant_user_list = ['sexually', 'deviant']
entities_as_offenders_list = ['offenders', 'espionage']

# access violation

physical_tampering_list = ['physical access', 'physical computer access', 'physical tampering']
local_computer_access_list = ['local access', 'local computer access']
remote_computer_access_list = ['remote access', 'remote computer access']

# target

physical_abuse_list = ['physical assault', 'physical battery', 'murder', 'death']
emotional_abuse_list = ['mental anguish', 'offending sanity', 'offending privacy']
sexual_abuse_list = ['pornographic', 'porn', 'sexual assault', 'sexual battery', 'rape', 'raping', 'pornography']
financial_abuse_list = ['management of funds', 'unauthorized use of assets', 'unauthorized use of resources']
ict_abuse_list = ['ICT abuse']
infrastructure_ict_abuse_list = ['infrastructure ICT abuse']
social_abuse_list = ['afflicting prosperity', 'afflicting stability', 'afflicting prosperity',
                     'inaccessible services to civilians']

# victim

kid_list = ['kid', 'kids', 'child', 'children']
adult_list = ['adult', 'adults']
company_list = ['company', 'organization', 'employee']
country_list = ['country', 'state']

# harm

individual_harm_list = ['loss of life', 'moral harm', 'physical injury', 'substantial damage', 'fear',
                        'emotional distress']
aggregated_individual_harm_list = ['moral harm', 'accumulated loss of property', 'emotional distress', 'fear']
generalized_individual_harm_list = ['dispossession of wealth', 'moral decay', 'social disorder']
direct_systemic_harm_list = ['direct', 'chaos', 'anarchy', 'country engagement']
inchoate_harm_list = ['inferential', 'potential', 'inchoate']

add_more = True
while (add_more):

    crime_name = input("Insert name for the case (STOP to end process): ")

    if crime_name != "STOP":

        # create individual without assigned class

        new_case = Thing(name=str(crime_name), namespace=crime)
        crime_case = input("Insert case description: ")

        # checking for offender characteristics in crime case

        for x in abusive_user_list:
            if crime_case.__contains__(x):
                new_case.hasOffender = ['Abusive User']
                break

        for x in cyber_bully_list:
            if crime_case.__contains__(x):
                new_case.hasOffender = ['Cyber Bully']
                break

        for x in cyber_criminal_list:
            if crime_case.__contains__(x):
                new_case.hasOffender = ['Cyber Criminal']
                break

        for x in cyber_fighter_list:
            if crime_case.__contains__(x):
                new_case.hasOffender = ['Cyber Fighter']
                break

        for x in hacktivist_list:
            if crime_case.__contains__(x):
                new_case.hasOffender = ['Hacktivist']

        for x in cyber_terrorist_list:
            if crime_case.__contains__(x):
                new_case.hasOffender = ['Cyber Terrorist']
                break

        for x in script_kiddie_list:
            if crime_case.__contains__(x):
                new_case.hasOffender = ['Script Kiddie']
                break

        for x in insider_list:
            if crime_case.__contains__(x):
                new_case.hasOffender = ['Insider']
                break

        for x in online_social_hacker_list:
            if crime_case.__contains__(x):
                new_case.hasOffender = ['Online Social Hacker']
                break

        for x in entities_as_offenders_list:
            if crime_case.__contains__(x):
                new_case.hasOffender = ['Entities as Offenders']
                break

        for x in sexually_deviant_user_list:
            if crime_case.__contains__(x):
                new_case.hasOffender = ['Sexually Deviant User']
                break

        # checking for access violation characteristics

        for x in physical_tampering_list:
            if crime_case.__contains__(x):
                new_case.hasAccessViolation = ['Physical Tampering']
                break

        for x in local_computer_access_list:
            if crime_case.__contains__(x):
                new_case.hasAccessViolation = ['Local Computer Access']
                break

        for x in remote_computer_access_list:
            if crime_case.__contains__(x):
                new_case.hasAccessViolation = ['Remote Computer Access']
                break

        # checking for target characteristics

        for x in physical_abuse_list:
            if crime_case.__contains__(x):
                new_case.hasTarget = ['Physical Abuse']
                break

        for x in emotional_abuse_list:
            if crime_case.__contains__(x):
                new_case.hasTarget = ['Emotional Abuse']
                break

        for x in social_abuse_list:
            if crime_case.__contains__(x):
                new_case.hasTarget = ['Social Abuse']
                break

        for x in sexual_abuse_list:
            if crime_case.__contains__(x):
                new_case.hasTarget = ['Sexual Abuse']
                break

        for x in financial_abuse_list:
            if crime_case.__contains__(x):
                new_case.hasTarget = ['Financial Abuse']
                break

        for x in ict_abuse_list:
            if crime_case.__contains__(x):
                new_case.hasTarget = ['ICT Abuse']
                break

        for x in infrastructure_ict_abuse_list:
            if crime_case.__contains__(x):
                new_case.hasTarget = ['Infrastructure ICT Abuse']
                break

        # checking for victim characteristics

        for x in kid_list:
            if crime_case.__contains__(x):
                new_case.hasVictim = ['Kid']
                break

        for x in adult_list:
            if crime_case.__contains__(x):
                new_case.hasVictim = ['Adult']
                break

        for x in company_list:
            if crime_case.__contains__(x):
                new_case.hasVictim = ['Company']
                break

        for x in country_list:
            if crime_case.__contains__(x):
                new_case.hasVictim = ['Country']
                break

        # checking for harm characteristics

        for x in individual_harm_list:
            if crime_case.__contains__(x):
                new_case.hasHarm = ['Individual Harm']
                break

        for x in generalized_individual_harm_list:
            if crime_case.__contains__(x):
                new_case.hasHarm = ['Generalized Individual Harm']
                break

        for x in aggregated_individual_harm_list:
            if crime_case.__contains__(x):
                new_case.hasHarm = ['Aggregated Individual Harm']
                break

        for x in direct_systemic_harm_list:
            if crime_case.__contains__(x):
                new_case.hasHarm = ['Direct Systemic Harm']
                break

        for x in inchoate_harm_list:
            if crime_case.__contains__(x):
                new_case.hasHarm = ['Inchoate Harm']
                break

    else:
        add_more = False

crime.save("Cyber_crime_ontology_with_new_crime_cases.owl")


def nlp_most_words_in_description(filename):
    # input abusive user description from file
    with open("./descriptions/characteristics/offender/abusive user.txt", "r") as myfile:
        case = myfile.read()

    # tokenization
    tokens = nltk.word_tokenize(case)
    # stopwords and special characters
    wordlist = nltk.corpus.stopwords.words("english")
    wordlist2 = [",", ".", "’", ":", "“", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "''", "``", "'", "The"]
    # to calculate frequency of words
    fdist = FreqDist()
    # stemming if needed
    pst = PorterStemmer()
    # remove useless tokens
    new = []
    # if needed to switch to bigrams or trigrams
    bigrams = nltk.bigrams(list(tokens))
    trigrams = nltk.trigrams(list(tokens))
    # remove unnecessary words & special chars
    for words in tokens:
        # frequency
        flag = True
        for x in wordlist:
            if x == words or words in wordlist2:
                flag = False
                break
        if flag == True:
            # new.append(words)
            new.append(pst.stem(words))

    for x in new:
        fdist[x] += 1

    listtoreturn = []
    for x in fdist.most_common(15):
        listtoreturn.append(x[0])

    # print(list(listtoreturn))
