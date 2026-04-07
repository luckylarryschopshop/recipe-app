# Product Requirements Document (PRD) - Recipe Manager Web App

## 1. Overview

The Recipe Manager Web App is a tool designed to help users manage their recipes. It allows users to add, scale, search, and delete recipes. The application is built with a FastAPI backend and an HTML frontend. Recipes are stored in JSON format.

## 2. Features

### 2.1 Add Recipe
- Users can add a new recipe with the following details:
  - Name
  - Ingredients list (name and quantity)
  - Steps (instructions)
  - Servings (number of people the recipe serves)

### 2.2 Scale Recipe
- Users can scale a recipe up or down based on the number of servings required.

### 2.3 Search
- Users can search for recipes by name or ingredients.

### 2.4 Delete
- Users can delete a recipe from their collection.

### 2.5 Storage
- All recipes are stored in a JSON file on the server.

## 3. User Stories

### 3.1 As a user, I want to add a recipe so that I can save and manage my favorite dishes.

### 3.2 As a user, I want to scale a recipe so that I can adjust the quantity based on the number of people I’m cooking for.

### 3.3 As a user, I want to search for recipes so that I can quickly find what I’m looking for.

### 3.4 As a user, I want to delete a recipe so that I can remove recipes I no longer need.

## 4. Acceptance Criteria

### 4.1 Add Recipe
- The user can input a recipe name.
- The user can input a list of ingredients with quantities.
- The user can input step-by-step instructions.
- The user can input the number of servings.
- The recipe is saved in JSON format.

### 4.2 Scale Recipe
- The user can input a desired number of servings.
- The application adjusts the ingredients and steps accordingly.
- The scaled recipe is displayed to the user.

### 4.3 Search
- The user can search by recipe name.
- The user can search by ingredient.
- The application returns matching recipes.

### 4.4 Delete
- The user can select a recipe to delete.
- The application removes the selected recipe from storage.

### 4.5 Storage
- All recipes are stored in a JSON file.
- The JSON file is accessible and readable by the backend.