import time
from mtablica import MonitorowanaTablica
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

################################################################
################################################################
def insertion_sort(tablica: MonitorowanaTablica):
    i = 1
    while i < len(tablica):
        j = i
        while j > 0 and tablica[j-1] > tablica[j]:
            tablica[j-1], tablica[j] = tablica[j], tablica[j-1]
            j -= 1
        i += 1

def shell_sort(tablica: MonitorowanaTablica):
    n = len(tablica)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = tablica[i]
            j = i
            while j >= gap and tablica[j - gap] > temp:
                tablica[j] = tablica[j - gap]
                j -= gap
            tablica[j] = temp
        gap //= 2


def bubble_sort(tablica: MonitorowanaTablica):
    n = len(tablica)
    for i in range(n):
        for j in range(0, n - i - 1):
            if tablica[j] > tablica[j + 1]:
                tablica[j], tablica[j + 1] = tablica[j + 1], tablica[j]

def merge_sort(tablica: MonitorowanaTablica):
    mergesort(tablica, 0, len(tablica) - 1)
def mergesort(tablica: MonitorowanaTablica, left, right):
    if right is None:
        right = len(tablica) - 1
    if left < right:
        middle = (left + right) // 2   # wyznaczanie środka
        mergesort(tablica, left, middle)
        mergesort(tablica, middle + 1, right)
        merge(tablica, left, middle, right)   # scalanie

def merge(tablica: MonitorowanaTablica, left, middle, right):
    """Łączenie posortowanych sekwencji."""
    n1 = middle - left + 1
    n2 = right - middle
    A = [None] * (n1 + 1)   # o jeden więcej
    B = [None] * (n2 + 1)   # o jeden więcej
    for i in range(n1):
        A[i] = tablica[left + i]
    for i in range(n2):
        B[i] = tablica[middle + 1 + i]
    A[n1] = float("inf")   # wartownik
    B[n2] = float("inf")   # wartownik
    i, j = 0, 0
    for k in range(left, right+1):
        if A[i] <= B[j]:
            tablica[k] = A[i]
            i += 1
        else:
            tablica[k] = B[j]
            j += 1


def quick_sort(tablica: MonitorowanaTablica):
    quicksort(tablica, 0, len(tablica) - 1)


def quicksort(tablica: MonitorowanaTablica, low, high):
    while low < high:
        pivot_index = partition(tablica, low, high)

        # Optymalizacja dla mniejszej części
        if pivot_index - low < high - pivot_index:
            quicksort(tablica, low, pivot_index - 1)
            low = pivot_index + 1
        else:
            quicksort(tablica, pivot_index + 1, high)
            high = pivot_index - 1


def partition(tablica: MonitorowanaTablica, low, high):
    pivot = tablica[high]
    i = low - 1

    for j in range(low, high):
        if tablica[j] <= pivot:
            i += 1
            tablica[i], tablica[j] = tablica[j], tablica[i]

    tablica[i + 1], tablica[high] = tablica[high], tablica[i + 1]
    return i + 1

# Wersja algorytmu Tim Sort w Pythonie

def insertion_sortts(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

def mergets(arr, left, mid, right):
    len_left = mid - left + 1
    len_right = right - mid

    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]

    i, j, k = 0, 0, left

    while i < len_left and j < len_right:
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

    while i < len_left:
        arr[k] = left_part[i]
        i += 1
        k += 1

    while j < len_right:
        arr[k] = right_part[j]
        j += 1
        k += 1

def tim_sort(arr):
    min_run = 32
    n = len(arr)

    for i in range(0, n, min_run):
        insertion_sortts(arr, i, min((i + min_run - 1), n - 1))

    size = min_run
    while size < n:
        for left in range(0, n, size * 2):
            mid = min((left + size - 1), (n - 1))
            right = min((left + size * 2 - 1), (n - 1))
            mergets(arr, left, mid, right)

        size *= 2



################################################################


################################################################
def plot_sorting_animation(tablica: MonitorowanaTablica, algorithm_name: str, fps=60):
    '''Plots the sorting animation for the given data.
    
    Args:
    tablica (MonitorowanaTablica): The array being sorted.
    algorithm_name (str): Name of the sorting algorithm.
    fps (int): Frames per second for the animation.
    '''
    plt.rcParams['font.size'] = 16
    fig, ax = plt.subplots(figsize=(16, 8))
    container = ax.bar(range(len(tablica)), tablica.pelne_kopie[0], align='edge', width=0.8)
    fig.suptitle(f'Sorting: {algorithm_name}')
    ax.set(xlabel='Index', ylabel='Value')
    ax.set_xlim([0, len(tablica)])
    txt = ax.text(0.01, 0.99, '', ha='left', va='top', transform=ax.transAxes)

    def update(frame: int):
        '''Updates the histogram for each frame of the animation.
        
        Args:
        frame (int): The current frame number.
        '''
        txt.set_text(f'Operations = {frame}')
        for rectangle, height in zip(container.patches, tablica.pelne_kopie[frame]):
            rectangle.set_height(height)
            rectangle.set_color('darkblue')

        idx, op = tablica.aktywnosc(frame)
        if op == 'get':
            container.patches[idx].set_color('green')
        elif op == 'set':
            container.patches[idx].set_color('red')

        return (txt, *container)

    ani = FuncAnimation(fig, update, frames=range(len(tablica.pelne_kopie)), blit=True, interval=1000./fps, repeat=False)
    plt.show()

################################################################


################################################################
def main():

    file = open("results.txt", "w")

    N = 50
    options = ['A', 'S', 'R', 'T']
    file.write(f"Number of elements: {N}\n")
    sort_functions = [insertion_sort, bubble_sort, shell_sort, merge_sort, quick_sort, tim_sort]
    for sort in sort_functions:
        file.write(f"\nSorting: {sort.__name__}\n")
        for option in options:
            array = MonitorowanaTablica(0, 1000, N, option)
            t0 = time.perf_counter()
            sort(array)
            delta_t = time.perf_counter() - t0
            file.write(f"{option}: Array sorted in {delta_t*1000:.1f} ms.Number of operations: {len(array.pelne_kopie):.0f}.\n")

    file.close()

if __name__ == '__main__':
    main()
