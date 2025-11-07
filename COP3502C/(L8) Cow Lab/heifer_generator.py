# heifer_generator.py
from cow import Cow
from dragon import Dragon
from ice_dragon import IceDragon

def get_cows():
    # Keep the three leading quote lines exactly as before
    quote_lines = "    \\\n"
    quote_lines += "     \\\n"
    quote_lines += "      \\\n"

    heifer_art = (
        "        ^__^\n"
        "        (oo)\\_______\n"
        "        (__)\\       )\\/\\\n"
        "            ||----w |\n"
        "            ||     ||\n"
    )

    kitteh_art = (
        "       (\"`-'  '-/\") .___..--' ' \"`-._\n"
        "         ` *_ *  )    `-.   (      ) .`-.__. `)\n"
        "         (_Y_.) ' ._   )   `._` ;  `` -. .-'\n"
        "      _.. `--'_..-_/   /--' _ .' ,4\n"
        "   ( i l ),-''  ( l i),'  ( ( ! .-'\n"
    )

    # Dragon ASCII art (exactly as sample)
    dragon_art = (
        "           |\\___/|       /\\  //|\\\\\n"
        "           /0  0  \\__   /  \\\\// | \\ \\\n"
        "          /     /  \\/_ /   //  |  \\  \\\n"
        "          \\_^_\\'/   \\/_   //   |   \\   \\\n"
        "          //_^_/     \\/_ //    |    \\    \\\n"
        "       ( //) |        \\ //     |     \\     \\\n"
        "     ( / /) _|_ /   )   //     |      \\     _\\n"
        "   ( // /) '/,_ _ _/  ( ; -.   |    _ _\\.-~       .-~~~^-.\n"
        " (( / / )) ,-{        _      `.|.-~-.          .~         `.\n"
        "(( // / ))  '/\\      /                ~-. _.-~      .-~^-.  \\\n"
        "(( /// ))      `.   {            }                 /      \\  \\\n"
        " (( / ))     .----~-.\\        \\-'               .~         \\  `.   __\n"
        "            ///.----..>        \\            _ -~            `.  ^-`  \\\n"
        "              ///-._ _ _ _ _ _ _}^ - - - - ~                   `-----'\n"
    )

    cows = []

    # Order must match sample: heifer kitteh dragon ice-dragon
    heifer = Cow("heifer")
    heifer.set_image(quote_lines + heifer_art)
    cows.append(heifer)

    kitteh = Cow("kitteh")
    kitteh.set_image(quote_lines + kitteh_art)
    cows.append(kitteh)

    dragon = Dragon("dragon", quote_lines + dragon_art)
    cows.append(dragon)

    ice_dragon = IceDragon("ice-dragon", quote_lines + dragon_art)  # same art as sample
    cows.append(ice_dragon)

    return cows

