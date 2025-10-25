# DSA GIF Generator Scripts
# This script generates educational matplotlib-style GIFs for key algorithms
# GIFs are saved in the 'gifs' folder

import os
import heapq
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from PIL import Image as PILImage

os.makedirs('gifs', exist_ok=True)

def save_animation_checked(ani, n_frames, filename, fig=None):
    if n_frames <= 0:
        raise RuntimeError("No animation frames were generated.")
    if fig is None:
        fig = getattr(ani, '_fig', None)
    if fig is None:
        raise RuntimeError("Figure not available for saving animation.")
    if getattr(fig, 'canvas', None) is None:
        FigureCanvas(fig)
    fig.canvas.draw()
    ani.save(filename, writer='pillow')
    return filename

# ---------------- Bubble Sort GIF ----------------
def bubble_sort_gif(arr, filename='gifs/bubble_sort.gif'):
    arr_copy = arr.copy()
    states = []  # each state: (array_snapshot, highlight_indices)
    n = len(arr_copy)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
            states.append((arr_copy.copy(), (j, j + 1)))

    fig, ax = plt.subplots()
    ax.set_title('Bubble Sort')
    ax.set_ylim(0, max(arr) + 1 if arr else 1)
    bars = ax.bar(range(len(arr)), arr, color='skyblue')

    def update(frame):
        data, hi = states[frame]
        for idx, bar in enumerate(bars):
            bar.set_height(data[idx])
            bar.set_color('red' if idx in hi else 'skyblue')
        return list(bars)

    ani = animation.FuncAnimation(fig, update, frames=len(states), interval=500, blit=False, repeat=False)
    save_animation_checked(ani, len(states), filename, fig)
    plt.close(fig)

# ---------------- Binary Search GIF ----------------
def binary_search_gif(arr, target, filename='gifs/binary_search.gif'):
    low, high = 0, len(arr) - 1
    states = []  # each state: (low, high, mid)
    while low <= high:
        mid = (low + high) // 2
        states.append((low, high, mid))
        if arr[mid] == target:
            break
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    fig, ax = plt.subplots()
    ax.set_title('Binary Search')
    bars = ax.bar(range(len(arr)), arr, color='skyblue')
    ax.set_ylim(0, max(arr) + 1 if arr else 1)

    def update(frame):
        low, high, mid = states[frame]
        for idx, bar in enumerate(bars):
            if idx == mid:
                bar.set_color('green')
            elif low <= idx <= high:
                bar.set_color('yellow')
            else:
                bar.set_color('skyblue')
        return list(bars)

    ani = animation.FuncAnimation(fig, update, frames=len(states), interval=800, blit=False, repeat=False)
    save_animation_checked(ani, len(states), filename, fig)
    plt.close(fig)

# ---------------- Heap GIF ----------------
def heap_gif(arr, filename='gifs/heap.gif'):
    heap = []
    states = []  # list of heap snapshots
    for val in arr:
        heapq.heappush(heap, val)
        states.append(heap.copy())
    if heap:
        heapq.heappop(heap)
        states.append(heap.copy())

    max_n = max(1, len(arr))
    fig, ax = plt.subplots()
    ax.set_title('Min Heap Insert & Pop')
    ax.set_ylim(0, max(arr) + 1 if arr else 1)
    bars = ax.bar(range(max_n), [0] * max_n, color='skyblue')

    def update(frame):
        h = states[frame]
        for idx, bar in enumerate(bars):
            if idx < len(h):
                bar.set_visible(True)
                bar.set_height(h[idx])
                bar.set_color('skyblue' if frame < len(states) - 1 else 'red')
            else:
                bar.set_visible(False)
        return list(bars)

    ani = animation.FuncAnimation(fig, update, frames=len(states), interval=800, blit=False, repeat=False)
    save_animation_checked(ani, len(states), filename, fig)
    plt.close(fig)

# ---------------- Fibonacci Recursion GIF ----------------
def fibonacci_gif(n, filename='gifs/fibonacci.gif'):
    calls_snapshots = []

    def fib_record(k, calls):
        calls.append(k)
        calls_snapshots.append(calls.copy())
        if k <= 1:
            return k
        return fib_record(k - 1, calls.copy()) + fib_record(k - 2, calls.copy())

    fib_record(n, [])

    max_len = max(len(s) for s in calls_snapshots) if calls_snapshots else 0
    fig, ax = plt.subplots()
    ax.set_title('Fibonacci Recursion Tree')
    ax.set_ylim(0, max(max((max(s) if s else 0) for s in calls_snapshots), 1) + 1)
    bars = ax.bar(range(max_len), [0] * max_len, color='skyblue')

    def update(frame):
        calls = calls_snapshots[frame]
        for idx, bar in enumerate(bars):
            if idx < len(calls):
                bar.set_visible(True)
                bar.set_height(calls[idx])
                bar.set_color('skyblue')
            else:
                bar.set_visible(False)
        return list(bars)

    ani = animation.FuncAnimation(fig, update, frames=len(calls_snapshots), interval=500, blit=False, repeat=False)
    save_animation_checked(ani, len(calls_snapshots), filename, fig)
    plt.close(fig)

# ---------------- Merge Sort GIF ----------------
def merge_sort_gif(arr, filename='gifs/merge_sort.gif'):
    arr_copy = arr.copy()
    states = []  # snapshots of full array; highlight index updated

    def merge_sort(a, l=0):
        if len(a) > 1:
            m = len(a) // 2
            L = a[:m]
            R = a[m:]
            merge_sort(L, l)
            merge_sort(R, l + m)
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    a[k] = L[i]; i += 1
                else:
                    a[k] = R[j]; j += 1
                arr_copy[l + k] = a[k]
                states.append((arr_copy.copy(), l + k))
                k += 1
            while i < len(L):
                a[k] = L[i]; arr_copy[l + k] = a[k]
                states.append((arr_copy.copy(), l + k))
                i += 1; k += 1
            while j < len(R):
                a[k] = R[j]; arr_copy[l + k] = a[k]
                states.append((arr_copy.copy(), l + k))
                j += 1; k += 1

    merge_sort(arr_copy)
    if not states:
        states.append((arr_copy.copy(), -1))

    fig, ax = plt.subplots()
    ax.set_title('Merge Sort')
    ax.set_ylim(0, max(arr) + 1 if arr else 1)
    bars = ax.bar(range(len(arr_copy)), arr_copy, color='skyblue')

    def update(frame):
        data, hi = states[frame]
        for idx, bar in enumerate(bars):
            bar.set_height(data[idx])
            bar.set_color('red' if idx == hi else 'skyblue')
        return list(bars)

    ani = animation.FuncAnimation(fig, update, frames=len(states), interval=500, blit=False, repeat=False)
    save_animation_checked(ani, len(states), filename, fig)
    plt.close(fig)

# ---------------- Quick Sort GIF ----------------
def quick_sort_gif(arr, filename='gifs/quick_sort.gif'):
    arr_copy = arr.copy()
    states = []  # snapshots of full array; optionally highlight range/pivot

    def quick_sort(a, lo=0):
        if len(a) <= 1:
            return a
        pivot = a[len(a) // 2]
        left = [x for x in a if x < pivot]
        middle = [x for x in a if x == pivot]
        right = [x for x in a if x > pivot]
        sorted_left = quick_sort(left, lo)
        sorted_right = quick_sort(right, lo + len(left) + len(middle))
        combined = sorted_left + middle + sorted_right
        for i, val in enumerate(combined):
            arr_copy[lo + i] = val
            states.append((arr_copy.copy(), lo + i))
        return combined

    quick_sort(arr_copy)
    if not states:
        states.append((arr_copy.copy(), -1))

    fig, ax = plt.subplots()
    ax.set_title('Quick Sort')
    ax.set_ylim(0, max(arr) + 1 if arr else 1)
    bars = ax.bar(range(len(arr_copy)), arr_copy, color='skyblue')

    def update(frame):
        data, hi = states[frame]
        for idx, bar in enumerate(bars):
            bar.set_height(data[idx])
            bar.set_color('red' if idx == hi else 'skyblue')
        return list(bars)

    ani = animation.FuncAnimation(fig, update, frames=len(states), interval=500, blit=False, repeat=False)
    save_animation_checked(ani, len(states), filename, fig)
    plt.close(fig)

# ---------------- DFS & BFS GIF ----------------
def dfs_bfs_gif(graph, start, filename='gifs/dfs_bfs.gif'):
    nodes = list(graph.keys())
    visited = []
    states = []  # snapshots: list of visited nodes at each step

    def dfs(node):
        visited.append(node)
        states.append(visited.copy())
        for nbr in graph.get(node, []):
            if nbr not in visited:
                dfs(nbr)

    dfs(start)
    if not states:
        states.append([])

    fig, ax = plt.subplots()
    ax.set_title('DFS & BFS')
    ax.set_ylim(0, 1.5)
    bars = ax.bar(nodes, [0] * len(nodes), color='skyblue')

    def update(frame):
        vis = states[frame]
        for idx, n in enumerate(nodes):
            bars[idx].set_height(1 if n in vis else 0)
            bars[idx].set_color('red' if (n in vis and n == vis[-1]) else ('gray' if n in vis else 'skyblue'))
        return list(bars)

    ani = animation.FuncAnimation(fig, update, frames=len(states), interval=700, blit=False, repeat=False)
    save_animation_checked(ani, len(states), filename, fig)
    plt.close(fig)

# ---------------- Example Usage ----------------
if __name__ == '__main__':
    bubble_sort_gif([64, 34, 25, 12])
    binary_search_gif([10, 20, 30, 40, 50], 30)
    heap_gif([5, 2, 8, 1])
    fibonacci_gif(6)
    merge_sort_gif([38, 27, 43, 3, 9, 82, 10])
    quick_sort_gif([3, 6, 8, 10, 1, 2, 1])
    dfs_bfs_gif({0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2]}, 0)