#99 bottles of cola on the wall. 99 bottles of cola, take one down, pass it around. 98 bottles of cola on the wall. 98 bottles of cola, take one down, pass it around.... A computer should be able to sing this song in no time at all...

count = int(input('How many bottles of cole are on the wall? '))
while count > 0:
  print(count, 'bottles of cola on the wall.', count, 'bottles of cola, take one down, pass it around.')
  count = count - 1
