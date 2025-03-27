from astropy.io import fits
from specutils import Spectrum1D
from astropy.visualization import quantity_support
import matplotlib.pyplot as plt

file = fits.open('data/ganymede.fits')
print(file.info())