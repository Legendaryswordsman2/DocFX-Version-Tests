---
uid: character-type-fields
---

# Character Type Fields

The following are fields that are shared across all **Character Type** [Scriptable Objects](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ScriptableObject.html).

Don’t know what a Character Type is?  
[🔗 Read More → Character Types](xref:character-types)

---

## CharacterTypeID
| Field | Type | Description |
|----------|------|-------------|
| **CharacterTypeID** | `String` | A unique identifier for this Character Type. Must be unique across all types. |

> [!WARNING]  
> A **Character Type** with the same **ID** as another will fail to initialize and all characters of that type will also fail to load.

[🔗 API](xref:BlazerTech.CharacterManagement.Characters.CharacterTypeBaseSO.CharacterTypeID)

---

## BaseSpritesheet
| Field | Type | Description |
|----------|------|-------------|
| **BaseSpritesheet** | `Spritesheet` | The base reference spritesheet used for all characters of this type. Every character spritesheet must match its dimensions exactly. |

> [!WARNING]  
> Character Spritesheets of a different size will be rejected, and a warning will be logged.

### Setup Requirements
- **Sprite Mode** must be set to **Multiple** so the sheet can be sliced into individual frames.  
- All animations and shaders reference the **Base Spritesheet**. When the character is loaded a shader will display the correct character over the Base Spritesheet.

[🔗 API](xref:BlazerTech.CharacterManagement.Characters.CharacterTypeBaseSO.BaseSpritesheet)

---

## CharacterController
| Property | Type | Description |
|----------|------|-------------|
| **CharacterController** | `RuntimeAnimatorController` | An Animator Controller that animates all characters of this Character Type. |

> [!NOTE]  
> This field is **optional**.  

Because all characters of a type use the **Base Spritesheet** (see [BaseSpritesheet](#basespritesheet)), a single Animator Controller can be reused as long as its animations reference frames from the **Base Spritesheet**.  

> [!TIP]  
> When using a Character Loader component, this Animator Controller will be applied automatically if **Set Animator Controller** is enabled.  
> See [🔗 Character Usage](xref:character-usage) for more info.

[🔗 API](xref:BlazerTech.CharacterManagement.Characters.CharacterTypeBaseSO.CharacterController)