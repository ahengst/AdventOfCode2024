# Practice
# learned...
# thing1
# thing2


def reversal(input: str):
    if len(input) == 1:
        return input
    return input[-1] + reversal(input[:-1])


print(reversal("hello"))
