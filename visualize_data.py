import pandas as pd
import matplotlib.pyplot as plt

def visualize_data(df):
    df.plot(kind='bar', x='Name', y='Value')
    plt.title('Data Visualization')
    plt.xlabel('Name')
    plt.ylabel('Value')
    plt.show()

if __name__ == '__main__':
    sample_data = [
        {'Name': 'Item1', 'Value': 1000},
        {'Name': 'Item2', 'Value': 2000}
    ]
    df = pd.DataFrame(sample_data)
    visualize_data(df)
