# KFC Stream setup

## Weekly setup
### Mappool data
- Grab `beatmap.json` and `beatmap_data.json` from [@shdewz](https://github.com/shdewz) or the sheets or from [JSONs](JSONs)
- Place them into `static/_data` (create `_data` if it doesn't already exist)

### Intro
- Grab `coming_up.json` from [JSONs/ComingUp](JSONs/ComingUp/README.md) or from [@shdewz](https://github.com/shdewz) or from the sheets (ref sheet, `Schedule` tab, column Q)
- Place it into `static/_data`

### Tournament client
- Select the right skin (rename skin to `User`) for Showcase/Matches
  - Matches: [Finesse_2023_TClient_WIP.osk](Skins/Finesse_2023_TClient_WIP.osk)
  - Showcase: [Finesse_2023_Showcase_WIP.osk](Skins/Finesse_2023_Showcase_WIP.osk)
- Load map pack
- Tournament client settings:

| Setting                  |  Setting value   |
|--------------------------|:----------------:|
| Client stream            | **Cutting Edge** |
| Background video         |     **Off**      |
| Storyboards              |     **Off**      |
| Combo bursts             |     **Off**      |
| Hit lighting             |     **Off**      |
| Seasonal backgrounds     |    **Never**     |
| Background dim           |     **80%**      |
| Always show key overlay  |      **On**      |
| Ignore all beatmap skins |      **On**      |
| Always use skin cursor   |      **On**      |
| Cursor size              |     **1.0**      |
| Automatic cursor size    |     **Off**      |



____

## Scenes
### Matches
#### Scenes transition
- Luma wipe
  - Duration: 300ms
#### Intro

- Browser source:
  - [ ] Local file 
  - URL: `http://localhost:24050/intro`
  - Width: 1920
  - Height: 1080
- Media source (overlay)
  - [x] Local file
  - Local file: [stream_starting_small_vp9.webm](OBS/stream_starting_small_vp9_.webm)
  - [x] Loop
  - [ ] Restart playback when source becomes active
  - [ ] Use hardware decoding when available **(important)**
  - [ ] Show nothing when playback ends
  - Leave rest default
- Media source (bg)
  - [x] Local file
  - Local file: [bg.mp4](OBS/bg.mp4)
  - [x] Loop
  - [ ] Restart playback when source becomes active
  - [x] Use hardware decoding when available (optional)
  - [ ] Show nothing when playback ends
  - Leave rest default

#### Main
- 4x Window captures for the 4 tournament clients

  | Client       | Position (x) | Position (y) |
  |--------------|--------------|--------------| 
  | Top Left     | 0px          | 160px        |
  | Bottom Left  | 0px          | 520px        |
  | Top Right    | 960px        | 160px        |
  | Bottom Right | 960px        | 520px        |

- Browser source (main overlay)
  - [ ] Local file
  - URL: `http://localhost:24050/main`
  - Width: 1920
  - Height: 1080



#### Mappool
- Browser source (mappool overlay)
  - [ ] Local file
  - URL: `http://localhost:24050/mappool`
  - Width: 1920
  - Height: 700
  - **Transform**:
    - Position: `0.00px` `190.00px`


<br>

### Showcase
@TODO
