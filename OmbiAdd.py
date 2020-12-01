#!/usr/bin/python3
import re, requests, os, yaml, sys
from requests.structures import CaseInsensitiveDict
import sqlite3

def markAvailable(scanType, scanId, configPath):
    print("Will attempt to make {scanId} available using {scanType}".format(scanType = scanType, scanId = scanId))
    config_path = configPath
    with open(config_path) as parameters:
      config = yaml.safe_load(parameters)

#    config = yaml.load(open(config_path), Loader=yaml.FullLoader)
    ombiId = 0

    ombiApi_key = config['ombi']['apikey']
    ombiDb_path = config['ombi']['database_path']
    ombiDb = sqlite3.connect(ombiDb_path)
    url = config['ombi']['url'] + "/api/v1/Request"

    querystring = {"apiKey": "{}".format(ombiApi_key), 'Content-Type': "application/json"}

    if "None" in (ombiApi_key, url):
        print("Please check your config.yml again. Missing values.")
        return

 
    if scanType == 'IMDB':
        ombiId = ombiDb.execute("SELECT Id FROM MovieRequests WHERE ImdbId = '{}'".format(scanId)).fetchall()[0][0]
        url = url + "/movie/available"
        print("IMDB Request ID: {}".format(ombiId))

 
    elif scanType == 'TheMovieDB':
        ombiId = ombiDb.execute("SELECT Id FROM MovieRequests WHERE TheMovieDbId = '{}'".format(scanId)).fetchall()[0][0]
        url = url + "/movie/available"
        print("TMDB Request ID: {}".format(ombiId))
 
    elif scanType == 'TheTVDB':
        ombiId = ombiDb.execute("SELECT Id FROM TvRequests WHERE TvDbId = '{}'".format(scanId)).fetchall()[0][0]
        childId = ombiDb.execute("SELECT * FROM ChildRequests WHERE ParentRequestId = '{}'".format(ombiId)).fetchall()[-1][0]
        url = url + "/tv/available"
        print("TVDB Request ID: {} Child Request {}".format(ombiId, childId))
        ombiId = childId
 
    else:
        print("Incorrect option")
        return

    print("Will mark available {id} using {url}".format(id = ombiId, url = url))
 



#    resp = requests.post(url, headers=headers, data=data)
 #   print("{}".format(resp.status_code))
    print(url)
    headers = CaseInsensitiveDict()
    headers["accept"] = "application/json"
    headers["ApiKey"] = "{}".format(ombiApi_key)
    headers["Content-Type"] = "application/json"

    data = '{  "id": %ID}'.replace("%ID", str(ombiId))


    resp = requests.post(url, headers=headers, data=data)

    print(resp.status_code)




markAvailable(sys.argv[1], sys.argv[2], sys.argv[3])
