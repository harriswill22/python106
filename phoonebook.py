phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}
#print Elizabeth's Phone Number 
print(phonebook_dict['Elizabeth'])

#add Kareem's Phone Number 
phonebook_dict['Kareem'] = '938-489-1234'

#Delete Alice's phone entry
del phonebook_dict['Alice']

#Change Bob's phone number to '968-345-2345'
phonebook_dict['Bob'] = '968-345-2345'

print(phonebook_dict)

