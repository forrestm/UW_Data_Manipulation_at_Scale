import sys
import json
import re
from operator import itemgetter


us_states = {
    'AK': 'Alaska',
    'AL': 'Alabama',
    'AR': 'Arkansas',
    'AS': 'American Samoa',
    'AZ': 'Arizona',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DC': 'District of Columbia',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'GU': 'Guam',
    'HI': 'Hawaii',
    'IA': 'Iowa',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'MA': 'Massachusetts',
    'MD': 'Maryland',
    'ME': 'Maine',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MO': 'Missouri',
    'MP': 'Northern Mariana Islands',
    'MS': 'Mississippi',
    'MT': 'Montana',
    'NA': 'National',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'NE': 'Nebraska',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NV': 'Nevada',
    'NY': 'New York',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'PR': 'Puerto Rico',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VA': 'Virginia',
    'VI': 'Virgin Islands',
    'VT': 'Vermont',
    'WA': 'Washington',
    'WI': 'Wisconsin',
    'WV': 'West Virginia',
    'WY': 'Wyoming'
}
hp_state = {}
running_dic = {}
scores = {}
def hw():
    print('Hello, world!')

def lines(fp):
    print(str(len(fp.readlines())))

def main():
    happy_score = 0
    afinnfile = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    # afinnfile = open("AFINN-111.txt")
    # scores = {} # initialize an empty dictionary
    for line in afinnfile:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.

    # print(scores.items()) # Print every (term, score) pair in the dictionary

    tweetcleanup = {}

    for line in tweet_file:
        tweetlines = json.loads(line)
        if 'place' in tweetlines.keys():
            place = tweetlines['place']
            if place != None:
                if place['country_code'] == 'US' and place['place_type'] == 'city':
                    city_state = place['full_name']
                    ci, st = city_state.split(',')
                    # print(st.strip())
                    # if len(city_state) >= 2:
                    #     print(city_state)
                    #     ci, st = city_state.split(',')
                    st = st.strip()
                    # print(type(us_states[]))
                    if st in us_states:
                        # print('happy score')
                        if 'text' in tweetlines.keys():
                            tweet = tweetlines['text'].encode('utf-8').lower().split(' ')
                            for item in tweet:
                                # print('happy score')
                                if item in scores:
                                    # print('happy score')
                                    happy_score += scores[item]
                        if st in hp_state:
                            if happy_score >= hp_state[st]:
                                hp_state[st] = happy_score
                        else:
                            hp_state[st] = happy_score
    happiest = sorted(hp_state.items(), key = itemgetter(1), reverse = True)
    happiest_state = happiest[0]
    print(happiest_state[0])

if __name__ == '__main__':
    main()
