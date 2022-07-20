import os
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import csv

# start scrapper
# https://github.com/DGGomez?tab=repositories

csv_file = "portfolio_breakdown.csv"

def git_check():
    portfolio = {}

    url = "https://github.com/DGGomez?tab=repositories"
    page = requests.get(url)
    if page.ok:
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find_all("li", itemprop="owns")

        # Add languages to list and github link to list
        for result in results:
            name = result.find("a")
            lang = result.find("span", itemprop="programmingLanguage")
            if lang:
                l = lang.text.strip()
                if l in portfolio:
                    portfolio[l].append(name["href"])
                else:
                    portfolio[l] = [name["href"]]

        # add up experience
        labels = portfolio.keys()
        sizes = []
        for i in labels:
            sizes.append(len(portfolio[i]))

        try:
            with open(csv_file, 'w') as csvfile:
                for key in portfolio.keys():
                    csvfile.write("%s,%s\n"%(key,portfolio[key]))
        except IOError:
            print("I/O error")

        # Plot
        plt.pie(sizes, labels=labels,
                autopct='%1.1f%%', shadow=True, startangle=140)
        plt.axis('equal')
        plt.show()

git_check()
