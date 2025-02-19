def umsatzrechner():
    berechnungen = []
    try:
        while True:  #Schleifenbeginn
            try:
                netto= float(input("Geben sie Nettobetrag an :\n" ))
                if netto <= 0 :
                    print("Sie sollen nur positive Zahlen eingeben")
                    continue # Springt zum Anfang der Schleife
            
                mwst=0.19
                brutto = netto + (netto*mwst)
               
                # Berechnung speichern
                berechnung= {"Netto": netto,
                             "Brutto": brutto,
                             "MWST_betrag": brutto - netto}
                
                berechnungen.append(berechnung)

                # Liste auf 2 Einträge begrenzen
                if len(berechnungen) > 2:
                    berechnungen.pop(0)
            
                print(f"Ihr Bruttobetrag beträgt jetzt {brutto:.2f} €")
                #{brutto:.2f} zeigt die 2 nachkommastellen
                
                for i,b in enumerate(berechnungen):
                    print(f"{i+1}: Netto: {b['Netto']:.2f} €, Brutto: {b['Brutto']:.2f} €, MWST: {b['MWST_betrag']:.2f} €")
                # enumerate gibt die Position des Elements in der Liste zurück
                # enumerate = 1: Netto: 1000.00 €, Brutto: 1190.00 €, MWST: 190.00 €
                # 1 wird addiert, da die Positionen bei 0 beginnen

                reset = input("Wollen Sie noch eine Rechnung machen? (ja/nein)")
                if reset.lower() != "ja":# lower macht die Eingabe klein
                    print("Auf Wiedersehen")
                    break # Beendet die Schleife
            except ValueError:
                print("Ungültige Eingabe: Bitte nur Zahlen verwenden")

    except KeyboardInterrupt:
        print("\nProgramm wurde beendet")

if __name__ == "__main__": # Wird IMMER ausgeführt, auch wenn die Datei importiert wird
    umsatzrechner()