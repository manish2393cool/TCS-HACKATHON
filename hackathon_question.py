###                Hackathon for Machine Learning Engineer Program
###        Web Scrapping, Data Cleaning & Exploratory Analysis with Python

# In this challenge you will be scrapping the data related to cryptocurrencies,
# perform necessary data cleaning and build few visualization plots.

# NOTE: Use this link 'https://coinmarketcap.com/' as a reference to understand
# the page structure of html page used in this exercise. Both are similar.
# This reference is required for identifying required html tags for parsing the
# given web page and extracting the needed information

# Please complete the definition of following 9 functions, inorder to complete the exercise:
# 1. parse_html_page,
# 2. get_all_tr_elements,
# 3. convert_tr_elements_to_cryptodf,
# 4. transform_cryptodf,
# 5. draw_barplot_top10_cryptocurrencies_with_highest_market_value,
# 6. draw_scatterplot_trend_of_price_with_market_value
# 7. draw_scatterplot_trend_of_price_with_volum
# 8. draw_barplot_top10_cryptocurrencies_with_highest_positive_change
# 9. serialize_plot

# The above nine functions are used in 'main' function.
# The 'main' function parses an input html page, converts required info into pandas datarame,
# and draws two barplots and two scatter plots.

# Please look into definition of 'main' function, to understand inputs and exepcted outputs from above listed 9 functions.
# Also read the documention provided in each function to understand it's functionality.

## Importing python libraries, necessary for solving this exercise.
import requests
from requests import get
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import numpy as np
import re
import pickle


def parse_html_page(htmlpage):
    '''
    Parses the input 'htmlpage' using Beautiful Soup html parser and returns it.
    '''

    # write the functionality of 'parse_html_page' below.
    html = requests.get(htmlpage)

    #Convert the parsed page into beautifulsoup object
    html_soup = BeautifulSoup(html.content, 'html.parser')
    return html_soup

def get_all_tr_elements(soup_obj):
    '''
    Identifies all 'tr' elements, present in beautiful soup object, 'soup_obj', and returns them
    '''

    # write your functionality below


def convert_tr_elements_to_cryptodf(htmltable_rows):
    '''
    Extracts the text associated with seven columns of all records present in 'htmltable_rows' object.
    Builds a pandas dataframe and returns it.

    NOTE: Information in seven columns have to be stored in below initilaized lists.
    '''
    rank = []                    #List for rank of the currency (first column in the webpage)
    currency_name = []           #List for name of the currency
    market_cap = []              #List for market cap
    price = []                   #List for price of the crypto currency
    volume = []                  #List for Volume(24h)
    supply = []                  #List for Circulating supply
    change = []                  #List for Change(24h)

    # write your functionality below


    # Creating the pandas dataframe
    df = pd.DataFrame({
                         'rank' : rank,
                         'currency_name' : currency_name,
                         'market_cap' : market_cap,
                         'price' : price,
                         'volume' : volume,
                         'supply' : supply,
                         'change' : change
                         })

    # Returning the data frame.
    return df


def transform_cryptodf(cryptodf):
    '''
    Returns a modified dataframe.
    '''

    # Modify values of the columns : 'market_cap', 'price', 'volume', 'change', 'supply'.
    # Remove unwanted characters like dollar symbol ($), comma symbol (,) and
    # convert them into corresponding data type ie. int or float.

    # NOTE : After transformation, the first five rows of the transformed dataframe should be
    #       similar to data in 'expected_transformed_df.csv' file, present in project folder.

    # write your functionality below


def draw_barplot_top10_cryptocurrencies_with_highest_market_value(cryptocur_df):
    '''
    Returns barplot
    '''

    # Create a horizontal bar plot using seaborn showing
    # Top 10 Cryptocurrencies with highest Market Capital.
    # Order the cryptocurrencies in Descending order. i.e
    # bar corresponding to cryptocurrency with highest market value must be on top of bar plot.

    # Write the functionality below


def draw_scatterplot_trend_of_price_with_market_value(cryptocur_df):
    '''
    Returns a scatter plot
    '''

    # Create a scatter plot, using seaborn, showing trend of Price with Market Capital.
    # Consider 50 Cryptocurrencies, with higest Market Value for seeing the trend.
    # Set the plot size to 10 inches in width and 2 inches in height respectively.

    # Write the functionality below


def draw_scatterplot_trend_of_price_with_volume(cryptocur_df):
    '''
    Returns a scatter plot
    '''
    # Create a scatter plot, using seaborn, showing trend of Price with 24 hours Volume.
    # Consider all 100 Cryptocurrencies for seeing the trend.
    # Set the plot size to 10 inches in width and 2 inches in height respectively.

    # Write the functionality below



def draw_barplot_top10_cryptocurrencies_with_highest_positive_change(cryptocur_df):
    '''
    Returns a bar plot
    '''

    # Create a horizontal bar plot using seaborn showing
    # Top 10 Cryptocurrencies with positive change in last 24 hours.
    # Order the cryptocurrencies in Descending order. i.e
    # bar corresponding to cryptocurrency with highest positive change must be on top of bar plot.

    # Write the functionality below


def serialize_plot(plot, plot_dump_file):
    '''
    Dumps the 'plot' object in to 'plot_dump_file' using pickle.
    '''

    # Write the functionality below


def main():

    input_html = 'file:data/input_html/Cryptocurrency Market Capitalizations _ CoinMarketCap.html'

    html_soup = parse_html_page(input_html)

    # crypto_containers = get_all_tr_elements(html_soup)

    # crypto_df = convert_tr_elements_to_cryptodf(crypto_containers)

    # crypto_df = transform_cryptodf(crypto_df)

    # plot1 = draw_barplot_top10_cryptocurrencies_with_highest_market_value(crypto_df)

    # plot2 = draw_scatterplot_trend_of_price_with_market_value(crypto_df)

    # plot3 = draw_scatterplot_trend_of_price_with_volume(crypto_df)

    # plot4 = draw_barplot_top10_cryptocurrencies_with_highest_positive_change(crypto_df)

    # serialize_plot(plot1, "plot1.pk")

    # serialize_plot(plot2.axes, "plot2_axes.pk")

    # serialize_plot(plot2.data, "plot2_data.pk")

    # serialize_plot(plot3.axes, "plot3_axes.pk")

    # serialize_plot(plot3.data, "plot3_data.pk")

    # serialize_plot(plot4, "plot4.pk")


if __name__ == '__main__':
    main()
