from derivedClasses import *

conn2 = sqlite3.connect("taxonomyRelations.db")
c2 = conn2.cursor(cursor)

"""wSs = c2.getWordSenses()

for wS in wSs[:]:
    if (len(c2.getTPsOfAWordSense(wS)) < 1):
        wSs.remove(wS)

dictWSToTPs = dict()
for wS in wSs:
    tps = c2.getTPsOfAWordSense(wS)
    dictWSToTPs[wS] = tps

for i, wS1 in enumerate(wSs):
    wSs.remove(wS1)
    print("wS " + str(wS1) + ":")
    for tP in dictWSToTPs[wS1]:
        supportOCAndSentences = c2.getListOfSupportOCAndSentences(tP, wS1)
        for supportOCAndSentence in supportOCAndSentences:
            print("\t%s | %s " % (tP, supportOCAndSentence[2]) )
    for wS2 in wSs[i:]:
        if c2.sameVerb(dictWSToTPs[wS1][0], dictWSToTPs[wS2][0]):
            wSs.remove(wS2)
            print("wS " + str(wS2) + ":")
            for tP in dictWSToTPs[wS2]:
                supportOCAndSentences = c2.getListOfSupportOCAndSentences(tP, wS2)
                for supportOCAndSentence in supportOCAndSentences:
                    print("\t%s | %s " % (tP, supportOCAndSentence[2]) )
    print("")
    print("")"""

wSs = c2.getWordSenses()

dictWSToTPs = dict()
for wS in wSs:
    tps = c2.getTPsOfAWordSense(wS)
    if (len(tps) >= 1):
        dictWSToTPs[wS] = tps

print("1st part done.")

dictVerbToWSs = c2.getWSsGroupAccordingToSameVerbs()

print("2nd part done.")

for verb in dictVerbToWSs.keys():
    if len(dictVerbToWSs[verb]) > 1:
        print(str(verb) + ": ")
        for wS in dictVerbToWSs[verb]:
            print("\t" + str(wS))
            for tP in dictWSToTPs[wS]:
                supportOCAndSentences = c2.getListOfSupportOCAndSentences(tP, wS)
                for supportOCAndSentence in supportOCAndSentences:
                    print("\t\t%s | %s " % (tP, supportOCAndSentence[0]) )