from astropy.io import fits
from specutils import Spectrum1D
from astropy.visualization import quantity_support
import matplotlib.pyplot as plt

file = fits.open('data/ganymede.fits')
print(file.info())

header = file[0].header
print(header[:5])

spectra = Spectrum1D.read(file)
spectra

quantity_support()
fig, ax = plt.subplots()
plt.title("1D Spectra Visualization of Ganymede")
ax.step(spectra.spectral_axis, spectra.flux)