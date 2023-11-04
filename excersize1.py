#!usr/bin/python3
"""
    Այս կոդը լիստը սորտավորելու համար է:
"""
def selection_sort_first(arr):
    """
        Այս ֆունկցիան ըստ աճման սորտավորում է առաջին 5 անդամները.
    """
    num = len(arr)
    for i in range(5):
        min_idx = i
        for j in range(i+1, 5):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
def selection_sort_last(arr):
    """
        Այս ֆունկցիան ըստ նվազման սորտավորում է վերջին 5 անդամները:
    """
    num = len(arr)
    for i in range(num-5, num):
        max_idx = i
        for j in range(i+1, num):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return arr
def selection_sort_middle(arr):
    """
        Այս ֆունկցիան փոխում է այն անդամների դիրքը որոնք գտնվում են
        առաջին 5 եւ վերջին 5 անդամների միջեւ:
    """
    num = len(arr)
    for i in range(5, num // 2):
        arr[i], arr[num - i - 1] = arr[num - i - 1], arr[i]
    return arr
def main():
    """
        Սա մեր հիմնական ֆունկցիան է որի մեջ մենք կանչում ենք բոլոր 
        մեր գրած ֆունկցիաները:
    """
    arr = list(map(int,input("Մուտքագրեք թվերը: ").split()))
    selection_sort_first(arr)
    selection_sort_last(arr)
    selection_sort_middle(arr)
    print(arr)
main()