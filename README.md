# Recipe App

Recipe manager with ingredient scaling

## Run

```bash
docker compose up -d
# Open http://127.0.0.1:PORT
```

## API

  - GET /api/recipe_app — list all items
  - POST /api/recipe_app — add item (send JSON body)
  - PUT /api/recipe_app/{id} — update item (send JSON body)
  - DELETE /api/recipe_app/{id} — delete item
  - GET /api/recipe_app/search?q=term — search items

