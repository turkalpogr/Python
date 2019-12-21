x = 6
result = 5 < x < 10
hak = 5
devam = 'e'
print(result) # cevabı false olarak döndürür

# and

result  = x >5 and x < 10
print(result)
result = hak > 5 and devam == 'e'
print(result)

result = ((x>5) and (x <10)) and (x%2 ==0)

print(f'{x} bir çift sayıdır')