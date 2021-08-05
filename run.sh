# Download dataset stored on cloud
curl -o dataset.csv https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv
# Install libraries in requirements.txt
pip3 install -r requirements.txt
# Execute main script
if [ -n "$1" ]; then
  echo python3 main.py -f experiments/$1
else
  echo python3 main.py -f experiments/default_config.yaml
fi
