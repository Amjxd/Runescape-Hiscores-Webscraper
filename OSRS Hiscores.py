import requests
import bs4
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Combat Level Calculator")
root.configure(background = '#642b09')
root.geometry("330x550+0+0")
root.resizable(width=False,height=False)


logo = ImageTk.PhotoImage(Image.open('logo.jpg'))
logo_lbl = Label(image=logo,bg='#642b09')
logo_lbl.grid(row=0,column=0,columnspan=3)

#Search Feature
search1 = Label(root,text= 'USERNAME',font=('arial',16,'bold'),fg='white',bg='#642b09')
search1.grid(row=1,column=0)
search = Entry(root, width=20, borderwidth=2,fg='#642b09')
search.grid(row=1,column=1)

def search_get():
    global un
    un = search.get()
    if ' ' in un:
        un = un.replace(' ','+')
    def get_level(skill):
        link = str(skill + un)
        req = requests.get(link)
        soup = bs4.BeautifulSoup(req.text,'lxml')
        item1 = soup.select('.left')
        count = 0
        for i in item1:
            count += 1
            m = str(i)
            m = m.lower()
            t_f = 'color:' in m
            if t_f == True:
                count -= 1
                break
        to = soup.select('.personal-hiscores__row')[count].getText()
        to = to.split('\n')
        while '' in to:
            to.remove('')
        return to[-2]
    
    #Attack
    try:
        atk = get_level('https://secure.runescape.com/m=hiscore_oldschool/overall?table=1&user=')
        att1.delete(0,END)
        att1.insert(0,atk)
    except:
        print('Attack Not on Hiscores')
        att1.delete(0,END)
        att1.insert(0,1)

    #Prayer
    try:
        pray = get_level('https://secure.runescape.com/m=hiscore_oldschool/overall?table=6&user=')
        pray1.delete(0,END)
        pray1.insert(0,pray)
    except:
        print('Prayer Not on Hiscores')
        pray1.delete(0,END)
        pray1.insert(0,1)
        
    #HP
    try:
        hp = get_level('https://secure.runescape.com/m=hiscore_oldschool/overall?table=4&user=')
        hp1.delete(0,END)
        hp1.insert(0,hp)
    except:
        print('HP Not on Hiscores')
        hp1.delete(0,END)
        hp1.insert(0,1)
    #Strength
    try:
        strength = get_level('https://secure.runescape.com/m=hiscore_oldschool/overall?table=3&user=')
        str2.delete(0,END)
        str2.insert(0,strength)
    except:
        print('Strength Not on Hiscores')
        str2.delete(0,END)
        str2.insert(0,1)
    #Defence
    try:
        defence = get_level('https://secure.runescape.com/m=hiscore_oldschool/overall?table=2&user=')
        def2.delete(0,END)
        def2.insert(0,defence)
    except:
        print('Defence Not on Hiscores')
        def2.delete(0,END)
        def2.insert(0,1)

    #Magic
    try:
        magic = get_level('https://secure.runescape.com/m=hiscore_oldschool/overall?table=7&user=')
        mage1.delete(0,END)
        mage1.insert(0,magic)
    except:
        print('Magic Not on Hiscores')
        mage1.delete(0,END)
        mage1.insert(0,1)
    #Ranged
    try:
        ranged = get_level('https://secure.runescape.com/m=hiscore_oldschool/overall?table=5&user=')
        rng1.delete(0,END)
        rng1.insert(0,ranged)
    except:
        print('Ranged Not on Hiscores')
        rng1.delete(0,END)
        rng1.insert(0,1)
        
search_but = Button(root,text='SEARCH',width=11,font=('arial',16,'bold'), highlightbackground='#642b09',command = search_get)
search_but.grid(row=2,column=1,pady=12,padx=2)
#ADD WEBSCRAPER ##############################################################################

#PRAYER
pray = Label(root,text= 'PRAYER',font=('arial',16,'bold'),fg='white',bg='#642b09')
pray.grid(row=3,column=0)
pray1 = Entry(root, width=20, borderwidth=2,fg='#642b09')
pray1.grid(row=3,column=1)

#HP
hp = Label(root,text= 'HITPOINTS',font=('arial',16,'bold'),fg='white',bg='#642b09')
hp.grid(row=4,column=0)
hp1 = Entry(root, width=20, borderwidth=2,fg='#642b09')
hp1.grid(row=4,column=1,pady=3)

#DEF
def1 = Label(root,text= 'DEFENCE',font=('arial',16,'bold'),fg='white',bg='#642b09')
def1.grid(row=5,column=0)
def2 = Entry(root, width=20, borderwidth=2,fg='#642b09')
def2.grid(row=5,column=1)

#STR
str1 = Label(root,text= 'STRENGTH',font=('arial',16,'bold'),fg='white',bg='#642b09')
str1.grid(row=6,column=0)
str2 = Entry(root, width=20, borderwidth=2,fg='#642b09')
str2.grid(row=6,column=1,pady=3)

#ATT
att = Label(root,text= 'ATTACK',font=('arial',16,'bold'),fg='white',bg='#642b09')
att.grid(row=7,column=0)
att1 = Entry(root, width=20, borderwidth=2,fg='#642b09')
att1.grid(row=7,column=1)

#MAGE
mage = Label(root,text= 'MAGIC',font=('arial',16,'bold'),fg='white',bg='#642b09')
mage.grid(row=8,column=0)
mage1 = Entry(root, width=20, borderwidth=2,fg='#642b09')
mage1.grid(row=8,column=1,pady=3)

#RANGE
rng = Label(root,text= 'RANGE',font=('arial',16,'bold'),fg='white',bg='#642b09')
rng.grid(row=9,column=0)
rng1 = Entry(root, width=20, borderwidth=2,fg='#642b09')
rng1.grid(row=9,column=1)


#Presets
rng1.insert(0,1)
mage1.insert(0,1)
att1.insert(0,1)
str2.insert(0,1)
def2.insert(0,1)
hp1.insert(0,1)
pray1.insert(0,1)

#####################################################################
#CALCULATE

def calc():
    pray = float(pray1.get())/2
    hp = int(hp1.get())
    defence = int(def2.get())
    strength = int(str2.get())
    atk = int(att1.get())
    rng = int(rng1.get())
    mage = int(mage1.get())
    #BASE
    base = (defence + hp + pray)/4
    #MELEE
    melee = (strength + atk) *0.325
    #RANGE
    range2 = float(rng/2)
    range_final = 0.325*(range2 + rng)
    #MAGE
    mage2 = float(mage/2)
    mage_final = 0.325*(mage2 + mage)

    element = max(melee,range_final,mage_final)
    cmb = str(base + element)

    final = Label(root, text= f'Your Combat Level is: {cmb}',font=('arial',10,'bold'),fg='white',bg='#642b09')
    final.grid(row=12,column=0,columnspan=2)

    
calc = Button(root,text='CALCULATE',width=20,font=('arial',16,'bold'), highlightbackground='#642b09',command=calc)
calc.grid(row=10,column=0,pady=18,padx=2,columnspan=2)

root.mainloop()
