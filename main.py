import matplotlib.pyplot as plt
import squarify
import math
from matplotlib.gridspec import GridSpec



def main():
    # Sample data
    labels = ['Amis\n(1774594)', 'Atayal\n(892089)', 'Bunun\n(155330)', 'Kanakanavu\n(48463)', 'Kavalan\n(74295)', 'Paiwan\n(193519)', 
              'Puyuma\n(125494)', 'Rukai\n(146324)', 'Saaroa\n(26758)', 'Saisiyat\n(55910)', 'Sakizaya\n(423935)', 'Seediq\n(1317978)', 
              'Taroko\n(41574)', 'Thao\n(53362)', 'Tsou\n(25238)', 'Yami\n(47093)']
    sizes = [1774594, 892089, 155330, 48463, 74295, 193519, 125494, 146324, 26758, 55910, 423935, 1317978, 41574, 53362, 25238, 47093]    
    sizes = [math.sqrt(x) for x in sizes]
    # Normalize the sizes to sum up to 1
    sizes_normalized = squarify.normalize_sizes(sizes, 10, 20)

    color_palette = [
    '#1f77b4',  # Teal
    '#ff7f0e',  # Orange
    '#2ca02c',  # Green
    '#d62728',  # Red
    '#9467bd',  # Purple
    '#8c564b',  # Brown
    '#e377c2',  # Pink
    '#7f7f7f',  # Gray
    '#bcbd22',  # Olive
    '#17becf',  # Cyan
    '#e41a1c',  # Magenta
    '#ffcc00',  # Yellow
    '#2bcbba',  # Light Green
    '#393b79',  # Dark Blue
    '#9edae5',  # Light Purple
    '#8c6d31',  # Dark Red
    ]
    
    # # Plot the treemap
    plt.figure(figsize=(10, 11))

    plot1 = plt.subplot2grid((10, 11), (0, 4), colspan=7, rowspan=8)
    plot2 = plt.subplot2grid((10, 11), (0, 0), colspan=4, rowspan=3)
    plot3 = plt.subplot2grid((10, 11), (3, 0), colspan=4, rowspan=3)
    plot4 = plt.subplot2grid((10, 11), (6, 0), colspan=4, rowspan=2)

    plot1.axis('off')
    plot1.set_title('Words scraped per Formosan language (5401956 total)')
    squarify.plot(sizes=sizes_normalized, label=labels, color=color_palette, alpha=.8, ax=plot1)

    plot2.set_title('Francis & Kucera Corpus')
    plot2.axis('off')
    squarify.plot(sizes=[1], label=['~ 1 Million Words'], alpha=.8, ax=plot2)

    plot3.set_title('Penn Treebank - WSJ section')
    plot3.axis('off')
    squarify.plot(sizes=[1], label=['~ 1 Million Words'], alpha=.8, ax=plot3)

    plot4.set_title('Adam, Eve, and Sarah Corpus')
    plot4.axis('off')
    squarify.plot(sizes=[1], label=['672,429 Words'], alpha=.8, ax=plot4)


    plt.tight_layout()
    plt.savefig("Treemap.png")
    plt.show()



   

if __name__ == "__main__":
    main()