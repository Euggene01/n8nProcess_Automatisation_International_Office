# Process Automatisation International Office
## Ausgangslage & Problem
Im International Office der Philipps-Universität-Marburg musste die Zimmerzuteilung für Austauschstudierende manuell durchgeführt werden.

Das Problem: Die Daten lagen in zwei getrennten Excel-Listen vor. Mitarbeiter mussten die E-Mail-Adressen manuell anhand der Personalnummer (Pers.-Nr.) suchen.
Es gab massive Medienbrüche bei der Erstellung der E-Mails wegen unterschiedlicher Vorlagen für Erasmus und Overseas. Der Prozess war zeitaufwändig und fehleranfällig.
### Ist-Zustand (Manueller Prozess mit Medienbrüchen)
![Ist-Zustand](https://raw.githubusercontent.com/Euggene01/n8nProcess_Automatisation_International_Office/f587e96afe68219b739d2c63abb142eab20eb8da/Process_Automatisation_International_Office/BPMN%202.0/istProzess.svg)
Zwei Mitarbeiter, getrennte Listen, manuelle E-Mail-Erstellung
## Zielsetzung
Entwicklung eines automatisierten Workflows zur Zusammenführung der Daten, dynamischen Generierung von zweisprachigen E-Mails (DE/EN) und automatischen Zustellung via SMTP ohne manuellen Eingriff.
## Wirtschaftlichkeitsbetrachtung
**Ist-Zustand (Manueller Prozess):**
Die Vorbereitung (Öffnen der zwei Excel-Tabellen und der E-Mail-Vorlage) dauert ca. 1 Minute. Für jeden Studierenden werden ca. 3 Minuten zum Ausfüllen der Vorlage sowie 30 Sekunden für die Qualitätskontrolle benötigt. Das ergibt 3,5 Minuten pro Person (= 0,0583 Stunden).

Bei einem Stundenlohn einer studentischen Hilfskraft von 14,50 € kostet die Benachrichtigung eines Studierenden 0,84 €.
Ausgehend von 400 Austauschstudierenden pro Jahr (200 pro Semester) bedeutet das für die Universität einen reinen Verwaltungsaufwand von 23,33 Stunden bzw. 338 € pro Jahr (bei Einsatz einer studentischen Hilfskraft, deren Stundensatz etwa die Hälfte eines festangestellten Mitarbeiters beträgt).

**Soll-Zustand (Automatisierter Prozess):**
Durch den automatisierten n8n-Workflow reduziert sich der Aufwand auf ca. 2 Minuten pro Durchlauf (hauptsächlich für den Start und die finale Kontrolle). Bei zwei Durchläufen pro Jahr sind das lediglich 4 Minuten.

**Ergebnis:**
Die benötigte Zeit sinkt von 23,33 Stunden auf 4 Minuten pro Jahr. Das entspricht einer Reduzierung des manuellen Aufwands um 99,4% und einer Beschleunigung des Prozesses um das 350-fache. Die Universität spart dadurch jährlich über 23 Stunden Arbeitszeit und mindestens 336 € Personalkosten für repetitive, fehleranfällige Tätigkeiten.

### Soll-Zustand (Automatisierter n8n-Workflow)
![Soll-Zustand](https://raw.githubusercontent.com/Euggene01/n8nProcess_Automatisation_International_Office/b29e10e2e62207422d902eeaf017cada17710536/Process_Automatisation_International_Office/BPMN%202.0/sollProzess.svg)
Automatisches Mergen, dynamische Logik für Erasmus/Overseas, Loop für alle Datensätze
## Technologie Wahl
Für die Umsetzung dieses Prototyps wurde bewusst n8n gewählt. n8n ist eine Open-Source-Plattform für Workflow-Automatisierung, die sich besonders für die Digitalisierung von einfachen, linearen Geschäftsprozessen eignet.
**Warum nicht andere Tools?**
Zapier / Make.com: Diese Tools sind hervorragend für SaaS-Integrationen, aber sie sind cloudbasiert (Datenschutzbedenken bei Studentendaten) und verursachen bei zunehmender Komplexität hohe monatliche Abo-Kosten.
Reine Python/Java-Skripte: Ein reines Skript ist schwerer zu warten, wenn die Person, die es geschrieben hat, das Team verlässt. n8n bietet eine visuelle Dokumentation des Prozesses, die auch von Nicht-Programmierern verstanden wird.
## Technische Umsetzung
![Technische Umsetzung](https://github.com/Euggene01/n8nProcess_Automatisation_International_Office/raw/main/Process_Automatisation_International_Office/Screenshots/n8n_workflow.jpg?raw=true)
Die Business-Logik ist in der Datei email_generator.py implementiert.
## Prerequisites & Installation
1. Voraussetzungen:

Ein n8n-Account (Cloud) oder eine lokale n8n-Instanz.

Zwei Excel-Tabellen (eine für Zimmerdaten, eine für Kontaktdaten). Beide müssen die Spalte Pers.-Nr. enthalten.

Ein E-Mail-Konto mit SMTP-Zugang (z. B. eine Testadresse oder das Universitätskonto).

2. Daten vorbereiten:

Variante A (n8n Cloud): Laden Sie die beiden Excel-Tabellen in Ihren Google Drive hoch.

Variante B (Lokales n8n): Legen Sie die beiden Excel-Tabellen im lokalen Dateisystem ab.

3. Workflow importieren und ausführen:

Laden Sie die .json Datei aus diesem Repository herunter.

Öffnen Sie Ihre n8n-Instanz und klicken Sie oben rechts auf "Import from File". Wählen Sie die heruntergeladene JSON-Datei aus.

Credentials einrichten: Klicken Sie auf den Knoten Google Drive (oder Read File), um sich mit Ihrem Google-Konto zu verbinden. Klicken Sie auf den Knoten Send Email, um Ihre SMTP-Zugangsdaten (Host, Port, User, Passwort) einzugeben.

Testlauf: Klicken Sie oben rechts auf "Execute Workflow". Der Prozess liest die Daten ein, führt den Merge durch, generiert die E-Mails und versendet sie.

Sicherheitshinweis für den Test: Ändern Sie im Knoten Send Email das Feld To Email temporär auf Ihre eigene E-Mail-Adresse, um zu prüfen, ob das Layout und die Logik (Erasmus vs. Overseas) korrekt funktionieren, bevor Sie echte E-Mails an Studierende senden.

