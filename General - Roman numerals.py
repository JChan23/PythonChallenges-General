#Print the first 100 numbers in roman numerals.
#This program requires the external module "roman". It can be installed by using: $ pip install roman
import roman

for i in range(100):
    romannumeral = roman.toRoman(i+1)
    print(romannumeral)
