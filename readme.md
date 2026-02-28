# AbletonLoopingSurface

Ableton Live 12 Control Surface script that lets you record fixed-length clips, toggle metronome, and delete the currently selected clip in Session View using MIDI notes.

## Features

- Toggle metronome via MIDI
- Delete selected clip via MIDI
- Fully quantized recording (same method as Ableton Push)
- Supports all Ableton editions (including Lite)
- Lightweight, no dependencies

## Requirements

- Ableton Live 12
- MIDI controller

## Installation

Download or clone this repository, then copy the /AbletonLoopingSurface folder to:

**Mac**

`/Applications/Ableton Live xxx.app/Contents/App-Resources/MIDI Remote Scripts`

**Windows**

`C:\ProgramData\Ableton\Live 12 xxx\Resources\MIDI Remote Scripts`


Restart Ableton.

## ⚠️ Important Installation Note (GitHub users)

If you downloaded this project from GitHub, the folder name may include **-main**.

Example:

`AbletonLoopingSurface-main`

This will **NOT work** in Ableton.

You must rename the folder to:

`AbletonLoopingSurface`

**Correct structure:**

```
MIDI Remote Scripts
└── AbletonLoopingSurface
    ├── __init__.py
    └── AbletonLoopingSurface.py
```

**Wrong structure (will NOT work in Ableton):**

```
MIDI Remote Scripts
└── AbletonLoopingSurface-main
    ├── __init__.py
    └── AbletonLoopingSurface.py
```

## Enable in Ableton

Go to:

**Settings → Link / Tempo / MIDI**

Set:

- **Control Surface:** AbletonLoopingSurface  
- **Input:** your MIDI controller  
- **Remote:** ON  

## Configuration

Edit:

```AbletonLoopingSurface.py```

```ruby
MIDI_CHANNEL = 0

RECORD_2_NOTE = 67
RECORD_4_NOTE = 79

METRO_NOTE = 71
DELETE_NOTE = 72
```

Default notes: 

- **G3** - rec 2 bars
- **A3** - rec 4 bars
- **B3** - metro toggle
- **C4** - delete selected clip (usually last key on mini keyboards)

You can bind functions on less used range.

MIDI Note Reference:

```
C3	60
C4	72
C5	84
```

## Troubleshooting

Script not visible:
- Restart Ableton
- Check folder structure

Log file:

**Mac**
```~/Library/Preferences/Ableton/Live 12/Log.txt```

**Windows**
```C:\Users\<username>\AppData\Roaming\Ableton\Live 12\Preferences\Log.txt```

## License

MIT