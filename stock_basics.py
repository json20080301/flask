# 基本面（长线） 
# http://tushare.org/fundamental.html#id2
import pandas as pd
from sqlalchemy import Column, String, create_engine , engine_from_config
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

data = {'state':['Ohino','Ohino','Ohino','Nevada','Nevada'],
        'year':[2000,2001,2002,2001,2002],
        'pop':[1.5,1.7,3.6,2.4,2.9]}


df = pd.DataFrame(data,index=[0,1,2,3,4], columns=['year','state','pop','debt'])
 
print (df.to_json(orient='records') )


if  ((df['pop'].max() + df['pop'].min()) /2 >  df['pop'].min())  and (df['pop'].max() ==3.6):
    print('stock no is ')
    print(df['pop'][0])
    print(df['pop'].min())
    print(df['pop'].max())
    print((df['pop'].max() + df['pop'].min()) /2 )
    print(df.head(1))
    print('===============')
    
    
    
#
for name in df.index:
    print(name)
    
config = {
      'sqlalchemy.url':'mysql+pymysql://root:root@127.0.0.1/test?charset=utf8',
      'sqlalchemy.echo':True
      };
# df = ts.get_tick_data('600848', date='2014-12-22')
# engine = create_engine(config['sqlalchemy.url'], echo=True)
engine = engine_from_config(config);
df.to_sql('tick_data',engine,if_exists='append')
 
