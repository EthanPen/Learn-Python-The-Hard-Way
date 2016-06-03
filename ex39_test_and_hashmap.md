###EX39_TEST AND HASHMAP  
The Code Description

---
####hashmap:  
"**_a list of buckets, which are a list of slots, which have key/value pairs in them._**"  

**"a list of buckets...":** In the hashmap function, it create the aMap variable which is a list, and then fill it with other lists...  

**"which are a list of slots...":** These bucket lists are empty at first, but as we add key/value pairs to the data structure they will fill with "slots" or...  

**"which have key/value pairs in them.":** Meaning each slot inside a bucket contains a (key, value) tuple or "pair".  

**_hashmap algorithms_**  

1. Convert a key to an integer using a hashing function: hash_key.
2. Convert this hash to a bucket number using a **% (modulus)** operator.
3. Get this bucket from the aMap list of buckets, and then traverse it to find the slot that contains the key we want.  

**_function_:**  
**new:** use len(aMap) in other functions to find out how many buckets there are  

**hash_key:** built-in Python hash function to convert a string to a number.   

**get_bucker:** whatever bucket_id I get will fit into the aMap list. Using the bucket_id I can then get the bucket where the key could be.  

**get_slot:** it simply rolls through every element of that bucket until it finds a matching key.Once it does it returns the tuple of (i, k, v) which is the index the key was found in, the key itself, and the value set for that key.  

**get:** t uses get_slot to get the (i, k, v) and then just returns the v (value) only. 

**set:** find the bucket then check if this key already exists. If it does then I replace it in the bucket with the new one, and if it doesn't then I append. 

**delete:** To delete a key, I simply get the bucket and search for the key in it, and delete it from the list. 

**list:** prints out what's in the hashmap
