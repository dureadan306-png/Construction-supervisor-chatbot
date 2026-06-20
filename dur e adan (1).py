print("================================")
print("     CHATBOT                    ")
print("================================")
print("Type 'help' to see what you can ask, or 'bye' to exit.")

while True:
    question = input("\nAsk something about my Baba: ").lower()

    if "help" in question:
        print("You can ask about: name, job, experience, education, sites, labor, personality, routine, stress, advice, laugh, future, proud, team, or tea!")

    elif "name" in question:
        print("My Baba's name is Muhammad Arshad.")

    elif "job" in question or "work" in question:
        print("He is a professional construction supervisor. He has been doing this for many years!")

    elif "experience" in question or "years" in question:
        print("He has years of experience in the field. He really knows the ins and outs of how buildings are made.")

    elif "education" in question:
        print("He has a simple FA degree, but his real-world knowledge is far beyond what you find in books.")

    elif "sites" in question or "construction" in question:
        print("His daily work involves visiting construction sites, checking the progress, and making sure everything is built correctly.")

    elif "labor" in question or "material" in question:
        print("He is excellent at managing labor and construction materials. He knows how to keep a project moving smoothly.")

    elif "personality" in question or "polite" in question or "nature" in question:
        print("That is his best quality! Even when the site gets stressful, he remains very polite and kind to everyone. He's a true gentleman.")
    
    elif "routine" in question or "morning" in question:
        print("He is an early bird. He likes to start his day fresh to check the sites before the sun gets too hot.")
        
    elif "stress" in question:
        print("Even under the pressure of huge projects, he never loses his cool. He just drinks a cup of tea and keeps working.")
        
    elif "advice" in question:
        print("He always says: 'Hard work brings respect.' He believes in honesty in every brick we lay.")
        
    elif "laugh" in question or "smile" in question:
        print("He has a very calm smile. It’s his way of saying that 'everything is under control.'")
        
    elif "future" in question or "goal" in question:
        print("He wants to see all his kids well-settled and successful. That is his only real goal.")
        
    elif "proud" in question:
        print("He feels proud when he sees a building completed from scratch because of his supervision.")
        
    elif "team" in question or "colleague" in question:
        print("He treats his labor team like family. He believes if you respect them, they will give their best work.")
        
    elif "tea" in question:
        print("Yes! He is a tea lover. A cup of tea on the construction site is his favorite break.")
        
    elif "strength" in question:
        print("His biggest strength is his patience. In construction, things go wrong, but he handles them one by one.")
        
    elif "home" in question or "family" in question:
        print("He works hard all day at the sites, but at home, he is the most relaxed and loving father.")

    elif "bye" in question:
        print("Goodbye! Take care.")
        break

    else:
        print("I'm not sure about that. Try asking 'help' to see what you can ask me!")