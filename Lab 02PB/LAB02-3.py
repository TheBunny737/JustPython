#Lab02-3 (Space Print)

x = float(input())
y = float(input())
print("1234567890" * 3) #Do not use this, this cause - on ELAB
print("Total Income {:+8.2f} bahts" .format(x))
print("Expense      {:+8.2f} bahts" .format(y))
print("Profit       {:08.2f} bahts" .format(x+y))