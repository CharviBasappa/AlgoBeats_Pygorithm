# 🔢 Sorting Algorithms Visualizer – AlgoBeats

A visually rich Python application using **Pygame** to animate and compare popular sorting algorithms with sound, themes, and interaction.

---

## 🎯 Features

- ✅ **6 Sorting Algorithms**
  - Bubble, Insertion, Selection, Merge, Quick, Heap
- 🔼🔽 **Ascending / Descending Toggle**
- 🎨 **Theme Toggle** (`T` key) with colorful gradient bars
- ⏱️ **Live Timer** during sorting
- ⌨️ **Keyboard Shortcuts** for control
- 🎚️ **Speed Control** (`+ / -`)

---

## 🖥️ Tech Stack

- Python 3.x
- [Pygame](https://www.pygame.org/)

---

## 🎮 Controls

| Key          | Action                          |
|--------------|----------------------------------|
| SPACE      | Start sorting                    |
| R          | Reset list                       |
| O          | Replay last unsorted list        |
| A / D    | Ascending / Descending order     |
| T          | Toggle themes                    |
| + / -    | Speed up / slow down             |
| B          | Bubble Sort                      |
| I          | Insertion Sort                   |
| S          | Selection Sort                   |
| Q          | Quick Sort                       |
| M          | Merge Sort                       |
| H          | Heap Sort                        |

---

## 📁 Project Structure

```plaintext
AlgoBeats/                   # Root project folder for the visualizer
│
│── main.py                  # Main Pygame loop, input handling, and sorting control
│── sorts.py                 # All sorting algorithm implementations (as generators)
│── visualizer.py            # Drawing functions: bars, text, themes, timer, etc.
│── settings.py              # Global settings: screen size, themes, color gradients
│── data.py                  # Generates random data for sorting
│── visualsort.py            # (Optional) Preview or test mode logic
│── README.md                # Full project documentati
```

---

## 🚀 How to Run

```bash
pip install pygame
python main.py
```

---

## 🎨 UI Preview

Here’s how the Visualizer looks:

### Intro View
<img src="https://github.com/CharviBasappa/AlgoBeats_Pygorithm/blob/main/screenshots/Intro.png?raw=true" width="600"/>

### Selection Sort with Theme (ASC)
<img src="https://github.com/CharviBasappa/AlgoBeats_Pygorithm/blob/main/screenshots/SelectionSort_Theme_ASC.png?raw=true" width="600"/>

### Selection Sort with Theme (DESC)
<img src="https://github.com/CharviBasappa/AlgoBeats_Pygorithm/blob/main/screenshots/SelectionSort_Theme_DESC.png?raw=true" width="600"/>


---

## 📚 Sorting Algorithm Summaries

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
  
---

## 👤 Author

Made with 💙 by [Charvi Basappa](https://github.com/CharviBasappa)

If you liked this project, feel free to ⭐ the repo and share it!

---

## 🤝 Contributions

If you’d like to contribute to **AlgoBeats**, feel free to:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some feature'`)
5. Push to the branch (`git push origin feature-name`)
6. Open a pull request

---

## ⭐ Show Some Love

If you found this project useful, please ⭐ star the repository on GitHub! ❤️

---

📄 Licensed under the [MIT License](https://opensource.org/licenses/MIT) © 2025 Charvi Basappa
