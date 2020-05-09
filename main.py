from pandas_datareader import data
import datetime
from bokeh.plotting import figure, show, output_file


start = datetime.datetime(2019, 1, 1)
end = datetime.datetime(2019, 12, 31)

df = data.DataReader('TSLA', 'google', start, end)

p = figure(x_axis_type='datetime', width=1000, height=300)
p.title = "Tesla Stock Information for 2019"


p.rect
p.rect
