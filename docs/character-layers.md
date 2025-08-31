# Character Layers
A Character Layer is a [Scriptable Object](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ScriptableObject.html) that contains all available character spritesheets for that specific layer.

## What's a Character Piece Definition?
A Character Piece Definition is a wrapper for a spritesheet which allows for easy loading/unloading of the sprite when needed.

---

## Properties

### Attached Character Type
The **Layered Character Type** the layer is meant to be used for.

### Layer Name
The name of the layer. Used in the [Character Creator](character-creator.md) when displaying character layers.

### Character Piece Asset Label
The **Addressables label** used to load sprites into **Character Piece Definitions**. **BT-CMS** uses Unity's **Addressables package** to dynamically load/unload sprites when needed. Select the label you'd like to use and make sure all character spritesheets meant to be used for this layer are marked as Addressable and have the same label.

### Include None Option
Decides if a blank option should be added to the list of available Character Pieces. This will essentially allow a character to be created without using that layer.

> [!WARNING]
> The **Character Pieces** list must be refreshed whenever **Include None Option** is changed!

---

## Buttons

### Get Character Pieces
Finds all sprites matching the **Character Piece Asset Label** and are the same size as the [Base Spritesheet](character-type-fields.md#basespritesheet) in the **Layered Character Type**, creates a **CharacterPieceDefinition** for each one and adds it to the **Character Pieces** list.

### Clear Character Pieces
Clears the Character Pieces list

> [!CAUTION]
> This cannot be undone!