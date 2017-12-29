/*
Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.
Example
    For sequence = [1, 3, 2, 1], the output should be
    almostIncreasingSequence(sequence) = false;
    There is no one element in this array that can be removed in order to get a strictly increasing sequence.
    For sequence = [1, 3, 2], the output should be
    almostIncreasingSequence(sequence) = true.
    You can remove 3 from the array to get the strictly increasing sequence [1, 2]. Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].
Input/Output
    [execution time limit] 0.5 seconds (c)
    [input] array.integer sequence
    Guaranteed constraints:
    2 ≤ sequence.length ≤ 105,
    -105 ≤ sequence[i] ≤ 105.
    [output] boolean
    Return true if it is possible to remove one element from the array in order to get a strictly increasing sequence, otherwise return false.
*/

// Definition for arrays:
// typedef struct arr_##name {
//   int size;
//   type *arr;
// } arr_##name;
//
// arr_##name alloc_arr_##name(int len) {
//   arr_##name a = {len, len > 0 ? malloc(sizeof(type) * len) : NULL};
//   return a;
// }

bool almostIncreasingSequence(arr_integer sequence) {
    int mistakes = 0;
    bool err_prev = false;
    bool err_next = false;
    
    for (int i = 0; i < sequence.size - 1; i++)
    {
        if (sequence.arr[i + 1] && sequence.arr[i] >= sequence.arr[i + 1])
        {
            if (sequence.arr[i - 1] && sequence.arr[i + 1])
                err_prev = sequence.arr[i - 1] >= sequence.arr[i + 1];
            if (sequence.arr[i + 2])
                err_next = sequence.arr[i] >= sequence.arr[i + 2];
            mistakes += (err_prev && err_next) ? 2 : 1;
        }
        if (mistakes > 1)
            return (false);
    }
    return (true);
}