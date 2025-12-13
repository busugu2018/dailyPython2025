#Section 4.1

def message():
    print("Enter a value: ")
 
message()
a = int(input())
message()
b = int(input())
message()
c = int(input())




def hello(name): # defining a function, function name hello, argument is name
    print("Hello,", name) # body of the function
 
 
name = input("Enter your name: ")
 
hello(name)  # calling the function



#===============================================================
#4.3 Section 3 – Returning a result from a function  








#IBM TEST:

def getMinimumOperations(versionNumbers):
    # Write your code here
    operations = 0
    for i in range(1, len(versionNumbers)):
        previous_number = versionNumbers[i-1]
        current_number = versionNumbers[i]
        
        needed_value = previous_number + 1
        
        add_amount = i + 1
        
        while current_number < needed_value:
            current_number = current_number + add_amount
            operations = operations + 1
            
        versionNumbers[i] = current_number
    return operations




# select 
#     wallet,
#     count * as total_transactions,
#     round(sum(case when value > 0 then value else 0 end), 2) as total bought,
#     round(sum(case when value < 0 then -value else 0 end), 2) as total sold
# from
#     transactions
# where
#     Date_format(transaction_date, '%Y-%m') = '2024-02'
# Group By
#     wallet
# Order By
#     wallet;




def numSubarrays(arr, minLen, threshold):
    n = len(arr)

    # Prefix sum for fast range-sum calculation
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + arr[i]

    count = 0
    i = 0

    # Greedy: always take the earliest valid subarray starting at i
    while i + minLen <= n:
        j = i + minLen - 1   # minimum possible end index

        # Expand j until the subarray sum >= threshold OR j hits the end
        while j < n and prefix[j+1] - prefix[i] < threshold:
            j += 1

        if j == n:      # no valid subarray starting from i
            break

        # Found a valid subarray from i → j
        count += 1
        i = j + 1       # move to next starting point (non-overlapping)

    return count


# Example usage:
arr = [5, 7, 9, 12, 10, 13]
minLen = 2
threshold = 15
print(numSubarrays(arr, minLen, threshold))  # Output: 2














# super beginner:



def numSubarrays(arr, minLen, threshold):
    n = len(arr)
    count = 0      # how many valid subarrays we found
    i = 0          # start of the current subarray

    # go through the array
    while i < n:
        # if not enough space left to make even the minimum size, stop
        if i + minLen > n:
            break

        # j will try to extend the subarray from i
        j = i + minLen - 1

        # calculate the sum of the first minLen elements
        current_sum = 0
        for k in range(i, j + 1):
            current_sum += arr[k]

        # now extend j until the sum is enough
        while current_sum < threshold and j + 1 < n:
            j += 1
            current_sum += arr[j]

        # if even after extending, sum is still too small → no more valid subarrays
        if current_sum < threshold:
            break

        # we found a valid subarray
        count += 1

        # move i to the next index after j (non-overlapping)
        i = j + 1

    return count


# Example
arr = [5, 7, 9, 12, 10, 13]
minLen = 2
threshold = 15

print(numSubarrays(arr, minLen, threshold))  # Output: 2










import requests

def transferAmount(name, city):
    base_url = "https://sonmock.hackerrank.com/api/transactions"

    max_credit = 0.0
    max_debit = 0.0

    page = 1

    while True:
        # 1. Fetch the page
        response = requests.get(base_url, params={"page": page})
        data = response.json()

        # 2. Go through all records in this page
        for record in data["data"]:
            # Filter by name and city
            if record["userName"] == name and record["location"]["city"] == city:

                # Example format: "$123.456.78"
                amount_str = record["amount"].replace("$", "").replace(",", "")
                amount_val = float(amount_str)

                if record["txnType"] == "credit":
                    if amount_val > max_credit:
                        max_credit = amount_val

                elif record["txnType"] == "debit":
                    if amount_val > max_debit:
                        max_debit = amount_val

        # 3. Stop when we finish the last page
        if page >= data["total_pages"]:
            break

        page += 1

    # Convert numbers back to currency format: "$123.45"
    result_credit = "$" + format(max_credit, ",.2f")
    result_debit  = "$" + format(max_debit, ",.2f")

    return [result_credit, result_debit]





import requests

def transferAmount(name, city):
    base_url = "https://sonmock.hackerrank.com/api/transactions"

    max_credit = 0.0
    max_debit = 0.0

    page = 1

    while True:
        # 1. Fetch the page
        response = requests.get(base_url, params={"page": page})
        data = response.json()

        # 2. Go through all records in this page
        for record in data["data"]:
            # Filter by name and city
            if record["userName"] == name and record["location"]["city"] == city:

                # Example format: "$123.456.78"
                amount_str = record["amount"].replace("$", "").replace(",", "")
                amount_val = float(amount_str)
                
                if record["txnType"] == "credit":
                    if amount_val > max_credit:
                        max_credit = amount_val

                elif record["txnType"] == "debit":
                    if amount_val > max_debit:
                        max_debit = amount_val

        # 3. Stop when we finish the last page
        if page >= data["total_pages"]:
            break

        page += 1

    # Convert numbers back to currency format: "$123.45"
    result_credit = "$" + format(max_credit, ",.2f")
    result_debit  = "$" + format(max_debit, ",.2f")

    return [result_credit, result_debit]