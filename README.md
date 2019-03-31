# Trinomial triangle 
### Python 3.7 program that includes following functionality: <br>
**1) prints trinomial triangle** (see more https://en.wikipedia.org/wiki/Trinomial_triangle) <br>
**2) for given LENGTH and TOTAL values returns the list of LENGTH long lists, consisting only of _-1, 0 and 1_ numbers, whose sum is TOTAL**

**Run with "py trinomial.py [arg]" command, where [arg] is the max height of printed triangle**

Function **trit_sim(length, total)** can be also used for finding all possible variations of (length) long lists of -1, 0 and 1 elements, that in total give (total) value

<p align="center">
          <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/cc502b2cecdfb28fa8674bd32b3f1097ce6451be">
          <br><br>
          Example with length = 5
</p>


# V tomto ukolu uvazujeme pole, ktera obsahuji pouze cisla -1, 0, 1.
# Vasim ukolem bude implementovat funkci trit_sum, ktera pro zadana cisla
# `length` a `total` vrati seznam vsech takovych poli delky `length`, jejichz
# soucet je presne `total`.
