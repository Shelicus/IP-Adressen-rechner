class ip4v:
    def __init__(self):
        # speicherung der einzelnen Teile als self von der IP
        try:
            self.erster_teil = int(ip.split('.')[0])
            self.zweiter_teil = int(ip.split('.')[1])
            self.dritter_teil = int(ip.split('.')[2])
            self.vierter_teil = int(ip.split('.')[3])
            self.netzwerks_bits = int(netzwerks_bits)
        except:
            print("\nDas Eingegebene ist nicht legitim!")
            exit(-1)

        #ob es sich um eine IP-Adresse handelt
        abfrage_eins = self.klasse()
        abfrage_zwei = self.klasse_ip()
        abfrage_drei = self.ip_controll()
        if abfrage_eins == -1 or abfrage_zwei == -1 or abfrage_drei == -1:
            print("\nDie IP-Adresse ist nicht legitim!")
            exit(-1)

        #Ausführung der Berechnung:
        self.ausfuehrung()


#Zur Kontrolle ob es sich um eine IPv4 Adresse handelt
    def ip_controll(self):
        if self.erster_teil < 0 or self.erster_teil > 255 or self.zweiter_teil < 0 or self.zweiter_teil > 255 or self.dritter_teil < 0 or self.dritter_teil > 255 or self.vierter_teil < 0 or self.vierter_teil > 255:
            return -1

    def klasse(self):
        if self.netzwerks_bits <= 16:
            return "\nNetzklasse: A"
        elif self.netzwerks_bits <= 24:
            return "\nNetzwerksklasse: B"
        elif self.netzwerks_bits <= 31:
            return "\nNetzwerksklasse: C"
        elif self.netzwerks_bits == 0:
            return 0
        else:
            return -1

    def klasse_ip(self):
        if self.erster_teil == 127:
            return -1
        elif self.erster_teil <= 126:
            return "\nNetzklasse: A"
        elif self.erster_teil <= 191:
            return "\nNetzwerksklasse: B"
        elif self.erster_teil <= 223:
            return "\nNetzwerksklasse: C"
        else:
            return -1

    #Berechnung der einzelnen Teile der IPv4 Adresse:
    def ausfuehrung(self):
        # Klasse feststellung
        klasse = self.klasse()
        if klasse == -1:
            klasse = self.klasse_ip()
            print(klasse)
        else:
            print(klasse)

        # Abfrage, ob privat oder öffentlich
        netz_raum = self.netz_art()
        print(netz_raum)

        #Umwandlung der IP-Adresse in binär
        bin = self.bin()
        print("\nDie IP-Adresse in bin.: "+bin)

        #Erstellung der CIDR-Maske
        cidr_maske = self.cidr()
        print("Die CIDR-Maske der IP: "+cidr_maske)

        #Erstellung der Net-IP-bin
        net_ip_bin = self.net_ip_bin()
        print("Die Net-Ip Binär ist: "+net_ip_bin)

        #Erstellung der Net-IP-dez
        net_ip_dez = self.net_ip_dez()
        print("Die Net-Ip Dezimal ist: "+net_ip_dez)

        #Erstellung der niedrigsten Host-IP bin
        min_host_ip_bin = self.min_host_bin()
        print("Die Niedrigste Host-Ip in Binär ist: "+min_host_ip_bin)

        # Erstellung der niedrigsten Host-IP dez
        min_host_ip_dez = self.min_host_dez()
        print("Die Niedrigste Host-Ip in Dezimal ist: " + min_host_ip_dez)

        # Erstellung der höchsten Host-IP bin
        max_host_ip_bin = self.max_host_bin()
        print("Die Höchste Host-Ip in Binär ist: " + max_host_ip_bin)

        # Erstellung der höchste Host-IP dez.
        max_host_ip_dez = self.max_host_dez()
        print("Die Höchste Host-Ip in Dezimal ist: " + max_host_ip_dez)

    def netz_art(self):
        if self.erster_teil == 10:
            return "Es Handelt sich um 1 Privates Netz (2^24-2 = 16.777.214 Host-Adressen)!"
        elif self.erster_teil == 172 and self.zweiter_teil >= 16 and self.zweiter_teil <= 31:
            return "Es Handelt sich um 16 Private Netze (2^20-2 = 1.048.574 Host-Adressen)!"
        elif self.erster_teil == 192 and self.zweiter_teil == 168:
            return "Es Handelt sich um 256 Private Netze (2^16-2 = 65.534 Host-Adressen)!"
        else:
            return "Es Handelt sich um ein öffentliches Netz!"

    def bin(self):
        bin_adresse = []
        punkt_counter = 0
        vier_teile = [self.erster_teil, self.zweiter_teil, self.dritter_teil, self.vierter_teil]

        for x in range(4):
            berechnung = True
            zu_berechnen = vier_teile[x]
            variabel = []
            teil = ""
            counter = 0
            while berechnung == True:
                if zu_berechnen % 2 == 1:
                    variabel.append("1")
                    counter = counter+1
                elif zu_berechnen % 2 == 0:
                    variabel.append("0")
                    counter = counter+1
                zu_berechnen = zu_berechnen // 2
                if zu_berechnen == 1:
                    variabel.append("1")
                    counter = counter+1
                    zu_berechnen = 0
                if zu_berechnen == 0:
                    if counter < 8:
                        for t in range(8-counter):
                            variabel.append("0")
                    berechnung = False
            for p in range(len(variabel)-1, 0, -1):
                    teil = teil+variabel[p]
            teil = teil+variabel[0]
            punkt_counter = punkt_counter+1
            if punkt_counter <= 3:
                teil = teil+"."
            bin_adresse.append(teil)

        bin_adresse_sendung = ""

        for n in range(4):
            bin_adresse_sendung = bin_adresse_sendung+bin_adresse[n]
        return bin_adresse_sendung

    def cidr(self):
        zaehler = 1
        cidr_maske = "1"
        for x in range(self.netzwerks_bits-1):
            if zaehler == 8:
                cidr_maske = cidr_maske+"."
                zaehler = 0
            cidr_maske = cidr_maske+"1"
            zaehler = zaehler+1
        nullen = 32 - self.netzwerks_bits
        for x in range(nullen):
            if zaehler == 8:
                cidr_maske = cidr_maske+"."
                zaehler = 0
            cidr_maske = cidr_maske+"0"
            zaehler = zaehler + 1
        return cidr_maske

    def net_ip_bin(self):
        net_ip = ''

        for x in range(4):
            if len(self.bin().split('.')[x]) < 8:
                for p in range(8-len(self.bin().split('.')[x])):
                    self.bin().split('.')[x] = '0'+self.bin().split('.')[x]

        for x in range(4):
            for p in range(8):
                if self.bin().split('.')[x][p] == '1' and self.cidr().split('.')[x][p] == '1':
                    net_ip = net_ip+'1'
                else:
                    net_ip = net_ip+'0'
            net_ip = net_ip+'.'
        net_ip = net_ip[:-1]
        return net_ip

    def net_ip_dez(self):
        counter = 0

        net_ip_dez = ""
        for i in range(4):
            variable = 0

            multiplikator = 1
            for x in range(7, 0, -1):
                zahl = int(self.net_ip_bin().split('.')[i][x])
                variable = variable+zahl*multiplikator
                multiplikator = multiplikator*2
            zahl = int(self.net_ip_bin().split('.')[i][0])
            variable = variable + zahl * multiplikator
            net_ip_dez = net_ip_dez+str(variable)
            counter = counter+1
            if counter <= 3:
                net_ip_dez = net_ip_dez+"."

        return net_ip_dez

    def min_host_bin(self):
        net_ip = self.net_ip_bin()
        net_ip = net_ip[:-1]
        min_host_ip_bin = net_ip + '1'
        return min_host_ip_bin

    def min_host_dez(self):
        return self.net_ip_dez().split('.')[0]+"."+self.net_ip_dez().split('.')[1]+"."+self.net_ip_dez().split('.')[2]+"."+str(int(self.net_ip_dez().split('.')[3])+1)


    def max_host_bin(self):
        ein_teil = self.net_ip_bin().split('.')[1]+self.net_ip_bin().split('.')[2]+self.net_ip_bin().split('.')[3]

        liste = []
        for x in range(len(ein_teil)):
            liste.append(ein_teil[x])

        for p in range(23, self.netzwerks_bits - 9, -1):
            liste[p] = "1"

        teil = ""
        counter = 0
        for x in range(len(liste)):
            teil = teil+liste[x]
            counter = counter+1
            if counter == 8:
                counter = 0
                teil = teil + "."

        max_host_ip_bin = self.net_ip_bin().split('.')[0]+"."+teil
        max_host_ip_bin = max_host_ip_bin[:-2]
        max_host_ip_bin = max_host_ip_bin+"0"
        return max_host_ip_bin

    def max_host_dez(self):                     #Ja ich weiß, ich hätte die obere Definition umschreiben können und zwei mal verwenden können. Aber hier musste ich nur zwei Dinger umändern um es so zu nutzen.
        counter = 0
        net_ip_dez = ""
        for i in range(4):
            variable = 0

            multiplikator = 1
            for x in range(7, 0, -1):
                zahl = int(self.max_host_bin().split('.')[i][x])
                variable = variable + zahl * multiplikator
                multiplikator = multiplikator * 2
            zahl = int(self.max_host_bin().split('.')[i][0])
            variable = variable + zahl * multiplikator
            net_ip_dez = net_ip_dez + str(variable)
            counter = counter + 1
            if counter <= 3:
                net_ip_dez = net_ip_dez + "."

        return net_ip_dez

if __name__ == "__main__":
    netzwerks_bits = input("Gebe mir die Anzahl der Netzwerksbits an: ")
    ip = input("Gebe bitte die IP Adresse an: ")
    start = ip4v()
