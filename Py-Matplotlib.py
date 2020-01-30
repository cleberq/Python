import matplotlib.pyplot as plt
from pandas import DataFrame
#####
plt.plot([1, 3, 5], [2, 5, 7])
plt.show()
###########
data = {'Estado': ['Santa Catarina', 'Paraná', 'Goiás', 'Bahia', 'Minas Gerais'], 
        'População': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data)
print(frame)
############
plt.plot(frame['Estado'],frame['População'])
plt.show()
