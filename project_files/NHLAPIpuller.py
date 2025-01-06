import requests
import json
from datetime import datetime

PING_URL = "https://api.nhle.com/stats/rest/ping"
SEASON_ID = 20242025 # 2024-25 season

def setDefault(url):
    if 'cayenneExp=' not in url: # default to globally defined season
        url += f'&cayenneExp=seasonId={SEASON_ID}'
    if requests.get(url) == 500:
        print("Invalid Parameters")
        return
    return url

    
"""
For API API queries parameters should be broken up by '&'
list of valid params:
    -isAggregate (query, boolean) - Optional
    -isGame (query, boolean) - Optional
    -factCayenneExp (query, string) - Optional
    -include (query, string) - Optional
    -exclude (query, string) - Optional
    -sort (query, string) - Optional
    -dir (query, string) - Optional
    -start (query, int) - Optional
    -limit (query, int) - Optional (Note: a limit of -1 will return all results)
    -cayenneExp (query, string) - Required
"""

def getGoalieSummary(params):
    """
    sortKeys:
        "wins",
        "savePct"
    -------------------
    example for summary sorted by wins:
    https://api.nhle.com/stats/rest/en/goalie/summary?limit=-1&sort=wins&cayenneExp=seasonId=20242025
    """
    baseURL = 'https://api.nhle.com/stats/rest/en/goalie/summary?'
    finalURL = baseURL + params
    return setDefault(finalURL)


def getGoalieSvByStrength(params):
    """
    sortKeys:
        "wins",
        "savePct"
    ---------------
    example for savesbystrenght sorted by savePct:
    https://api.nhle.com/stats/rest/en/goalie/savesByStrength?limit=-1&sort=savePct&cayenneExp=seasonId=20242025
    """
    baseURL = "https://api.nhle.com/stats/rest/en/goalie/savesByStrength?"
    finalURL = baseURL + params
    return setDefault(finalURL)


def saveToJSON(url, filename):
    """ dumps json from url to local file """
    timestamp = datetime.now().isoformat() + " ET"
    data = url.json()
    data = {"Timestamp":timestamp, **data}
    
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


def main():
    ping = requests.get(PING_URL)
    
    # return if fails to connect
    if ping.status_code != 200:
        print("Failed to connect to network")
        return
    
    """ CALLS FOR URL SEARCHES"""
    goal_summary = getGoalieSummary("limit=-1&sort=wins")
    goal_sv_by_str = getGoalieSvByStrength("limit=-1&sort=wins")

    goal_summary = requests.get(goal_summary)
    goal_sv_by_str = requests.get(goal_sv_by_str)
    saveToJSON(goal_summary, "json_files/GoalieSummary.json")
    saveToJSON(goal_sv_by_str, "json_files/GoalieSavesByStrength.json")

if __name__ == '__main__':
    main()
