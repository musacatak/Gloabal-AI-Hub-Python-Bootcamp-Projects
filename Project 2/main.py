# encoding:utf-8
import questions.Q1 as Q1
import questions.Q10 as Q10
import questions.Q11 as Q11
import questions.Q12 as Q12
import questions.Q13 as Q13
import questions.Q14 as Q14
import questions.Q15 as Q15
import questions.Q2 as Q2
import questions.Q3 as Q3
import questions.Q4 as Q4
import questions.Q5 as Q5
import questions.Q6 as Q6
import questions.Q7 as Q7
import questions.Q8 as Q8
import questions.Q9 as Q9


def exitCond():
    x = input("1.Continue\n2.Exit")
    if x == "2":
        exit()
    elif x != "1":
        print("Invalid value! Please enter 1 to continue, 2 to exit.")
        exitCond()

def main():
    while True:
        print("Please enter a number that represent the following query:"
              "\n1. What are the languages of the long-running movies in dataset? Visualize."
              "\n2. Evaluate IMDB scores of the movies shot in the genre of Documentary between 2019 January and 2020 June, and visualize."
              "\n3. What genre has the highest IMDB score among movies made in English?"
              "\n4. What is the average runtime of Hindi movies?"
              "\n5. How many categories are in the genre column and what are these categories? Visualize."
              "\n6. Find three most used languages in the dataset."
              "\n7. What are the first 10 movies having highest IMDB score?"
              "\n8. What is the correlation between IMDB Score and Runtime? Analyze and visualize."
              "\n9. What are the first 10 Genre having highest IMDB score? Visualize."
              "\n10. What are the first 10 movies having highest runtime value?"
              "\n11. In which year was the most movies released? Visualize."
              "\n12. What are the languages of the movies having lowest average IMDB score? Visualize."
              "\n13. Which year has the highest total runtime value?"
              "\n14. What is the genre which each language is used the most?"
              "\n15. Is there any outlier data in dataset? Explain."
              "\n0. Exit")
        cas = input("Enter operation number:")
        if cas == "1":
            Q1.main()
            exitCond()
        elif cas == "2":
            Q2.main()
            exitCond()
        elif cas == "3":
            Q3.main()
            exitCond()
        elif cas == "4":
            Q4.main()
            exitCond()
        elif cas == "5":
            Q5.main()
            exitCond()
        elif cas == "6":
            Q6.main()
            exitCond()
        elif cas == "7":
            Q7.main()
            exitCond()
        elif cas == "8":
            Q8.main()
            exitCond()
        elif cas == "9":
            Q9.main()
            exitCond()
        elif cas == "10":
            Q10.main()
            exitCond()
        elif cas == "11":
            Q11.main()
            exitCond()
        elif cas == "12":
            Q12.main()
            exitCond()
        elif cas == "13":
            Q13.main()
            exitCond()
        elif cas == "14":
            Q14.main()
            exitCond()
        elif cas == "15":
            Q15.main()
            exitCond()
        elif cas == "0":
            break
        else:
            print("Invalid operand ! Please enter a value between 0-15.")
            exitCond()


main()

