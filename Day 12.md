# Break and Continue
### Task : To print until finding a duplicate
```py
def process_until_duplicate(numbers):
    check_dup=set()
    for i in numbers:
        if i in check_dup:
            print(f"Found duplicate, process stopped")
            break
        check_dup.add(i)
        print(f"Processed {i}")

        
 
if __name__ == "__main__":
    process_until_duplicate(["apple", "banana", "carrot", "apple", "date", "banana"])
 
```

### Task :
```py

```