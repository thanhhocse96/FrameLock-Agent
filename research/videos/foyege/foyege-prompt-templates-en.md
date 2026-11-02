# Foyege Prompt Templates (English, Structural Reconstruction)

## Change log — update 2026-10-28, after user request

What was changed in this update, and only this:
- Added explicit source links mapped to each template below (Template A = 11 Oct post, Template B = 23 Sep post, Template C = 16 Sep post), so the analyzing agent can open the original X post for each template without hunting through the list.
- Added this change log itself, at the top of the file, stating what was edited.
- Did NOT add a verbatim translation of Foyege's original prompts. The templates remain structural reconstructions in the author's own analysis wording, for the copyright reason explained in the note below.
- Deep structural analysis was NOT added here. Per the user's instruction, it goes in a separate file: `foyege-prompt-structure-deep-analysis.md` (same folder).

Source links by template:
- Template A (transformation and fight): https://x.com/Foyege24/status/2109113006953263233
- Template B (butterfly-to-woman single take): https://x.com/Foyege24/status/2102610496683933915
- Template C (DEADSHOT title montage): https://x.com/Foyege24/status/2100222945499263146

## Important note for the analyzing agent

This file is NOT a verbatim copy or a verbatim translation of Foyege's original prompts.
The original prompts were published by @Foyege24 in self-replies (comments) on X, not in the main posts.
Use this file to analyze prompt *structure*, *timeline control*, and *consistency mechanisms*.
For the original wording, open the source posts below and read the author's own replies.

Sources (read-only, no login was used for the first two posts' main threads):
- Transformation and aerial fight, 11 Oct 2026, paid partnership for Seedance 2.5 on Pippit AI:
  https://x.com/Foyege24/status/2109113006953263233
- Single-take butterfly-to-woman reveal, 23 Sep 2026:
  https://x.com/Foyege24/status/2102610496683933915
- Title-sequence montage, 16 Sep 2026, Minimax H3, title DEADSHOT:
  https://x.com/Foyege24/status/2100222945499263146

Caveats:
- The Seedance post is a paid partnership. Do not assume the tool named there is the tool used for the Malfoy/Draconia series. No prompt for the Malfoy series itself was found in this investigation.
- Some nested replies on X require login and were not read. Do not fill those gaps by guessing.
- All templates below use placeholders such as [CHARACTER], [SCENE], [PROP]. Replace them with your own character, scene, and prop. Do not reuse copyrighted characters if the output is intended for commercial use.

---

## 0. The shared architecture (all three cases)

Every Foyege prompt in this set follows the same section order. That order itself is the workflow:

1. Image references, each with a single, named role.
2. Global setting.
3. Style.
4. Cinematography / camera and lighting.
5. Character and effect rules.
6. Core rules (spatial lock, what must not move, what must not happen).
7. Timeline, beat by beat, with time ranges.
8. Sound design.
9. Consistency rules, repeated at the end.
10. Negative prompts, as a separate list.

Key structural ideas to analyze:
- One image reference = one job. A scene image is not also a character image. An eyes-only image is not also a costume image.
- A reference image's background and text are explicitly excluded unless that image is the scene image.
- Spatial position is locked: left stays left, right stays right, no axis crossing.
- What must stay still is specified as carefully as what must move.
- Timeline is controlled by *states*, not only by seconds: a light turning off, an armor piece assembling, a title appearing. Seconds are attached to states.
- The clip usually ends mid-action or on a held title, not on a resolved, fading ending.

---

## Template A. Transformation and Action (15-second and 30-second pattern)

Source: https://x.com/Foyege24/status/2109113006953263233

Tool pattern in the source: image-to-video with multiple image references.
Duration pattern: 15 seconds for a transformation, 30 seconds for a fight. One beat per second.

```
IMAGE REFERENCES
- [IMAGE_SCENE]: the environment only. Use its space, architecture, and atmosphere.
  Do not copy any text or background detail from other reference images.
- [IMAGE_GESTURE]: a single hand gesture or pose. Use the gesture only.
- [IMAGE_FINAL_FORM]: the final transformed form. Use its armor, materials, and silhouette.
- [IMAGE_INITIAL_FORM]: the character before transformation. Use its face, body, and costume.
- [IMAGE_PROP]: the weapon or key prop. Specify the main grip hand: [LEFT/RIGHT].

GLOBAL SETTING
- Genre and world: [GENRE, e.g. mythic science fiction]
- Time and place: [PLACE, TIME OF DAY]
- Aspect ratio: [16:9 or 9:16]
- Resolution and finish: [e.g. high dynamic range, film grain]

STYLE
- Visual reference style: [e.g. live-action visual effects, realistic computer-generated imagery]
- Render and material rules: [e.g. physically based materials, volumetric light]
- Particle and destruction rules: [e.g. sparks, dust, debris, cloth simulation]
- Light direction and color accents: [e.g. cold daylight from upper right, one accent color only]

CINEMATOGRAPHY
- Camera feel: [e.g. documentary handheld, telephoto compression, shallow depth of field]
- Camera shake rule: [e.g. short shake only on impacts, no continuous shake]
- Lens flaws allowed: [e.g. real lens optical flaws, no clean digital look]

CHARACTER AND EFFECT RULES
- [CHARACTER] moves [slow and heavy / fast and light]. Describe weight, not only speed.
- Effect trails: [e.g. smoke, energy, debris]. State how they form, move, and decay.
- Transformation rule: armor or costume assembles piece by piece, from [CENTER, e.g. chest core] outward.
  It must not appear instantly. The face plate or final detail latches last.
- Opponent or second character: describe its move set by name, one move per line, e.g.:
  - Move 1: [NAME] - [what it does, in one sentence]
  - Move 2: [NAME] - [what it does, in one sentence]
  - Ultimate move: [NAME] - [what it does, in one sentence]

CORE RULES
- [CHARACTER] always starts on the [LEFT/RIGHT]. [OPPONENT] always starts on the opposite side.
  No character crosses the central axis.
- Environment time rule, if used: [e.g. debris and clouds hover while characters, lightning, and camera move normally].
- No slow motion. No freeze frames. No dialogue.
- One [CHARACTER], one [OPPONENT], one [PROP]. No duplicates.

TIMELINE - ONE BEAT PER SECOND
Format for every beat:
  [START]-[END]s | Camera: [shot type and movement] | Action: [one action only] | Effect: [one effect only] | State after beat: [what has changed]

Example format, generic only:
  0-1s | Camera: whip pan following [CHARACTER] | Action: [CHARACTER] tumbles, trailing [EFFECT] | Effect: [EFFECT] spirals | State: [CHARACTER] is off balance, [OPPONENT] dominates the frame
  [Continue one beat per second until the end. End mid-action, not on a resolution.]

SOUND DESIGN
- Ambient: [e.g. low rumble, wind, crowd, machine hum]
- Impact sounds: [e.g. crash, servo clicks, latch click]
- Final sound: [e.g. sonic boom, low-frequency hit]
- No dialogue. No music, unless the template explicitly requires it. No subtitles.

CONSISTENCY RULES (repeat at the end, even if stated above)
- Same face, same costume, same prop in every beat.
- [CHARACTER] position rule repeated.
- Transformation order repeated: piece by piece, face detail last.

NEGATIVE PROMPTS
- No text, subtitles, or watermarks in frame.
- No axis crossing.
- No character shrinking, speeding up, or changing scale without cause.
- No instant costume change.
- No cartoon or plastic look.
- No slow motion, no freeze frames, no dialogue.
```

Analysis questions for Template A:
- Why does one beat per second help timeline control more than a paragraph describing the whole clip?
- What breaks first if the axis rule is removed?
- Why is "assembles piece by piece, face last" a timeline control device, not only a visual detail?

---

## Template B. Single-Take Reveal (13-second pattern)

Source: https://x.com/Foyege24/status/2102610496683933915

Tool pattern in the source: image-to-video, one continuous take, no reference video.
Duration pattern: about 13 seconds, divided into phases, not into one-second beats.

```
IMAGE REFERENCES
- [IMAGE_SUBJECT_A]: the first form, e.g. an animal or object. Specify its real structure:
  body shape, surface texture, and one distinctive pattern.
- [IMAGE_EYES_ONLY]: the eyes of the second form only. Specify pupil, iris rings, colors, and gaps.
  The face, hairstyle, and costume of the second form follow the established character, not this image.
- No reference video.

CINEMATOGRAPHY AND LIGHTING
- Look: live-action film, suspense, one continuous long take.
- Camera: handheld with real weight: breathing, irregular weight shifts, small framing corrections, inertia and damping.
- Camera position: the operator stays in place. No push-in. No zoom.
- Lens: mid-telephoto compression down a corridor or enclosed space.
- Focus: focus racks naturally and ends locked on the eyes.
- Lighting design: [e.g. spaced ceiling lights forming alternating light zones and dark gaps].
  Light color: [e.g. cold white, slightly cyan].
  Wall color: [e.g. low-saturation gray-blue].
  Color contrast: [e.g. blue environment vs. warm accent color in the eyes].
- Light-death rule: when a light dies, its zone and its reflection must truly fade.
  After the last light dies, the space must be completely black. No rim light, no base fill, no extra light.

SUBJECT CONTINUITY - THE MOTIF RULE
- One subject throughout. [FORM_A] continuously becomes [FORM_B]. It is the same subject, not two subjects.
- [FORM_A] stays in the mid-far section, never approaches the camera.
- The distinctive pattern from [IMAGE_SUBJECT_A] must persist and must become the eye pattern of [FORM_B].
  Example mechanism: a pattern on wings becomes the iris pattern of the woman.
- The pattern is visible only at certain angles and naturally hidden when the subject folds or turns.
  It must not look like a floating icon or a separate 3D object.

TIMELINE - PHASES, NOT A PARAGRAPH
Phase 1 - [0-5s, e.g. distant movement]:
  [FORM_A] moves in place, with natural rise, fall, and lateral drift.
  Motion blur is light and continuous. No slow-motion spread. No mechanical hovering.
Phase 2 - [5-7.5s, e.g. lights die one by one]:
  Lights turn off one by one, from far to near, with clear time gaps between them.
  Darkness advances section by section toward the camera. This is not a global fade.
Phase 3 - [7.5-10s, e.g. pure black transition]:
  Only two faint glowing patterns remain in pure black, dim and phosphor-like, no halo.
  They track the same camera motion, then smoothly become [FORM_B]'s irises.
  [FORM_B] is already standing in front of the camera but invisible in the dark. No early reveal.
Phase 4 - [10s, e.g. lights snap back]:
  All lights return at once. This is not a flash and not a fade-in face.
  Reveal [FORM_B] in a chest-up medium close-up, facing the camera.
  The two glowing patterns continue exactly as [FORM_B]'s irises.
  Key light from [DIRECTION], restrained rim light on hair and shoulders.
Phase 5 - [10-13s, e.g. held portrait]:
  [FORM_B] holds for about 3 seconds: still, lips closed, micro-expressions, slight breathing, hair movement.
  Handheld camera continues. Focus stays locked on the eyes.
  End on the close-up. No photo freeze. No early fade.

SOUND AND CONTINUITY
- Ambient: [e.g. low corridor ambience, faint electrical current as each lamp decays].
- Transition sound: [e.g. a short power-on snap when all lights return].
- End sound: [e.g. faint breathing].
- No music. No dialogue. No subtitles.
- Repeat the summary rules at the end: one take, one subject, lights die one by one to true black,
  no early reveal, lights return with the subject already present, about 3 seconds of hold, no smoke,
  no particle explosion, no white-flash transition.

NEGATIVE PROMPTS
- No early reveal of [FORM_B].
- No global fade to black and back.
- No extra light in the black phase.
- No floating pattern, no separate eyeball object.
- No music, dialogue, or subtitles.
```

Analysis questions for Template B:
- Why is a shared pattern (wing pattern = iris pattern) a stronger continuity anchor than "same face"?
- Why does "lights die one by one, from far to near" control timeline better than "lights fade out"?
- Why is the 3-second held portrait at the end essential, and what happens if it is cut to 0.5 seconds?

---

## Template C. Title-Sequence Montage (15-second pattern)

Source: https://x.com/Foyege24/status/2100222945499263146

Tool pattern in the source: image-to-video from a strongly stylized reference image.
Duration pattern: about 15 seconds, vertical, fragment montage, not continuous action.

```
IMAGE REFERENCES
- [IMAGE_PROTAGONIST]: one protagonist only. Specify face, hair, clothing, vest, gloves, and weapon.
  All close-ups, details, and silhouettes are the same person.
- Adversaries: specify them only as fragments: side faces, reaching hands, shoulders, backs, unbalanced silhouettes.
  They must always be visually distinct from the protagonist. Never give an adversary a clear full face.

STYLE AND PALETTE
- Treatment: [e.g. high-contrast monochrome, cold gray-white, deep charcoal black, small gray-green].
- Accent color: [e.g. dark red] only as brief accents. It must never fill the frame.
- Texture: real scanned-film grain varying frame to frame, denser in shadows, slight registration drift, breathing exposure.
- No fixed noise overlay. No heavy scratches.

MOVEMENT AND LAYERS
- Every layer moves at a different direction and speed: hair, sleeves, fog, trails, double-exposure layers.
- Foreground mist sweeps fast. Background exposure layer drifts slowly, swallowing then revealing shoulders, weapon, and legs.
- Motion trails: long-exposure smears that form, stretch, and decay. They must never become extra people or limbs.
- Double exposure: only in selected shots. Second layer examples: trees, empty road, power poles, printed over dark clothing.
  Eyes, weapon hands, and weapon must stay clearly readable.
- Lens: wide-aperture cinema lens. Eyes, skin, and gear texture sharp. Foreground mist and hair soft.
- Flares: brief, thin, entering with side backlight then fading. Never covering the figure.

EDITING AND RHYTHM - THE CORE OF THIS TEMPLATE
- Shot length: fragmentary montage, about 0.3-0.8 seconds per shot.
- Holds: confrontation shots are even shorter, interspersed with about 0.5-1 second clear holds.
- Rhythm formula: fast cuts, grab one frame, speed up again.
- Cut types: mainly hard cuts, action-match cuts, a few extremely short exposure flash-cuts. No slow dissolves.
- Frame-drop definition: a clear pose held briefly, then a short directional motion blur, then a jump to the next pose.
  Mist and exposure layers keep flowing, creating temporal displacement.
  This is not smooth slow motion and not random stutter.
- Story rule: do not show a full fight. Show only pre-contact, contact moment, and post-contact fragments.
  The viewer assembles the fight.

TIMELINE - FIVE PHASES
Phase 1 - [0-3s, establish the character]:
  Start from the reference image composition, hold about 0.5 seconds, then quick hard cuts:
  eyes, weapon hand, boot landing, clothing brushing across frame, back to the full figure slightly advanced.
  Trails connect the cuts. Eyes are sharp in brief holds.
  End phase with a small on-screen credit, e.g. [PRESENTS CREDIT], lower-left, thin type, wide tracking,
  visible about 1 second while footage keeps cutting beneath, then it vanishes.
Phase 2 - [3-6s, first confrontation fragments]:
  Adversary fragment from near foreground, out of focus, then hero's turning shoulder and weapon hand.
  Side-face close-up: jaw tight, eyes locked offscreen, hair sweeping the face, brief hold, then sudden push.
  One extremely short impact insert: only a shoulder, a collar, a half-blurred side face, rising mist.
  Contact point stays offscreen. No wound shown.
  One macro insert: a few accent-color droplets slanting across a neutral background, near drops defocused,
  far drops briefly sharp, then hard cut back to the eyes.
Phase 3 - [6-9s, accent color and double exposure interwoven]:
  Half-body dark silhouette holding the weapon, empty road receding, mist moving opposite.
  Figure turns via frame-drops.
  Three short inserts: re-grip the weapon; adversary arm brushing frame edge, hero sidesteps;
  accent-color droplets flung in arcs, viscous, with brief threads before separating, not a water splash.
  Only splatter and surface traces, no wound source.
  One match cut: an accent-color trace on a neutral surface matches tree branches inside the hero's shoulder.
  A thin horizontal flare sweeps past the weapon edge into the next phase.
Phase 4 - [9-11.5s, abstract confrontation climax]:
  Fastest fragmentary montage, one piece of information per shot: hair, unbalanced side face,
  muzzle flash lighting mist, glove colliding with gear, droplet flying horizontally with a short trail, eyes sharp again.
  Link shots by motion direction and sound. Weapon and hand continuity must hold across shots.
  No body distortion. No duplicated limbs.
  After each fast blur, cut immediately to sharp eyes or sharp metal edges. Sharp / trailing alternation.
  Last close-up holds about 0.5 seconds: hero looks forward, gear bearing faint accent-color traces,
  exposure layer sweeping past the cheek, then hard cut to title.
Phase 5 - [11.5-15s, title]:
  Montage stops dead. Hard cut to a deep charcoal black background.
  Faint silhouette of the weapon-holding figure lingers at one side. Mist drifts slowly across the lower frame.
  Grain keeps shifting.
  Center-lower, the only title: [TITLE, all caps, cold gray-white, narrow sans-serif, medium weight, moderately widened tracking].
  Title width about two-thirds of frame width, with large black space above and below.
  Letterforms sharp and clean, only a hairline of print wear. No blood-drip, no metallic 3D, no neon glow.
  No translation, no subtitle, no other copy.
  Title flashes in dim gray then settles to cold gray-white. An extremely faint horizontal flare passes and vanishes.
  Text always clear, undistorted, steady. Title holds to the end. Mist still moving behind. Final hard cut to black.

SOUND DESIGN
- Ambient: low, sparse suspense ambience throughout.
- Confrontation fragments: short cloth friction, gear impacts, low body thuds, one dry gunshot.
- Droplet shots: do not exaggerate wet sounds.
- Frame-drop cuts: slight mechanical clicks.
- One brief sound drop-out in the middle.
- Title: one restrained low-frequency hit, then only a slowly decaying ambient tail.
- No dialogue. No voiceover.
- On-screen text limited to the presents credit and the title.

CONSISTENCY AND NEGATIVE RULES
- Strict face, wardrobe, and weapon consistency.
- Adversaries never read as the protagonist.
- Trails never become extra bodies.
- Double exposure only in selected shots.
- No fixed noise overlays, no heavy scratches.
- Flares never obscure the figure.
- No smooth slow motion, no random stutter.
- No full fight choreography.
- No blood-drip, metallic, or neon title treatment.
- No extra titles or subtitles. No dialogue.
- Accent color never dominates the frame.
```

Analysis questions for Template C:
- Why does "one piece of information per shot" make a 15-second title sequence feel faster and clearer than a continuous 15-second action shot?
- How does frame-drop editing hide a model's weak timeline control, and where does it fail?
- Why is the title phase a timeline anchor, not just a graphic?

---

## Master template (combine the three, for a new original project)

Use this when you need one prompt structure for a new clip, not a copy of any single Foyege clip.

```
[1] IMAGE REFERENCES - one role per image, background/text excluded unless it is the scene image.
[2] GLOBAL SETTING - genre, place, time, aspect ratio, finish.
[3] STYLE - visual style, materials, particles, light direction, accent color limit.
[4] CINEMATOGRAPHY - camera feel, lens, focus rule, lighting design, light-death rule if used.
[5] CHARACTER AND EFFECTS - weight, move set by name, transformation order, motif that persists across forms.
[6] CORE RULES - left/right lock, what stays still, no slow motion, no freeze frames, no dialogue, one of each key subject.
[7] TIMELINE - either one beat per second (Template A), phases with state changes (Template B),
    or fragment montage with holds (Template C). Pick one timeline method per clip. Do not mix all three in one clip.
[8] SOUND - ambient, impacts, transition sound, final sound. No dialogue unless explicitly required.
[9] CONSISTENCY - repeat face, costume, prop, position, and motif rules at the end.
[10] NEGATIVE PROMPTS - text, axis crossing, scale change, instant change, cartoon look, slow motion, extra subjects.
```

---

## What the analyzing agent should NOT conclude from this file

- Do not conclude that the Malfoy/Draconia series was made with Seedance, Pippit, or Minimax. Those tools are named only in the three non-Malfoy posts above.
- Do not conclude that Foyege published a single "official workflow document". The workflow evidence found here is prompt text in X self-replies.
- Do not treat the templates above as verbatim translations. They are structural reconstructions for analysis.
- Do not fill the login-blocked nested replies by guessing. Mark them as unverified.

## Appendix A: [x.com/Foyege24/status/2109113006953263233](https://x.com/Foyege24/status/2109113006953263233)

```
Transformation Prompt👇
————————
【Global Settings】 @Image1
 defines the scene: A white celestial palace above a sea of clouds, with eaves and palace halls with white jade railings on the left, a suspended pavilion and long corridor in the center, and an endless sea of clouds on the right; a hundreds-of-meters-tall black steel mechanical giant birdman stands in the cloud sea on the right, with an eagle head, steel feathers, and exposed mechanical structures. Inherit the layout, styling, and lighting from the reference image. @Image4
 defines the male protagonist's initial form: Black long hair, crown ornament, black carbon fiber mecha suit and long robe. @Image5
 defines the mechanical square-heaven halberd, held in the right hand throughout, without using the reference image's background or text. @Image2
 only defines the mudra hand gesture: Right index finger held vertical, left hand grasping the right hand, positioned in front of the chest, without using the characters, background, or text in the image. @Image3
 defines the male protagonist's final transformation form: Glossy black mecha suit, pointed crown helmet, white pointed horn faceplate, white V-shaped glowing light strip, black cable long hair, black-and-white shoulder armor, back with long blades, without using the reference image's background.

Style: Hollywood live-action blockbuster visual texture, blended with the realistic CG style of *Love, Death & Robots*. UE5 rendering, PBR materials, volumetric lighting, physical destruction and cloth simulation, 8K HDR, 16:9. Cold daylight from the upper right pierces through the cloud layers, with red lightning as an accent color, featuring film grain.

Cinematography: Documentary handheld feel, telephoto lens compressing space, giant objects looming like walls, shallow depth of field. Abrupt whip pans during impacts and giant footsteps, with a touch of real lens optical imperfections.

【Characters and Effects】 The male protagonist's initial form trails black ink-smoke wakes during high-speed movement, exploding into white sonic boom clouds during breakthrough acceleration, with red lightning arcing along the mecha suit. The final form strictly inherits @Image3
, with the entire body wrapped in red lightning, trailing ink and lightning-interwoven wakes during flight. The birdman's movements are slow and ponderous, its wing flaps or footsteps displacing the cloud sea and churning up massive cloud waves, with metal debris shaking loose from armor seams. The frame accompanies multi-layered particles: Sparks, rubble, metal dust, cloud mist.

【Core Rules】 The palace complex always remains on the left, the birdman always on the right, with all shots adhering to the 180-degree rule. The male protagonist is extremely fast, the birdman extremely slow. Collisions must convey intense impact, with debris obeying gravity, and destruction marks persisting to the end of the piece. 6—13 seconds feature environmental time freeze: Rubble, cloud waves, and dust hang suspended in mid-air, while the male protagonist, lightning, and camera move normally. The entire piece has no slow motion, no freeze frames, zero dialogue.

【Storyboard (15 seconds)】 1｜0-1s Whip pan chase shot: The male protagonist is batted airborne by the birdman's massive wing, tumbling uncontrollably in mid-air toward a fall, trailing helical ink smoke, with roiling cloud waves in the right background. 2｜1-2s Ground-level telephoto low-angle shot: A mass of ink smoke slashes diagonally down from the sky, smashing toward a multi-tiered palace hall. 3｜2-3s Impact-enhanced whip pan: The palace hall's roof explodes, eaves collapse, roof tiles and rubble scatter in all directions, smoke and dust billowing skyward. 4｜3-4s Frontal close-up: The male protagonist kneels on one knee at the crater's bottom, face caked in dust, faceplate cracked, teeth gritted, eyes lifting to look rightward. 5｜4-5s Left shoulder rear over-the-shoulder telephoto: The birdman fills the right frame like a towering wall, eagle head locked on the male protagonist, its footfall churning up massive cloud waves, camera shaking. 6｜5-6s Frontal eye-level shot: The male protagonist rises, performs the mudra per @Image2
, red lightning spreading across his body; everything abruptly freezes, the birdman halted mid-stride. 7｜6-7s Low-angle upward shot: The male protagonist maintains the mudra and slowly ascends, rubble and debris at his feet floating and rotating, red lightning flickering among them. 8｜7-8s Chest-level circling shot: Transformation begins, old armor plates peeling off layer by layer and dissipating, @Image3
 mecha assembling piece by piece outward from the chest core, accompanied by sparks and steam. 9｜8-9s Shoulder and arm close-up: Shoulder armor unfurls in a fan shape, red thin seams glowing, arm joints and outer plating snapping into segments. 10｜9-10s Waist and legs upward shot: Skirt armor drapes down, white leg armor locks tight, long hem taking shape. 11｜10-11s Back circling pan: Back long blades pop out one by one, cable long hair draping and swaying, halberd's red cords lighting up in sync. 12｜11-12s Head side-rear slow push: Pointed crown helmet rises in segments, white faceplate closing from both sides, the male protagonist's face still exposed at this point. 13｜12-13s Frontal fast push: Faceplate flips and locks shut, venting steam, V-shaped light strip igniting from the center. 14｜13-14s Low-angle upward shot with enhanced whip pan: A beam of red lightning-wrapped light descends from the heavens striking the male protagonist, frame nearly all white, shockwave exploding outward, world snapping back to full speed; final form manifests, right hand gripping the halberd, birdman abruptly raising its head. 15｜14-15s Right rear over-the-shoulder with whip pan follow shot: The male protagonist breaks the sound barrier charging the birdman, streaking as a black-red trajectory across the cloud sea; the birdman spreads its wings to meet the assault, ending in high-speed motion.

Sound: Whistling fall, thunderous building collapse, heavy breathing, low-frequency rumble of the birdman's footfalls; after the mudra, environmental sounds vanish, leaving only electric crackles and heartbeat pulses; transformation features mechanical servo and latching sounds, faceplate lock with a crisp click; post-beam thunder, environmental sounds resume, culminating in a final sonic boom. No voice lines, no score, no subtitles.

Consistency: One male protagonist, one birdman, one halberd. Pre-transformation inherits @Image4
, post-transformation inherits @Image3
, with piece-by-piece assembly, faceplate locking last. Palaces on the left, birdman on the right.

【Negative Prompt】 Prohibit text, subtitles, watermarks; prohibit crossing the axis; prohibit the birdman shrinking or speeding up; prohibit intact buildings or ruins regenerating; prohibit the mecha appearing all at once; prohibit forms mismatched to reference images; prohibit incorrect gestures or deformed fingers; prohibit slow motion and freeze frames; prohibit cartoonish style, plastic textures, gore.
```

## Appendix B: [x.com/Foyege24/status/2102610496683933915](https://x.com/Foyege24/status/2102610496683933915)

```
提示词⬇️
——————————
@图片1参考蝴蝶的真实身体结构、蝶翼形状、鳞粉质感和天然眼状斑纹的分布。蝴蝶底色为深蓝与宝石蓝，左右翅面各有一处主要眼状花纹，改为与女主虹膜相似的橙色多重同心圆细线。
@图片2仅参考女主眼睛：黑色圆形瞳孔，外围一圈一圈橙色与橙金色圆线，环间保留深色间隔。女主外貌、发型与服装沿用既定角色设定。不使用参考视频。
【电影摄影与光影】
真人电影实拍质感，悬疑长镜头。真实皮肤、细腻发丝、厚实衣料与自然昆虫质感，细微胶片颗粒，柔和高光过渡，深沉纯净的黑位，避免锐化过度、塑料质感与廉价CG感。

全程采用战争纪实式肩扛手持摄影，摄影机具有真实重量：轻微呼吸起伏、不规则重心偏移、小幅构图修正，动作有惯性和缓冲。克制而紧张，保持清晰的画面组织，不剧烈甩镜。摄影师始终留在原地，一镜到底，不向蝴蝶推进，不变焦。使用中长焦电影镜头的空间压缩感，沿走廊纵深拍摄，让远处蝴蝶可辨，同时保留它与镜头之间明确的距离。焦点随主体变化自然衔接，最终落在近处女主双眼。
狭长封闭走廊，两侧房门与天花板形成强烈纵深线条。顶灯彼此间隔，每盏灯在墙面和地面形成独立光区，明亮光区与深暗间隙交替延伸。冷白光略带青色，墙面保留低饱和灰蓝，蝴蝶的蓝色与眼纹的橙金色形成精准冷暖对比。地面有克制的柔和反射，灯具高光不过曝，暗部层次由真实光源建立，不使用均匀环境补光。

灯亮时，侧上方的走廊灯在主体表面形成有方向的明暗；灯灭时，对应光区与反射真实消退。最后一盏灯熄灭后，整个空间必须彻底全黑。电影光影不能成为保留轮廓光、蓝色底光或额外补光的理由。

【蝴蝶与眼纹】
全片只有一个主体，由一只蓝色蝴蝶连续化为同一个女生。

蝴蝶身体纤细，触角自然，两对宽薄蝶翼协调运动，具有真实翅脉、细密鳞粉和柔软翼缘。蝴蝶始终停留在走廊中后段的小范围内，一扑一扑地飞动，不飞到镜头面前。

左右翅面各有一个主要眼状花纹：深色圆心，外围多层橙色同心圆细线。花纹始终存在于翅面上，随翅膀弯折、收合和改变透视。只有在部分展翅角度，才能短暂看清两个像眼睛的花纹；收翅或侧转时，自然被遮挡。花纹不是浮在翼面外的图标，不是立体眼球。
【0—5秒：远处扑翼】
蝴蝶在走廊中后段自然飞动，双翼上抬收合，再向下扑动展开，带动身体轻微升降，伴随小幅横向漂移与方向修正，整体不向镜头逼近。

拍翼轻快、连续，有节奏变化，翼根带动翼尖，薄翼发生微小弯曲，翼缘带自然运动模糊。不要慢动作摊翅，不要机械悬停。

远处顶灯从不同角度掠过蓝色翼面，鳞粉光泽随拍翼短暂显现。左右橙色环纹时而同时露出，时而只看见一侧，随后又随收翅消失。镜头以微幅手持捕捉这一过程，背景灯光柔和虚化，但灯具排列、明暗光区与走廊纵深仍然可辨。

【5—7.5秒：光区逐段消失】
走廊灯光突然开始出现异常。最远处一盏灯先逐渐暗下，接着下一盏，再下一盏，沿纵深由远到近缓慢熄灭。每盏灯有短暂亮度衰减，相邻灯之间存在清楚的时间差。
灯光衰减落实到整个空间：对应墙面的亮区收暗，门框高光消失，地面反射逐渐减弱，黑暗一段一段向镜头推进。不是整幅画面统一降低亮度。

蝴蝶仍在远处自然扑翼，被尚未熄灭的灯短暂照到。蓝色翼面逐渐不可见，橙色环纹随展翅间歇显露。

最后一盏灯熄灭，空间彻底全黑。墙壁、地面、门框、顶灯、蝶翼与蝴蝶身体全部消失。没有应急灯、轮廓光、空气光或残留反射。曝光不自动抬高，不把黑暗提成灰色。

【7.5—10秒：纯黑中的无缝衔接】
画面只剩两处微弱的橙色同心圆花纹，像夜光涂层在暗处的余辉，低亮度、柔和、细小，勉强能辨认一圈一圈的圆线。没有明显光晕，不照亮周围，不呈现霓虹或火焰质感。
最初，两处微光仍随最后几次扑翼产生轻微角度变化与小幅起伏，随后运动自然收缓。始终是同一对微光，不熄灭后重现，不叠入另一对眼睛。

借助纯黑隐藏身体和空间距离的变化，让蝶翼眼纹连续成为女主虹膜。两处微光的颜色、圆环结构与画面轨迹延续一致，间距和大小只作平滑、克制的调整，不突然跳位，不夸张放大，不像光圈冲向镜头。

女主已经在黑暗中完成转换并站在镜头前，但此时看不见她的眼白、眼睑、鼻梁、脸、头发或身体。画面始终只有纯黑与两处夜光般的橙色圆环。

摄影机的细微手持运动持续不断，微光自然响应同一套摄影机运动，不固定贴在屏幕上。焦点在纯黑遮蔽下自然转移至近处，为亮灯后的双眼做好清晰衔接，不出现可见的反复寻焦。

【第10秒：灯亮揭示】
整条走廊的灯突然同时恢复正常照明。不是闪白，不是渐渐显出一张透明脸，而是真实灯光瞬间照见已经站在镜头前的女主。
女主正面直视镜头，胸部以上中近景。亮灯前的两处微光，准确接成亮灯后她双眼中的橙色同心圆虹膜，位置、形状和运动轨迹连续。直到这一刻，观众才发现远处蝴蝶已经化为近处的女生。

近处侧上方顶灯为她形成有方向的电影主光：额头、鼻梁、一侧颧骨与上唇边缘接住柔和亮面，另一侧面颊落入深而自然的阴影，保留必要肤色细节。她身后的顶灯在发丝和肩线形成细窄、克制的边缘亮度，将人物从幽深走廊中分离。背景恢复交替排列的亮区与暗区，突出纵深。肤色保持自然，与冷青灰背景形成细微色温差，不把脸整体染成蓝色。

双眼清晰：黑色圆形瞳孔，外围多重橙色、橙金色细圆线，眼白、睫毛与角膜反光真实自然。环纹仍有克制微光，与正常照明融合，不照亮整张脸，不糊成两个光球。蝴蝶已完全消失。

【10—13秒：人形电影肖像】
完整人形保持约3秒。女主原地直视镜头，嘴唇自然闭合，只有微表情、轻微呼吸与少量发丝运动，不走动、不转头、不继续变形。

摄影师保持原地肩扛手持，细微呼吸起伏贯穿始终。景别稳定，焦点锁在双眼，脸部光影、自然皮肤纹理、发丝层次与服装褶皱清楚可见。背景适度虚化，保留走廊光区的纵深节奏。以女主近景和清晰的橙色环形眼瞳结束，不冻结成照片，不提前黑屏，不淡出。

【声音与连续性】
走廊低沉环境底噪、灯具逐盏衰减的细微电流声、整体亮灯时短促通电声，最后保留微弱呼吸。远处蝴蝶不配夸张振翅声。无背景音乐，无对白，不要字幕。
全程真人电影质感、肩扛手持、一镜到底。蝴蝶留在远处自然扑翼，眼纹始终存在但随展翅时隐时现。灯逐盏熄灭后必须纯黑，只留两处夜光般微弱的橙色同心圆。黑暗中不提前显露人形。第10秒灯光突然整体恢复，女主已经在镜头前，两处蝶翼眼纹无缝接成她的双眼，最后完整停留约3秒。无烟雾、无粒子爆炸、无闪白转场。
```

## Appendix C: [x.com/Foyege24/status/2100222945499263146](https://x.com/Foyege24/status/2100222945499263146)

```
提示词⬇️选一种风格化强一点的图生
————————
生成15秒竖屏悬疑惊悚丧尸电影片头，画幅与参考图一致。快速混剪、抽帧印片、动态双重曝光、真实胶片颗粒。冷灰白、深炭黑与少量灰绿色，暗红色只作为短促点缀。整体光怪陆离、压抑，但构图与文字排版高级简约。

【人物与参考图】

唯一主角是参考图中持枪、装备精良的成年亚洲女性。严格保持她的面容、黑色长发、黑色战术服、战术背心、手套及枪械外观。

双手控制胸前枪械，枪身斜置胸腹前，身体前倾，目光冷峻而专注。所有近景、局部和剪影都是同一女性。枪械与装备具有真实重量，持握关系连续。

交锋对象是穿破旧日常衣服的成年丧尸，只通过灰败侧脸、伸来的手、肩背和失衡轮廓出现。主角与丧尸形象始终明确区分。

【流动影像与胶片质感】

不要把参考图当作静态照片缓慢推近。人物、发丝、衣袖、灰白雾状区域、黑色拖影与双重曝光层都在运动，方向和速度各不相同。

前景失焦薄雾较快掠过，背景灰白曝光层缓慢移动，时而吞没肩膀、枪身边缘和腿部，随后退开，让人物重新清楚。薄雾有前后层次，不是铺在画面上的平面滤镜。

黑色拖影来自发丝、衣袖与身体动作的长曝光痕迹：沿运动方向延展，随后衰减。每一次拖影都有产生、拉长和消散的过程，不变成额外人物或肢体。

树林、空旷道路和电线杆作为第二层曝光，局部叠印在战术服与肩背暗部。环境层与人物错速移动，眼睛、持枪手和枪械保留清晰辨认点。双重曝光只在选定镜头出现，不让每一帧都塞满纹理。

真实胶片扫描质感：细密颗粒逐帧变化，暗部颗粒稍明显，伴随轻微画面套准偏移、曝光呼吸和高光边缘溢光。不是固定噪点贴图，不铺满夸张划痕。

大光圈电影镜头，焦内眼睛、皮肤与装备纹理清楚，近处雾层与发丝柔和失焦。战术背心呈粗糙哑光尼龙质感，枪身呈低反射金属质感，皮肤保留自然纹理。

细窄银蓝色横向变形镜头光晕只短暂出现，随侧逆光进入镜头而延伸、消退，不持续遮住人物。

【剪辑与抽帧节奏】

以约0.3—0.8秒的短镜头组成碎片蒙太奇，中段交锋镜头进一步缩短，穿插约半秒至一秒的清晰停顿。整体节奏是“快速切换—抓住一个画面—再次加速”。

主要使用硬切、动作匹配切和少量极短曝光闪切，不连续缓慢溶解。

抽帧表现为清晰姿态短暂保持，紧接一小段方向性运动模糊，再跳入下一姿态。人物动作断续推进，雾层和曝光层仍持续流动，形成时间错位感。不是全程顺滑慢动作，也不是随机卡顿。

交锋不完整展开，不拍成普通枪战。用接触前、接触瞬间和接触后的局部，让观众自行拼出动作。

【00:00—00:03｜快速建立人物】

从参考图的俯视持枪构图开始，停留约半秒。女性向前迈步，长发向画面左侧甩动，灰白雾层从下方掠过。

快速硬切至：
散发下的眼睛；
手套控制枪身的局部；
靴子落地；
衣摆擦过画面；
重新回到俯视人物，姿态比开场向前推进一点。

每个片段都有真实动作。发丝与衣摆的长曝光拖曳连接切点，眼睛在短暂停顿中锐利清楚。

最后一次回到人物时，黑色战术背心内部浮现稀薄树林叠印。左下留白处出现小号文字：

FOYEGE PRESENTS

细窄无衬线大写、宽字距、深灰色，稳定停留约一秒；文字之下的影像继续切换，随后文字消失。

【00:03—00:06｜第一次交锋碎片】

硬切至一只灰败的手从近前景探来，手指经过焦点，后方丧尸面孔深度虚化。

紧接着切到主角转身的肩部与持枪手。枪身和衣袖形成短促方向性拖影，装备带随转身绷紧。

再切至主角侧脸近景：下颌收紧，眼睛锁定画外，头发横扫脸侧。动作短暂保持，随后突然推进。

极短插入丧尸肩背受到撞击后向侧方偏转的画面，只看到衣领、半张失焦侧脸与被带起的灰白雾。接触点位于画外，不展示伤口。

紧接一组微距意象：少量暗红液滴从画外斜掠过灰白背景，近处大液滴失焦，较远的小液滴短暂清楚。随即硬切回主角眼睛，红色不持续占满画面。

【00:06—00:09｜红色与双重曝光交错】

主角持枪半身暗轮廓中，空旷道路缓慢向纵深延伸。薄雾向相反方向移动，人物以抽帧方式轻微转身。

穿插三个短促局部：
黑色手套重新握稳枪身；
丧尸伸来的手臂擦过镜头边缘，主角侧身避开；
深色袖口上的几颗暗红液珠随急转甩离，沿弧线散开。

液体有黏附感，离开布料前形成短小牵连，随后断成独立液滴，不像大量清水泼洒。只见飞溅和表面痕迹，不见伤口来源。

将液滴落在灰白表面的一小处暗红痕迹，与主角肩背内部的黑色树枝做一次形状匹配切。红色形态与树林线条短暂呼应，然后叠印减淡。

一束细薄横向光晕掠过枪身边缘，切入下一段。

【00:09—00:11.50｜抽象交锋高潮】

进入全段最快的一组碎片混剪，每个画面只突出一个信息：

主角发丝骤然甩向左侧；
灰败侧脸从焦点边缘失衡退出；
枪口短暂闪光，照亮近处雾层；
黑色手套与装备碰撞；
一小片暗红液滴横向飞过，留下短促曝光拖痕；
主角的眼睛重新清楚显露。

这些片段通过动作方向和声音连接，暗示她正在对抗周围丧尸。不同镜头里的枪械和手部归属一致，不用身体变形或肢体重复制造混乱。

模糊的快速动作之后，立即切到清楚的眼神或金属边缘，形成锐利与拖曳交替的视觉节奏。

最后一个人物近景停留约半秒。她从散发下看向前方，黑色战术服保留少量暗红痕迹，灰白曝光层掠过脸侧。随后硬切片名。

【00:11.50—00:15｜悬疑惊悚片名：DEADSHOT】

快速混剪骤然停止，硬切至深炭黑背景。右侧只残留极淡的持枪女性轮廓，灰白薄雾从画面下缘缓慢横向流过，细腻胶片颗粒持续变化。

中央偏下出现唯一片名：

DEADSHOT

全大写、冷灰白色、窄体无衬线字体，中等字重，字距适度拉开。标题宽度约占画面三分之二，上下保留大量黑色空间，呈现悬疑惊悚丧尸电影的简约片名设计。

字形锋利、端正，边缘仅有极细微的印片磨损，不做滴血字、立体金属字或霓虹发光字。不增加中文译名、副标题和其他文案。

标题先以偏暗灰色快速显现，随即稳定为冷灰白。一道极弱的银白横向光晕从背景边缘掠过后消失，文字始终清楚、不扭曲、不跳动。

片名稳定停留至最后，背景薄雾仍缓慢移动。最后硬切黑场。

【声音】

低沉、稀疏的悬疑氛围音贯穿。交锋碎片配合短促衣料摩擦、装备撞击、低沉身体碰撞与一次干燥枪声；液滴镜头不夸张放大湿黏音效。

抽帧切点穿插轻微机械咔嗒，中间留一次短暂声音抽空。片名出现时落下一记克制的低频重音，随后只剩缓慢衰减的环境尾音。

无对白、无旁白。文字仅保留“FOYEGE PRESENTS”和“DEADSHOT”。
```