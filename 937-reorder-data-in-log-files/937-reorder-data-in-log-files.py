class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        def get_key(log):
            _id, rest = log.split(" ", maxsplit = 1)
            
            # key_1, flag, 0, letter logs, 1 for digit logs; key_2 contents of letter logs
            return (0, rest, _id) if rest[0].isalpha() else (1, )
        
        return sorted(logs, key=get_key)
        
        
"""

If maxsplit is specified, the list will have a maximum of maxsplit+1 items.


        As a reminder, here are a list of the rules that we defined before, concerning the order of logs:

1). The letter-logs should be prioritized above all digit-logs.
2). Among the letter-logs, we should further sort them based on firstly on their contents, and then on their identifiers if the contents are identical.
3). Among the digit-logs, they should remain in the same order as they are in the collection.

To ensure the above order, we could define a tuple of 3 keys, (key_1, key_2, key_3), as follows:

key_1: this key serves as a indicator for the type of logs. For the letter-logs, we could assign its key_1 with 0, and for the digit-logs, we assign its key_1 with 1. As we can see, thanks to the assigned values, the letter-logs would take the priority above the digit-logs.

key_2: for this key, we use the content of the letter-logs as its value, so that among the letter-logs, they would be further ordered based on their content, as required in the Rule (2).

key_3: similarly with the key_2, this key serves to further order the letter-logs. We will use the identifier of the letter-logs as its value, so that for the letter-logs with the same content, we could further sort the logs based on its identifier, as required in the Rule (2).

Note: for the digit-logs, we don't need the key_2 and key_3. We can simply assign the None value to these two keys. As a result, the key value for all the digit-logs would be (1, None, None).

Finally, thanks to the stability of sorting algorithms, the elements with the same key value would remain the same order as in the original input. Therefore, the Rule (3) is ensured.
"""