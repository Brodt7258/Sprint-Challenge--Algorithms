#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The runtime will be `O(n)`. The loop condition breaks at `n^3`, and the value checked against it grows at a rate of `n^2` per iteration. It will take `n` iterations for `a` to grow to `n^3`.

`n^3 = n^2 * X` -> `n^3 / n^2 = X` -> `n = X`

b) The runtime will be `O(n^2)`. The outer loop runs in `O(n)`, and each inner loop will run for `n/2` iterations. The coefficient is omitted, as constants of any kind lose their relevance as `n` grows in size, leaving `O(n)` for the inner loop as well.

`n * n = n^2` -> `O(n^2)`


c) The runtime will be `O(n)`. Each value in the range from `0` to `n` requires only a single operation, no inner loops, no growing number of recursive calls. The number of operations grows at the same rate as `n`.

## Exercise II

let c = the current floor.

let l = the lowest possible floor
let h = the highest possible floor

begin with c = n / 2, l = 0, and h = n

drop the egg

If the egg breaks:
  Set h to c - 1
  Set c to halfway between c and l ((c + l) / 2)

If the egg does not break:
  Set l to c + 1
  Set c to halfway between c and h ((c + h) / 2)

Continue to drop eggs and change floors as described above, until l and h converge to the same value. If the egg does not break on that value, then that is f. If it does, then f is that value, minus 1.