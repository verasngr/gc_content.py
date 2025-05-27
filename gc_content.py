#gc_content.py 
def calcola_gc_content(nome_file):
    with open(nome_file, 'r') as f:
        righe = f.readlines()

    intestazione = righe[0].strip()
    sequenza = ''.join([riga.strip() for riga in righe[1:]])

    g = sequenza.count('G')
    c = sequenza.count('C')
    gc_content = (g + c) / len(sequenza) * 100

    print("ID:", intestazione[1:])
    print("Lunghezza sequenza:", len(sequenza))
    print("GC Content:", round(gc_content, 2), "%")

# Esempio d’uso:
# calcola_gc_content("sequenza.fasta")
