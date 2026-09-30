# HW00 Writeup — Song Analysis

Run `uv run python analysis.py` to generate the results, then answer the five questions
below. Replace each `[your answer here]` with your response.

- Questions 1–3 are factual. One or two sentences is enough.
- Question 4 asks you to reflect on something that surprised you.
- Question 5 asks you to connect what you implemented in Part 1 to the two new tools from Part 2.

---

## Question 1 (2 pts)

**Which genre averaged the most weeks on the Billboard chart, and how many songs is that average computed from?**

The Afrobeats genre with an average of 30.0 weeks (from only one song)

---

## Question 2 (2 pts)

**Who was the most-streamed artist in the dataset (by total streams across all their songs)?**

Taylor Swift with 6560mil total streams

---

## Question 3 (2 pts)

**Which year had the most top-10 hits (songs that peaked at position 10 or better)?**

2024, with 26 top hits

---

## Question 4 (4 pts)

**What surprised you about the data?**

Pick one finding from your analysis that was unexpected — something that contradicts what you assumed going in, or that is more interesting than you expected. Explain:
- What you expected to see, and why.
- What the data actually showed.
- What might explain the difference.

I naturally expected to see a more popular genre like pop to be on top for the most average weeks on chart by genre because it has the most songs
But really it's afrobeats that consists of just one song that placed the highest
And it now makes sense since it's ranked by average and the more songs there are the more likely the data is to tend towards a middle range number compared to the fact the afrobeats being controlled by just one song it has a really wide opportunity to bring the genre average really low or of course really high.

---

## Question 5 (5 pts)

In Part 1 you implemented `count_occurrences` from scratch using only a plain Python
dict. `collections.Counter`, which you used in Part 2, does the same thing but with
extra conveniences built in.

Answer both parts:

**a)** Walk through, step by step, how you accumulated a running total per genre/artist in `avg_weeks_by_genre` and `most_streamed_artist`, and how you determined the maximum in `most_streamed_artist`. Would `collections.Counter` have made any part of this easier, and if so, which part (drawing on how you'd extend your own `count_occurrences`
to do the same thing)?  
For both I found a pattern to all of these functions that they were all quite similar to the group by function I had done earlier, where I made a dictionary where each genre or artist maps to a list of its values. Then off of that I made a second dictionary with sum(list)/len(list) for the genre averages, and sum(list) for the artist totals. To find the maximum I used max(sums, key=sums.get), which simply returns the artist with the highest total. My own counting function from part 1 could add up streams instead of counting by 1, but Counter can do the set up and find the max for me. 

**b)** `StreamsRanker` and `LongevityRanker` both subclass `SongRanker` and share its `rank` method, overriding only `score`. If they did **not** share a common base class —
if you had written two separate, unrelated classes instead — what code would you have had to duplicate? What does inheritance buy you here?

I would have had to duplicate the rank() function. 
It makes it so that the code's located in one place, less chance for typos and if i change something it means both subclasses will be updated in sync and that adding new rankers is easy.
