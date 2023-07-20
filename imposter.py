import os 
import time
def clear_output():
    os.system("cls" if os.name == "nt" else 'clear')




def motivate():
    while True:
        response = input('How are you feeling? stuck/ stupid / slow / frustrated. \nEnter, quit when you feel better!').lower().strip()
        clear_output()

        if response == 'stuck':
            print("\nRemember when you were stuck yesterday or the day before, and now you get those concepts? Take a break from your work until you feel ready to come back. Take some deep breaths, and focus on the present. You'll get through this!\n")
            time.sleep(5)
            clear_output()
        elif response == 'stupid':
            print("\nEveryone starts at a different place, and learns at a different pace. Energy spent comparing ourselves to others is energy wasted.\n")
            time.sleep(5)
            clear_output()
        elif response == 'slow':
            print("\nSpeed is relative. What feels slow to you may seem fast to someone else. With time, everything will come together.")
            time.sleep(5)
            clear_output()
        elif response == 'frustrated':
            print("If we're uncomfortable it means we're growing. Think about how much you've already learned today, yesterday, or the weeks before. You've been putting in the work, and it's okay to feel frustrated from time to time. Remember what your end goal is, and why you're going through this. Try taking a break and doing breathing exercise's to calm your nerves.")
            time.sleep(5)
            clear_output()
        elif response == 'quit':
            break
        else:
            print("Please try again, it's okay deep breaths.")
motivate()
