import datetime
import os
from pathlib import Path


def get_result_output_path():
    return get_results_directory() + "run-" + str(datetime.datetime.now()).replace(" ", "-").replace(":", "-") + ".csv"


def get_results_directory():
    return get_resources_directory() + "results\\"


def read_presidential_votes_state_data():
    return get_resources_directory() + "working_data\\presidential-votes-by-state-1976-2020-working.csv"


def read_presidential_votes_county_data():
    return get_resources_directory() + "working_data\\presidential-votes-by-county-2000-2016-working.csv"


def get_resources_directory():
    return get_root_directory() + "resources\\"


def get_root_directory():
    return str(Path(os.path.realpath(__file__)).parent.parent) + "\\"
