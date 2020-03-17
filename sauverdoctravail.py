#!/usr/bin/env python

from gimpfu import *
from pdf2image import convert_from_path
import os
import tempfile




def sauverdoc(timg,tdrawable):
    # chemin du fichier utilise pour l'export:
    filename = "/home/lechat/Nextcloud/CPGE/Documents_divers/tableau.png"
    # on duplique l'image pour applatir puis on sauve puis on efface l'image cree
            
    new_image = pdb.gimp_image_duplicate(timg)
    layer = pdb.gimp_image_merge_visible_layers(new_image, CLIP_TO_IMAGE)
    pdb.file_png_save(new_image, layer, filename, filename, 1, 9, 1, 0, 0, 1, 1)
    pdb.gimp_image_delete(new_image)
        
    
    
register(
        "python_fu_sauver",
        "Exporter tableau",
        "Exporter tableau",
        "PAF Fournie",
        "PAF Fournie",
        "2020",
        "<Image>/File/_Sauver le tableau...",
        "RGB*, GRAY*",
        [],
        [],
        sauverdoc)
main()
