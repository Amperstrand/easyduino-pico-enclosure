"""Easyduino Pico-format case parameters (enclosure-forge target #6).

Boss-class: 4 mounting holes (note the authentic slanted-end hole at
u 16.59 vs 17.39 — extracted, not assumed). Micro-USB at the v=0 edge.
Template reused from target #3.
"""

from __future__ import annotations

import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _load(name):
    with open(os.path.join(ROOT, "analysis", name)) as f:
        return json.load(f)


GEOM = _load("pcb_geometry.json")
COMPS = _load("component_geometry.json")

BOARD_W = GEOM["outline"]["w"]          # 21.0
BOARD_L = GEOM["outline"]["h"]          # 51.0
BOARD_T = GEOM["thickness"]             # 1.6

WALL_T = 1.6            # enclosure_design_decision
FLOOR_T = 1.6           # enclosure_design_decision
CORNER_R = 2.5          # enclosure_design_decision
COMP_Z_CLEARANCE = 1.0  # enclosure_design_decision

BOSS_OUTER = 5.5        # enclosure_design_decision (drill ~2.1 + wall)
BOSS_PILOT = 1.7        # enclosure_design_decision: M2 self-tap in PETG
BOARD_SEAT_Z = 3.0      # enclosure_design_decision

USB_U = next(c for r, c in COMPS.items()
             if "USB" in c["footprint"].upper())["u"]  # derived_kicad
USB_PLUG_W = 8.0        # manufacturer_doc class: micro-B overmold
USB_PLUG_H = 3.2        # manufacturer_doc class
USB_CLEAR = 0.6         # enclosure_design_decision
USB_REACH = 12.0        # enclosure_design_decision

TALLEST = max(c["height"] for c in COMPS.values())
LID_INT_Z = BOARD_SEAT_Z + BOARD_T + TALLEST + COMP_Z_CLEARANCE

LID_LIP = 1.2           # enclosure_design_decision
LID_GAP = 0.25          # enclosure_design_decision
HEADERS_2X18 = {}     # template no-op: Pico headers are mid-board (no wall reliefs)
