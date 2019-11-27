import pandas as pd
import numpy as np


def get_kickstarter():
    df = pd.read_csv("/Users/cris/codeup-data-science/kickstarter_project/kickstarter.csv")
    return df

def recode_locations(kick):
    kick[["city","origin"]] = kick["location"].str.split(', ', n=1, expand=True)
    kick.origin.replace(to_replace="Argent",value="Argentina",inplace=True)
    kick.origin.replace(to_replace="Mt",value="MT",inplace=True)
    kick.origin.replace(to_replace="Dominican Re",value="Dominican Republic",inplace=True)
    kick.origin.replace(to_replace="Kyoto, Japan",value="Japan",inplace=True)
    kick.origin.replace(to_replace="Nakagyo Ward",value="Kyoto",inplace=True)
    kick.origin.replace(to_replace="Kamigyo Ward",value="Kyoto",inplace=True)
    kick.origin.replace(to_replace="Scotland, United Kingdom", value="Scotland", inplace=True)
    kick.origin.replace(to_replace="Middleburg, MD", value="MD", inplace=True)
    return kick
