#! /usr/bin/env python

# from ROOT import RooFit as rf
# from ROOT import *
# import ROOT as r
import sys
import os
# import glob
import math
# import datetime
# import numpy as np
# from array import array
# import re
# import matplotlib as ml
# import matplotlib.pyplot as plt
# from PIL import Image

# R.gSystem.Load('libRooFit')


def read_tubs():
    finname = 'beamtest2017B-tubs.tsv'
    fin = open( finname )
    out = []
    for line in fin:
        if len( line ) < 3:
            continue
        if '#' == line[0]:
            continue
        lin = line.rstrip( '\n' ).rstrip( '\r' ).split( '\t' )
        if lin[3] == '':
            continue
        x = {}
        try:
            x['name'] = lin[9]
            x['rin'] = float( lin[1] )
            x['rout'] = float( lin[2] )
            x['length'] = float( lin[4] )
            x['material'] = lin[5]
            x['zcentre'] = float( lin[6] )
            x['zupstream'] = float( lin[7] )
            x['zdownstream'] = float( lin[8] )
            out.append( x )
        except ValueError:
            print 'ERROR'
            print lin
    return out


def main():
    tubs = read_tubs()
    # print tubs
    for tub in tubs:
        print """G4VSolid* {name}_solid = new G4Tubs("{name}", {rin}, {rout}, {length}, 0., 360.*degree);""".format(
                name = tub['name'], rin = tub['rin'], rout = tub['rout'], length=tub['length'] )
        print """{name}_logic = new G4LogicalVolume({name}_solid, {mat}, "{name}");""".format(
                name = tub['name'], mat = tub['material'] )
        print


if __name__ == '__main__':
    main()