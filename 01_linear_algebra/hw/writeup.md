# HW01 Writeup — Matrices as Transformations

Finish Part 3, then run `uv run --frozen --python 3.11 python analysis.py` to generate `transforms.png`
and the printed values. Answer the three questions below using **your own**
figure and output. Replace each `[your answer here]` with your response.

---

## Question 1 (3 pts)

**What does each transformation change, and what does it preserve?**

Look at the rotation, scaling, and shear panels of your `transforms.png`.
For each of the three transformations, describe in a sentence or two:

- What changed about the arrow (size? angles? direction it points? proportions?).
- What stayed the same.

For rotation it of course changed the angle in which the arrow points, turning it counterclockwise 60 degrees. But it stayed the same norm/magnitude.
Scaling changes the size and proportions and the angles. But in this case it's still points to the right being stretched to twice as long and half as tall.
For shear every point in the arrow slid to the right by k times it height, so the arrow now leans to the right and the angle changed. The height always stays the same. The base on the x-axis doesn't move.

---

## Question 2 (3 pts)

**Why are the R @ S and S @ R panels different?**

Both panels apply the *same* two matrices — a $60^\circ$ degree? rotation and a
$(2, 0.5)$ scaling — to the *same* arrow, just in opposite order. Using your
figure and the printed matrices and arrow-tip positions:

- Describe how the two results differ.
- Explain *why* the order changes the outcome. Connect your explanation to the
  principle that $AB \neq BA$ in general. (Hint: in each
  composition, which transformation does the arrow experience first?)

The RS has a higher, more scaled norm/magnitude than the SR. RS also points higher at a steeper angle. The tip of RS lands at (2.78, 5.32) about 62 degrees up, while the tip of SR lands at (2.13, 1.42) at about 34 degrees above the horizontal. For RS the stretch hits the arrow while it's still flat, making it logner and then rotating it. SR rotates it first and then the y * 0.5 ends up squashing it. This shows that the order of the matrices matter. (All this goes to show: SR does not equal RS)

---

## Question 3 (4 pts)

**What does the matrix part of a dense neural-network layer do?**

A dense layer uses a weight matrix to transform its input vectors. Here,
consider only that matrix operation, before adding a bias or applying a
nonlinearity. Your Part 3 figure shows several $2 \times 2$ examples.

Using your own figure and printed output, explain:

- Choose one panel and describe what its matrix did geometrically. If $X$
  stores $N$ two-dimensional points as rows and the weight matrix $W$ has
  shape $(2, 2)$, what shape should the transformed points have? Explain how
  storing points in rows fits the lecture's column-vector expression $Wp$.
- Why can changing the order of two weight matrices change the output?
  Support your answer with your two arrow-tip positions from Question 2,
  identifying which transformation acts first in each composition.

Scaling Panel - it's matrtix [[2,0], [0,0.5]] doubles every point's x cordinate point and halves every point's y cordinate. So the arrow becomes twice as long and half as tall while still pointing right in the same direction. It's a linear transformation. 

If X stores N points as rows (R^Nx2) and W is R^2x2, then the transformed points matrix is also R^Nx2. Storing points in rows fits the lecture's column-vector expression because we compute X*W^T instead, which gives the same new points, just written as rows.

Like in question 2 changing the order of 2 weight matrtices can change the output because matrix multiplication isn't commutative (AB does not equal BA). Not to be mixed with the associative rule of problem 11 from the problem rules, which is just being able to move around the parentheses. In RS the scaling acts first and the tip lands at (2.78, 5.32). In SR the rotation acts first and it lands at (2.13, 1.42)