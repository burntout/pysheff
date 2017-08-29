#!/usr/bin/env python

''' 

This is an attemt to solve 

http://codingdojo.org/kata/Potter/

'''

bookprice = 8
discounts = [ 0, 0.95, 0.9, 0.8, 0.75 ]
price_perset = [8, 15.2, 21.6, 25.6, 30]
basket = {}
#basket["book1"] = 3
#basket["book2"] = 3
#basket["book3"] = 3
#basket["book4"] = 2
#basket["book5"] = 2

# basket["book1"] = 3
# basket["book2"] = 0
# basket["book3"] = 0
# basket["book4"] = 0
# basket["book5"] = 0

# basket["book1"] = 2
# basket["book2"] = 2
# basket["book3"] = 2
# basket["book4"] = 1
# basket["book5"] = 1

basket["book1"] = 2
basket["book2"] = 2
basket["book3"] = 2
basket["book4"] = 2
basket["book5"] = 0



print basket

total_books = 0
for book in basket:
    total_books += basket[book]

books = []
for book in basket:
    if basket[book] > 0:
        books.append(book)

def remove_zero(basket):
    tmp_basket = {}
    for book in basket:
        num_book = basket[book]
        if num_book > 0:
            tmp_basket[book] = num_book
    return tmp_basket

def reduce_basket(basket):
    tmp_basket = {}
    for book in basket:
        num_book = basket[book]
        if num_book > 1:
            tmp_basket[book] = num_book-1
    return tmp_basket

tmp_basket = remove_zero(basket)
#print reduce_basket(tmp_basket)

total = 0
while len(tmp_basket)> 0:
    print "length of basket", len(tmp_basket), "price of basket", price_perset[len(tmp_basket) - 1]
    total  +=  price_perset[len(tmp_basket) - 1]
    tmp_basket = reduce_basket(tmp_basket)


print "You pay", total




#print "Nondiscount", total_books*bookprice
#print "number of different Books", len(books)
#print "discount",  discounts[len(books) - 1]

