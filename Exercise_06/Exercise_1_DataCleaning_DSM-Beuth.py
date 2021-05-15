import pandas as pd
import numpy as np

#csv von externer Quelle laden
url="data/dsm-beuth-edl-demodata-dirty.csv"
df = pd.read_csv(url)

print("\nStep 0: Daten ausgeben")
print(df)

print("Analyse: % fehlende Daten:")
missing_values_count = df.isnull().sum()
total_cells = np.product(df.shape)
total_missing = missing_values_count.sum()
print((total_missing/total_cells) * 100)

# ---------------- 1 ----------------------------------
# als erstes loesche ich die Spalten "id" und "full_name",
# weil diese aus meiner Sicht redundant sind
# denn die jeweiligen Infos sind durch den Index
# und die Spalten "first_name" und "last_name" gegeben

print("\nStep 1: loesche redundante Spalten")
df_clean = df.drop(['id', 'full_name'], axis=1)
print(df_clean)

# ---------------- 2 ----------------------------------
# als naechtes loesche ich die Zeilen die jetzt noch mehr als 1 NaN enthalten

print("\nStep 2: loesche Zeilen mit NaN > 1")
df_clean = df_clean.dropna(axis=0, thresh=1)
print(df_clean)

# ---------------- 3 ----------------------------------
# Dublikate loeschen

print("\nStep 3: loesche Dublikate")
df_clean = df_clean.drop_duplicates()
print(df_clean)

# ---------------- 4 ----------------------------------
# Strings in Spalte "age" ersetzen
print("\nStep 4: 'old' mit hoechsten Wert ersetzen")

df_clean['age'] = df_clean['age'].replace(['old'],pd.to_numeric(df_clean['age'], errors='coerce').max() )
print(df_clean)

# ---------------- 5 ----------------------------------

# den Betrag der Spalte age ausgeben, um negative Werte zu invertieren
print("\nStep 5: negative Altersangaben invertieren")
df_clean['age'] = pd.to_numeric(df_clean['age'], errors='coerce').abs()
print(df_clean)


# ---------------- 6 ----------------------------------

# NaN Werte mit einem leeren String ersetzen
print("\nStep 6: statt NaN leeren String")
df_clean = df_clean.fillna('')
print(df_clean)


# ---------------- 7 ----------------------------------

#Bereinigte Daten in neue CSV schreiben
df_clean.to_csv("cleaned-data.csv", sep='\t', encoding='utf-8')


# ---------------- 8 ----------------------------------

#Bereinigte Datei analysieren
df_final = pd.read_csv("cleaned-data.csv")
missing_values_count = df_final.isnull().sum()
total_cells = np.product(df_final.shape)
total_missing = missing_values_count.sum()
print("\nAnalyse: % fehlende Daten in dem bereinigten Datensatz:")
print((total_missing/total_cells) * 100)
