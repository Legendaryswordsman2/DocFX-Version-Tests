---
uid: character-groups
---

# Character Groups

## Character Group Definitions

Character Groups make it easy to categorize and use characters in a variety of situations. They are optional in most cases but can be very handy.

Every Layered Character Type contains three group types.

| Type | Description | Use Case
|----------|-------------|
| **Single** | Contains one character. Only **one** Single Group can exist per Character Type.               | simple situations where only one character is used such as a player character. |
| **Flexible** | A list of any amount of characters. Characters can be added, removed or edited at any time. | Situations where a dynamic and editable list is needed. Such as a collection of playable characters the player can create and choose from. |
| **Fixed** | A list of a pre-determined amount of characters. The number is set when the list is created and all characters are created immedietely. Characters within the list can be edited at anytime but cannot be removed and new characters cannot be added. | Situations where an immutable list is needewd. Such as a set list of playable characters the player can choose from. |

---

## Character Group Registry

The [CharacterGroupRegistry](xref:BlazerTech.CharacterManagement.Characters.CharacterGroupRegistry) class contains all three groups types.
It contains one Single Group and a list of Flexible and Fixed Groups.

The [LayeredCharacterGroupManager](xref:BlazerTech.CharacterManagement.Characters.LayeredCharacterGroupManager) class contains a dictionary of `CharacterTypeGroupsRegistry`. One entry for each Layered Character Type used.

---

## Single Group

A group which contains only one character. This group is always present in every Character Group Registry.

This group mainly exists to make creating simple scenarioes easily. For example if you have a Character Creation Menu setup you can call the `EnableMenuSingleGroup` to automically enable the menu and save the created character to the Single Group of the Character Type used.

Then later that character can be used by using the **Layered Character Loader**, giving it the same character type and telling it to load the Single Group.

---

## Flexible Group

A dynamic list where characters can be added to, removed from, or edited at anytime.

---

## Fixed Group

An immutable list of characters. The size is defined when creating the list and all characters are created immedietely upon group creation. Characters within the group can be modified or even swapped out but the size of the list cannot change.

---

## Adding a Layered Character to a Group