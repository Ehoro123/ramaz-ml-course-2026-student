# HW02 Writeup — Derivatives and Autograd

After implementing all six functions, run the comparison script:

```bash
uv run --frozen --python 3.11 python derivatives.py
```

It prints a side-by-side table of your manual gradients and your autograd
gradients. Use that output to answer the three questions below. Replace each
`[your answer here]` with your response.

---

## Question 1 (3 pts)

**Do your manual and autograd gradients agree?**

Paste (or neatly transcribe) the comparison table printed by
`uv run --frozen --python 3.11 python derivatives.py`. Then answer:

- Do the manual and autograd values agree, allowing for floating-point
  rounding, at **every** point in the table?
- If any pair disagreed at some point while you were developing your
  solutions, what was the bug, and how did the table (or the tests) help you
  find it? If they agreed on your first try, say so — and describe one
  specific mistake the table *would* have caught (for example, in which rows
  the numbers would split apart if you forgot part of a derivative rule).

[function @ point                                   manual     autograd     |diff|
---------------------------------------------------------------------------------
quadratic   a=1, b=0, x=2                          4.0000       4.0000   0.00e+00
quadratic   a=3, b=2, x=1                          8.0000       8.0000   0.00e+00
quadratic   a=-2, b=5, x=1                         1.0000       1.0000   0.00e+00
quadratic   a=0.5, b=-1, x=4                       3.0000       3.0000   0.00e+00
composite   x=0                                    0.0000       0.0000   0.00e+00
composite   x=1                                   18.0000      18.0000   0.00e+00
composite   x=2                                  240.0000     240.0000   0.00e+00
composite   x=-1                                   6.0000       6.0000   0.00e+00
partial df/dx  (x,y)=(1,2)                         8.0000       8.0000   0.00e+00
partial df/dy  (x,y)=(1,2)                        11.0000      11.0000   0.00e+00
partial df/dx  (x,y)=(2,1)                         7.0000       7.0000   0.00e+00
partial df/dy  (x,y)=(2,1)                        10.0000      10.0000   0.00e+00
partial df/dx  (x,y)=(0,0)                         0.0000       0.0000   0.00e+00
partial df/dy  (x,y)=(0,0)                         0.0000       0.0000   0.00e+00
partial df/dx  (x,y)=(-1,3)                        7.0000       7.0000   0.00e+00
partial df/dy  (x,y)=(-1,3)                        9.0000       9.0000   0.00e+00
---------------------------------------------------------------------------------
If every |diff| is ~0, your manual rules and autograd agree.
  
Yes, they do agree for every case. |diff| is equal to zero all along my first run of the table.
One mistake the table could catch is any error while manually deriving and writing down the derivatives. For example: forgetting the inner derivative in manual_gradient_composite, writing 2(x³ + 2) instead of 2(x³ + 2)·3x².  Which would show up in the table numbers by  not matching up. In this specific example would be in the composite row  x = 1, manual would give 6 instead of 18.]

---

## Question 2 (4 pts)

**The chain rule, by hand and by `.backward()`.**

Take the composite function from this assignment, $f(x) = (x^3 + 2)^2$.

**a)** Write out the chain-rule steps you used in
`manual_gradient_composite`: identify the outer function and the inner
function, give the derivative of each, and show how they combine into
$f'(x)$.

**b)** Now explain what PyTorch is doing when `autograd_gradient_composite`
runs its backward pass. Autograd is bookkeeping of the
chain rule over a computation graph — walk through how *your* steps from
part (a) show up in that process: what operations get recorded as you build
`f` from the input, and how the backward pass combines their derivatives to
produce the gradient stored on your input tensor.

[The outer function is u^2, the inner function is (x^3+2). Because it's a composite/chain setup it's first a power rule of the whole term which is: 2(x^3+2) and then you multiply it by the derivative of the inside function (x^3+2) which is 3x^2. So f'(x) = 2(x^3+2)*3x^2

x = torch.tensor(x_val, requires_grad=True), tells torch to keep track of x. 
Then f = (x**3 + 2)**2 is the forward pass, where torch records each step in the graph: x->x^3->+2->squared
f.backward(): torch walks that graph in reverse and multiplies each step's derivative (2(x³ + 2), then 1, then 3x², the same as part (a)), which is chain rule. Then finally the answer goes into x.grad, which then I also add .item() to, to get the output as a python float]

---

## Question 3 (3 pts)

**From your gradient to a parameter update.**

**a) One update (1 pt).** Use the row for the composite function at $x=1$
from **your** comparison table. State the gradient value $g$ you obtained,
then compute one update $x_{new}=1-0.01g$. Explain why your step moves left
or right.

**b) A gradient error (1 pt).** Suppose the gradient used in that same step
were $g+2$ instead. Compute the new update and its difference from part (a).
Does this error change the direction, the distance, or both? A different
step is not automatically worse; explain what you can conclude from this
calculation without running further steps.

`**c) Choosing a method (1 pt).** Suppose you want the gradient of a scalar
function with $d$ inputs. Compare estimating each partial derivative using
forward differences with computing the gradient using PyTorch autograd: (IGNORE- update: We did not end up covering 3c in class, so you can skip that question on the write-up.)`

- How many function evaluations would forward differences require if you
  reuse the value at the original input? How does autograd avoid repeating
  that work separately for each input?
- Which source of error does autograd avoid, and why are its results still
  not perfectly exact?

Refer to the lecture box **“Why not estimate derivatives from nearby values?”**
if needed.

[ I got 18 at x=1, 1-0.18 = 0.82. It moved left because the gradient is positive (at x=1 f is going up) and gradient descent steps the opposite way.

1-0.20 = 0.80. This error only changes the distance. 20 is positive, so it still moves left, only 0.02 farther. From just one step you can't say it's worse, but only that it moved a little further.
]
