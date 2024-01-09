import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def read_csv(filename):
    df = pd.read_csv(filename, index_col=0)
    print(df)
    return df


def generate_histgram(datalist):
    fig, ax1 = plt.subplots()

    # plot histgram
    n, bins, patches = ax1.hist(datalist, label='Frequency')
    ax1.set_ylabel('Frequency')
    ax1.set_xlabel("Apple's weight [g]")

    # cumulative ratio
    cr_y = np.add.accumulate(n) / n.sum()
    cr_x = np.convolve(bins, np.ones(2) / 2, mode='same')[1:]

    # plot cumulative ratio
    ax2 = ax1.twinx()
    lines = ax2.plot(cr_x, cr_y, marker='o', color='red', ls='--')
    ax2.set_ylabel('Cumulative Ratio')
    ax2.set_ylim(0, 1.1)
    ax2.grid()

    plt.savefig('./matplotlib/hist.png')


def main():
    CSV_FILE = 'matplotlib/sample_data.csv'

    df = read_csv(CSV_FILE)
    df = df[df.columns.values[1]]
    generate_histgram(df)


if __name__ == '__main__':
    main()
