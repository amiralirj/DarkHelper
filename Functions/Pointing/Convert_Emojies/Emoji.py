import random
def show_emt(points:int,emojis):
    medal_count=int(points/36)
    if medal_count==0:
        medal=''
    else:
        medal=f'{emojis[0]}' * medal_count
    tala_count=int(int(points%36) / 6)
    if tala_count==0:
        tala=''
    else:
        tala=f'{emojis[1]}' * tala_count
    boronz_count=int(int(points%36) % 6)
    if boronz_count==0:
        boronz=''
    else:
        boronz=f'{emojis[2]}' * boronz_count
    return [medal,tala,boronz]

def rand_moon():
    moon_list=['🌕','🌖', '🌗' ,'🌘', '🌑', '🌒', '🌓', '🌔']
    radom_moon=random.choice(moon_list)
    return radom_moon