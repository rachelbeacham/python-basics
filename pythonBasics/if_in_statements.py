movies_watched = {'The Matrix', 'Green Book', 'Her'}
user_movie = input("Enter a movie you've watch recently: ")

#if statement evaluates whether user_movie is in the movies_watched set
if user_movie in movies_watched:
  #if true this statemnt runs
  print(f"I've watched {user_movie} too!")
else:
  #if false the else statment runs
  print("I haven't watched that yet.")
