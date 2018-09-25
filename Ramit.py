ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}
print()

#gets the email address of Ramit
print("Rammits emaill adress is: " '%s' % ramit['email'] )

print()

#gets the first of Ramit's interests.
print("Rammits interests are: " '%s' % ramit['interests'][0])

print()

# gets the email address of Jasmine.
Jasmine_Email = "jan@hotmail.com"
for friends in ramit['friends']:
    if friends['name'] == 'Jasmine':
        print("Jasmine's email is: '%s'" % friends['email'] )
print()

#gets the second of Jan's two interests
for friends in ramit['friends']:
    if friends['name'] == 'Jan':
        print("Jan's second interest is: " '%s' % friends['interests'][1])

    