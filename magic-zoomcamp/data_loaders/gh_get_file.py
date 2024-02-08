import io
import pandas as pd
import requests
import gzip
from github import Github

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

url_list = [
    "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-10.csv.gz",
    "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-11.csv.gz",
    "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-12.csv.gz"
]
token = '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'

@data_loader
def load_data_from_api(url_list=url_list, token = token, *args, **kwargs):
    """
    Template for loading data from API
    """
    
    g = Github(token)

    repo = g.get_repo('DataTalksClub/nyc-tlc-data')

    contents = repo.get_contents('green_tripdata_2020-10.csv.gz')

    decoded = contents.decoded_content

    # with open('green_tripdata_2020-10.csv.gz', 'wb') as f:
    #     f.write(decoded)
    
    with gzip.open('green_tripdata_2020-10.csv.gz', 'rb') as f:
        file_content = f.read()

    print(file_content)
    # return pd.read_csv(io.StringIO(response.text), sep=',')


# @test
# def test_output(output, *args) -> None:
#     """
#     Template code for testing the output of the block.
#     """
#     assert output is not None, 'The output is undefined'
