# 🔢 Sorting Algorithms Visualizer – AlgoBeats

A visually rich Python application using **Pygame** to animate and compare popular sorting algorithms with sound, themes, and interaction.

---

## 🎯 Features

- ✅ **6 Sorting Algorithms**
  - Bubble, Insertion, Selection, Merge, Quick, Heap
- 🔼🔽 **Ascending / Descending Toggle**
- 🎨 **Theme Toggle** (`T` key) with colorful gradient bars
- ⏱️ **Live Timer** during sorting + total runtime
- ⌨️ **Keyboard Shortcuts** for control
- 🎚️ **Speed Control** (`+ / -`)

---

## 🖥️ Tech Stack

- Python 3.x
- [Pygame](https://www.pygame.org/)

---

## 🚀 How to Run

```bash
pip install pygame
python main.py
```

### Sorting Algorithm Summaries
1. Bubble Sort
   - Start from the first element in the list.
   - Compare each pair of adjacent elements (arr[i] and arr[i+1]).
   - If the left element is greater, swap them (to move the larger one right).
   - After the first full pass, the largest element "bubbles" to the end.
   - Repeat the process for the remaining unsorted part of the list.
   - Continue until no swaps are needed — the list is now sorted.
2. Insertion Sort
   - Assume the first element is already sorted.
   - Take the next element (key) and compare it with elements in the sorted section (to its left).
   - Shift elements to the right until you find the correct position for key.
   - Insert the key at that position.
   - Repeat this for all elements until the entire list is sorted.
3. Selection Sort
   - Start with the full list as the unsorted portion.
   - Find the smallest element in the unsorted portion.
   - Swap it with the first unsorted element.
   - Move the boundary of the sorted section one step right.
   - Repeat until the list is fully sorted.
4. Merge Sort
   - Divide the list into two halves recursively until each sublist has one element.
   - Merge the sublists back together in sorted order.
   - While merging, compare the smallest available elements from both halves.
   - Place the smaller element into the merged list, then continue.
   - Final result is a fully sorted merged list.
5. Quick Sort
   - Choose a pivot element (commonly the last, first, or middle).
   - Partition the list: move smaller elements left of pivot, larger to the right.
   - Recursively apply the same process to left and right sublists.
   - Do not include the pivot in the recursive calls (it’s already in place).
   - Continue until all sublists are sorted.
6. Heap Sort
   - Build a max-heap from the unsorted list (largest element at root).
   - Swap the root with the last element and reduce heap size.
   - Heapify the root again to maintain max-heap property.
   - Repeat until all elements have been moved to the end in sorted order.
   - Result: sorted list in ascending order.
