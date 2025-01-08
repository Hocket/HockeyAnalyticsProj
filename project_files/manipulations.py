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
    __slots__ = ["__url", "__filename", "__timestamp", "__dataframe"]
    def __init__(self, url, filename):
        self.__url = url
        self.__filename = filename
        if nap.ping():
            nap.saveToJSON(url, filename)
            self.__timestamp, self.__dataframe = cj.convertToDataframe(filename)
    
    def getTime(self):
        return self.__timestamp
    
    def getFilename(self):
        return self.__filename

    def getDataframe(self):
        return self.__dataframe


def main():
    """ manual test """
    table = Data(nap.getGoalieSvByStrength("limit=-1"), "test.json")
    print(table.getDataframe())

if __name__ == "__main__":
    main()