import pandas as pd

data = pd.read_csv('d6.txt', sep=' ', header = None)
data.columns = ['data']
data['col1'] = data['data'].apply( lambda x : x[0])
data['col2'] = data['data'].apply( lambda x : x[1])
data['col3'] = data['data'].apply( lambda x : x[2])
data['col4'] = data['data'].apply( lambda x : x[3])
data['col5'] = data['data'].apply( lambda x : x[4])
data['col6'] = data['data'].apply( lambda x : x[5])
data['col7'] = data['data'].apply( lambda x : x[6])
data['col8'] = data['data'].apply( lambda x : x[7])

print(data['col1'].value_counts().idxmax())
print(data['col2'].value_counts().idxmax())
print(data['col3'].value_counts().idxmax())
print(data['col4'].value_counts().idxmax())
print(data['col5'].value_counts().idxmax())
print(data['col6'].value_counts().idxmax())
print(data['col7'].value_counts().idxmax())
print(data['col8'].value_counts().idxmax())

