import os
import sqlite3

# construct a path to wherever your database exists
#DB_FILEPATH = "module1-introduction-to-sql/chinook.db"
#DB_FILEPATH = os.path.join("module1-introduction-to-sql", "chinook.db")
#DB_FILEPATH = os.path.join(os.path.dirname(__file__), ",,", "module2-0...", ""chinook.db")
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "rpg_db.sqlite3")

# connecting to the database
connection = sqlite3.connect(DB_FILEPATH)

# cursor
cursor = connection.cursor()


# How many total Characters are there?
query = "SELECT COUNT(distinct character_id) FROM charactercreator_character"

# How many of each specific subclass?
query = "SELECT COUNT(distinct character_ptr_id) FROM charactercreator_mage"

query = "SELECT COUNT(distinct mage_ptr_id) FROM charactercreator_necromancer"

query = "SELECT COUNT(distinct character_ptr_id) FROM charactercreator_fighter"

query = "SELECT COUNT(distinct character_ptr_id) FROM charactercreator_cleric"

query = "SELECT COUNT(distinct character_ptr_id) FROM charactercreator_thief"

# How many total Items?
query = "SELECT COUNT(distinct item_id) FROM armory_item"

# How many of the Items are weapons? How many are not?
query = "SELECT COUNT(item_ptr_id) as weapons_count FROM armory_weapon"

# How many Items does each character have? (Return first 20 rows)
query = "SELECT character_id,item_id FROM charactercreator_character_inventory LIMIT 20"

# How many Weapons does each character have? (Return first 20 rows)
query = "SELECT character_id ,count(distinct item_id) as weapons_count FROM charactercreator_character_inventory WHERE item_id IN (SELECT distinct item_ptr_id FROM armory_weapon) GROUP BY character_id LIMIT 20"

# On average, how many Items does each Character have?
query = "SELECT ccc.character_id ,AVG(cinv.item_id) as items FROM charactercreator_character ccc LEFT JOIN charactercreator_character_inventory cinv ON ccc.character_id = cinv.character_id"

# On average, how many Weapons does each character have?
query = "SELECT character_id ,count(item_id) as items FROM charactercreator_character_inventory WHERE item_id IN (SELECT distinct item_ptr_id from armory_weapon) GROUP BY character_id"

#result = cursor.execute(query)
#print("RESULT", result) #> returns cursor object w/o results (need to fetch the results)

result3 = cursor.execute(query).fetchone()
print("RESULT 3", type(result3), result3)

for row in result3:
    print(type(row), row)

