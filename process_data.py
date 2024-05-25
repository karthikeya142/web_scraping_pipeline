import pandas as pd


def process_data(data):
    df = pd.DataFrame(data)

    # Example: Data cleaning and transformation
    df['Value'] = df['Value'].str.replace(',', '').astype(float)

    return df


if __name__ == '__main__':
    sample_data = [
        {'Name': 'Item1', 'Value': '1,000'},
        {'Name': 'Item2', 'Value': '2,000'}
    ]
    processed_df = process_data(sample_data)
    print(processed_df)
