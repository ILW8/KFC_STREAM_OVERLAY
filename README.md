# KFC Stream setup

## Weekly setup
### Mappool data
- Grab `beatmap.json` and `beatmap_data.json` from [@shdewz](https://github.com/shdewz) or the sheets
- Place them into `static/_data` (create `_data` if it doesn't already exist)

### Intro
- Grab `coming_up.json` from [@shdewz](https://github.com/shdewz) or from the sheets
- Place it into `static/_data`

## Scenes
### Intro

- Browser source:
  - [ ] Local file 
  - URL: `http://localhost:24050/intro`
  - Width: 1920
  - Height: 1080
- Media source (overlay)
  - [x] Local file
  - Local file: `OBS/stream_starting_small_vp9.webm`
  - [x] Loop
  - [ ] Restart playback when source becomes active
  - [ ] Use hardware decoding when available **(important)**
  - [ ] Show nothing when playback ends
  - Leave rest default
- Media source (bg)
  - [x] Local file
  - Local file: `OBS/bg.mp4`
  - [x] Loop
  - [ ] Restart playback when source becomes active
  - [x] Use hardware decoding when available (optional)
  - [ ] Show nothing when playback ends
  - Leave rest default

### Main
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



### Mappool
- Browser source (mappool overlay)
  - [ ] Local file
  - URL: `http://localhost:24050/mappool`
  - Width: 1920
  - Height: 700
  - **Transform**:
    - Position: `0.00px` `190.00px`
