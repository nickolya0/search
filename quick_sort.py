import buble_sort
import binary_search
import merge
import quick_sort_
import time
    
def vergleichZeitMessung(list):
    print()
    print()
    begin = time.time()
    buble_sort.bubbleSort(list)
    ende = time.time()
    print("bubbleSort - Zeit: ", ende-begin)
    list = list2.copy()
    
    begin = time.time()
    list.sort()
    binary_search.binary_search(list,1)
    ende = time.time()
    print("index gefunden war: ", ende-begin)
    list = list2.copy()

    begin = time.time()
    merge.merge_sort(list)
    ende = time.time()
    print("merge_sort Zeit: ", ende-begin)
    list = list2.copy()

    begin = time.time()
    quick_sort_.quick_sort(0,len(list)-1, list)
    ende = time.time()
    print("quick_sort Zeit: ", ende-begin)
    list = list2.copy()

    begin = time.time()
    list.sort()
    ende = time.time()
    print("Mit def .sort(): ", ende-begin)
    list = list2.copy()

list = [i for i in range(900, 1, -1)]
list2 = list.copy()

x = 1
while x != 0:
    print("eingeben '1' für: - Bubble sort -\neingeben '2' für: - Binary Suchung -\neingeben '3' für: - Merge sort -\neingeben '4' für: - Quick sort -\neingeben '5' für: - Sort() -\neingeben '6' für: - List init -\neingeben '7' für: - wie List aussieht -\neingeben '8' für: - vergleichen Sort -")
    auswahl = int(input("_______: "))

    begin = time.time()

    match auswahl:
        case 1:
            print(buble_sort.bubbleSort(list))
            list = list2.copy()
        case 2:
            list.sort()
            print("gefunden, index ist: ", binary_search.binary_search(list,1))
            list = list2.copy()
        case 3:
            print(merge.merge_sort(list))
            list = list2.copy()
        case 4:
            quick_sort_.quick_sort(0,len(list)-1, list)
            print(list)
            list = list2.copy()
        case 5:
            list.sort()
            print(list)
            list = list2.copy()
        case 6:
            print(list)
            list = list2.copy()
        case 7:
            print(list)
        case 8:
            vergleichZeitMessung(list)
            break
        case _: break
        

    ende = time.time()
    print("Zeit: ", ende-begin)

