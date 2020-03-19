import csv
import codecs
import requests
import time
import os
import pandas as pd

from contextlib import closing

from local import *

ABUSE_API = "https://www.bitcoinabuse.com/api"


# See: https://www.bitcoinabuse.com/api-docs

def download_abuse_database(time_period='forever'):
    """
    Downloads the latest versions of the Bitcoinabuse databases
    Returns a CSV file containing all reports within the given time period.
    The "1d" file is updated daily in the early morning.
    The "30d" file is updated weekly on Sunday morning.
    The "forever" file is updated monthly on the 15th of the month.
    All updates occur between 2am-3am UTC.
    :param time_period: 1d, 30d or forever
    :return: bool
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
    This report is cached and only updates once per hour.
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


def get_abuse_types():
    """
    Get the list of known abuse types in the Bitcoinabuse database
    :return:
    """
    res = requests.get(f"{ABUSE_API}/abuse-types?api_token={ABUSE_API_TOKEN}")
    return res.json()


def get_distinct_reports(page=1, reverse='false'):
    """
    This report is cached and only updates once per hour.
    :param page: Integer great than or equal to 1.
    :param reverse: Reverse the order so oldest reports are first.
    :return:
    """
    res = requests.get(f"{ABUSE_API}/reports/distinct?api_token={ABUSE_API_TOKEN}&page={page}&reverse={reverse}")
    return res.json()


def report_address(address, abuse_type_id, abuse_type_other=None, abuser=None, description=None):
    """
    The Report Address API allows you to report bitcoin addresses automatically.
    :param address: Required
    :param abuse_type_id: Required. Integer.
    :param abuse_type_other: Required if abuse_type_id is 99 (other).
    :param abuser:
    :param description:
    :return: bool
    """
    if abuse_type_id not in get_abuse_types():
        raise ValueError("Unknown abuse type")
    elif abuse_type_id == 99 and not abuse_type_other:
        raise ValueError("Abuse type other is required when type is 99")
    report_data = {
        'api_token': ABUSE_API_TOKEN,
        'address': address,
        'abuse_type_id': abuse_type_id,
        'abuse_type_other': abuse_type_other,
        'abuser': abuser,
        'description': description,
    }
    requests.post(f"{ABUSE_API}/reports/create", data=report_data)

    return True


def main():
    data_frame = open_abuse_database()

    # All unique addresses in database
    print(len(data_frame.address.unique()))
    print(get_abuse_types())


if __name__ == "__main__":
    main()
