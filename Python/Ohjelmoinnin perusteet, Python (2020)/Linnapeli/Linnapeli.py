#otetaan käyttöön satunnaisuus
import random
import json

def tallennaPeli(pelaaja):
    print(pelaaja)
    with open("tallennus.json","w") as f:
        kopio = dict(pelaaja)
        kopio['kartta'] = {}
        json.dump(kopio, f)

def lataaPeli():
    pelaaja = None

    with open("tallennus.json") as f:
        pelaaja = json.load(f)
    
    return pelaaja
    
def tulostaKartta(kartta):
    pelialue = 5
    tuntematon = "."

    for x in range(pelialue):
        for y in range(pelialue):            
            if (x,y) in kartta:
                print(kartta[(x,y)], end="")
            else:
                print(tuntematon, end="")
        print()
    
def luePakotettuSyote(alku, vaihtoehdot):
    
    kehote = alku+str(vaihtoehdot)
    action = input(kehote)
    while action not in vaihtoehdot:
        action = input(kehote)
    print()
    return action
    
def taistelu(pelaaja, vihollinen):
    nimi = vihollinen['nimi']
    vihuHP = vihollinen['HP']
    vihuATK = vihollinen['ATK']
    pelaajaATK = pelaaja['ATK']
    pelaajaHP = pelaaja['HP']

    print("Tunnistat mörön olevan perus",nimi,"ja taistelu alkaa!")
    print()

    if "rautatanko" in pelaaja['inv']:
        print("Otat rautatankosi esille ja hyökkäysvoimasi kasvaa +2")
        pelaajaATK = pelaajaATK+2

    vihuPuolustus = False
    hyokkaysPenalty = 0
    
    while pelaajaHP > 0 and vihuHP > 0:
        print("Sinulla on",pelaajaHP,"elämää. Vihollisellasi",nimi,"on",vihuHP)
        puolustaa = False
        
        print("""1: Hyökkää
2: Puolusta""")
        action = int(luePakotettuSyote("Kokonaisluku:", ["1","2"]))

        #Pelaajan vuoro
        if action == 1:
            adjektiivit = ["raivokkaasti", "nokkelasti"]
            
            if vihuPuolustus:
                hyokkaysPenalty = vihuATK
            else:
                hyokkaysPenalty = 0
            print("Hyökkäät " + random.choice(adjektiivit)+ " ja teet",pelaajaATK-hyokkaysPenalty,"vahinkoa")
            vihuHP = vihuHP - (pelaajaATK - hyokkaysPenalty)
        if action == 2:
            print("Otat suojaavan asennon ja valmistaudut vihollisen iskuun.")
            puolustaa = True


        #Vihollisen vuoro
        if random.randint(0,1) == 0:
            dmg = vihuATK
            if puolustaa:
                #dmg = dmg - pelaajaATK
                dmg -= pelaajaATK
                
            if dmg < 0:
                dmg = 0
            
            #pelaajaHP = pelaajaHP - dmg
            pelaajaHP -= dmg
            print(vihollinen,"hyökkää kimppuusi ja tekee",dmg,"vahinkoa.")
            vihuPuolustus = False
        else:
            print(vihollinen," ottaa puolustavan asennon ja valmistautuu seuraavaan iskuusi.")
            vihuPuolustus = True
            
    return pelaaja['HP'] > 0

def vampyyritaistelu(pelaaja):
    import vampyyri
    pelaaja['alue'] = 7
    tallennaPeli(pelaaja)
    
    print("Huoneen kaikki kynttilät, soihdut ja sähkölamput syttyvät yht'aikaisesti aiheuttaen sokaisevan valon.")
    print("Kun näet taas hieman, huomaat edessäsi seisovan vampyyrin, joka katsoo sinua nälkäisesti.")
    print("Valmistaudut viimeiseen taistoon vampyyrin kanssa. Tämä on se hetki, johon olet valmistautunut koko linnaseikkailun ajan!")

    while True:
        try:
            vampyyri.hyokkaa()
        except Exception:
            print("Nostat mielesi suojat pystyyn vampyyrin oudon taian torjumiseksi. Vampyyrin taika epäonnistuu!")
        vampyyri.vahingoita()            
    
    
def alue1(pelaaja):    
    print ("""Tervetuloa pelaamaan Vampyyripeliä!
    Olet vamppyyrimetsästäjä ja kuulit, että läheisesä linnassa on vamppyyri.
    Lähdet metsästämään sitä.""")
    print()
    pelaaja['kartta'][(0,3)] = "|"
    tulostaKartta(pelaaja['kartta'])
    print("Seisot vanhan linnan edessä. Näet suljetun oven. Voit liikkua itään, jossa on vaja.")
    #-merkkiä seuraavat merkit eivät kuulu koodiin, vaan ovat ns. kommentteja.
    #Kommenttien tarkoitus on antaa lisätietoa koodia lukevalle ihmiselle
    #N == pohjoiseen
    #E = itään
    #S = etelään
    #W = länteen

    suunta = input("Mitä teet? (N,E,S,W)")

    #Tässä ehto on käännetty, jotta yltiöpäisiltä sisennyksiltä vältytään.
    #Jos suunta ei ole "E", suorita lohko (joka sulkee ohjelman)
    #""" tarkoittaa monirivistä merkkijonoa
    if suunta != "E":
        print("""Lähdit haparoimaan pimeyteen. Kompastuit puun juureen ja löit pääsi. 
              Kyläläiset eivät enää ikinä nähneet sinua.""")
        exit()

    #Käyttäjä syötti "E", koska ohjelmaa ei vielä suljettu; peli siis jatkuu
    pelaaja['kartta'][(0,4)] = "V"
    tulostaKartta(pelaaja['kartta'])
    print("Vaja on pimeä, mutta näet nurkassa kimaltelevan avaimen.")
    action = luePakotettuSyote("Mitä teet?", ['Palaa takaisin', 'ota avain'])
        
    if action == 'Palaa takaisin':
        print("Lähdit kävelemään ulos ovesta ...")
        exit()
        
    print("Otit avaimen. Se tuntuu painavalta.")
    #Tässä luodaan uusi muuttuja nimeltään avain ja asetetaan sen arvoksi True, koska pelaajalla on nyt avan hallussaan
    pelaaja['inv'].append("Avain")
    for yritys in range(3):
        action = input("Minneköhän se mahtaisi mahtua?")
        if action != "Linnan oveen":
           print("Keksit kokeilla avainta lähimpään oveen. Avain syttyy tuleen käsissäsi hetkeksi.")
           print("Avain vaikuttaisi kestävän enää",(3-yritys),"syttymistä.")
        else:
            break
    else:
        print("Avain syttyi niin monta kertaa tuleen, että se suli.")
        pelaaja['inv'].remove("Avain")
        
    if "Avain" not in pelaaja['inv']:
        print("Jostain syystä sinulla ei olekaan avainta.")
        exit()
        
    print("""Palaat linnan eteen ja kokeilet avainta oveen.
    Se mahtuu täydellisesti ja ovi avautuu äänekkäästi naristen.""")
    alue2(pelaaja)

#Eka aula
def alue2(pelaaja):
    pelaaja['kartta'][(1,3)] = "|"
    pelaaja['kartta'][(2,3)] = "+"
    pelaaja['alue'] = 2
    tallennaPeli(pelaaja)
    
    tulostaKartta(pelaaja['kartta'])
    print("""Astuessasi aulaan kaikki aulan soihdut syttyvät kuin taikaiskusta ja ovi sulkeutuu takanasi PAM!
          Järkytyksestä toivuttuasi huomaat usvaisen hahmon aulan keskellä.""")
    action = input("Mitä teet? ('Tutki hahmo', 'Pakene')")

    if action == 'Tutki hahmo':
        print("""Astelet usvan luo. Lähestyessäsi usvaa se alkaa saada ihmismäistä muotoa.
    Kävelet hahmoa parin metrin päähän ja huomaat lattialla rautatangon. Nostatko sen?""")
        if input("Otatko sen? ('K','E')") == "K":
            pelaaja['inv'].append('Rautatanko')
            print("""Nappaat rautatangon.
    Usvasta kuuluu pahaenteistä sihinää ja lähdet juoksemaan lähimpään huoneeseen.""")
    if action == 'Pakene':
        print("Lähdet juoksemaan lähimpään huoneeseen!")
    alue3(pelaaja)

#Sivuhuone
def alue3(pelaaja):
    pelaaja['kartta'][(2,4)] = "o"
    pelaaja['alue'] = 3
    tallennaPeli(pelaaja)
    tulostaKartta(pelaaja['kartta'])
    
    print("""Hengästyneenä suljet oven takanasi ja silmäilet hieman huonetta.
    Seinillä on paljon tauluja ja hämähäkkien seittejä.
    Näet ikkunana alla laatikoston ja takaseinällä vaatetangon.
    Aulakin tuntuu jo rauhoittuneen.""")
    action = luePakotettuSyote("Mitä teet?", ["Tutki laatikosto", "Palaa aulaan"])
       
    if (action == "Tutki laatikosto"):
        print("""Löydät laatikostosta sekalaista rompetta ja pienen lasipullon, jossa on salaperäistä läpinäkyvää nestettä.
    Saat huoneesta pahat vibat ja palaat aulaan.""")
        pelaaja['inv'].append("Pyhävesi")

    if action == "Palaa aulaan":
        print("Sinulla ei ole aikaa tutkia huonetta enempää ja palaat aulaan.")
    alue4(pelaaja)

#Toka aula, eka taistelu
def alue4(pelaaja):
    tulostaKartta(pelaaja['kartta'])
    pelaaja['alue'] = 4
    tallennaPeli(pelaaja)
    
    #Otetaan satunnaisesti 50% mahdollisuudella mörkö katosta tai ovesta
    if random.randint(0,1) == 0:
        print("Näet liikkuvan varjon katossa, joka tipahtaa eteesi!")
    else:
        print("Linnan toisesta huoneesta aulaan syöksyy pelottava mörkö!")

    tulos = taistelu(pelaaja, {'nimi':"limalöllö", 'HP':10, 'ATK':1})
    if tulos:
        print("Olet voitokas!")
    else:
        print("Hävisit taistelun etkä onnistunut pelastamaan kylää vampyyrilta.")
        exit()

    print()
    print("Olet täynnä uhoa ja koet olevasi valmis taistelemaan pahaa vampyyria vastaan. ")
    print("Ainoa ongelma on, ettet aivan tiedä missä vampyyri on.")
    print("Näet aulassa portaat jotka kohoavat ylimpään kellotorniin.")
    print("Näet aulassa pienet heiluvaiset kierreportaat, jotka laskeutuvat pimeään katakombiin.")
    action = luePakotettuSyote("Mitä teet?",["Mene ylös", "Mene alas"])
    if action == "Mene ylös":
        alue5(pelaaja)
    else:
        alue6(pelaaja)


#Kellotorni
def alue5(pelaaja):
    pelaaja['kartta'][(2,2)] = "^"
    pelaaja['alue'] = 5
    pelaaja['paikat'].append("Kellotorni")
    tallennaPeli(pelaaja)
    
    print("Lähdet kipuamaan portaita kellotorniin. Jalkasi alkavat jo mennä maitohapoille kun kuulet pahaenteisen ulinan.")
    print()
    print()
    print("Saavut kellotorniin ja maailma välähtää valkoisena ja tunnet ruumiisi tärisevän ukkosen jylinästä.")
    print("Näkösi hieman palautuessa huomaat laihan ihmismäisen hahmon huoneen nurkassa ja vaikuttaisi AAAHH SE HYÖKKÄÄ")

    tulostaKartta(pelaaja['kartta'])

    ##TODO: tulos on aina None 
    tulos = taistelu(pelaaja, {'nimi':"luuranko", 'HP':8, 'ATK':2})
    if tulos:
        print("Luuranko hajoaa tomuksi ja huomaat tomukasasta kimallusta.")
        action = luePakotettuSyote("Otatko esineen?",["K","E"])
        if action == "K":
            pelaaja['inv'].append('Riipus')
            print("Seulot tomukasan läpi hämärässä ja saat kouraasi hopeisen riipuksen.")
        else:
            print("Et halua koskea likaisen luurangon jämiin. Mysteerinen tuuli puhaltaa tomukasan pois.")
    else:
        print("Luuranko oli voitokas ja sinä hävisit.")
        exit()

    print("Huomaat tornissa massiivisen kivioven, jossa on vampyyrin kuva.")
    action = luePakotettuSyote("Avaatko oven?",["K","E"])
    if action == "K":
        if "Katakombit" in pelaaja['paikat']:
            vampyyritaistelu()
        else:
            #Ei vampyyria; ansa
            print("Astut huoneeseen ja huomaat huoneen keskellä suuren arkun.")
            print("Lähestyt arkkua varvasti ja päästessäsi lähelle arkkua kuulet kovan naksahduksen ja säikähdät kovasti.")
            print("Mitään ei kuitenkaan tunnu tapahtuvan joten jatkat arkulle.........")
            print(".....")
            print("Arkku on TYHJÄ!")
            print("Nostaessasi pääsi arkusta kolautat sen matalaan kattokruunuun... hmm, kattokruunu ei tainnut olla näin alhaalla aikaisemmin.")
            print("Huomaat myös, että seinät liikkuvat hitaasti kasaan! Sinulla on vain hetki aikaa.")
            action = input("Sinulla on:"+str(pelaaja['inv'])+". Minkä valitset?")
            if(action == "Pyhävesi"):
                print("Heität paniikissa pyhän vetesi arkkuun. Arkun pohja alkaa sulaa ja sulanut reikä on tarpeeksi iso, jotta pääset pakenemaan.")
                pelaaja['inv'].remove("Pyhävesi")
                alue4(pelaaja)
            elif action == "Rautatanko":
                print("Olet katsonut paljon elokuvia ja laitat rautatankosi seinien väliin. Rautatanko on tarpeeksi vahva rikkomaan seinän mekanismin mutta tanko hajoaa prosessissa.")
                pelaaja['inv'].remove("Rautatanko")
                alue4(pelaaja)
            else:
                print("Et keksi mitä teet kyseisellä tavaralla. Seinät murskaavat sinut. Loppu.")
                exit()
            
            
    else:
        print("Et uskalla avata ovea ja palaat aulaan.")
        alue4(pelaaja)

def alue6(pelaaja):
    pelaaja['alue'] = 6
    pelaaja['paikat'].append("Katakombit")
    tallennaPeli(pelaaja)
    pelaaja['kartta'][(3,2)] = "v"
    tulostaKartta(pelaaja['kartta'])

    print("Katakombit ovat pimeät, etkä oikein näe kunnolla.")
    if "Riipus" in pelaaja['inv']:
        print("Riipuksesi alkaa hohtaa ja valaisee tien hautakammioon, jossa punamusta arkku.")
    else:
        tulos = taistelu(pelaaja, {'nimi':random.choice(["Varjo","Lepakko","Hämähäkki", "Rotta"]), 'HP':10, 'ATK':2})
        #Tarina jatkuu
        
    if "Kellotorni" in pelaaja['paikat']:
            vampyyritaistelu()
    else:
            print("Harhailet katakombeissa ikuisuudelta tuntuvan ajan. Lopulta löydät tiesi takaisin lähtöpisteeseen ja palaat aulaan.")

##Peli alkaa
pelaaja = None
if luePakotettuSyote("Ladataanko peli?",["K","E"]) == "K":
    pelaaja = lataaPeli()

if pelaaja == None:
    #Pelaaja ei lataa peliä
    pelaaja = {'ATK':3,
               'HP': 10,
               'inv': [],
               'kartta': {},
               'alue':1,
               'nimi':"",
               'paikat':[]
        }
            
    pelaaja['nimi'] = input("Vampyyrimetsästäjä, mikä on nimesi?")
    
    alue1(pelaaja)
else:
    ##Voidaan myös tallentaa metodiviittaukset listaan ja kutsua oikeaa metodia
    #alueet = [alue1,alue2,alue3,alue4,alue5,alue6]
    #alueet[pelaaja['alue']-1]()
    
    #Pelaaja lataa pelin
    if pelaaja['alue'] == 1:
        alue1(pelaaja)
    elif pelaaja['alue'] == 2:
        alue2(pelaaja)
    elif pelaaja['alue'] == 3:
        alue3(pelaaja)
    elif pelaaja['alue'] == 4:
        alue4(pelaaja)
    elif pelaaja['alue'] == 5:
        alue5(pelaaja)
    elif pelaaja['alue'] == 6:
        alue6(pelaaja)
    elif pelaaja['alue'] == 7:
        vampyyritaistelu(pelaaja)
        
#[-..--]
#[--.--]
#[-----]

##kartta = {
##(0,1) : "."
##(0,2) : "."
##(1,2) : "."
##}
