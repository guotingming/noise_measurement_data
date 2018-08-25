import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
#import seaborn
filename='measurement_data/RFA01d_Bias1.csv'
def csv_to_df(filename):
    df=pd.read_csv(filename,header=None,sep=',',names=["1",'2','3','4','5','6','7','8','9'])
    #print(df)
    name=df.iloc[5,:]
    print(name.values)
    data=df.iloc[6:-1,:]
    data=data.rename(columns=name)
    #data.index = data['Freq(Hz)'].tolist()
    data=data.reset_index()
    del data['index']
    return data

#print(data)
#data.to_csv('DATA.csv',sep=',')
def draw(data):
    freq=data.iloc[:,0].values
    freq=np.array(freq,dtype=float)
    freq=freq/1000000000
    #print(freq)
    NF_dB=data.iloc[:,1].values
    NF_dB=np.array(NF_dB,dtype='float16')
    #print(float(NF_dB))
    S21_dB=data.iloc[:,3].values
    S21_dB=np.array(S21_dB,dtype='float16')
    S11_dB=data.iloc[:,5].values
    S11_dB=np.array(S11_dB,dtype='float16')
    T_Eff=data.iloc[:,7].values
    T_Eff=np.array(T_Eff,dtype='float16')
    plt.style.use('ggplot')
    fig, ax = plt.subplots(2,2)
    #设置子图之间间距
    plt.tight_layout(2)
    # Call plot() method on the appropriate object

    ax[0,0].plot(freq,NF_dB,'-k')
    ax[0,0].set_title('NF(dB)',fontsize=20)
    ax[0,0].set_xlabel('freq(GHz)',fontsize=25)
    ax[0,0].set_ylabel('NF(dB)',fontsize=25)
    ax[0,0].tick_params(labelsize=18)
    ax[0,0].set_xlim(0,19)
    ax[0,1].plot(freq,S21_dB,'-k',linewidth=3)
    ax[0,1].set_title('S21(dB)',fontsize=20)
    ax[0,1].set_xlabel('freq(GHz)',fontsize=25)
    ax[0,1].set_ylabel('S21(dB)',fontsize=25)
    ax[0,1].tick_params(labelsize=18)
    ax[0,1].set_xlim(0,19)
    ax[1,0].plot(freq,S11_dB,'-k',linewidth=3)
    ax[1,0].set_title('S11(dB)',fontsize=20)
    ax[1,0].set_xlabel('freq(GHz)',fontsize=25)
    ax[1,0].set_ylabel('S11(dB)',fontsize=25)
    ax[1,0].tick_params(labelsize=20)
    ax[1,0].set_xlim(0,19)
    ax[1,1].plot(freq,T_Eff,'-k')
    ax[1,1].set_title('T-Eff(dB)',fontsize=20)
    ax[1,1].set_xlabel('freq(GHz)',fontsize=25)
    ax[1,1].set_ylabel('T-Eff(dB)',fontsize=25)
    ax[1,1].tick_params(labelsize=18)
    ax[1,1].set_xlim(0,19)
    fig.set_size_inches(18.5, 10.5)
    fig.savefig('test.png', dpi=120)
    #fig.savefig('test.png')
    plt.show()
#data=csv_to_df(filename)
#draw(data)
