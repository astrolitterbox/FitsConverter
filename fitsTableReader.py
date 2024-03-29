import pyfits
import numpy as np

def readFitsTable(filename):
	hdulist = pyfits.open(filename)
	print hdulist.info()
	tbdata = hdulist[1].data
	prihdr = hdulist[1].header
	
	return tbdata

def writeFitsTable(columnNames, data, formats, outputFilename):
	colObjects = []
	print type(data), data
	for col in range(0, len(columnNames)):
		print col, type(data)
		colObjects.append(pyfits.Column(name=columnNames[col], format=formats[col], array=data[:, col]))
	tbhdu = pyfits.new_table(pyfits.ColDefs(colObjects))
	hdu = pyfits.PrimaryHDU()
	thdulist = pyfits.HDUList([hdu, tbhdu])
	thdulist.writeto(outputFilename, clobber=True)	
	
