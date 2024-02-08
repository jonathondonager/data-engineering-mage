import io
import pandas as pd
import requests
import gzip
from github import Github

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@data_loader
def load_data(*args, **kwargs):
    """
    Template code for loading data from any source.

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """

    taxi_dtypes = {
        'VendorID': pd.Int64Dtype(),
        'passenger_count': pd.Int64Dtype(),
        'trip_distance': float,
        'RatecodeID': pd.Int64Dtype(),
        'store_and_fwd_flag': str,
        'PULocationID': pd.Int64Dtype(),
        'DOLocationID': pd.Int64Dtype(),
        'payment_type': pd.Int64Dtype(),
        'fare_amount': float,
        'extra': float,
        'mta_tax': float,
        'tip_amount': float,
        'tolls_amount': float,
        'improvement_surcharge': float,
        'total_amount': float,
        'congestion_surcharge': float
    }

    parse_dates = ['tpep_pickup_datetime','tpep_dropoff_datetime']
  
    # url_list = [
    #     "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-10.csv.gz",
    #     "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-11.csv.gz",
    #     "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-12.csv.gz"
    #     ]

    # df_list = []
    # for url in url_list:
    #     print(url)
    #     df = pd.read_csv(url) #, sep=",",compression="gzip",dtype=taxi_dtypes,parse_dates=parse_dates)
    #     df_list.append(df)

    url_list = [
        "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2020-10.parquet",
        "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2020-11.parquet",
        "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2020-12.parquet"
        ]
    
    df_list = []
    for url in url_list:
        print(url)
        df = pd.read_parquet(url) #, sep=",",compression="gzip",dtype=taxi_dtypes,parse_dates=parse_dates)
        df_list.append(df)

    df = pd.concat(df_list)
    
    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
