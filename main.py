from _utils import *
import pandas as pd

logging.basicConfig(
    format="%(asctime)s %(levelname)s %(message)s",
    level=logging.DEBUG,
    stream=sys.stdout,
)


def main(yaml_filepath):
    """Machine learning pipeline of covid19 data."""

    # Load the configuration
    cfg = load_cfg(yaml_filepath)
    pprint(cfg)
    raise ljdfd
    # Load dataset
    data = imp.load_source(
        "data", cfg["dataset"]["script_path"]).get_live_data()

    # Train
    trained_model = imp.load_source(
        "train_model", cfg["train"]["script_path"]).fit(data)

    # Save the model
    evaluated_model = imp.load_source(
        "evaluate_model", cfg["evaluate"]["script_path"]).evaluate(trained_model)


if __name__ == "__main__":
    args = get_parser().parse_args()
    main(args.filename)
