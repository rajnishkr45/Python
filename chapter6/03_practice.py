# Spam detector

sentance = input("Enter the sentence: ")

if (
    "subscribe this" in sentance
    or "Make a lots of money" in sentance
    or "click this" in sentance
    or "buy now" in sentance
):
    print("This is spam !")
    print("\tBlock it now")

else:
    print("No spam detected\n\tIts fine to use")
