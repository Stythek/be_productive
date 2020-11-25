import time
from tqdm import tqdm, trange
from colorama import init, Fore, Back, Style
from playsound import playsound

init(autoreset=True)

# Get durations (in min) for Timers
print(Fore.CYAN + Back.BLACK + Style.BRIGHT + 'How many minutes for the Timer?')
print(Fore.CYAN + Back.BLACK + Style.BRIGHT +
      '(Minutes between 1 & 90, Default: 25 min., enter for Default):')
timer_minutes = int(input() or "25")
while timer_minutes < 1 or timer_minutes > 90:
    print(Fore.RED + Back.BLACK + 'Minutes must be between 1 & 90, (Default: 25):')
    timer_minutes = int(input() or "25")

# Get durations (in min) for Short Breaks
print(Fore.CYAN + Back.BLACK + Style.BRIGHT +
      'How many minutes for the short Break?')
print(Fore.CYAN + Back.BLACK + Style.BRIGHT +
      '(Minutes between 1 & 10, Default: 5 min., enter for Default):')
break_short_minutes = int(input() or "5")
while break_short_minutes < 1 or break_short_minutes > 10:
    print(Fore.RED + Back.BLACK + 'Minutes must be between 1 & 10, (Default: 5):')
    break_short_minutes = int(input() or "5")

# Get durations (in min) for Long Breaks
print(Fore.CYAN + Back.BLACK + Style.BRIGHT +
      'How many minutes for the long Break?')
print(Fore.CYAN + Back.BLACK + Style.BRIGHT +
      '(Minutes between 1 & 30, Default: 15 min., enter for Default):')
break_long_minutes = int(input() or "15")
while break_long_minutes < 1 or break_long_minutes > 30:
    print(Fore.RED + Back.BLACK + 'Minutes must be between 1 & 30, (Default: 15):')
    break_long_minutes = int(input() or "15")

# Get input for manual/auto start of timers
print(Fore.CYAN + Back.BLACK + Style.BRIGHT +
      'Press enter to start timers? (y/n), Default="y" :')
manual_start = str.lower(str(input() or "y"))
while manual_start not in ["y", "n", "yes", "no"]:
    print(Fore.RED + Back.BLACK +
          'Invalid input, please type "Y" or "n", Default="y" :')
    manual_start = str.lower(str(input() or "y"))
if manual_start in ["y", "yes"]:
    manual_start = True
else:
    manual_start = False

# Variables for organizing the Timers
overall_cycles = 0
iterations = 4
timer_cycles = 1
seconds_in_timer = 60  # For config & debugging purposes

# Running the timers
while True:

    # Check if user wants another timer run
    if overall_cycles != 0:
        print(Fore.CYAN + Back.BLACK + Style.BRIGHT +
              'Run again? (y/n), Default="y" :')
        answer = str.lower(str(input() or "y"))
        while answer not in ["y", "n", "yes", "no"]:
            print(Fore.RED + Back.BLACK +
                  'Invalid input, please type "y" or "n", Default="y" :')
            answer = str.lower(str(input() or "y"))
        if answer in ["y", "yes"]:
            timer_cycles = 1
            pass
        else:
            print(Fore.BLACK + Back.MAGENTA + 'Productive: ' +
                  str(overall_cycles * 4 * timer_minutes) + ' minutes!')
            print(Fore.BLACK + Back.GREEN + 'Breaks: ' +
                  str(overall_cycles * (3 * break_short_minutes + break_long_minutes)) + ' minutes!')
            input("Press Enter to exit.")
            break

    # Run the timer
    while timer_cycles <= iterations:
        print(Fore.WHITE + Back.BLACK + Style.BRIGHT + 'Iteration: ' +
              str(timer_cycles))
        if manual_start:
            print(Fore.BLACK + Back.MAGENTA +
                  'Start timer with Enter.', end='')
            input()
        print(Fore.BLACK + Back.MAGENTA +
              'No interuptions for ' + str(timer_minutes) + ' minutes!')
        for i in trange((timer_minutes * seconds_in_timer), bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.MAGENTA, Fore.RESET)):
            time.sleep(1)
        playsound('./sounds/alarm_timer.wav')

        # Run the short break
        if timer_cycles <= 3:
            print(Fore.BLACK + Back.GREEN + 'Short break, ' +
                  str(break_short_minutes) + ' minutes!')
            if manual_start:
                print(Fore.BLACK + Back.GREEN +
                      'Start short break with Enter.', end='')
                input()
            for i in trange((break_short_minutes * seconds_in_timer), bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.GREEN, Fore.RESET)):
                time.sleep(1)
            playsound('./sounds/alarm_break_short.wav')

        # Run the long break
        else:
            print(Fore.BLACK + Back.YELLOW + 'Long break, ' +
                  str(break_long_minutes) + ' minutes!')
            if manual_start:
                print(Fore.BLACK + Back.YELLOW +
                      'Start long break with Enter.', end='')
                input()
            for i in trange((break_long_minutes * seconds_in_timer), bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.YELLOW, Fore.RESET)):
                time.sleep(1)
            playsound('./sounds/alarm_break_long.wav')

        timer_cycles += 1
    overall_cycles += 1
