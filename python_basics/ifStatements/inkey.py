friends = ["rolf", "bob", "jen"]
print("rolf" in friends)
print("ab" in friends)

movies_watched = {"movie1", "movie2", "movie3"}
user_movie = input("Enter movie watched recently")
print(user_movie in movies_watched)

if user_movie in movies_watched:
    print(f"I have watched {user_movie} too")
else:
    print("Havent watched")
