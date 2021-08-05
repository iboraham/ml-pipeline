import imp
from _utils import *
import yaml

yaml_filepath = "experiments/config.yaml"
# Load the configuration
cfg = load_cfg(yaml_filepath)

# Print the configuration
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(cfg)

# Load dataset
dpath = cfg["dataset"]["script_path"]
data = imp.load_source("data", cfg["dataset"]["script_path"]).get_live_data()
data.to_csv("data.csv")
