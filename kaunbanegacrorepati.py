
from numpy.random import choice
from playsound import playsound
playsound('k.mp3')
j=0

def loose():
    playsound('end.mp3')
    exit()


#------------this are the easy questions-----------

def easy():
    ddd='''No man your answer was wrong
Now u can't play further 
It was fun playing game with you'''

    AA='''who is the highest scorer in the ipl 2016
    a.Virat Kohli      b.MS Dhobi
    c.Chris Gayle      d.David Warner
    Your answer please:::'''
           

    BB='''enter the name of the winning team in ipl 2019
    a.Mumbai Indians       b.Royal Challengers Banglore
    c.Chennai Super Kings  d.Sunrisers Hyderabad
    Your answer please:::'''
    
        

    CC='''What is the name of the house of Shah Rukh Khan in Mumbai
    a.Shes Mahal      b.Jannat
    c.Mannat          d.Antilla
    Your answer please:::'''
    

    DD='''Who is the main lead actor in flim Iron-Man
    a.Chris Evans     b.Robert Downey Jr.
    c.Salman Khan     c.Justin Bieber
    Your answer please:::'''
    

    e='''Who is the capital of India
    a.Mumbai          b.Delhi
    c.Hyderabad       d.Pune
    Your answer please:::'''
    lis=[AA,BB,CC,DD,e]
    dic={AA:'a',BB:'a',CC:'c',DD:'b',e:'b'}
    lis2=[]
    while len(lis)!=len(lis2):
        a=choice(lis)
        if a not in lis2:
            lis2.append(a)
    global j
    for i in lis2:
        j+=1

        print(i)
        ch=input('enter the choice :')
        if ch == dic[i]:
            money(j)
        else:
            print(ddd)
            loose()

#------------this are the medium questions
   
def medium():
   
    ddd='''No man your answer was wrong
    Now u can't play further 
    It was fun playing game with you'''

    AA='''Which is the richest city in India
    a.Mumbai          b.Delhi
    c.Hyderabad       d.Pune
    Your answer please:::'''
    

    BB='''In which city did Amazon built its world largest campus
    a.Mumbai          b.Delhi
    c.Hyderabad       d.Pune
    Your answer please:::'''
  

    CC='''Which is the richest city in the world
    a.New York       b.Singapore
    c.London         d.Tokya
    Your answer here:::'''


    DD='''Jeventus club is in which city
    a.Spain          b.Italy
    c.france         d.germany
    your answer here:::'''

    EE='''Which is the Silicon Valley of India
    a.Mumbai         b.Banglore
    c=Pune           c.Ooty
    your answer here:::'''

    lis=[AA,BB,CC,DD,EE]
    dic={AA:'a',BB:'c',CC:'a',DD:'b',EE:'b'}
    lis2=[]
    while len(lis)!=len(lis2):
        a=choice(lis)
        if a not in lis2:
            lis2.append(a)
    global j
    for i in lis2:
        j+=1
    

    print(i)
    ch=input('enter the choice :')
    if ch == dic[i]:
            money(j)
    else:
            print(ddd)
            exit()


ddd='''Fuck man your answer was wrong
    Now u can't play further 
    It was fun playing game with you'''


def hard():
    AA='''who is the founder of Infosys
    a.Ambani       b.N.R.Narayana Murthy
    c.Trump        d.Modi
    enter your choice:::'''

    
    BB='''who is the inverter of bulb
    a.Ashish Bhoya     b.Srinivas Reddy
    c.Shazib Rahman    d.Thomas Alva Edison
    enter your choice:::'''

    CC='''Who is the president of USA when USA bombared atom bomb on Hiroshima Nagasaki
    a.George Bhush      b.Abhraman Lincoln
    c.Hary S. Truman    d.John F. Keneddy
    enter your choice:::'''


    lis=[AA,BB,CC]
    dic={AA:'b',BB:'d',CC:'c'}
    lis2=[]
    while len(lis)!=len(lis2):
        a=choice(lis)
        if a not in lis2:
            lis2.append(a)
    global j
    for i in lis2:
        j+=1


        print(i)
        ch=input('enter the choice :')
        if ch == dic[i]:
            money(j)
        else:
            print(ddd)
            loose()


def jackpot():
    print(''' Congrats u are on the last stage of the game
    You have won 5 crore .
    The jackpot question is of 7 crore.
    IF u decide u play it and win , u win 7 crore
    else lose all money...
    ''')

    ch=int(input('press 1. to play else press any to exit: '))
    if ch==1:
        chh=input('''
so , you are a daring person and here is your final question
        
who is the creater of world\'s famous programming language PYTHON
     a.Bjarne Stroustrup        b.James Gosling
     c.Ross Ihaka               d.Guiod Van Rossum
     enter your choice:::''')
        if chh=='d':
            print('''What the fuck mate you just won jackpot of 7 Croses''')
        else:
            print('''
     your overconfident fucked you.
     your are going with 0 amount .
     so sad''')
    else:
        print(''' 
     thanks for playing with us and  congrats for your 5 Crore prize
     have a nice day
              ''')


def welcome():
    print('''\nWelcome to the Fantastic Kaun Banega Crorepati by Ashish Bhoya
Here are the sets of rules that u need to follow and the instructions to play the game
1.There are 4 rounds
i)Easy...............Max u win is 1 lakh
ii)Medium............max u win is 50 lakh
iii)Hard.............max u win is 5 crore
iv)The Jackpot question

The Easy and the medium round contains 5 questions each
The hard round contains 3 questions 
The last round which is the mega 7 crore jackpot question
In this even if u got one wrong answer  u will lose the game
WISHING YOU ALL THE BEST FOR YOUR GAME\n\n''')


mon=0
i=0
def money(a):
    mmm=[5000,10000,25000,50000,100000,250000,500000,1000000,25000000,50000000,100000000,200000000,500000000]
    mon=mmm[a-1]
    print('CONGRATS your answer was right and u won ',mon,'\n')



nam=input('Enter your name::')
welcome()
print(f'So {nam} are u ready to play this exciting game::')
zz=input('print y for yes and any key to exit::')
if zz=='y':
  print('\n')
  easy()
  medium()
  hard()
  jackpot()
else:
    exit()
