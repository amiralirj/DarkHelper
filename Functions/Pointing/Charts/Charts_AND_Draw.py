import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
from random import choice , randint
path=''
def Random_Name():
    names=['amoamirali','amiralirj','rjrj','mio','linux','tehran','hazrat_mohamad','emamali','hitler','anishtan','hossainmola','madar','in_robot_kosshere','halnadaram','WW3','mardom','kholase_ke_are','chie']
    rand=choice(names)
    return f'{rand}{randint(1,99999999)}.jpg'

def add_value_labels(ax, spacing=5):
    """Add labels to the end of each bar in a bar chart.

    Arguments:
        ax (matplotlib.axes.Axes): The matplotlib object containing the axes
            of the plot to annotate.
        spacing (int): The distance between the labels and the bars.
    """

    # For each bar: Place a label
    for rect in ax.patches:
        # Get X and Y placement of label from rect.
        y_value = rect.get_height()
        x_value = rect.get_x() + rect.get_width() / 2

        # Number of points between bar and label. Change to your liking.
        space = spacing
        # Vertical alignment for positive values
        va = 'bottom'

        # If value of bar is negative: Place label below bar
        if y_value < 0:
            # Invert space to place label below
            space *= -1
            # Vertically align label at top
            va = 'top'

        # Use Y value as label and format number with one decimal place
        label = "{:.1f}".format(y_value)

        # Create annotation
        ax.annotate(
            label,                      # Use `label` as label
            (x_value, y_value),         # Place label at end of the bar
            xytext=(0, space),          # Vertically shift label by `space`
            textcoords="offset points", # Interpret `xytext` as offset in points
            ha='center',                # Horizontally center label
            va=va)                      # Vertically align label differently for
                                        # positive and negative values.



def Single_Bar(frequencies,x_labels,title,xlable,ylable):
    freq_series = pd.Series(frequencies)
    fig= plt.figure(figsize=(25, 20))
    plt.rc('axes', unicode_minus=False)
    ax = freq_series.plot(kind='bar' , color={'b', 'g','c', 'r', 'm', 'y', 'k'} )
    ax.set_title(title)
    ax.set_xlabel(xlable , fontweight='bold')
    ax.set_ylabel(ylable, fontweight='bold')
    fig.patch.set_facecolor('xkcd:black')
    ax.tick_params(axis='x', colors='lawngreen' )
    ax.tick_params(axis='y', colors='snow'  )
    ax.set_facecolor('xkcd:white')
    ax.set_xticklabels(x_labels ,  rotation = 45, zorder=100 , weight='bold', fontsize=15)
    add_value_labels(ax)
    f_name=Random_Name()
    plt.savefig(f'{path}{f_name}')
    try:
        plt.cla()
        plt.clf()
        plt.close()
    except:
        pass
    return f'{path}{f_name}'


def plot_stacked_bar(data, series_labels, category_labels=None, 
                     show_values=False, value_format="{}", y_label=None, 
                     colors=None, grid=True, reverse=False):
    """Plots a stacked bar chart with the data and labels provided.

    Keyword arguments:
    data            -- 2-dimensional numpy array or nested list
                       containing data for each series in rows
    series_labels   -- list of series labels (these appear in
                       the legend)
    category_labels -- list of category labels (these appear
                       on the x-axis)
    show_values     -- If True then numeric value labels will 
                       be shown on each bar
    value_format    -- Format string for numeric value labels
                       (default is "{}")
    y_label         -- Label for y-axis (str)
    colors          -- List of color labels
    grid            -- If True display grid
    reverse         -- If True reverse the order that the
                       series are displayed (left-to-right
                       or right-to-left)
    """

    ny = len(data[0])
    ind = list(range(ny))

    axes = []
    cum_size = np.zeros(ny)

    data = np.array(data)

    if reverse:
        data = np.flip(data, axis=1)
        category_labels = reversed(category_labels)

    for i, row_data in enumerate(data):
        color = colors[i] if colors is not None else None
        axes.append(plt.bar(ind, row_data, bottom=cum_size, 
                            label=series_labels[i], color=color))
        cum_size += row_data

    if category_labels:
        plt.xticks(ind, category_labels)

    if y_label:
        plt.ylabel(y_label)

    plt.legend()

    if grid:
        plt.grid()

    if show_values:
        for axis in axes:
            for bar in axis:
                w, h = bar.get_width(), bar.get_height()
                plt.text(bar.get_x() + w/2, bar.get_y() + h/2, 
                         value_format.format(h), ha="center", 
                         va="center")


def Two_Bars(data , labels ,downlabel , uplable):
    plt.figure(figsize=(6, 4))
    series_labels = [downlabel , uplable]
    plot_stacked_bar(
        data, 
        series_labels, 
        category_labels=labels, 
        show_values=True, 
        value_format="{:.0f}",
        colors=['tab:orange', 'tab:green'],
        y_label="Students"
    )
    f_name=Random_Name()
    plt.savefig(f'{path}{f_name}')
    try:
        plt.cla()
        plt.clf()
        plt.close()
    except:
        pass
    return f'{path}{f_name}'

def Pie_Chart(afk,plyr,labels , title):
    y = np.array([plyr,afk])
    mylabels = labels
    myexplode = [0, 0.2]

    plt.pie(y, labels = mylabels, explode = myexplode)
    plt.legend(title = title)
    f_name=Random_Name()
    plt.savefig(fname=f_name)
    try:
        plt.cla()
        plt.clf()
        plt.close()
    except:
        pass
    return f_name

def Tree_Kind_Chart(list_1 , list_2,title):
    plt.figure(figsize=(9, 3))
    plt.subplot(131)
    plt.bar(list_1, list_2)
    plt.subplot(132)
    plt.scatter(list_1, list_2)
    plt.subplot(133)
    plt.plot(list_1, list_2)
    plt.suptitle(title)

    # plt.plot(list_hour,list_player)
    # plt.ylabel('join time (sec)')
    # plt.xlabel('number of game')
    f_name=Random_Name()
    plt.savefig(f'{path}{f_name}')
    try:
        plt.cla()
        plt.clf()
        plt.close()
    except:
        pass
    return f'{path}{f_name}'

def Normall_Bar(mainlist,xlabel,ylabel):
    plt.plot(mainlist[0],mainlist[1])
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    f_name=Random_Name()
    plt.savefig(f'{path}{f_name}')
    try:
        plt.cla()
        plt.clf()
        plt.close()
    except:
        pass
    return f'{path}{f_name}'

def reqt(pix,path):
    # Create figure and axes

    fig, ax = plt.subplots()
    
    # Display the image
    im = Image.open(path)
        
    # Create a Rectangle patch
    ax.imshow(im)
    for i in pix['output']['detections']:
        print(i)
        HT=i['bounding_box']
    
        rect = patches.Rectangle((HT[0], HT[1]), HT[2], HT[3], linewidth=1, edgecolor='r', facecolor='b')
        # Add the patch to the Axes
        ax.add_patch(rect)
    f_name=Random_Name()
    plt.savefig(f'{path}{f_name}')
    try:
        plt.cla()
        plt.clf()
        plt.close()
    except:
        pass
    return f'{path}{f_name}'


def Get_User_Role(item):
    '''{'win':Bool,'point':INT,'alive':BOOL,'naghsh':STR,'team':STR}'''
    if '⚒' in item:
        team='روستا👨🏻'
        naghsh='⚒'
        point=10
    elif '💍🧛🏻' in item:
        team='ومپایر 🧛🏻‍♂️'
        naghsh='💍🧛🏻'
        point=75
    elif '🃏' in item:
        team='روستا👨🏻'
        naghsh='🃏'
        point=10
    elif '👿' in item:
        team='روستا👨🏻'
        naghsh='👿'
        point=20
    elif '👷' in item:
        team='روستا👨🏻'
        naghsh='👷'
        point=10
    elif '👨‍🔬' in item:
        team='روستا👨🏻'
        naghsh='👨‍🔬'
        point=30
    elif '☮️' in item:
        team='روستا👨🏻'
        naghsh='☮️'
        point=30
    elif '🧙🏻‍♂️' in item:
        team='گرگ 🐺'
        naghsh='🧙🏻‍♂️'
        point=25
    elif '💘' in item:
        team='روستا👨🏻'
        naghsh='💘'
        point=20
    elif '👶🏻' in item or '👶' in item:
        team='گرگ 🐺'
        naghsh='👶🏻'
        point=25
    elif '🔮' in item :
        team='گرگ 🐺'
        naghsh='🔮'
        point=30
    elif '💣' in item:
        naghsh='💣'
        point=40
        team='بمب گذار 💣'
    elif '🔥' in item:
        team='اتش🔥'
        naghsh='🔥'
        point=60
    elif '👨🏻' in item or '👱' in item:
        team='روستا👨🏻'
        naghsh='👨🏻'
        point=5
    elif '📚' in item:
        team='روستا👨🏻'
        naghsh='📚'
        point=20
    elif '🙇🏻‍♂' in item:
        team='روستا👨🏻'
        naghsh='🙇🏻‍♂'
        point=25
    elif '🦅' in item:
        team='روستا👨🏻'
        naghsh='🦅'
        point=20
    elif '🍾' in item:
        team='قاتل 🔪'
        naghsh='🍾'
        point=30
    elif '👩🏻‍🌾' in item:
        team='روستا👨🏻'
        naghsh='👩🏻‍🌾'
        point=15
    elif '👰🏻' in item:
        team='روستا👨🏻'
        naghsh='👰🏻'
        point=20
    elif '🎩' in item:
        team='فرقه👤'
        naghsh='🎩'
        point=30
    elif '👑' in item:
        team='روستا👨🏻'
        naghsh='👑'
        point=25
    elif '🔪' in item:
        team='قاتل 🔪'
        naghsh='🔪'
        point=100
    elif '🔫' in item:
        team='روستا👨🏻'
        naghsh='🔫'
        point=40
    elif '🐶' in item:
        team='گرگ 🐺'
        naghsh='🐶'
        point=70
    elif '🦹🏻‍♂️' in item:
        team='روستا👨🏻'
        naghsh='🦹🏻‍♂️'
        point=40
    elif '⚡️' in item:
        team='گرگ 🐺'
        naghsh='⚡️🐺'
        point=85
    elif '💤🐺' in item:
        team='گرگ 🐺'
        naghsh='💤🐺'
        point=30
    elif '🌀' in item:
        team='روستا👨🏻'
        naghsh='🌀'
        point=35
    elif '🖕🏿' in item:
        team='گرگ 🐺'
        naghsh='🖕🏿'
        point=30
    elif '👳🏻‍♂️' in item or '👳' in item :
        team='روستا👨🏻'
        naghsh='👳🏻‍♂️'
        point=60
    elif '👺' in item:
        team='منافق'
        naghsh='👺'
        point=150
    elif '🧝🏻‍♀️' in item:
        team='گرگ 🐺'
        naghsh='🧝🏻‍♀️'
        point=70
    elif '🌝🐺' in item:
        team='گرگ 🐺'
        naghsh='🌝🐺'
        point=70
    elif '🎭' in item:
        team='روستا👨🏻'
        naghsh='🎭'
        point=20
    elif '👁' in item:
        team='روستا👨🏻'
        naghsh='👁'
        point=20
    elif '🗡' in item:
        team='روستا👨🏻'
        naghsh='🗡'
        point=80
    elif '🤴🏻' in item:
        team='روستا👨🏻'
        naghsh='🤴🏻'
        point=15
    elif '💂🏻‍♂️' in item or '💂‍♂️' in item:
        team='روستا👨🏻'
        naghsh='💂🏻‍♂️'
        point=100
    elif '👨‍🔬️' in item:
        team='روستا👨🏻'
        naghsh='👨‍🔬️'
        point=30
    elif '🧙🏻‍♀️' in item:
        team='گرگ 🐺'
        naghsh='🧙🏻‍♀️'
        point=30
    elif '🧟‍♂️' in item:
        team='فرقه👤'
        naghsh='🧟‍♂️'
        point=45
    elif '👼🏻' in item:
        team='روستا👨🏻'
        naghsh='👼🏻'
        point=45
    elif '👤' in item:
        team='فرقه👤'
        naghsh='👤'
        point=25
    elif '👮🏻‍♂' in item:
        team='روستا👨🏻'
        naghsh='👮🏻‍♂'
        point=30
    elif '😾' in item:
        team='گرگ 🐺'
        naghsh='😾'
        point=20
    elif '🍵' in item:
        team='گرگ 🐺'
        naghsh='🍵'
        point=30
    elif '🦊' in item:
        team='گرگ 🐺'
        naghsh='🦊'
        point=30
    elif '🕵🏻‍♂️' in item:
        team='روستا👨🏻'
        naghsh='🕵🏻‍♂️'
        point=60
    elif '☃️' in item:
        team='گرگ 🐺'
        naghsh='☃️'
        point=40
    elif '💤' in item:
        team='روستا👨🏻'
        naghsh='💤'
        point=25
    elif '🍂' in item:
        team='روستا👨🏻'
        naghsh='🍂'
        point=30
    elif '👹' in item:
        team='گرگ 🐺'
        naghsh='👹'
        point=35
    elif '🍻' in item: 
        team='روستا👨🏻'
        naghsh='🍻'
        point=10
    elif '❄️' in item:
        team='اتش🔥'
        naghsh='❄️'
        point=50
    elif '💋' in item:
        team='روستا👨🏻'
        naghsh='💋'
        point=35
    elif '🪓' in item:
        team='روستا👨🏻'
        naghsh='🪓'
        point=50
    elif '🐺' in item:
        team='گرگ 🐺'
        naghsh='🐺'
        point=55
    elif '🧛🏻‍♀️' in item:
        team='ومپایر 🧛🏻‍♂️'
        naghsh='🧛🏻‍♀️'
        point=75
    elif '🧛🏻‍♂️' in item:
        team='ومپایر 🧛🏻‍♂️'
        naghsh='🧛🏻‍♂️'
        point=50
    elif '🏹' in item:
        team='قاتل 🔪'
        naghsh='🏹'
        point=80
    elif '🎖' in item:
        team='روستا👨🏻'
        naghsh='🎖'
        point=30
    else:
        team='?'
        naghsh='??'
        point=15
    if item.find("بُرد") != -1 or item.find("برنده") != -1 :
        win_txt='🌟'
        win=True
    else:
        win_txt='💩'
        win=False

    if item.find("مرده") != -1 :
        alive_txt='💀'
        alive=False
    else:
        alive_txt='🙂'
        alive=True
        
    return {'win':win,'point':point,'alive':alive,'naghsh':naghsh,'team':team,'win_emoji':win_txt,'alive_emoji':alive_txt}