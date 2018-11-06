#!/usr/bin/env python
# Name: Quincy van Iersel
# Student number: 12475998
"""
This script visualizes data obtained from a .csv file
"""

import csv
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

# Global constants for the input file, first and last year
INPUT_CSV = "movies.csv"
list_year = []
list_rating = []
list_title = []
list_tot_year = []
list_tot_rating = []
list_avr = []
dict = {}
dict2 = {}
with open('movies.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['Year']:
            x = row['Year']
            y = row['Rating']
            z = row['Title']
            list_tot_year.append(int(x))
            list_tot_rating.append(float(y))
            # append year, rating and title to seperate lists
            if not int(x) in list_year:
                list_year.append(int(x))
                list_rating.append(float(y))
                list_title.append(z)
            # if the year is in the dict
            if row['Year'] in dict:
                dict[row['Year']].append(float(y))
            # if the year is not in the dict
            elif not row['Year'] in dict:
                dict[row['Year']] = [float(y)]

# formula to calculate the average top movies from each year
average = sum(list_rating)/ float(len(list_rating))
# formula to calculate the total average rating of all movies
average_tot = sum(list_tot_rating) / float(len(list_tot_rating))

# Global dictionary for the data
for key in dict:
    # takes the average ratings from each year and put it in a second dict
    dict2[key] = sum(dict[key]) / len(dict[key])
    list_avr.append(dict2[key])

if __name__ == "__main__":


    # block chart that shows the average rating of the combined movies per year
    plt.title('Average combined movie ratings per year')
    plt.xlabel('Year')
    plt.ylabel('Rating')
    plt.bar(list_year, list_avr)
    plt.axis([2007, 2018, 7,  10])
    plt.xticks(list_year)
    red_patch = mpatches.Patch(color='red', label='Average Rating')
    plt.legend(handles=[red_patch])
    # sets a line of average rating from all movies
    plt.axhline(y = average_tot, color='red')
    plt.show()

    # block chart that shows the best movie rating from every year
    plt.title('Graph from the best movies from every year')
    plt.xlabel('Year')
    plt.ylabel('Rating')
    plt.bar(list_year, list_rating)
    plt.axis([2007, 2018, 7,  10])
    plt.xticks(list_year)
    red_patch = mpatches.Patch(color='red', label='Average Rating')
    plt.legend(handles=[red_patch])
    # sets a line of average rating from all movies
    plt.axhline(y = average, color='red')
    plt.show()
    
    # arctest that shows the average rating of the combined movies per year
    l = plt.plot(list_year, list_avr, 'ro')
    plt.xlabel('Year')
    plt.ylabel('Rating')
    plt.title('Average combined movie ratings per year')
    plt.setp(l, markersize=5)
    plt.setp(l, markerfacecolor='C0')
    plt.axis([2007, 2018, 7.5,  9.5])
    red_patch = mpatches.Patch(color='red', label='Average Rating')
    plt.legend(handles=[red_patch])
    # sets a line of average rating from all movies
    plt.axhline(y = average_tot, color='red', label = 'Average Rating')
    plt.show()
