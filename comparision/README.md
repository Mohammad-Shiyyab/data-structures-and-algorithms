# Sorting: Comparisons

sorting an array, a key step in the algorithm is determining what their order should be.

For numbers, this comparison is easy - they go in ascending order. JavaScript, Python, and all the languages have a built-in operator to make this check for numbers: <, the less-than operator.
However, we very rarely want to sort an array of numbers. Usually, we want to sort an array of some complex data object we have created for our programs. For instance, we could sort an array of Cookie Stand objects by cookies sold, or an array of HornedBeasts by the name of their species.

## Pseudocode

function compareNumbers(a, b) {
  if (a == b) return 0;
  if (a < b) return -1;
  if (a > b) return 1;
}


## Approach & Efficiency
Big O 
space/time

# Solution

 <a href="#comparision.py">solution</a>

 <a href="#test_comparision.py">test</a>
