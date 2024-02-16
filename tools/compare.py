import csv
import sys

def main(file1, file2):
    csv1_dict = {}
    csv2_dict = {}

    csv.field_size_limit(100000000)

    with open(file1, 'r', newline='', encoding='utf-8') as csvfile1:
        reader1 = csv.reader(csvfile1, delimiter=';')
        next(reader1)  
        for row in reader1:
            csv1_dict[row[0]] = row
            

    with open(file2, 'r', newline='', encoding='utf-8') as csvfile2:
        reader2 = csv.reader(csvfile2, delimiter=';')
        next(reader2)
        for row in reader2:
            csv2_dict[row[0]] = row

    differences = []

    for id_key in csv2_dict.keys():
        if id_key not in csv1_dict:
            differences.append(f"L'ID {id_key} est présent uniquement dans le deuxième fichier.")

    if differences:
        print("Différences trouvées :")
        for diff in differences:
            print(diff)
    else:
        print("Aucune différence trouvée entre les fichiers CSV.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python compare.py file1.csv file2.csv")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
