
![logo](https://github.com/MareSeestern/HeartFailure/blob/master/res/Logo_neu.jpg?raw=true)
---

# Heart Failure

> Erkennen von der Präsenz einer Herzkrankheit

> Erstellt von: Maria-Theresa Licka und Mario Schweikert

---

## Table of Contents 

- [Projektbeschreibung](#Projektschreibung)
- [Inhalt](#Inhalt)
- [Setup](#Setup)
- [Support](#Support)

---

## Projektbeschreibung

Insgesamt leiden 1,8 Millionen Menschen in Deutschland an einer Herzinsuffizienz. Damit ist eine Herzschwäche mit 400 Tausend Fällen im Jahre der häufigste Grund für eine Aufnahme in das Krankenhaus. Dies zeigt, wie aktuell das Thema auch heute noch, trotz medizinischen Fortschrittes, ist.  Es ist sehr wichtig, eine Herzinsuffizienz bei allen Menschen frühzeitig  zu erkennen, denn wird eine Herzinsuffizienz rechtzeitig erkannt, steigt die Lebenserwartung deutlich. Mithilfe von künstlicher Intelligenz soll eine regelmäßige Untersuchung, zum Beispiel in Seniorenheimen, ohne Arzt möglich werden. Ein Laie kann Kreislaufparameter, z.B Puls, in eine Eingabemaske am Computer eingeben. Das „machine learning“ Modell, welches mit Tensorflow realisiert wird, analysierts die Werte und fällt dann eine Entscheidung, basierend auf alten Patientendaten. So kann der Laie dann entscheiden, ob eine Untersuchung beim Arzt nötig ist. Mit der Methode kann eine regelmäßige Untersuchung gewährleistet werden. 

---

## Inhalt

Unser Projekt lässt sich in folgende Parts unterteilen:
- Python Datei, um missing values zu ergänzen.
- Python Notebook, um das Modell zu trainieren, testen und anschließend zu speichern.
- Python Datei, um eine Eingabemaske mit Tkinter anzuzeigen und auszuwerten.

---
# Clone

- Klone dieses Repository mit Hilfe von GitHub Desktop oder über den Browser auf Deine lokale Maschiene und entpacke die .zip Datei.

# Setup

Wir nutzen als Programme Anaconda und zum Ausführen die Anaconda Prompt. Öffne diese dazu über das Start-Menü und navigiere anschließend mit "cd" zu dem Entpackten Repository.


---
## Datensatz
Der Datensatz liegt als .csv Datei im "Train" Ordner. Source: <a href="https://archive.ics.uci.edu/ml/datasets/Heart+Disease">https://archive.ics.uci.edu/ml/datasets/Heart+Disease</a>

Creators:

1. Hungarian Institute of Cardiology. Budapest: Andras Janosi, M.D.
2. University Hospital, Zurich, Switzerland: William Steinbrunn, M.D.
3. University Hospital, Basel, Switzerland: Matthias Pfisterer, M.D.
4. V.A. Medical Center, Long Beach and Cleveland Clinic Foundation: Robert Detrano, M.D., Ph.D. 

## Trainieren von dem Modell (Datensatz benötigt)

> Installieren von den nötigen Bibliotheken in "Anaconda Prompt"

```shell
$ pip install -r requirements.txt
```

> Nun kann das Training über folgenden Befehl gestartet werden:

```shell
$ cd Train
$ python heart_disease_training.py
```

---

## Ausführen von dem User Interface (Datensatz benötigt)

> Installieren von den nötigen Bibliotheken in "Anaconda Prompt"

```shell
$ pip install -r requirements.txt
```

> Nun kann das UI über folgenden Befehl gestartet werden:

```shell
$ cd Auswertungsprogramm
$ python Auswertung_programm.py
```
Wir haben in dem Ordner /Auswertungsprogramm auch ein Tabellendokument mit Beispiel Personen hinterlegt. Gerne können diese Werte zum Testen eingesetzt werden.

---
## Support

Wir sind hier zu finden:

- Website at <a href="https://matheli.github.io/Herzinsuffizienz/" target="_blank">`Erkennung einer Herzinsuffizienz mit KI`</a>
- Youtube at <a href="https://www.youtube.com/channel/UCsGZt4UtInZ01tBjM1B-FbQ?view_as=subscriber" target="_blank">`INFOrmAtIc Teens`</a>


---


