# Project
movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

movie_input_decision = input("Do you want to add more movies to the existing list? Yes or No :: ")
if (movie_input_decision == "Yes") | (movie_input_decision == "yes"):
    print(f"\nYour entered: Yes")
    new_movie_count = int(input("\nHow many movies do you want to add? "))
    for _ in range(new_movie_count):
        new_movie_name = input("\nEnter the name of your movie: ")
        new_movie_budget = int(input("\nEnter the budget of your movie: "))
        new_movie = (new_movie_name, new_movie_budget)
        movies.append(new_movie)
    print(f"\nMoving to calculations: ")
else:
    print(f"\nYour entered: {movie_input_decision} \nMoving to calculations. ")

print(f"\nNew movie list is:\n{movies}")
budget_total = 0
for movie in movies:
    budget_total += movie[1]

avg_budget = budget_total/(len(movies))
print(f"\nAverage budget: {avg_budget}")

counter = 0
for m in movies:
    if m[1] > avg_budget:
        print(m[0])
        counter += 1

print(f"Number of movies that spent more than the average: {counter}")