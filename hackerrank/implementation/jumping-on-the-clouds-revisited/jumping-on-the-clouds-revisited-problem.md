# 🧮 Jumping on the Clouds (Revisited) - Easy

---

## 📌 Problem Statement

A child is playing a cloud-hopping game with the following rules:

- There are `n` clouds in a circle, indexed from `0` to `n-1`.
- Each cloud is either:
  - `0`: a **cumulus cloud** (safe),
  - `1`: a **thunderhead** (dangerous, costs more energy).
- The player starts with `100` energy at cloud `0`.
- On each jump:
  - Move forward by `k` clouds (wrapping around using modulo: `(current + k) % n`).
  - Lose **1 energy** by default.
  - If landing on a thunderhead (`1`), lose **2 more** energy.
- The game ends once the player returns to cloud `0`.

**Your task:** Return the remaining energy after completing one full cycle.

---

## 💡 Example

### Sample Input:
```plaintext
8 2
0 0 1 0 0 1 1 0
```

### Sample Output:
```plaintext
92
```

### 🔍 Explanation:

Let’s simulate the jumps:

| Step | Current Cloud | Next Cloud | Cloud Type | Energy Lost | Energy Left |
|------|----------------|-------------|-------------|--------------|--------------|
| 0    | 0              | 2           | 1 (⚡)       | 3            | 97           |
| 1    | 2              | 4           | 0           | 1            | 96           |
| 2    | 4              | 6           | 1 (⚡)       | 3            | 93           |
| 3    | 6              | 0           | 0           | 1            | 92           |

➡️ Ended back at `0`, final energy: `92`.

---

## ✅ Recommended Time & Space Complexity

- **Time Complexity:** `O(n/k)` — We visit each cloud once in the cycle.
- **Space Complexity:** `O(1)` — No extra space needed.

---

## 📎 Constraints

- `1 ≤ n ≤ 25`
- `1 ≤ k ≤ n`
- Each `c[i] ∈ {0, 1}`

---

## 💡 Hints

- Use `%` (modulo) to make the route circular.
- Update energy using:
  ```python
  energy -= 1 + 2 * c[next_position]
  ```

---

## 📅 Date Done

**Date:** *02/07/2025*  
**Time Taken:** *10 minutes*

---