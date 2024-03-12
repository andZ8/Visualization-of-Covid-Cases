#visualizing covid case counts
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import pylab
On_Cases = pd.read_excel (r'Pandemic Research\Covid19 Research Data Ontario.xlsx')
Qc_Cases = pd.read_excel (r'Pandemic Research\Covid19 Research Data Quebec.xlsx')
On_Cases = pd.DataFrame(On_Cases, columns = ['Province','Date', 'Cases'])
Oc_Cases = pd.DataFrame(Qc_Cases, columns = ['Province','Date', 'Cases'])
On_Cases.plot(x ='Date', y='Cases', kind = 'line', title = "Ontario Cases", color = 'Blue')
fig = pylab.gcf()
fig.canvas.manager.set_window_title('Ontario Case Count')
Qc_Cases.plot(x ='Date', y='Cases', kind = 'line', title = "Quebec Cases", color = 'Orange')
fig = pylab.gcf()
fig.canvas.manager.set_window_title('Ouebec Case Count')
plt.show()