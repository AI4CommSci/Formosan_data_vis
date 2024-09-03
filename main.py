import matplotlib.pyplot as plt
import squarify
import math
from matplotlib.gridspec import GridSpec



def main():
    # Sample data
    labels = ['Amis\n(1785997)', 'Atayal\n(899827)', 'Bunun\n(133907)', 'Kanakanavu\n(64961)', 'Kavalan\n(87461)', 'Paiwan\n(200714)', 
              'Puyuma\n(133483)', 'Rukai\n(152891)', 'Saaroa\n(31443)', 'Saisiyat\n(64442)', 'Sakizaya\n(456174)', 'Seediq\n(1324932)', 
              'Taroko\n(45444)', 'Thao\n(62030)', 'Tsou\n(44438)', 'Yami\n(59723)']
    sizes = [1785997, 899827, 133907, 64961, 87461, 200714, 133483, 152891, 31443, 64442, 456174, 1324932, 45444, 62030, 44438, 59723]    
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

    plot1 = plt.subplot2grid((10, 12), (0, 4), colspan=8, rowspan=8)
    plot2 = plt.subplot2grid((10, 12), (0, 0), colspan=4, rowspan=3)
    plot3 = plt.subplot2grid((10, 12), (3, 0), colspan=4, rowspan=3)
    plot4 = plt.subplot2grid((10, 12), (6, 0), colspan=4, rowspan=2)

    plot1.axis('off')
    plot1.set_title('Words scraped per Formosan language (5547867 total)', fontsize=16)
    squarify.plot(sizes=sizes_normalized, label=labels, color=color_palette, alpha=.8, ax=plot1, text_kwargs={'fontsize': 14})

    plot2.set_title('Francis & Kucera Corpus', fontsize=16)
    plot2.axis('off')
    squarify.plot(sizes=[1], label=['~ 1 Million Words'], alpha=.8, ax=plot2, text_kwargs={'fontsize': 14})

    plot3.set_title('Penn Treebank - WSJ section', fontsize=16)
    plot3.axis('off')
    squarify.plot(sizes=[1], label=['~ 1 Million Words'], alpha=.8, ax=plot3, text_kwargs={'fontsize': 14})

    plot4.set_title('Adam, Eve, and Sarah Corpus', fontsize=16)
    plot4.axis('off')
    squarify.plot(sizes=[1], label=['672,429 Words'], alpha=.8, ax=plot4, text_kwargs={'fontsize': 14})


    plt.tight_layout()
    plt.savefig("Treemap.png")
    plt.show()



   

if __name__ == "__main__":
    main()