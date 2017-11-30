## plot random number against Shannon components
## plot random number against Simpson components

import pandas as pd
import numpy as np
import seaborn as sns

## add realistic array by hand
#s = [4.329,0.148,0.777,0.148,0.777,0.296,2.146,1.998,0.777,0.148,0.148,6.031,0.148,2.479,0.148,0.629,4.625,2.923,1.85,2.775,0.148,0.148,0.629,0.148,0.148,0.148,1.85,0.148,0.148,0.148,0.148,0.777,0.629,0.296,0.629,0.4625,1.221]
#sns.distplot(s,kde=False)

## select better distribution for random number generation
#s = np.random.lognormal(0.01,1,82)
#sns.distplot(s,kde=False)

s = np.random.weibull(.6,82)
sns.distplot(s,kde=False)


df = pd.DataFrame({'Abundance' : s}) 
df['PsubI'] = df.Abundance/np.sum(s) 

df['NL_PsubI'] = np.log(df.PsubI)
df['SH Component'] = -1*(df.PsubI*df.NL_PsubI)

df['SI Component'] = np.square(df.PsubI)

Shannon = np.sum(df['SH Component'])
Simpson = np.sum(df['SI Component'])

df['SH PercentofSum'] = df['SH Component']/Shannon
df['SI PercentofSum'] = df['SI Component']/Simpson

print("Shannon value: {0}".format(Shannon))
print("Simpson value: {0}".format(1-Simpson))

## Shannon raw 
df.plot.scatter(x='Abundance', y='SH Component', color ="red")

## Simpson raw
plot1 = df.plot.scatter(x='Abundance', y='SI Component', color ="green")
plot1.axes.set_ylim(0,0.005)

## Contributions to the total index (i.e. normalized to the sum)
plot2 = df.plot.scatter(x='Abundance', y='SH PercentofSum', color ="purple", label="SH PercentofSum")
df.plot.scatter(x='Abundance', y='SI PercentofSum',ax=plot2, label="SI PercentofSum")

## both components
plot3 = df.plot.scatter(x='SH Component', y='SI Component');
plot3.axes.set_ylim(0,0.005)
