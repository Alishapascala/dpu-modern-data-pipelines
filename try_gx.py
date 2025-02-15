import json

import pandas as pd


def _validate_data():
    columns = ["NewConfirmed", "Date"]
    df = pd.read_csv("data.csv", names=columns)

    valid_df = df[(df.NewConfirmed >= 0) & (df.NewConfirmed <= 322315)]
    dq = len(valid_df) / len(df)
    print(dq)

    assert len(valid_df) == len(df)


_validate_data()


def _validate_temperature_data():
    with open("weather_data_2024-02-03T04:00:00+00:00.json", "r") as f:
        data = json.load(f)
        print(data["main"])

        df = pd.DataFrame.from_records(data["main"], index=[0])
        print(df.head())

        dataset = PandasDataset(df)
        print(dataset.head())

        results = dataset.expect_column_values_to_be_between(
            column="temp",
            min_value=0,
            max_value=31,
        )
        print(results)


#_validate_temperature_data()