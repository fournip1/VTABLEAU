#!/usr/bin/env python

from gimpfu import *
from pdf2image import convert_from_path
import os
import tempfile
from datetime import datetime



def exportdoc(timg,tdrawable,tstring):
    # chemin du repertoire utilise pour l'export:
    directory = "/home/lechat/Nextcloud/CPGE/Documents_divers/archive_tableau/"
    
    # on duplique l'image pour applatir puis on sauve puis on efface l'image cree
    now = datetime.now()
    filename = directory + tstring + format(now.year,'04d') + format(now.month,'02d') + format(now.day,'02d') + "_" + format(now.hour,'02d') + format(now.minute,'02d') + format(now.second,'02d') + ".pdf"
    
    new_image = pdb.gimp_image_duplicate(timg)
    layer = pdb.gimp_image_merge_visible_layers(new_image, CLIP_TO_IMAGE)
    pdb.file_pdf_save(new_image, layer, filename, filename, 0, 0, 0)
    pdb.gimp_image_delete(new_image)
        
    
    
register(
        "python_fu_exporter",
        "Exporter PDF",
        "Exporter PDF",
        "PAF Fournie",
        "PAF Fournie",
        "2020",
        "<Image>/File/_Exporter le pdf...",
        "RGB*, GRAY*",
        [(PF_STRING, "string", "Prefixe fichier", "tableau_")],
        [],
        exportdoc)
main()
