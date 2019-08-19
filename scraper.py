import scraperwiki
import json
import math
import requests
import sqlite3
#

page = 1 

url = 'https://api.seek.com.au/v2/jobs/search?keywords=data%20science%20&page='+str(page)+'&sortmode=ListedDate'
    
source = requests.get(url).text

source_data=json.loads(source)

total_count = source_data['totalCount']
print(total_count)
total_pages = total_count / 20
print(math.ceil(total_pages))

while page <= total_pages:
    
    print('reading data from URL page '+str(page))
    for data in source_data['data']:
                    jobID = data['id']
                    title = data['title']
                    advertiser = data['advertiser']['description']
                    advertiserID = data['advertiser']['id']
                    area = data['area']
                    classification = data['classification']['description']
                    classificationID = data['classification']['id']
                    listingDate = data['listingDate']
                    location = data['location']
                    locationID = data['locationId']
                    locationWhere = data['locationWhereValue']
                    salary = data['salary']
                    subClassification = data['subClassification']['description']
                    subClassificationID = data['subClassification']['id']
                    worktype = data['workType']
                    #
                    print('Writing record '+JobID)
                    scraperwiki.sqlite.save(unique_keys=['jobID'], data={"jobID": jobID, "title": title,"AdvertiserID":advertiserID,"Advertiser":advertiser}) 
                   
    page = page + 1
    url = 'https://api.seek.com.au/v2/jobs/search?keywords=data%20science%20&page='+str(page)+'&sortmode=ListedDate'
    
print('Read all pages') 
