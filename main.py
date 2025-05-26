from random import randint
from time import perf_clock


def get_number_from_user() -> int:
  success = False
  while not success:
      try:
          user_input = int(input("Enter a number from 1 to 10: "))
          success = 1 <= user_input <= 10
      except:
          print("Try again!")
  return user_input


def get_number_from_user_timed() -> int, int:
  """
  returns number from user and time it took to get it
  """
  start = perf_counter()
  number = get_number_from_user()
  end = perf_counter()
  return number, end-start


def check_guess(user_input: int, number: int) -> bool:
  return user_input == number


def print_time(time):
  print(f"You took {time:.4f} seconds to guess.")


def generate_number() -> int:
  return randint(1, 10)


def positive_reaction():
  print("You won!")


def negative_reaction():
  print("You won!")


def start():
  name = input("Enter your name: ")
  print(f"Hello, {name}")


def main_loop():
  while True:
    number = generate_number()
    user_number, time = get_number_from_user_timed()
    print_time(time)
    if check_guess(user_number, number):
      positive_reaction()
    else:
      negative_reaction()
    
    if input("Continue?[y/n]: ").lower().strip() != "y":
      print("Goodbye.")
      break
    


def main():
  start()
  main_loop()


if __name__ == "__main__":
  main()
