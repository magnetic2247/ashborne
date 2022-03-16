def pgcd(a,b):
   result = float("inf")
   while result != 0:
       result = a%b
       a = b
       b = result
   return a
