from bioinfokit import visuz
# 3-way Venn
visuz.venn(vennset=(3,6,10,4,2,5,4))
# note: order the set in (100,010,110,001,101,011,111) format
# 2-way venn
visuz.venn(vennset=(1,2,3))
# note: order the set in (111,100,010,001,110,101,011) format
# change default color
# check for more colors at https://www.webucator.com/blog/2015/03/python-color-constants-module/
visuz.venn(vennset=(300,600,402,470,200,230,408), vennlabel=("X", "Y", "Z"), venncolor=('#ff6347', '#008000', '#FF00FF'))
#See WD to find the results
