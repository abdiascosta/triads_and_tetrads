#This program should mount musical scales, triads, tetrads and fundamental triads and tetrads postions on guitar fretboard.

import return_index

def notes(tonality):
    cflat=11
    c=0
    csharp=1
    dflat=1
    d=2
    dsharp=3
    eflat=3
    e=4
    esharp=5
    fflat=4
    f=5
    fsharp=6
    gflat=6
    g=7
    gsharp=8
    aflat=8
    a=9
    asharp=10
    bflat=10
    b=11
    bsharp=0

def mount_scale(tonality,scale):

    t=1
    st=2
    natural=[t,t,st,t,t,t,st]
    cromatic=[st,st,st,st,st,st,st,st,st,st,st,st]
    notes_number=[0,1,2,3,4,5,6,7,8,9,10,11]
    notes_names=['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
    enarmonics=['C#/Db','D#/Eb','F#/Gb','G#/Ab','A#/Bb']
    enarmonics2=['E#/F','Fb/E','B#/C','Cb/B']

    tonality_index=return_index.return_index(notes_names,tonality)

    triad=[]
    tetrad=[]

    #from the next line the cromatic scale in tonality will be mounted
    cromatic_in_tonality=[]

    for i in notes_names[tonality_index:]:
        cromatic_in_tonality.append(i)
    for i in notes_names[:tonality_index]:
        cromatic_in_tonality.append(i)

    #the scale is ready

    if scale=='cromatic':
        print(cromatic_in_tonality)
        return cromatic_in_tonality

    natural_in_tonality=[]

    #from the next line the natural scale in tonality woll be mounted

    natural_in_tonality.append(cromatic_in_tonality[0])
    natural_in_tonality.append(cromatic_in_tonality[2])
    natural_in_tonality.append(cromatic_in_tonality[4])
    natural_in_tonality.append(cromatic_in_tonality[5])
    natural_in_tonality.append(cromatic_in_tonality[7])
    natural_in_tonality.append(cromatic_in_tonality[9])
    natural_in_tonality.append(cromatic_in_tonality[11])

    #natural scale is ready

    if scale=='natural':
        print(natural_in_tonality)
        return natural_in_tonality


tonality=input('Which is the musical tonality?')

scale=input('Which musical scale should be mounted?')

scale=mount_scale(tonality,scale)
