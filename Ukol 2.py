sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

soucastka = input("Zadej kod soucastky: ")
mnozstvi = int (input ("Zadej mnozstvi:"))

if soucastka in sklad and mnozstvi <= {sklad[soucastka]}:
    print(f'{soucastka} je na sklade v dostatecnem mnozstvi, objednavka se bude expedovat.')
    nove_mnozstvi = soucastka in {sklad[soucastka]} - [mnozstvi] 
    sklad.update(nove_mnozstvi) 
    print(sklad)
    if soucastka in sklad and mnozstvi > {sklad[soucastka]}:
        print(f'{soucastka} je na sklade v omezenem mnozstvi {sklad[soucastka]} kusu. Chcete pokracovat v objednavce?')
else:  
    print(f'Bohuzel, produkt {soucastka} neni na sklade.')