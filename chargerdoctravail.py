#!/usr/bin/env python

from gimpfu import *
from pdf2image import convert_from_path
import os
import tempfile

##def chargerdoc():
##    filename = "/home/lechat/Bureau/test.pdf"
##    temp_dir = "/home/lechat/Bureau/Tmp"
##    images = convert_from_path(filename, output_folder=temp_dir)
##
##    for i in range(len(images)):
##        image_path = temp_dir+'/'+str(i)+'.jpg'
##        images[i].save(image_path, 'JPEG')
##
    
    
# chemin du fichier utilise pour l'import:
filename = "/home/lechat/Nextcloud/CPGE/Documents_divers/doc_travail.pdf"

def chargerdoc(timg,tdrawable):
    width = tdrawable.width
    height = tdrawable.height

    # on elimine tous les calques sauf celui des annotations
    for layer in timg.layers:
        if layer.name!="Annotations":
            timg.remove_layer(layer)

    
    img  = pdb.file_pdf_load(filename, "doc_travail.pdf")

    # on ajoute le calque correspondant au pdf qui vient d'etre recompile
    for layer in img.layers:
        pdb.gimp_edit_copy(layer)
        fsel = pdb.gimp_edit_paste(tdrawable, False)
        pdb.gimp_floating_sel_to_layer(fsel)
        timg.active_layer.name = "doc_travail"

    # on reactive le calque avec les annotations
    for layer in timg.layers:
        if layer.name=="Annotations":
            timg.active_layer = layer
        
    pdb.script_fu_reverse_layers(timg, tdrawable)
    gimp.delete(img)

register(
        "python_fu_charger",
        "Recharger image pdf",
        "Recharger image pdf",
        "PAF Fournie",
        "PAF Fournie",
        "2020",
        "<Image>/File/_Recharger le PDF...",
        "RGB*, GRAY*",
        #[  (PF_FILE, "pages", "PDF", "")],
        [],
        [],
        chargerdoc)
main()
