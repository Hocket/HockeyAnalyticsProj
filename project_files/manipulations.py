"""
Manipulates pandas dataframes
Alex Poyer
"""
# import libraries
import pandas
import numpy

# import modules
import convert_json as cj
import NHLAPIpuller as nap

class Data():
    """ for creation and manipulation of pandas datatables """
    def __init__(self, url, filename):
        self.url = url
        if nap.ping():
            nap.saveToJSON(url, filename)
            self.timestamp, self.dataframe = cj.convertToDataframe(filename)
    


def main():
    """ manual test """
    table = Data(nap.getGoalieSvByStrength("limit=-1"), "test.json")
    print(table.dataframe)

if __name__ == "__main__":
    main()