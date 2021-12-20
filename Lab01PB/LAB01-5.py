#Lab01-5 (Mowing Grass)

blength = int(input("Enter block length: "))
bwidth = int(input("Enter block width: "))
hlength = int(input("Enter house length: "))
hwidth = int(input("Enter house width: "))

cost = 35 * (blength * bwidth) - 35 * (hlength * hwidth)
print("Mowing cost is", cost, "baht.")