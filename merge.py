def merge_sort(liste):
    if len(liste) < 2:  # Abbruchbedingung, um die Rekursion beenden zu können
        return liste
    mitte = len(liste) // 2

    # print("Aktuelle Liste: ", liste)

    linkeListe = liste[:mitte]
    rechteListe = liste[mitte:]

    # print("Aktuelle linke Liste: ", linkeListe)
    # print("Aktuelle rechte Liste", rechteListe)

    merge_sort(linkeListe)
    merge_sort(rechteListe)

    return merge(liste, linkeListe, rechteListe)



# Hausaufgabe: Den Mergesort zu Ende programmieren und verstehen :)

def merge(liste, l, r):
    index = 0
    indexL = 0
    indexR = 0
    while indexL < len(l) and indexR < len(r):
        if l[indexL] <= r[indexR]:
            liste[index] = l[indexL]
            indexL+=1
        else:
            liste[index] = r[indexR]
            indexR +=1
        index += 1
    while indexL < len(l):
        liste[index] = l[indexL]
        index += 1
        indexL += 1
    while indexR < len(r):
        liste[index] = r[indexR]
        index += 1
        indexR += 1
    return liste

# merge_sort([54,26,93,17,77,31,44,55,20])