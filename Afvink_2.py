from Bio import Entrez
import numpy as np
import matplotlib.pyplot as plt



def get_counts(term, vanaf, tot):
    Entrez.email = "JD.Versantvoort@student.han.nl"

    handle = Entrez.esearch(db="pubmed", term=term, mindate=vanaf,
                            maxdate=tot)
    record = Entrez.read(handle)
    handle.close()
    return record["Count"]


def get_lijst_aantallen(term):
    aantallen = []
    jaren = []
    for i in range(1971, 2025, 5):
        aantal = get_counts(term, i, i + 4)
        aantallen.append(aantal)
        jaren.append(str(i)[-2:] + "-" + str(i + 4)[-2:])

    return aantallen, jaren


def matplotlib(hoogtes, bars):
    # Create dataset
    x_pos = np.arange(len(bars))

    # Create bars
    plt.bar(x_pos, hoogtes)

    # Create names on the x-axis
    plt.xticks(x_pos, bars)

    # Show graphic
    plt.show()

def matplotlib2(hoogtes1, hoogtes2, labels, naam1, naam2):


    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, hoogtes1, width, label=naam1)
    rects2 = ax.bar(x + width / 2, hoogtes2, width, label=naam2)

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Counts')
    ax.set_title('Counts van '+naam1+" "+naam2)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    # ax.bar_label(rects1, padding=3)
    # ax.bar_label(rects2, padding=3)

    fig.tight_layout()

    plt.show()


def main():
    aantallen1, lables = get_lijst_aantallen("toxin")
    aantallen2, lables = get_lijst_aantallen("heart")
    matplotlib2(aantallen1, aantallen2, lables, "toxin", "heart")


main()
