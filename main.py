#!/usr/bin/env python3
"""The printer's apology, printed once and nothing else.

The apology line is defined in entry_text; this script just
reaches into that module and echoes its constant to the terminal.
"""

import entry_text as source

print(source.LINE)
