import os

if __name__ == "__main__":
    print("Welcome to the RoboSpeaker created by Aman")
    while True:
      x = input("Enter what you want me to speak: ")
      if x == 'q':
        break
        command = f"echo{x}"
        os.system(command)

    