#! /usr/bin/env python3
import sys

def update_status(text):
    print("""<script id="___autoremovable">
        $("#status").text(""" + repr(text) + """);
        $("#___autoremovable").remove();
        </script>""")
#    print("New status:", text, file=sys.stderr)
    sys.stdout.flush()
