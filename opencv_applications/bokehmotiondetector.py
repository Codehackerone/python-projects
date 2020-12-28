from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool, ColumnDataSource
import pandas

df = pandas.read_csv("times.csv")
start = pandas.to_datetime(df["Start"])
end = pandas.to_datetime(df["End"])
df["Start"] = df["Start"].apply(lambda x: pandas.to_datetime(x))
df["End"] = df["End"].apply(lambda x: pandas.to_datetime(x))
df["Start_String"] = start.dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_String"] = end.dt.strftime("%Y-%m-%d %H:%M:%S")
cds = ColumnDataSource(df)
hover = HoverTool(tooltips=[("Start", "@Start_String"), ("End", "@End_String")])
p = figure(x_axis_type="datetime", height=200, width=500, title="Motion Graph", sizing_mode="stretch_width")
p.yaxis.minor_tick_line_color = None
p.add_tools(hover)
q = p.quad(left="Start", right='End', bottom=0, top=1, color="green",source=cds)
output_file("Motion_Graph.html")
show(p)
