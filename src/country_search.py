'''
Product:Country search feature
Description: will display the number of shows that are from the searched country.
Author: Seasickcake
'''
import csv

print ("This program will display the number of netflix titles from X country.")
answer = input("Name of the county you wish to search?")

count  = 0
with open('data\\netflix_titles.csv' , encoding="utf8") as csv_file:
    reader = csv.DictReader(csv_file)
    for i,row in enumerate(reader):
        if (row['country']==answer) :
            count = count + 1
        if(i >= 8806):
            print ("There are",count, "netflix titles that are from the",answer)
            break