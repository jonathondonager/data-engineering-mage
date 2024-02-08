if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    """
    print(data.shape[0])
    data = data.query('passenger_count > 0 & trip_distance > 0')
    print(data.shape[0])

    # print(data.dtypes)
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date
    # print(data.dtypes)

    data.columns = (data.columns
                    .str.replace(' ','_')
                    .str.lower()
                    )

    return data

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    #assert output is not None, 'The output is undefined'
    assert len(output) > 1

@test
def test_output(output, *args) -> None:
    count = output['passenger_count'].isin([0]).sum()
    assert count == 0

@test
def test_output(output, *args) -> None:
    count = output['trip_distance'].isin([0]).sum()
    assert count == 0

@test
def test_output(output, *args) -> None:
    """
    """
    #assert output is not None, 'The output is undefined'
    assert len(output) > 1

@test
def test_output(output, *args) -> None:
    """
    """
    #assert output is not None, 'The output is undefined'
    assert output['lpep_pickup_date'].dtype != 'datetime64'

@test
def test_output(output, *args) -> None:
    """
    """
    assert " " not in ''.join(output.columns) 

@test
def test_output(output, *args) -> None:
    """
    """
    assert "vendorid" in output.columns