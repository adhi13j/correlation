import numpy as np
from numpy.core.numeric import correlate
import plotly.express as px
import csv
def get_dataSorce(data_path):
    ice_cream_sales = []
    cold_drink_sales = []
    with open(data_path) as csv_file :
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader :
            ice_cream_sales.append(float(row["Temperature"]))
            cold_drink_sales.append(float(row["Ice-cream Sales"]))
    return{"x":ice_cream_sales,"y":cold_drink_sales}

def find_Correlation (datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print("corralation btw temp & ice cream sales 🍧",correlation[0,1])

def setup():
    data_path = "icecream.csv"
    datasource = get_dataSorce(data_path)
    find_Correlation(datasource)

setup()