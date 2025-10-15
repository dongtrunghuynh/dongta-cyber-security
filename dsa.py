# DSA GIF Generator Scripts
# This script generates educational matplotlib-style GIFs for key algorithms
# GIFs are saved in the 'gifs' folder

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os
import heapq

os.makedirs('gifs', exist_ok=True)

# ---------------- Bubble Sort GIF ----------------
def bubble_sort_gif(arr, filename='gifs/bubble_sort.gif'):
    fig, ax = plt.subplots()
    bars = ax.bar(range(len(arr)), arr, color='skyblue')
    ax.set_title('Bubble Sort')

    frames = []
    arr_copy = arr.copy()
    n = len(arr_copy)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr_copy[j] > arr_copy[j+1]:
                arr_copy[j], arr_copy[j+1] = arr_copy[j+1], arr_copy[j]
            for idx, bar in enumerate(bars):
                bar.set_height(arr_copy[idx])
                bar.set_color('red' if idx in [j,j+1] else 'skyblue')
            frames.append([bar for bar in bars])

    ani = animation.ArtistAnimation(fig, frames, interval=500, repeat=False)
    ani.save(filename, writer='pillow')
    plt.close()

# ---------------- Binary Search GIF ----------------
def binary_search_gif(arr, target, filename='gifs/binary_search.gif'):
    fig, ax = plt.subplots()
    bars = ax.bar(range(len(arr)), arr, color='skyblue')
    ax.set_title('Binary Search')

    low, high = 0, len(arr)-1
    frames = []

    while low <= high:
        mid = (low+high)//2
        for idx, bar in enumerate(bars):
            if idx == mid:
                bar.set_color('green')
            elif low <= idx <= high:
                bar.set_color('yellow')
            else:
                bar.set_color('skyblue')
        frames.append([bar for bar in bars])
        if arr[mid] == target:
            break
        elif arr[mid] < target:
            low = mid+1
        else:
            high = mid-1

    ani = animation.ArtistAnimation(fig, frames, interval=800, repeat=False)
    ani.save(filename, writer='pillow')
    plt.close()

# ---------------- Heap GIF ----------------
def heap_gif(arr, filename='gifs/heap.gif'):
    fig, ax = plt.subplots()
    ax.set_title('Min Heap Insert & Pop')
    heap = []
    frames = []

    for val in arr:
        heapq.heappush(heap, val)
        ax.clear()
        ax.set_title('Min Heap Insert')
        ax.bar(range(len(heap)), heap, color='skyblue')
        frames.append([ax.bar(range(len(heap)), heap, color='skyblue')])

    heapq.heappop(heap)
    ax.clear()
    ax.set_title('Min Heap Pop')
    ax.bar(range(len(heap)), heap, color='red')
    frames.append([ax.bar(range(len(heap)), heap, color='red')])

    ani = animation.ArtistAnimation(fig, frames, interval=800, repeat=False)
    ani.save(filename, writer='pillow')
    plt.close()

# ---------------- Fibonacci Recursion GIF ----------------
def fibonacci_gif(n, filename='gifs/fibonacci.gif'):
    fig, ax = plt.subplots()
    ax.set_title('Fibonacci Recursion Tree')
    frames = []
    calls = []

    def fib(k):
        calls.append(k)
        frame = ax.bar(range(len(calls)), calls, color='skyblue')
        frames.append([bar for bar in frame])
        if k <=1:
            return k
        return fib(k-1) + fib(k-2)

    fib(n)
    ani = animation.ArtistAnimation(fig, frames, interval=500, repeat=False)
    ani.save(filename, writer='pillow')
    plt.close()

# ---------------- Merge Sort GIF ----------------
def merge_sort_gif(arr, filename='gifs/merge_sort.gif'):
    fig, ax = plt.subplots()
    ax.set_title('Merge Sort')
    bars = ax.bar(range(len(arr)), arr, color='skyblue')
    frames = []

    def merge_sort(arr, start_idx=0):
        if len(arr) >1:
            mid = len(arr)//2
            L = arr[:mid]
            R = arr[mid:]
            merge_sort(L, start_idx)
            merge_sort(R, start_idx+mid)
            i=j=k=0
            while i < len(L) and j < len(R):
                if L[i]<R[j]: arr[k]=L[i]; i+=1
                else: arr[k]=R[j]; j+=1
                bars[k].set_height(arr[k])
                bars[k].set_color('red')
                frames.append([bar for bar in bars])
                k+=1
            while i < len(L): arr[k]=L[i]; bars[k].set_height(arr[k]); bars[k].set_color('red'); frames.append([bar for bar in bars]); i+=1;k+=1
            while j < len(R): arr[k]=R[j]; bars[k].set_height(arr[k]); bars[k].set_color('red'); frames.append([bar for bar in bars]); j+=1;k+=1
    merge_sort(arr)
    ani = animation.ArtistAnimation(fig, frames, interval=500, repeat=False)
    ani.save(filename, writer='pillow')
    plt.close()

# ---------------- Quick Sort GIF ----------------
def quick_sort_gif(arr, filename='gifs/quick_sort.gif'):
    fig, ax = plt.subplots()
    bars = ax.bar(range(len(arr)), arr, color='skyblue')
    frames = []

    def quick_sort(arr, start_idx=0):
        if len(arr) <=1:
            return arr
        pivot = arr[len(arr)//2]
        left = [x for x in arr if x<pivot]
        middle = [x for x in arr if x==pivot]
        right = [x for x in arr if x>pivot]
        sorted_left = quick_sort(left, start_idx)
        sorted_right = quick_sort(right, start_idx+len(left)+len(middle))
        combined = sorted_left + middle + sorted_right
        for idx, val in enumerate(combined):
            bars[start_idx+idx].set_height(val)
            bars[start_idx+idx].set_color('red')
        frames.append([bar for bar in bars])
        return combined

    quick_sort(arr)
    ani = animation.ArtistAnimation(fig, frames, interval=500, repeat=False)
    ani.save(filename, writer='pillow')
    plt.close()

# ---------------- DFS & BFS GIF ----------------
def dfs_bfs_gif(graph, start, filename='gifs/dfs_bfs.gif'):
    fig, ax = plt.subplots()
    ax.set_title('DFS & BFS')
    nodes = list(graph.keys())
    visited = []
    frames = []

    # Simple DFS animation
    def dfs(node):
        visited.append(node)
        ax.clear()
        ax.set_title('DFS Traversal')
        ax.bar(nodes, [1 if n in visited else 0 for n in nodes], color=['red' if n==node else 'skyblue' for n in nodes])
        frames.append([ax.bar(nodes, [1 if n in visited else 0 for n in nodes], color=['red' if n==node else 'skyblue' for n in nodes])])
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    dfs(start)
    ani = animation.ArtistAnimation(fig, frames, interval=700, repeat=False)
    ani.save(filename, writer='pillow')
    plt.close()

# ---------------- Example Usage ----------------
if __name__ == '__main__':
    bubble_sort_gif([64,34,25,12])
    binary_search_gif([10,20,30,40,50], 30)
    heap_gif([5,2,8,1])
    fibonacci_gif(6)
    merge_sort_gif([38,27,43,3,9,82,10])
    quick_sort_gif([3,6,8,10,1,2,1])
    dfs_bfs_gif({0:[1,2],1:[0,3],2:[0,3],3:[1,2]}, 0)
