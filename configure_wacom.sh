#!/bin/bash

# connaitre la liste des bouttons
# xsetwacom -s get "Wacom Intuos3 6x11 Pad pad" all

# connaire les ecrans
# xrandr

################
# config ecran #
################

xsetwacom set "Wacom Intuos3 6x11 Pad pad" MapToOutput VGA-1
xsetwacom set "Wacom Intuos3 6x11 Pen stylus" MapToOutput VGA-1
xsetwacom set "Wacom Intuos3 6x11 Pen eraser" MapToOutput VGA-1
xsetwacom set "Wacom Intuos3 6x11 Pen cursor" MapToOutput VGA-1


###################
# config bouttons #
###################

# gauche #

#####
# #1#
#3###
# #2#
#####
# 8 #
#####

xsetwacom set "Wacom Intuos3 6x11 Pad pad" Button 1 "Key ctrl alt r" # recharger doc (macro python perso)
xsetwacom set "Wacom Intuos3 6x11 Pad pad" Button 2 "Key ctrl alt e" # export png (macro python perso)
xsetwacom set "Wacom Intuos3 6x11 Pad pad" Button 3 "Key ctrl z" # annuler
xsetwacom set "Wacom Intuos3 6x11 Pad pad" Button 8 "Key ctrl alt p" # exporter le tableau
xsetwacom set "Wacom Intuos3 6x11 Pad pad" StripLeftDown "Key minus" # zoom out
xsetwacom set "Wacom Intuos3 6x11 Pad pad" StripLeftUp "Key shift plus" # zoom in


# droite #

#######
#9 #  #
####11#
#10#  #
#######
# 12  #
#######


xsetwacom set "Wacom Intuos3 6x11 Pad pad" Button 9 "Key N" # outil crayon
xsetwacom set "Wacom Intuos3 6x11 Pad pad" Button 10 "Key ctrl alt s" # outil palette
xsetwacom set "Wacom Intuos3 6x11 Pad pad" Button 11 "Key r" # selection retangulaire
xsetwacom set "Wacom Intuos3 6x11 Pad pad" Button 12 "Key ctrl A" # selectionner tout
