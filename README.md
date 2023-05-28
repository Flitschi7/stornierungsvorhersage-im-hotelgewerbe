##Stornierungsvorhersage im Hotelgewerbe
In diesem Projekt geht es darum, vorherzusagen, ob Hotelbuchungen storniert werden, um die Betriebsplanung zu optimieren und finanzielle Verluste zu minimieren. Wir nutzen verschiedene Machine Learning-Algorithmen wie Entscheidungsbäume (Random Forest), XGBoost und K-Nearest Neighbors (KNN).

#Projektbeschreibung
Unser Ziel ist es, genau vorherzusagen, ob eine Hotelbuchung storniert wird oder nicht. Dafür verwenden wir historische Buchungsdaten und berücksichtigen wichtige Faktoren wie den Buchungszeitpunkt, die Zimmerkategorie und vorherige Stornierungen. Unser Modell soll in der Lage sein, das Stornierungsverhalten der Kunden vorherzusagen. Dadurch können Hotels ihre Betriebsplanung verbessern und leere Zimmer vermeiden.

#Verwendete Algorithmen
Entscheidungsbäume mit Random Forest: Wir kombinieren mehrere Entscheidungsbäume, um genaue Vorhersagen zu treffen. Der Random Forest-Algorithmus berücksichtigt die Vorhersagen aller Bäume und liefert ein konsistentes Ergebnis.

XGBoost: Dieser Algorithmus basiert auf Entscheidungsbäumen und optimiert die Vorhersagen. XGBoost ist besonders effizient und liefert präzise Stornierungsvorhersagen.

K-Nearest Neighbors (KNN): KNN basiert darauf, dass ähnliche Buchungen oft die gleiche Klassenzugehörigkeit haben. Wir verwenden KNN, um Vorhersagen basierend auf den Mehrheitsklassen ähnlicher Buchungen zu treffen.

Hier wird bei Bedarf noch weiter entschieden, ob weitere algorithmen zur Evaluation zugezogen werden.

#Verwendung
Erforderlichen Abhängigkeiten mit pip install -r requirements.txt installieren.

Notebook "Stornierungsvorhersage.ipynb" ausführen, um den Datensatz zu laden, das Modell zu trainieren und Vorhersagen zu generieren.

Vorhersageergebnisse analysieren und bei Bedarf die Algorithmusparameter anpassen, um bessere Ergebnisse zu erzielen.

#Beitrag
Es bietet die Möglichkeit, die Stornierungsvorhersage im Hotelgewerbe zu verbessern und dadurch die Rentabilität und das Gästeerlebnis zu optimieren.
