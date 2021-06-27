
import json
import http.client

debug=0
print('Enter the Username fow which you wan to get feeds')
hashtag=input()

conn = http.client.HTTPSConnection("instagram85.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "c9240ebd54mshb6d1dce322d2f9cp1f13acjsn639b8c8b1bc2",
    'x-rapidapi-host': "instagram85.p.rapidapi.com"
    }


conn.request("GET", "/account/"+hashtag+"/feed?by=username", headers=headers)

res = conn.getresponse()
data = res.read()

'''print(data.decode("utf-8"))'''
json_dictionary = json.loads(data.decode("utf-8"))
print(json_dictionary);


outputHTML = "<html><head><meta charset='utf-8'><style> .instagram-wrapper{  display:grid;  grid-template-columns: 200px 200px 200px;} .post-wrapper{padding:10px;} .post-wrapper img {max-width:180px;}.post-likes{font-weight:bold;}</style></head><body><div class='instagram-wrapper'>"

outputFile = "instagramFeed.html"

for item in json_dictionary['data']:

    thisCaption = item['caption'].replace('n','<br />n')
    if debug>0:
        print("CAPTION:", thisCaption)
    thisURL = item['images']['original']['standard']
    if debug>0:
        print("image url", ":", thisURL)
    id = item['id']
    if debug>0:
        print("Id", ":", id)
  
    outputHTML+='<div class="post-wrapper"><img src="'+str(thisURL)+'" /><div class="post-caption">'+thisCaption+'</div><div class="post-caption">'+id+'</div></div>'

outputHTML+='</div></body></html>'

with open(outputFile, "w", encoding="utf-8") as f:
    f.write(outputHTML)


