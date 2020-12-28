from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

df=pandas.read_excel("verlegenhuken.xlsx")
df['Pressure']=df['Pressure'].apply(lambda x:x/10)
df['Temperature']=df['Temperature'].apply(lambda x:x/10)
x = df['Pressure']
y = df['Temperature']
output_file("Dot.html")
f = figure()
f.dot(x, y)
show(f)

'''
Plot Properties

p=figure(plot_width=500,plot_height=400, tools='pan',logo=None)
 
p.title.text="Cool Data"
p.title.text_color="Gray"
p.title.text_font="times"
p.title.text_font_style="bold"
p.xaxis.minor_tick_line_color=None
p.yaxis.minor_tick_line_color=None
p.xaxis.axis_label="Date"
p.yaxis.axis_label="Intensity"  
'''