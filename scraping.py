# DISCLAIMER: we don't believe in this bullcrap!!!

from bs4 import BeautifulSoup
from datetime import date, timedelta
from constants import *
import pandas as pd

url_base = "https://oroscopo.grazia.it/archivio/oroscopo-del-giorno"
# oroscopi_choices = ["oroscopo-del-giorno", "oroscopo-amore", "oroscopo-carriera"]


def date_creator():

    sdate = date(2008, 1, 1)
    edate = date(2022, 1, 1)

    date_ranges = pd.date_range(sdate, edate - timedelta(days=1), freq="d").to_frame(
        index=False, name="dates"
    )

    date_ranges.dates = pd.to_datetime(date_ranges.dates)
    date_ranges["new_dates"] = date_ranges["dates"].dt.strftime("%d-%m-%Y")
    return date_ranges["new_dates"].to_list()


dates = date_creator()
url_list = []
for date in dates:
    _, month, year = date.split("-")
    url_list.append(f"{url_base}/{MONTHS[month]}-{year}/{date}.html")
