#  Install an external module and use it 
import pyttsx3

class Animals:
    def details():
        print("They have four feet")


class Pet(Animals):
    def about():
        print("Prts are cute and they are amazing")


class Dog(Pet):
    @staticmethod
    def bark():
        engine = pyttsx3.init()
        engine.say("Bhow Bhow Bhow Bhow Bhow Bhow Bhow")
        engine.runAndWait()
        
        
d = Dog()

d.bark()