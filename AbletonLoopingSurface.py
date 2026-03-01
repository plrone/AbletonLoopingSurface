import Live

from _Framework.ControlSurface import ControlSurface
from _Framework.ButtonElement import ButtonElement
from _Framework.InputControlElement import MIDI_NOTE_TYPE


# ==============================
# CONFIG
# ==============================

MIDI_CHANNEL = 0

QUANTIZE_NOTE = 68   # G#3
METRO_NOTE    = 70   # A#3
RECORD_2_NOTE = 67   # G3
RECORD_4_NOTE = 69   # A3
UNDO_NOTE     = 71   # B3
DELETE_NOTE   = 72   # C4


# ==============================
# SCRIPT
# ==============================

class AbletonLoopingSurface(ControlSurface):

    def __init__(self, c_instance):

        super(AbletonLoopingSurface, self).__init__(c_instance)

        self.log_message("Controller initialized")

        with self.component_guard():

            # RECORD 2 BARS
            self._record2_button = ButtonElement(
                True,
                MIDI_NOTE_TYPE,
                MIDI_CHANNEL,
                RECORD_2_NOTE
            )

            self._record2_button.add_value_listener(
                self._record_2_bars
            )


            # RECORD 4 BARS
            self._record4_button = ButtonElement(
                True,
                MIDI_NOTE_TYPE,
                MIDI_CHANNEL,
                RECORD_4_NOTE
            )

            self._record4_button.add_value_listener(
                self._record_4_bars
            )


            # METRONOME
            self._metro_button = ButtonElement(
                True,
                MIDI_NOTE_TYPE,
                MIDI_CHANNEL,
                METRO_NOTE
            )

            self._metro_button.add_value_listener(
                self._toggle_metronome
            )


            # DELETE
            self._delete_button = ButtonElement(
                True,
                MIDI_NOTE_TYPE,
                MIDI_CHANNEL,
                DELETE_NOTE
            )

            self._delete_button.add_value_listener(
                self._delete_clip
            )

            # UNDO
            self._undo_button = ButtonElement(
                True,
                MIDI_NOTE_TYPE,
                MIDI_CHANNEL,
                UNDO_NOTE
            )

            self._undo_button.add_value_listener(
                self._undo
            )


            # QUANTIZE
            self._quantize_button = ButtonElement(
                True,
                MIDI_NOTE_TYPE,
                MIDI_CHANNEL,
                QUANTIZE_NOTE
            )

            self._quantize_button.add_value_listener(
                self._quantize
            )


# ==============================
# RECORD FUNCTIONS
# ==============================

    def _record_2_bars(self, value):

        if value == 0:
            return

        self._record_fixed_length(2)


    def _record_4_bars(self, value):

        if value == 0:
            return

        self._record_fixed_length(4)


    def _record_fixed_length(self, bars):

        song = self.song()

        clip_slot = song.view.highlighted_clip_slot

        if clip_slot:

            beats = song.signature_numerator * bars

            clip_slot.fire(record_length=beats)

            self.log_message("Recording " + str(bars) + " bars")


# ==============================
# METRONOME
# ==============================

    def _toggle_metronome(self, value):

        if value == 0:
            return

        song = self.song()

        song.metronome = not song.metronome

        self.log_message("Metronome: " + str(song.metronome))


# ==============================
# DELETE
# ==============================

    def _delete_clip(self, value):

        if value == 0:
            return

        song = self.song()

        clip_slot = song.view.highlighted_clip_slot

        if clip_slot and clip_slot.has_clip:

            clip_slot.delete_clip()

            self.log_message("Clip deleted")


# ==============================
# UNDO
# ==============================

    def _undo(self, value):

        if value == 0:
            return

        if self.song().can_undo:

            self.song().undo()

            self.log_message("Undo")


# ==============================
# QUANTIZE
# ==============================

    def _quantize(self, value):

        if value == 0:
            return

        song = self.song()
        clip_slot = song.view.highlighted_clip_slot

        if not clip_slot or not clip_slot.has_clip:
            self.log_message("No clip selected")
            return

        clip = clip_slot.clip

        if not clip.is_midi_clip:
            self.log_message("Not a MIDI clip")
            return


        # toggle strength
        if not hasattr(self, "_quantize_strength"):
            self._quantize_strength = 1.0


        if self._quantize_strength == 1.0:
            self._quantize_strength = 0.5
        else:
            self._quantize_strength = 1.0


        clip.quantize(
            Live.Clip.GridQuantization.g_sixteenth,
            self._quantize_strength
        )


        self.log_message(
            "Quantize strength: " + str(int(self._quantize_strength * 100)) + "%"
        )