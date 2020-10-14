import pandas as pd
from numpy import trapz
import plotly.express as px
from operator import add


def compare(arg1, *args,des,ang=1,vel=1,lower=200,upper=6000):
    ang,vel = str(ang),str(vel)
    title = "Angle "+ang+", Velocity "+vel
    
    area = {'Design':[des[0]], 'Area':[]}
    for trial in range(1,4):
        x = arg1+'_a'+ang+'_v'+vel+'_'+str(trial)+'.txt'
        try:
            dfx = pd.read_fwf('./Testing Data./'+x)

            freq,level = [],[]
            for n in dfx['Frequency (Hz)\tLevel (dB)']:
                freq.append(float(n.split('\t')[0]))
                level.append(float(n.split('\t')[1]))

            if trial == 1:
                df = pd.DataFrame({'Design': des[0], 'Frequency':freq, 'Level':level})
                df = df[(df['Frequency'] > lower) & (df['Frequency'] <= upper)]
                total = df['Level']
            else:
                dfn = pd.DataFrame({'Design': des[0], 'Frequency':freq, 'Level':level})
                dfn = dfn[(dfn['Frequency'] > lower) & (dfn['Frequency'] <= upper)]
                total = list(map(add, total, dfn['Level']))   
        except IOError:
            continue
        
    avg = list(map(lambda x: x/3, total))
    df = pd.DataFrame({'Design': des[0], 'Frequency':df['Frequency'], 'Level':avg})
    area['Area'].append(int(abs(trapz(df['Level'], dx=5.383301))))

    num = 1
    for arg in args:
        count = 0
        for trial in range(1,4):
            x = arg+'_a'+ang+'_v'+vel+'_'+str(trial)+'.txt'
            try:
                dfx = pd.read_fwf('./Testing Data./'+x)
                count += 1

                freq,level = [],[]
                for n in dfx['Frequency (Hz)\tLevel (dB)']:
                    freq.append(float(n.split('\t')[0]))
                    level.append(float(n.split('\t')[1]))

                if trial == 1:
                    dfn = pd.DataFrame({'Design': des[num], 'Frequency':freq, 'Level':level})
                    dfn = dfn[(dfn['Frequency'] > lower) & (dfn['Frequency'] <= upper)]
                    total = dfn['Level']
                else:
                    dfn = pd.DataFrame({'Design': des[num], 'Frequency':freq, 'Level':level})
                    dfn = dfn[(dfn['Frequency'] > lower) & (dfn['Frequency'] <= upper)]
                    total = list(map(add, total, dfn['Level'])) 
            except IOError:
                continue

        avg = list(map(lambda x: x/count, total))
        df_arg = pd.DataFrame({'Design': des[num], 'Frequency':dfn['Frequency'], 'Level':avg})   
        df = pd.concat([df,df_arg])
        area['Design'].append(des[num])
        area['Area'].append(int(abs(trapz(df_arg['Level'], dx=5.383301))))
        num += 1
    
    l = int(len(df))
    ii = len(area['Design'])
    comp = {'Design': area['Design'][1:ii+1], 'Level': []}
    for i in range(ii):
        dfn = df.iloc[int(i*l/ii):int((i+1)*l/ii)]
        if i == 0:
            ref_mean = dfn['Level'].mean()
        else:
            comp['Level'].append(ref_mean - dfn['Level'].mean())
        
    fig = px.line(df, x="Frequency", y="Level", color='Design',log_x=True, title=title, width=960, height=480,
                  labels=dict(Frequency='<b>Frequency (Hz)</b>', Level='<b>Level (dB)</b>', Design='<b>Design</b>'), 
                  template="simple_white", color_discrete_sequence=['red', 'blue', 'black','green', 'orange','purple','olive','royalblue'])
    fig.update_layout(font_family="Times New Roman",font_size=18)            
    fig.show()
    
    fig3 = px.bar(comp, x='Design', y='Level', color='Design', title=title, width=960, height=480,
                  labels=dict(Level='<b>Relative Difference (dB)</b>', Design='<b>Design</b>'),
                  template="simple_white", color_discrete_sequence=['red', 'blue', 'black', 'green', 'orange', 'purple'])
    fig3.update_xaxes(categoryorder='total descending')
    fig3.update_layout(font_family="Times New Roman",font_size=18)
    fig3.show()
    
    for i in range(len(comp['Level'])):
        print(round(comp['Level'][i],3))


compare('p0','z1',ang=1,vel=3,des=['Final','Reference'])
