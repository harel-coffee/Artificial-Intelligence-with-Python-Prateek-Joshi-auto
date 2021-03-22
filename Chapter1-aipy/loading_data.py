# Copyright @ Bagus Java @ Dr. MUHAMMAD FAISAL,S.Kom., M.T @ Magister Informatika @ UIN Maulana Malik Ibrahim @ UIN Malang (https://www.bagusjava.com/)
#import dataset
from sklearn import datasets

house_prices = datasets.load_boston()

# print "House prices"
print("******************************")
print("Output of Home Prices Data")
print("******************************")
print(house_prices.data)

# print "Predicted Home Prices"
print("******************************")
print("Output of Predicted Home Prices")
print("******************************")
print(house_prices.target)

digits = datasets.load_digits()

# print "Array Of Images"
print("******************************")
print("Output of scikit-learn Array of Images")
print("******************************")
print(digits.images[4])
