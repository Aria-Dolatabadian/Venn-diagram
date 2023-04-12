import geneview as gv
import matplotlib.pyplot as plt
table = {
    "Dataset 1": {"A", "B", "D", "E"},
    "Dataset 2": {"C", "F", "B", "G"},
    "Dataset 3": {"J", "C", "K"}
}
ax = gv.venn(table)
plt.show()
