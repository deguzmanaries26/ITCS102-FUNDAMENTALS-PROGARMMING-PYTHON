print("Hello! Welcome to Anime entry program. \nPlease provide the title of an anime to continue and type 'exit' to terminate.")

anime = True
anime_titles = []
while anime == True:
    title = input("Enter anime title: ")
    if title.lower() == 'exit':
        print("Program terminated. Goodbye!")
        break
    else:
        anime_titles.append(title)
        print(f"'{title}' has been added to your anime list.")
print("The anime titles you have entered are:")
for anime in anime_titles:
    print(f"- {anime}")