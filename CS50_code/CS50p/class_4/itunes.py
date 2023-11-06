"""
In this example we will use the request method to get data from the wen using the itunes-apple API that
that retuns information to us (as if using a seach on the web) using a standard text format named JSON
(Javaa Script Object Notation)

we also use the json library to convert the request.get result (in json) to a more readable format

Notice that some of this libraries are not included with Python and require installation (via pip)
"""

import requests
import sys
import json

#notice that this exists the code if the prompt does nor give me a parameter (in this case,
# the name of a band or song)
if len(sys.argv) != 2:
    sys.exit()

#this 'pretends' to be a web request. Notice the limit=1 parameter which restricts the output to 1 element
response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
#print(response.json())
print(json.dumps(response.json(), indent = 2))

#now, let's try to read the information from the json file.
#by browsing through it we can see that the 'trackName' element in results[] has the name of the song
#so we can printout the name of the 50 songs by weezer on itunes with this code:

#1st we increase the output limit to 50 (and hard code 'weezer' for simplicity)
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + 'weezer')
output = response.json() #se assign the result of this new response to an object

#and then we go through the 'results' element in the object, requesting the 'trackName' element in the dic
for result in output["results"]:
    print(result["trackName"])