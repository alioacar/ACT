"""
This module contains the common procedures used by all modules of the ARM
Community Toolkit.

"""
import lazy_loader as lazy

__getattr__, __dir__, __all__ = lazy.attach(
    __name__,
    submodules=['ship_utils'],
    submod_attrs={
        'data_utils': [
            'ChangeUnits',
            'accumulate_precip',
            'add_in_nan',
            'assign_coordinates',
            'convert_units',
            'create_pyart_obj',
            'get_missing_value',
            'ts_weighted_average',
            'height_adjusted_pressure',
            'height_adjusted_temperature',
            'convert_to_potential_temp',
        ],
        'datetime_utils': [
            'dates_between',
            'datetime64_to_datetime',
            'determine_time_delta',
            'numpy_to_arm_date',
            'reduce_time_ranges',
            'date_parser',
        ],
        'geo_utils': [
            'add_solar_variable',
            'destination_azimuth_distance',
        ],
        'inst_utils': ['decode_present_weather'],
        'qc_utils': ['calculate_dqr_times'],
        'radiance_utils': ['planck_converter'],
        'ship_utils': ['calc_cog_sog', 'proc_scog'],
    },
)
