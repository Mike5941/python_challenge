import prettytable

from prettytable import PrettyTable, MSWORD_FRIENDLY, PLAIN_COLUMNS
table = PrettyTable()
table.set_style(PLAIN_COLUMNS)

table.add_column("Pocketmon", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
