import numpy as np
from plantcv.plantcv.hyperspectral import extract_wavelength


def test_extract_wavelength(hyperspectral_test_data):
    new = extract_wavelength(spectral_data=hyperspectral_test_data.load_hsi(), wavelength=500)
    assert np.shape(new.array_data) == (1, 1600)
