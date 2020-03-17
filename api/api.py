import csv
import codecs
import requests
import time
import os
import pandas as pd

from contextlib import closing

from local import *

ABUSE_API = "https://www.bitcoinabuse.com/api"


def download_abuse_database(time_period='forever'):
    """
    Downloads the latest versions of the Bitcoinabuse databases
    :param time_period: 1d, 30d or forever
    :return:
    """
    abuse_url = f"{ABUSE_API}/download/{time_period}?api_token={ABUSE_API_TOKEN}"

    with closing(requests.get(abuse_url, stream=True)) as r:
        reader = csv.reader(codecs.iterdecode(r.iter_lines(), 'utf-8'), delimiter=',', quotechar='"', escapechar='\\')
        column_list = next(reader)
        abuse_db = list()
        for row in reader:
            abuse_db.append(row)
        abuse_db_pd = pd.DataFrame(data=abuse_db, columns=column_list)
    abuse_db_pd.to_pickle(f"../databases/{time.strftime('%Y%m%d')}-time-period-{time_period}")
    return True


def check_abuse_address(address):
    """
    Checks for a given Bitcoin address whether reports exists in the Bitcoinabuse database.
    :param address: The address to check
    :return: bool
    """
    res = requests.get(f"{ABUSE_API}/reports/check?address={address}&api_token={ABUSE_API_TOKEN}")
    return res.json()['count'] > 0


def open_abuse_database(time_period='forever'):
    """
    Open the databases of today
    :param time_period: 1d, 30d or forever
    :return:
    """
    if not os.path.exists(f"../databases/{time.strftime('%Y%m%d')}-time-period-{time_period}"):
        download_abuse_database(time_period)

    return pd.read_pickle(f"../databases/{time.strftime('%Y%m%d')}-time-period-{time_period}")


def main():
    data_frame = open_abuse_database()

    # All unqiue addresses in database
    print(len(data_frame.address.unique()))


if __name__ == "__main__":
    main()
