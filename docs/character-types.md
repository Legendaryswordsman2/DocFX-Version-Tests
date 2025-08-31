---
uid: character-types
---

# Character Types

Character types are [Scriptable Objects](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ScriptableObject.html) that define core aspects of a character. They are the heart of the **Character Management System**.

> [!NOTE]
> All characters **Require** a **Character Type**.

---

## Character Type Base
All Character Types inherit from [CharacterTypeBaseSO](xref:BlazerTech.CharacterManagement.Characters.CharacterTypeBaseSO), which contains the core properties shared across all Character Types.

### Core Character Type Properties
The following properties are shared across all character types.

| Property                | Type                      | Description
|-----------------------------------------------------------------------------|---------------------------|---------------------------
| **[CharacterTypeID](character-type-fields.md#charactertypeid)**         | String                    | A **unique** identifer
| **[BaseSpritesheet](character-type-fields.md#basespritesheet)**         | Sprite                    | The default character spritesheet
| **[CharacterController](character-type-fields.md#charactercontroller)** | RuntimeAnimatorController | The Animator Controller used

[🔗 Read More → Character Type Properties](xref:character-type-fields)

---

## Character Type Variants

| Variant   | Modularity | Runtime Customization | Best For |
|-----------|--------------------|---------------|----------|
| **Unified** | Single spritesheet | None | Pre-created, fixed characters |
| **Layered** | Layered spritesheets | High | Modular, editable characters |

---

### 1. Unified Character Type
Each character uses a single spritesheet containing the fully assembled character. No runtime customization is possible.  
- **Use Case:** Characters with fixed, pre-created appearances.  
- **Example:** Simplistic characters where their appearance is pre-determined and won't need to be changed.

[🔗 Read More → Unified Character Type](unified-character-type.md)

---

### 2. Layered Character Type
A set of separate spritesheets, each containing one visual layer of the character.  
- **Use Case:** Customizable player characters or dynamically generated NPCs.  
- **Example:** Body, Outfit, Hairstyle, Accessory.  

[🔗 Read More → Layered Character Type](layered-character-type.md)