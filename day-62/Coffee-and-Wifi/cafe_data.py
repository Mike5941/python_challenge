import pandas as pd
from pprint import pprint


def add_newline(form):
    new_data = pd.DataFrame({
        "Cafe Name": form.cafe_name.data,
        "Location": form.location.data,
        "Open": form.opening_time.data,
        "Close": form.closing_time.data,
        "Coffee": form.coffee_rating.data,
        "Wifi": form.wifi_strength.data,
        "Power": form.power_availability.data,
    }, index=[0])
    new_data.to_csv('day-62/Coffee-and-Wifi/cafe.csv',
                    mode='a', index=False, header=False)


def update_list():
    cafe_data = pd.read_csv(
        "/Users/wonsoong/Library/Mobile Documents/com~apple~CloudDocs/PycharmProjects/day-62/Coffee-and-Wifi/cafe.csv")

    cafe_graph = cafe_data.style \
        .format(formatter={"Location": '<a href="{0}">Maps Link</a>'}, na_rep=None, escape="html") \
        .hide(axis="index") \
        .to_html()

    return cafe_graph
