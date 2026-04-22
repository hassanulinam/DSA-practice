"""
Good. This is where you stop thinking “grid” and start thinking **graph hidden inside a problem**.

---

# 🔥 Problem: Word Ladder

You are given:

* `beginWord` (start word)
* `endWord` (target word)
* `wordList` (dictionary of valid words)

---

## 🎯 Goal

Return the **length of the shortest transformation sequence** from:

```text
beginWord → endWord
```

---

## 🔁 Rules

You can:

* Change **only one letter at a time**
* Each transformed word must exist in `wordList`

---

## 📥 Example

```python
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
```

### ✅ Output:

```text
5
```

---

## 💡 Explanation

One shortest path:

```text
hit → hot → dot → dog → cog
```

Length = **5 words**

---

## ❌ If impossible

```python
wordList = ["hot","dot","dog","lot","log"]
```

No `"cog"` → return `0`

---

# 🧠 Core Insight (This is the shift)

This is **not a grid problem**, but still:

> It is a **shortest path problem in an unweighted graph**

---

## 🔥 Hidden Graph

* Each word = node
* Edge exists if:

  * words differ by **exactly 1 letter**

---

### Example connections:

```text
hit → hot
hot → dot, lot
dot → dog
dog → cog
```

---

# 🚀 What Should Trigger in Your Brain

You see:

* “minimum transformations”
* “each step costs 1”

👉 **BFS**

---

# ⚠️ The Real Challenge

Not BFS.

👉 **How do you find neighbors efficiently?**

---

## ❌ Brute Force (Too Slow)

Compare each word with every other word:

```text
O(N^2 * word_length)
```

This will TLE.

---

## ✅ Smart Trick (Critical)

For each word:

👉 Change **one character at a time**

---

### Example:

Word = `"hot"`

Generate:

```text
aot, bot, cot, ..., zot
hat, hbt, hct, ..., hzt
hoa, hob, hoc, ..., hoz
```

Then check if it exists in a **set**

---
"""

from collections import deque


def word_ladder(begin_word: str, end_word: str, words_list: list[str]) -> int:
    words_set = set(words_list)
    if end_word not in words_set:
        return 0

    q = deque([(begin_word, 1)])
    while q:
        word, dist = q.popleft()
        if word == end_word:
            return dist
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        for i in range(len(word)):
            for ch in alphabets:
                new_word = word[:i] + ch + word[i + 1 :]
                if new_word in words_set:
                    q.append((new_word, dist + 1))
    return 0


print(word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "cog"]))
