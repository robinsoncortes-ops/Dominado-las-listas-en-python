# tu datos

edades = [14,15,17,13,12]
musica = ["salsa","rock","vallenato","pop","tramp"]

# RETO 1
promedio = sum(edades) / len(edades)
print("promedio de edad:",promedio)

# RETO 2
mayores = [edad for edad in edades if edad > 15]
print("edades > 15:", mayores)

# RETO 3 
fans_rock = [gen for gen in musica if gen == "rock"]
print("total de fans rock: ", len(fans_rock))
