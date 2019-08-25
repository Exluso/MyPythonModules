Modulo di esercizio.
Serve a gestire file DSV, ossia file txt che fanno il verso ai CSV ma usano 3 Dash come separatore.
separatore: "---"
il primo campo di ogni riga termina con un TAB "\t" per facilitare la lettura.

ACQUIRELINE()
La prima funzione AcquireLine serve per importare come lista i dati di una specifica linea del file,
identificata dal primo campo (considera il TAB)

TO DO: farle ritornare una lista di valori, il cui primo valore non abbia il TAB 