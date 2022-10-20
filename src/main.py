'''
Product:
Description:
Author:
'''
from databaseImporter import csvImport
import pandas as pd
import matplotlib

class Solution():
    def __init__(self):
        inst = csvImport()
        df = inst.import_database()
            
        
if __name__ == "__main__":
    obj = Solution()
    