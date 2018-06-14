try:
     a= 1/2
     raise Exception
except:
    print(a)
finally:
    print a