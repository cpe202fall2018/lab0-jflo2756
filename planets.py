def weight_on_planets():
    earthWeight = int(input("What do you weigh on earth? "))

    marsWeight = earthWeight * .38
    jupiterWeight = earthWeight * 2.34

    print("\nOn Mars you would weigh", marsWeight, "pounds.", "\nOn Jupiter you would weigh", jupiterWeight, "pounds.")

if __name__ == '__main__':
   weight_on_planets()
