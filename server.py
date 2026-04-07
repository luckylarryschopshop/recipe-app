from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import json
import os

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

recipes = []
recipe_id = 0

if os.path.exists("recipes.json"):
    with open("recipes.json", "r") as f:
        recipes = json.load(f)
        recipe_id = len(recipes)

@app.get("/api/recipes")
def get_recipes():
    return recipes

@app.post("/api/recipes")
def create_recipe(name: str, ingredients: list, steps: list, servings: int):
    global recipe_id
    recipe = {
        "id": recipe_id,
        "name": name,
        "ingredients": ingredients,
        "steps": steps,
        "servings": servings
    }
    recipes.append(recipe)
    recipe_id += 1
    with open("recipes.json", "w") as f:
        json.dump(recipes, f)
    return recipe

@app.delete("/api/recipes/{id}")
def delete_recipe(id: int):
    global recipes
    recipes = [r for r in recipes if r["id"] != id]
    with open("recipes.json", "w") as f:
        json.dump(recipes, f)
    return {"status": "deleted"}

@app.get("/api/recipes/{id}/scale")
def scale_recipe(id: int, servings: int):
    recipe = next((r for r in recipes if r["id"] == id), None)
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    scale = servings / recipe["servings"]
    scaled_ingredients = [
        {**ing, "quantity": ing["quantity"] * scale} for ing in recipe["ingredients"]
    ]
    return {"ingredients": scaled_ingredients}

@app.get("/")
def get_index():
    return HTMLResponse(content=open("static/index.html").read())