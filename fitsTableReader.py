import pyfits

def readInputFile(filename):
	hdulist = pyfits.open(filename)
	#print hdulist.info()
	tbdata = hdulist[1].data
	#prihdr = hdulist[1].header
	#fields = prihdr.keys()
	#print fields
	return tbdata



tbdata = readInputFile('sdss_supersample.fits')
print tbdata[0]
