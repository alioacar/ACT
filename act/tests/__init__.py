"""
This module contains sample files used for testing the ARM Community Toolkit.
Files in this module should only be used for testing, not production.

"""

from .sample_files import (
    EXAMPLE_AERI,
    EXAMPLE_ANL_CSV,
    EXAMPLE_AOSMET,
    EXAMPLE_BRS,
    EXAMPLE_CEIL1,
    EXAMPLE_CEIL_WILDCARD,
    EXAMPLE_CO2FLX4M,
    EXAMPLE_DLPPI,
    EXAMPLE_EBBR1,
    EXAMPLE_EBBR2,
    EXAMPLE_IRTSST,
    EXAMPLE_LCL1,
    EXAMPLE_MET1,
    EXAMPLE_MET_CONTOUR,
    EXAMPLE_MET_CSV,
    EXAMPLE_MET_TEST1,
    EXAMPLE_MET_TEST2,
    EXAMPLE_MET_WILDCARD,
    EXAMPLE_METE40,
    EXAMPLE_MFRSR,
    EXAMPLE_MPL_1SAMPLE,
    EXAMPLE_NAV,
    EXAMPLE_NOAA_PSL,
    EXAMPLE_RL1,
    EXAMPLE_SIGMA_MPLV5,
    EXAMPLE_SIRS,
    EXAMPLE_SONDE1,
    EXAMPLE_SONDE_WILDCARD,
    EXAMPLE_STAMP_WILDCARD,
    EXAMPLE_SURFSPECALB1MLAWER,
    EXAMPLE_TWP_SONDE_20060121,
    EXAMPLE_IRT25m20s,
)

try:
    from pysp2.testing import EXAMPLE_HK, EXAMPLE_INI, EXAMPLE_SP2B
except ImportError:
    pass
