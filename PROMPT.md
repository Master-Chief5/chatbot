# 🔁 Upgrade Prompt — paste this back to Claude to grow the game

Copy the block below, fill in the **[ ]** parts with what you want, and send it.
You can ask for one thing or a whole list — Claude will edit `index.html`, keep the
existing structure, push to the branch, and update the PR.

---

```
Keep building my first-person Backrooms game in this repo (index.html, Three.js,
single-file, mobile-friendly, no API key). Keep the existing architecture and the
persistent upgrade system. Don't break mobile touch controls.

Add / change the following:

- [ ] e.g. New level "The Poolrooms" you reach through a hidden exit door
- [ ] e.g. A map / minimap toggle
- [ ] e.g. A second entity type (Hound) that chases faster but is blind to sound
- [ ] e.g. A sprint-jump, crouch, or sound-meter mechanic
- [ ] e.g. A run timer + best-time leaderboard saved in localStorage
- [ ] e.g. New upgrade: "Almond Cache" that auto-collects nearby bottles
- [ ] e.g. Better graphics: textured ceiling lights, doors, exit signs
- [ ] e.g. A jumpscare + sound when the entity catches me

When done: commit, push to the branch, update the PR, and tell me how to test it.
```

---

## Ideas menu (pick any)

**Levels / world**
- Multiple named levels (Level 0, Level 1 "Habitable Zone", Poolrooms, Level !).
- Exit doors that no-clip you to the next level; level select after you find them.
- Bigger / infinite procedural chunks that stream as you walk.

**Mechanics**
- Crouch + sound system (running/loud = entities hear you).
- Stamina-based sprint-jump; ledges and vents.
- Hunger/thirst meters alongside sanity.
- Inventory with usable items (flares, batteries, keycards).

**Enemies**
- More entity types with distinct behavior (Hounds, Smilers, Skin-Stealers).
- Line-of-sight + hearing AI instead of pure distance.
- Proper jumpscares with audio stings.

**Progression / meta**
- Run timer, distance traveled, deepest level — saved as records.
- Daily seed challenge.
- Cosmetic unlocks (flashlight colors, HUD themes).

**Polish**
- Minimap / compass.
- Better lighting (real flickering fluorescents, baked light maps).
- Settings menu: sensitivity, FOV, quality, audio volume.
- Gamepad support.

## Notes for whoever picks this up

- Everything lives in `index.html`. Sections are labeled with `// ====` banners:
  SAVE/PROGRESSION, WORLD GENERATION, TEXTURES, RENDERER/SCENE, PICKUPS+ENTITY,
  PLAYER STATE, INPUT, ACTIONS, GAME LOOP, HUD/SCREENS, AUDIO.
- New upgrades: add an entry to the `UPGRADES` object and read its level in `stats()`.
- Save data persists under localStorage key `backrooms_save_v1` — bump the suffix if
  you change the save shape so old saves don't break.
