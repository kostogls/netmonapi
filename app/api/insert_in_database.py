import csv
from ..api.db_connection import connect_db
import pandas as pd
import sys

PATH_1 = 'https://raw.githubusercontent.com/sermpezis/ai4netmon/main/data/aggregate_data/asn_aggregate_data_20220720.csv'
PATH_2 = '../project_files/data/precalculated_bias.csv'
PATH_3 = '../project_files/data/ripe_ris_extension/data/diff_in_bias_Atlas.csv'
PATH_4 = '../project_files/data/ripe_ris_extension/data/diff_in_bias_RIS.csv'


def db_insertion(path):
    db = connect_db()
    # db.biasdiff.drop()

    agg_df = pd.read_csv(path, header=0, index_col=0)

    header = list(agg_df)
    # print(header)
    csvfile = open(path, 'r')
    reader = csv.DictReader(csvfile)

    for each in reader:
        row = {}
        for field in header:
            row[field] = each[field]

        print(row)
        db.biasdiff.insert_one(row)


# db_insertion(PATH_4)