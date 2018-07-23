from langdetect import *

def poll(text,NumberOfTries = 1):
    attempts = [detect_langs(text) for i in range(NumberOfTries)]
    confidences = {}
    for attempt in attempts:
        for item in attempt:
            language = str(item)
            if not confidences.__contains__(language):
                confidences[language] = attempt[language]
            else:
                confidences[language] += attempt[language]
    if NumberOfTries > 1:
        for thing in confidences:
            confidence[thing] = confidence[thing] / NumberOfTries

    return confidences
