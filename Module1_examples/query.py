GET_CHARACTERS = """
  SELECT *
  FROM charactercreator_character;
"""

GET_CHARACTER_NAMES = """
  SELECT name
  FROM charactercreator_character;
"""

QUERY_LIST = [GET_CHARACTERS, GET_CHARACTER_NAMES]
