#!/usr/bin/env python


import math
from gimpfu import *

def changercouleur(timg, tdrawable):
    foreground = pdb.gimp_context_get_foreground()
    num_colors, colors = pdb.gimp_palette_get_colors("Feutres")
    i=0
    while i<num_colors and (colors[i][0]!= foreground[0] or colors[i][1]!= foreground[1] or colors[i][2]!= foreground[2] or colors[i][3]!= foreground[3]):
        i+=1
    i=(i+1)%num_colors
    pdb.gimp_context_set_foreground(colors[i])
    
register(
        "python_fu_changer",
        "Sauter couleur",
        "Sauter couleur",
        "PAF Fournie",
        "PAF Fournie",
        "2020",
        "<Image>/Colors/_Sauter...",
        "RGB*, GRAY*",
        [],
        [],
        changercouleur)

main()
