import pokepy
import random
# define a main function
def main():
    player_score = 0
    questions = 1
    
    question_type = input("\nWhat kind of quiz do you want? Weight(w) / Height(h)  ")
    while(question_type!= 'w' and question_type!='h'):
        question_type = input("\nNot a valid character. Enter (w/h)  ")

    while(questions < 20):
        firstPokemon = pokepy.V2Client().get_pokemon(random.randint(1,500))
        secondPokemon = pokepy.V2Client().get_pokemon(random.randint(1,500))

        while(firstPokemon == secondPokemon): 
            secondPokemon = pokepy.V2Client().get_pokemon(random.randint(1,500))

        if(question_type == "w"):
            print(f"\nIs {firstPokemon.name} heavier than {secondPokemon.name}?")
            bool = firstPokemon.weight > secondPokemon.weight
        else:
            print(f"\nIs {firstPokemon.name} taller than {secondPokemon.name}?")
            bool = firstPokemon.height > secondPokemon.height

        user = input("\nEnter (y/n)  ")

        while(user!= 'y' and user!='n'):
            user = input("\nNot a valid character. Enter (y/n)  ")

        if user == "y":
            user_bool = True
        else:
            user_bool = False

        if(bool == user_bool):
            player_score+=1
            print("\nYou got it right!~")
        else:
            print("\nYou got it wrong! :(")

        print(f"\nYour current score: {player_score}/{questions}")
        questions+=1

    print(f"\nYou got {player_score}/20 questions right!")


if __name__=="__main__":
    main()