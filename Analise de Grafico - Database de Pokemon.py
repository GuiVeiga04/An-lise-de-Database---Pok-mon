import pandas as pd

pk = pd.read_csv("pokemon.csv")

sel = pk[["against_dark", "against_dragon", "against_fairy", "against_ice"]]
poke = pk[["name"]]
se = sel >= 2
mel_pok = pk[se]

print(mel_pok, poke)