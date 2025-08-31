---
uid: unified-character-type
---

# Unified Character Type
A Unified Character is made of one single spritesheet which contains every animation of the character.

## Creating a Layered Character Type
to create a new layered character type right click the **Project** window and navigate to **Create > BlazerTech Character Management System > Unified Character Type**.

> [!IMPORTANT]
> The **Unified Character Type Scriptable Object** does **NOT** need to be placed inside a Resources folder unlike **Layered Character Types**.

---

### Setting up a Unified Character Type
The following properties must be set:

| Property                | Type                      | Description
|-----------------------------------------------------------------------------|---------------------------|---------------------------
| **[CharacterTypeID](character-type-fields.md#charactertypeid)**         | String                    | A **unique** identifer
| **[BaseSpritesheet](character-type-fields.md#basespritesheet)**         | Sprite                    | The default character spritesheet
| **[CharacterController](character-type-fields.md#charactercontroller)** | RuntimeAnimatorController | The Animator Controller used

That's it! Once your **Unified Character Type** is all setup you can create a **Unified Character Template** to make characters from this **Character Type**.

[🔗 Read More → Unified Character Templates](character-templates.md#unified-character-template)