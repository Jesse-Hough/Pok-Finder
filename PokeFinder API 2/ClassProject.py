from string import capwords
from flask import Flask, render_template, request, abort
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, StringField, RadioField, validators
import requests
import main_functions
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)


class PokeForm(FlaskForm):
    PokemonName = StringField('Name', [validators.DataRequired()])
    PokemonType = SelectField("Type", choices=[
        ("Default"),
        ("Shiny"),
    ])
    PokeEra = SelectField("Pokemon Era", choices=[
        ("No Sprite Selected"),
        ("Red-Blue Sprite"),
        ("Yellow Sprite"),
        ("Crystal Sprite"),
        ("Gold Sprite"),
        ("Silver Sprite"),
        ("Emerald Sprite"),
        ("FireRed-LeafGreen Sprite"),
        ("Ruby-Sapphire Sprite"),
        ("Diamond-Pearl Sprite"),
        ("HeartGold-SoulSilver Sprite"),
        ("Platinum Sprite"),
        ("Black-White Sprite"),
        ("Omega Ruby-Alpha Sapphire Sprite"),
        ("X-Y Sprite"),
        ("Ultra-Sun-Ultra-Moon Sprite")
    ])
    PokemonStats = RadioField("Stat", [validators.InputRequired()],choices=[
        ("HP"),
        ("Attack"),
        ("Defense"),
        ("All Stats")
    ])
    submit = SubmitField()


def get_poke_data(pokemon_name, pokemon_type, pokemon_era, pokemon_stat):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    if response.status_code == 404:
        abort(404)
    response = response.json()
    main_functions.save_to_file(response, "pokemon.json")
    name = response["name"]
    if pokemon_type == "Default":
        type = response["sprites"]["other"]["official-artwork"]["front_default"]
    else:
        type = response["sprites"]["other"]["official-artwork"]["front_shiny"]
    if pokemon_era == "no sprite selected":
        era = ""
        pokemon_era = ""
    elif pokemon_era == "red-blue sprite":
        era = response["sprites"]["versions"]["generation-i"]["red-blue"]["front_transparent"]
    elif pokemon_era == "yellow sprite":
        era = response["sprites"]["versions"]["generation-i"]["yellow"]["front_transparent"]
    elif pokemon_era == "crystal sprite" and pokemon_type == "Default":
        era = response["sprites"]["versions"]["generation-ii"]["crystal"]["front_transparent"]
    elif pokemon_era == "crystal sprite" and pokemon_type == "Shiny":
        era = response["sprites"]["versions"]["generation-ii"]["crystal"]["front_shiny_transparent"]
    elif pokemon_era == "gold sprite" and pokemon_type == "Default":
        era = response["sprites"]["versions"]["generation-ii"]["gold"]["front_transparent"]
    elif pokemon_era == "gold sprite" and pokemon_type == "Shiny":
        era = response["sprites"]["versions"]["generation-ii"]["gold"]["front_shiny"]
    elif pokemon_era == "silver sprite" and pokemon_type == "Default":
        era = response["sprites"]["versions"]["generation-ii"]["silver"]["front_transparent"]
    elif pokemon_era == "silver sprite" and pokemon_type == "Shiny":
        era = response["sprites"]["versions"]["generation-ii"]["silver"]["front_shiny"]
    elif pokemon_era == "emerald sprite" and pokemon_type == "Default":
        era = response["sprites"]["versions"]["generation-iii"]["emerald"]["front_default"]
    elif pokemon_era == "emerald sprite" and pokemon_type == "Shiny":
        era = response["sprites"]["versions"]["generation-iii"]["emerald"]["front_shiny"]
    elif pokemon_era == "firered-leafgreen sprite" and pokemon_type == "Default":
        era = response["sprites"]["versions"]["generation-iii"]["firered-leafgreen"]["front_default"]
    elif pokemon_era == "firered-leafgreen sprite" and pokemon_type == "Shiny":
        era = response["sprites"]["versions"]["generation-iii"]["firered-leafgreen"]["front_shiny"]
    elif pokemon_era == "ruby-sapphire sprite" and pokemon_type == "Default":
        era = response["sprites"]["versions"]["generation-iii"]["ruby-sapphire"]["front_default"]
    elif pokemon_era == "ruby-sapphire sprite" and pokemon_type == "Shiny":
        era = response["sprites"]["versions"]["generation-iii"]["ruby-sapphire"]["front_shiny"]
    elif pokemon_era == "diamond-pearl sprite" and pokemon_type == "Default":
        era = response["sprites"]["versions"]["generation-iv"]["diamond-pearl"]["front_default"]
    elif pokemon_era == "diamond-pearl sprite" and pokemon_type == "Shiny":
        era = response["sprites"]["versions"]["generation-iv"]["diamond-pearl"]["front_shiny"]
    elif pokemon_era == "heartgold-soulsilver sprite" and pokemon_type == "Default":
        era = response["sprites"]["versions"]["generation-iv"]["heartgold-soulsilver"]["front_default"]
    elif pokemon_era == "heartgold-soulsilver sprite" and pokemon_type == "Shiny":
        era = response["sprites"]["versions"]["generation-iv"]["heartgold-soulsilver"]["front_shiny"]
    elif pokemon_era == "platinum sprite" and pokemon_type == "Default":
        era = response["sprites"]["versions"]["generation-iv"]["platinum"]["front_default"]
    elif pokemon_era == "platinum sprite" and pokemon_type == "Shiny":
        era = response["sprites"]["versions"]["generation-iv"]["platinum"]["front_shiny"]
    elif pokemon_era == "black-white sprite" and pokemon_type == "Default":
        era = response["sprites"]["versions"]["generation-v"]["black-white"]["front_default"]
    elif pokemon_era == "black-white sprite" and pokemon_type == "Shiny":
        era = response["sprites"]["versions"]["generation-v"]["black-white"]["front_shiny"]
    elif pokemon_era == "omega ruby-alpha sapphire sprite" and pokemon_type == "Default":
        era = response["sprites"]["versions"]["generation-vi"]["omegaruby-alphasapphire"]["front_default"]
    elif pokemon_era == "omega ruby-alpha sapphire sprite" and pokemon_type == "Shiny":
        era = response["sprites"]["versions"]["generation-vi"]["omegaruby-alphasapphire"]["front_shiny"]
    elif pokemon_era == "x-y sprite" and pokemon_type == "Default":
        era = response["sprites"]["versions"]["generation-vi"]["x-y"]["front_default"]
    elif pokemon_era == "x-y sprite" and pokemon_type == "Shiny":
        era = response["sprites"]["versions"]["generation-vi"]["x-y"]["front_shiny"]
    elif pokemon_era == "ultra-sun-ultra-moon sprite" and pokemon_type == "Default":
        era = response["sprites"]["versions"]["generation-vii"]["ultra-sun-ultra-moon"]["front_default"]
    elif pokemon_era == "ultra-sun-ultra-moon sprite" and pokemon_type == "Shiny":
        era = response["sprites"]["versions"]["generation-vii"]["ultra-sun-ultra-moon"]["front_shiny"]
    else:
        era = ""
    if pokemon_stat == "All Stats":
        hp1 = response["stats"][0]["stat"]["name"]
        hp2 = response["stats"][0]["base_stat"]
        att1 = response["stats"][1]["stat"]["name"]
        att2 = response["stats"][1]["base_stat"]
        def1 = response["stats"][2]["stat"]["name"]
        def2 = response["stats"][2]["base_stat"]
        specA1 = response["stats"][3]["stat"]["name"]
        specA2 = response["stats"][3]["base_stat"]
        specD1 = response["stats"][4]["stat"]["name"]
        specD2 = response["stats"][4]["base_stat"]
        speed1 = response["stats"][5]["stat"]["name"]
        speed2 = response["stats"][5]["base_stat"]
        height1 = "height"
        height2 = '%.1f' % (response["height"] * 0.328084)
        weight1 = "weight"
        weight2 = '%.1f' % (response["weight"] * 0.220462)
    else:

        if pokemon_stat == "HP":
            stat = response["stats"][0]["base_stat"]
        elif pokemon_stat == "Attack":
            stat = response["stats"][1]["base_stat"]
        else:
            stat = response["stats"][2]["base_stat"]
        return {
            "name": name,
            "type": type,
            "stat": stat,
            "pokeEra": capwords(pokemon_era),
            "era": era
        }
    return {
        "name": capwords(name),
        "type": type,
        "era": era,
        "pokeEra": capwords(pokemon_era),
        "hp1": capwords(hp1)+":",
        "hp2": hp2,
        "att1": capwords(att1)+":",
        "att2": att2,
        "def1": capwords(def1)+":",
        "def2": def2,
        "specA1": capwords(specA1)+":",
        "specA2": specA2,
        "specD1": capwords(specD1)+":",
        "specD2": specD2,
        "speed1": capwords(speed1)+":",
        "speed2": speed2,
        "height1": capwords(height1)+":",
        "height2": str(height2)+"ft",
        "weight1": capwords(weight1)+":",
        "weight2": str(weight2)+"lbs"
    }


@app.errorhandler(404)
def page_not_found(e):
    return render_template('500.html'), 404


@app.route('/', methods=['GET', 'POST'])
def index():
    form = PokeForm()
    if request.method == "POST":
        name_entered = form.PokemonName.data.lower()
        type_entered = form.PokemonType.data
        era_entered = form.PokeEra.data.lower()
        stat_entered = form.PokemonStats.data
        all_data = get_poke_data(name_entered, type_entered, era_entered, stat_entered)
        return render_template("poke_results.html", data=all_data, stat=stat_entered, era=capwords(era_entered))
    return render_template("home_page.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)