<a href="https://raw.githubusercontent.com/MareSeestern/VineLeafDisease/master/res/IMG_2417.JPG?token=AK7DBRW6IEW2N3ABYX6NDZ27ND43U" title="vine" alt="vine"></a>

---

# Heart Failure

> Erkennen von der Präsenz einer Herzkrankheit

> Erstellt von: Maria-Theresa Licka und Mario Schweikert

---

## Table of Contents 

- [Projektbeschreibung](#Projektschreibung)
- [Inhalt](#Inhalt)
- [Setup](#Setup)


---

## Projektbeschreibung
Insgesamt leiden 1,8 Millionen Menschen in Deutschland an einer Herzinsuffizienz. Damit ist eine Herzschwäche mit 400 Tausend Fällen im Jahre der häufigste Grund für eine Aufnahme in das Krankenhaus. Dies zeigt, wie aktuell das Thema auch heute noch, trotz medizinischen Fortschrittes, ist.  Es ist sehr wichtig, eine Herzinsuffizienz bei allen Menschen frühzeitig  zu erkennen, denn wird eine Herzinsuffizienz rechtzeitig erkannt, steigt die Lebenserwartung deutlich. Mithilfe von künstlicher Intelligenz soll eine regelmäßige Untersuchung, zum Beispiel in Seniorenheimen, ohne Arzt möglich werden. Ein Laie kann Kreislaufparameter, z.B Puls, in eine Eingabemaske am Computer eingeben. Das „machine learning“ Modell, welches mit Tensorflow realisiert wird, analysierts die Werte und fällt dann eine Entscheidung, basierend auf alten Patientendaten. So kann der Laie dann entscheiden, ob eine Untersuchung beim Arzt nötig ist. Mit der Methode kann eine regelmäßige Untersuchung gewährleistet werden. 
---

## Inhalt

Unser Projekt lässt sich in folgende Parts unterteilen:
- Python Datei, um missing values zu ergänzen
- Python Notebook, um das Modell zu trainieren, testen und anschließend zu speichern.
- Python Datei, um eine Eingabemaske mit Tkinter anzuzeigen und auszuwerten.


# Clone

- Klone dieses Repository mit Hilfe von GitHub Desktop oder über den Browser auf Deine lokale Maschiene.

# Setup
Wir nutzen als Programme Anaconda. 

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
$ cd train
$ python train_model.py
```



--

## Support

Wir sind hier zu finden:

- Website at <a href="google.com" target="_blank">`EINFÜGEN`</a>
- Youtube at <a href="https://www.youtube.com/channel/UCsGZt4UtInZ01tBjM1B-FbQ?view_as=subscriber" target="_blank">`INFOrmAtIc Teens`</a>


---


