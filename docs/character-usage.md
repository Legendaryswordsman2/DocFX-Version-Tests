---
uid: character-usage
---

# Character Usage

The following scripts can be used to load and use characters

- **Layered Character Loader** - Load pre-existing Layered Characters.
- **Layered Character Template Loader** - Create/load a layered character from a template.
- **[Unified Character Loader](#unified-character-loader)** - Load a Unified Character from a template.

---

## The Character Shader

A **shader** is used to display characters. Sprites from the **Base Spritesheet** are rendered in a component such as a **Sprite Renderer**

If a **Unified Character** is used, the shader takes the single spritesheet of the character and shows that over the **Base Spritesheet**.  
If a **Layered Character** is used, the shader combines all layers into the final rendered character.  

> [!NOTE]
> If a **Character Loader** is used the shader will be set automatically.

---

## Character Loaders

Character loading scripts can be used to load any character you've created regardless of the type. All Character Loaders have these fields:

### References:
| Field | Type | Description |
|-------|------|-------------|
| **Renderer** | `Renderer` | Reference to a **Render** component such as a **Sprite Renderer**. Used to apply shader. |
| **Set Animator Controller** | `Bool` | Toggle if an **animator controller** should be applied to animate the character.  |
| **Animator** | `Animator` | Reference to an **Animator** component to apply the animator controller. Only shown if  **Set Animator Controller** is true. |

### Loading Settings:
| Field | Type | Description |
|-------|------|-------------|
| **Loading Mode** | `Enum` | Option to load character asynchronously or synchronously. |
| **Load Character On Start** | `Bool` | Toggles if the character should be loaded when the **Start** method is called. |

---

## Unified Character Loader
Requirements:  
Have a [Unified Character Type](xref:unified-character-type) and at least one [Unified Character Template](xref:character-templates#unified-character-template) Setup.

The **Unified Character Loader** component can be used to create and load a character from a **Unified Character Template**.  
- Add the script to a game object.
- Set **Renderer** and optionally **Animator** references.
- Set Loading Settings.
- Reference the **Unified Character Template** you want to load.
- Play your game and if **Load Character On Start** is toggled, your character will be displayed.

---

## Layered Character Loaders

### Layered Character Loader
Requirements:  
Have a [Layered Character Type](xref:layered-character-type) setup and at least one **Layered Character** saved in a group.

[🔗 Read More → Character Groups](xref:character-groups)

The **Layered Character Loader** component can be used to load **Layered Characters** from a **Character Group**.
- Add the script to a game object.
- Set **Renderer** and optionally **Animator** references.
- Set Loading Settings.
- Reference the **Character Type** you want to load a character from.
- Set the **Character Group** you want to load your character from within the **Character Type**.

#### Character Groups
After a **Character Type** has been referenced, you can choose which group you want to load a **Layered Character** from:

| Group Type | Description |
|------------|-------------|
| **Single Group** | Only one character can exist in the group. No additional parameters required. |
| **Flexible Group** | A group of characters that can be added, removed, or edited at any time. |
| **Fixed Group** | A group with a preset number of characters. New characters cannot be added or removed after creation. |

If **Flexible Group** or **Fixed Group** is selected, the following parameters are required:

| Parameter | Type | Description |
|-----------|------|-------------|
| **Character Group Name** | `String` | A unique name used to find the fixed or flexible group. |
| **Character Load Method** | `Enum` | Determines how a character is selected from the group: <br> - **Character Name** → Load a character by its saved name. <br> - **Character Index** → Load a character by its index position in the group. <br> - **Randomized** → Randomly load a character from the group. |

---

### Layered Character Template Loader
Requirements:  
Have a [Layered Character Type](xref:layered-character-type) and at least one [Layered Character Template](xref:character-templates#layered-character-template) Setup.

The **Layered Character Template Loader** component can be used to create and load a character from a  **Layered Character Template**.  
- Add the script to a game object.
- Set **Renderer** and optionally **Animator** references.
- Set Loading Settings.
- Reference the **Layered Character Template** you want to load.
- Play your game and if **Load Character On Start** is toggled, your character will be displayed.
