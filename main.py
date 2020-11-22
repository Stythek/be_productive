import time
from tqdm import tqdm, trange
from colorama import init, Fore, Back, Style
from playsound import playsound

init(autoreset=True)

# Get durations (in min) for Timer, Short & Long Breaks
print(Fore.CYAN + Style.BRIGHT + 'How many minutes for the Timer?')
print(Fore.CYAN + Style.BRIGHT +
      '(Minutes between 1 & 90, Default: 25 min., enter for Default):')
timer_minutes = int(input() or "25")
while timer_minutes < 1 or timer_minutes > 90:
    print(Fore.RED + 'Minutes must be between 1 & 90, (Default: 25):')
    timer_minutes = int(input() or "25")

print(Fore.CYAN + Style.BRIGHT + 'How many minutes for the short Break?')
print(Fore.CYAN + Style.BRIGHT +
      '(Minutes between 1 & 10, Default: 5 min., enter for Default):')
break_short_minutes = int(input() or "5")
while break_short_minutes < 1 or break_short_minutes > 10:
    print(Fore.RED + 'Minutes must be between 1 & 10, (Default: 5):')
    break_short_minutes = int(input() or "5")

print(Fore.CYAN + Style.BRIGHT + 'How many minutes for the long Break?')
print(Fore.CYAN + Style.BRIGHT +
      '(Minutes between 1 & 30, Default: 20 min., enter for Default):')
break_long_minutes = int(input() or "20")
while break_long_minutes < 1 or break_long_minutes > 30:
    print(Fore.RED + 'Minutes must be between 1 & 30, (Default: 20):')
    break_long_minutes = int(input() or "20")

# Variables for organizing the Timers
overall_runs = 0
iterations = 4
timer_count = 1

while True:
    if overall_runs != 0:
        print(Fore.CYAN + Style.BRIGHT + 'Run again? (y/n):')
        answer = str(input())
        while str.lower(answer) not in ["y", "n", "yes", "no"]:
            print(Fore.RED + 'Invalid input, please type "y" or "n":')
            answer = str(input())
        if str.lower(answer) in ["y", "yes"]:
            timer_count = 1
            pass
        else:
            print(Fore.BLACK + Back.MAGENTA + 'Productive: ' +
                  str(4 * timer_minutes) + ' minutes!')
            print(Fore.BLACK + Back.GREEN + 'Breaks: ' +
                  str(4 * timer_minutes) + ' minutes!')
        break

    while timer_count <= iterations:
        print(Fore.WHITE + Style.BRIGHT + 'Iteration: ' +
              str(timer_count))
        print(Fore.BLACK + Back.MAGENTA +
              'No interuptions for ' + str(timer_minutes) + ' minutes!')
        for i in trange((timer_minutes * 60), bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.MAGENTA, Fore.RESET)):
            time.sleep(1)
        playsound('./sounds/alarm_timer.wav')
        if timer_count <= 3:
            print(Fore.BLACK + Back.GREEN + 'Short break, ' +
                  str(break_short_minutes) + ' minutes!')
            for i in trange((break_short_minutes * 60), bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.GREEN, Fore.RESET)):
                time.sleep(1)
            playsound('./sounds/alarm_break_short.wav')
        else:
            print(Fore.BLACK + Back.GREEN + 'Long break, ' +
                  str(break_long_minutes) + ' minutes!')
            for i in trange((break_long_minutes * 60), bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.GREEN, Fore.RESET)):
                time.sleep(1)
            playsound('./sounds/alarm_break_long.wav')
        timer_count += 1
    overall_runs += 1
