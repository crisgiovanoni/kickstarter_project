import pandas as pd


def get_kickstarter():
    df = pd.read_csv("/Users/cris/codeup-data-science/ds-methodologies-exercises/kickstarter_project/kickstarter.csv")
    return df

def clean_kickstarter():
    df = df[["name","category","subcategory","location","status","goal","funded percentage","backers","duration"]]
    df = df.location.fillna("Unknown, None", inplace=True)
    df = df[["city","state-country"]] = df["location"].str.split(',', n=1, expand=True)
    df = df.drop(["location"],axis=1)


# def split_test_train():

