from colorama import init, Fore
from generation import noise, cellular_automata, map_utils
import copy

init(convert=True)
show_noise_map = False

def select_options():
    print(Fore.YELLOW + "\nWelcome to a procedural generation example! Let's configure some stuff before we get to the generating." + Fore.RESET)

    answer = input("\nWould you like to see the noise map along side the generated map (Y/N)?\nCHOICE: ").lower()

    while answer not in ["y", "n"]:
        print(Fore.RED + "\nInvalid option! Please try again." + Fore.RESET)
        answer = input("Would you like to see the noise map along side the generated map (Y/N)?\nCHOICE: ").lower()
    
    global show_noise_map
    show_noise_map = True if answer == "y" else False

    main()

def main():
    keep_going = True
    while keep_going:
        invalid_value = True
        while invalid_value:
            try:
                width = int(input("\nMap Width: "))
                height = int(input("Map Height: "))
                fill_percentage = int(input("Noise Map Fill Percentage (whole number): "))

                print(Fore.YELLOW + "\nGENERATING NOISE MAP..." + Fore.RESET)
                noise_map = noise.generate_noise_map(width, height, fill_percentage)
                print(Fore.GREEN + "NOISE MAP GENERATED!" + Fore.RESET)

                use_same_map = True
                while use_same_map:
                    iterations = int(input("\nHow many times would you like to apply cellular\nautomata to the noise map: "))
                    cellular_automata_map = cellular_automata.apply_cellular_automata(copy.deepcopy(noise_map), iterations)

                    global show_noise_map
                    if show_noise_map:
                        print("\n\nNOISE MAP: ")
                        map_utils.print_map(noise_map)

                    print("\n\nCELLULAR AUTOMATA:")
                    map_utils.print_map(cellular_automata_map)

                    answer = input("Would you like to go again (Y/N)?\nCHOICE: ")
                    while answer not in ["y", "n"]:
                        print(Fore.RED + "\nInvalid option! Please try again." + Fore.RESET)
                        answer = input("Would you like to go again (Y/N)?\nCHOICE: ").lower()
                    
                    keep_going = True if answer == "y" else False

                    if keep_going == False:
                        break

                    answer = input("Would you like to use the same map (Y/N)?\nCHOICE: ").lower()
                    while answer not in ["y", "n"]:
                        print(Fore.RED + "\nInvalid option! Please try again." + Fore.RESET)
                        answer = input("Would you like to use the same map (Y/N)?\nCHOICE: ").lower()
                    
                    use_same_map = True if answer == "y" else False
                
                # Somewhat hacky, but works!
                if use_same_map == False:
                    invalid_value = True
                else:
                    invalid_value = False
            except ValueError:
                invalid_value = True
                print(Fore.RED + "\nInvalid value submitted! Please try again." + Fore.RESET)
    
    print(Fore.GREEN + "\nGoodbye!" + Fore.RESET)

if __name__ == '__main__':
    select_options()