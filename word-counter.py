# word counter

import urllib.request, urllib.error, urllib.parse, json
import obo

url = 'https://www.dhi.ac.uk/api/data/oldbailey_record_single?idkey=t17800628-33'

response = urllib.request.urlopen(url)
body = response.read().decode('UTF-8')
record = json.loads(body)
html = record['hits']['hits'][0]['_source']['html']
text = obo.stripTags(html).lower()
fullwordlist = obo.stripNonAlphaNum(text)
wordlist = obo.removeStopwords(fullwordlist, obo.stopwords)

from collections import Counter

counts = {}

counts = Counter(wordlist)
print(counts)