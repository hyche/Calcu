- Implement BigInt class to perform operation on string, the number of bytes to hold object is equal to the size of the string.
- Parser's idea is taken from https://stackoverflow.com/a/26227947. My original idea is to implement a Stack to parse, and process mathematical operations on it.
But using Stack is more complicated compared to using only function.
- I save user calculation history on the client side. For the sack of simplicity, because if we want to handle on server side, we must implement some kinds of
account manager and involve databases to store the information.