"""
converts json file into a pandas dataframe
author: Alex Poyer
"""
import pandas as pd
import json

def printFull(x):
    """ prints full dataframe cols&rows"""
    pd.set_option('display.max_columns', None)  # or 1000
    pd.set_option('display.max_rows', None)  # or 1000
    pd.set_option('display.max_colwidth', None)  # or 199
    print(x)
    pd.reset_option("display.max_rows")
    pd.reset_option('display.max_rows')
    pd.reset_option('display.max_colwidth')

def convertToDataframe(filename):
    """ 
    converts a json file to a pandas dataframe 
    returns timestamp and dataframe
    """
    try: # ADD EXCEPTION FOR JSON FORMATTED IN UNEXPECTED WAYS
        with open(filename) as json_file:
            json_data = json.load(json_file)
            timestamp = json_data["Timestamp"]
            dataframe = pd.DataFrame(json_data['data'])
            return timestamp, dataframe
    except FileNotFoundError:
        print("File does not exist")
        return

def main():
    """ manual test """
    timestamp, dataframe = convertToDataframe("json_files/GoalieSummary.json")
    print("Timestamp:",timestamp)
    print(dataframe)
    df_sorted = dataframe.sort_values(by=['goalsAgainst', 'losses', 'wins'], ascending=False)
    print(df_sorted)

if __name__ == "__main__":
    main()  