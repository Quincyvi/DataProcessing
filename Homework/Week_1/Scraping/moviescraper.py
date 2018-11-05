#!/usr/bin/env python
# Name:
# Student number:
"""
This script scrapes IMDB and outputs a CSV file with highest rated movies.
"""

import csv
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

TARGET_URL = "https://www.imdb.com/search/title?title_type=feature&release_date=2008-01-01,2018-01-01&num_votes=5000,&sort=user_rating,desc"
BACKUP_HTML = 'movies.html'
OUTPUT_CSV = 'movies.csv'


def extract_movies(dom):
    """
    Extract a list of highest rated movies from DOM (of IMDB page).
    Each movie entry should contain the following fields:
    - Title
    - Rating
    - Year of release (only a number!)
    - Actors/actresses (comma separated if more than one)
    - Runtime (only a number!)
    """
    list_act = []
    list_tot = []
    # open the html file and read it
    with open("movies.html") as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    # read trough the lines of the file
    for line in soup.find_all(class_="lister-item-content"):
        for title in line.select('a[href*="?ref_=adv_li_tt"]'):
            newtitle = title.text.strip()
        c = line.find('span', class_="lister-item-year")
        year = c.text.strip('(), I')
        b = line.find('strong')
        rating = b.text.strip()
        for t in line.find_all('p', class_="text-muted "):
            tnew = t.find('span', class_="runtime")
            time = tnew.text.strip()
        times = time.strip('min')
        list_act = []
        for actors in line.select('a[href*="?ref_=adv_li_st"]'):
            # movie actors
            act = actors.text.strip()
            list_act.append(act)
        list = [newtitle, rating, year, list_act, times]
        list_tot.append(list)

    return list_tot


def save_csv(outfile, movies):
    """
    Output a CSV file containing highest rated movies.
    """
    writer = csv.writer(outfile)
    writer.writerow(['Title', 'Rating', 'Year', 'Actors', 'Runtime'])
    # for name in movies
    for line in movies:
        writer.writerow(line)

def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None
    except RequestException as e:
        print('The following error occurred during HTTP GET request to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns true if the response seems to be HTML, false otherwise
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


if __name__ == "__main__":

    # get HTML content at target URL
    html = simple_get(TARGET_URL)

    # save a copy to disk in the current directory, this serves as an backup
    # of the original HTML, will be used in grading.
    with open(BACKUP_HTML, 'wb') as f:
        f.write(html)

    # parse the HTML file into a DOM representation
    dom = BeautifulSoup(html, 'html.parser')

    # extract the movies (using the function you implemented)
    movies = extract_movies(dom)

    # write the CSV file to disk (including a header)
    with open(OUTPUT_CSV, 'w', newline='') as output_file:
        save_csv(output_file, movies)
