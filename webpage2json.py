#! /usr/bin/env python3

''' Summarize webpage

    Read the webpage http://www-01.ibm.com/support/docview.wss?uid=nas4PSPbyNum,
    and create a shortened version of the table found there.

    Output is JSON containing a list of dictionaries, each dictionary
    containing entries for release, title, group, level, and updated date.
    Output is to stdout, so that it can be fed into another program, or
    saved to a file. The JSON is formatted for easy (human) reading.
'''

import sys
import requests
import json
from bs4 import BeautifulSoup

if len( sys.argv ) > 1:  # If provided, accept a file on the command line.
    with open( sys.argv[ 1 ], "r" ) as f:
        text = f.read()
    # Parse and break down the HTML found on the page
    soup = BeautifulSoup( text, features="lxml" )
else:
    # retrieve the web page
    page = requests.get( "http://www-01.ibm.com/support/docview.wss?uid=nas4PSPbyNum" )
    if page.status_code != 200:
        print("Could not fetch webpage. Status code = {}".format(page.status_code))
        exit(1)
    # Parse and break down the HTML found on the page
    soup = BeautifulSoup( page.text, features="lxml" )

# Find the division which contains the table.
div = soup.find_all("div", { "class" : "dblue-table-container" } )

table = div[0].find_all( "tr" )
collected = list()
for trow in table:
    if len(trow) > 0:
        tdr = trow.find_all("td")
        if len(tdr) > 0:
            row = dict()
            row["release"] = tdr[0].text
            row["title"] = tdr[1].text
            row["group"] = tdr[2].text
            row["level"] = tdr[3].text
            row["updated"] = tdr[4].text
            collected.append(row)

print(json.dumps(collected, indent=2))
