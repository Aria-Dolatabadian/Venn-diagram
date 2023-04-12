import matplotlib.pyplot as plt
import geneview as gv

dataset_dict = {'A': {6, 9, 10, 13, 18, 27, 28, 30, 31, 32, 38, 45, 47, 52, 53, 54, 56, 60, 62, 63, 64, 75, 76, 87, 89},
                'B': {1, 8, 10, 11, 17, 23, 24, 31, 43, 54, 56, 57, 60, 61, 64, 65, 71, 73, 78, 79, 80, 82, 90, 92, 93},
                'C': {0, 6, 8, 11, 16, 21, 24, 25, 27, 30, 35, 47, 49, 51, 61, 69, 77, 78, 84, 85, 91, 94, 95, 96, 99},
                'D': {0, 1, 4, 6, 7, 14, 20, 21, 29, 33, 35, 42, 46, 55, 59, 60, 62, 64, 66, 68, 76, 81, 83, 92, 95}
                }

print(dataset_dict)
petal_labels = gv.generate_petal_labels(dataset_dict.values(), fmt="{logic}\n({percentage:.1f}%)")
ax = gv.venn(data=petal_labels, names=list(dataset_dict.keys()), legend_use_petal_color=True)
plt.show()
