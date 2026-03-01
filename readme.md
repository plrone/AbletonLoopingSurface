# AbletonLoopingSurface

Ableton Live 12 Control Surface script that adds fixed-length recording, undo, quantize, delete, and metronome control via MIDI in Session View.

If this script improves your workflow and helps your live looping setup, consider supporting its development.

You can buy me a coffee here:

☕ https://buymeacoffee.com/hazedrifter

Thank you for your support and happy looping!

## Features

- Delete selected clip
- Undo last action
- Fixed length clip recording (same method as Ableton Push)
- Quantize with two strength levels (first press: 50%, second press: 100%)
- Metronome toggle
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

```python
QUANTIZE_NOTE = 68   # G#3
METRO_NOTE    = 70   # A#3
RECORD_2_NOTE = 67   # G3
RECORD_4_NOTE = 69   # A3
UNDO_NOTE     = 71   # B3
DELETE_NOTE   = 72   # C4
```

Default notes: 

- **G#3** - Quantize
- **A#3** - Metro toggle
- **G3** - Rec 2 bars
- **A3** - Rec 4 bars
- **C4** - Delete selected clip

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