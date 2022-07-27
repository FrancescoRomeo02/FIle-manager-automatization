# DESCRIZIONE

Programma per il controllo costante di una o più cartelle e la gestione dei file che si trovano in esse, in particoalre lo "smistamento" dei file aggiunti nella/e cartella/e osservata/e in diverse sottocartelle.

# IMPORTANTE
## librerie richieste per l'esecuzione:
Per l'esecuzione del programma è richiesta l'installazione di alcune librerie python: <br>
- dotenv: pip3 install python-dotenv [link](https://pypi.org/project/python-dotenv/)<br>
- watchdog: pip3 install watchdog [link](https://pypi.org/project/watchdog/)

## Path dei file che si vogliono gestire:
Per eseguire il programma è necessario creare un file .env ed inizializzare al suo interno le varibaili come segue:<br>
- PATH_TO_SCAN = percorso da scannerizzare <br>
- PATH_IMAGE = percorso della cartella delle immagini <br>
- PATH_VIDEO = percorso della cartella dei video <br>
- PATH_DOCUMENTS = percorso della cartella dei documenti <br>
- PATH_COMPRESSED = percorso della cartella dei file compressi <br>
- PATH_EXECUTABLES = percorso della cartella dei file eseguibili <br>
- PATH_NOT_RECOGNIZED = percorso della cartella dei file non riconosciuti <br>
Se non hai voglai di scrvere ecco il [link](https://github.com/FrancescoRomeo02/FIle-manager-automatization/blob/main/demo.env)per scaricare un file .env preconfigurato.
## Esecuzione automatica
Per eseguire automaticamente il programma è necessario creare un link al file .vbs all'interno della cartella: <br>
C:\Users\'NOME UTENTE'\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
