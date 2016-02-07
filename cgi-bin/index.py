#! /usr/bin/env python3
import time
from lib import const

print("Set-cookie: seed=", time.time(), sep='')
print("Content-type: text/html\n")

print("""<!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8" />
            <script src="../js/jquery.min.js"></script>
            <link rel="shortcut icon" href="../favicon.ico" type="image/x-icon" />
<!--            <link href="../css/style.css" rel="stylesheet" /> -->
            <title>Plotter</title>
        </head>
        <body>
            <script src="../js/index.js"></script>
            <h1>XY Plotter v1.0</h1>
            <h2>Send a request: </h2>
            <form action="preview.py" method="post">
                <input id="num" type="hidden" name="num_of_objects" value="0" />
                <table id="functions" class="input" hidden>
                </table>
                <table id="points" class="input" hidden>
                </table>
                <table id="graph_settings" class="input" hidden>
                    <tr>
                        <td hidden>
                            X coordinate in center:
                        </td>
                        <td hidden>
                            <input type="text" name="x_pos" value="0" />
                        </td>
                        <td hidden>
                            Y coordinate in center:
                        </td>
                        <td hidden>
                            <input type="text" name="y_pos" value="0" />
                        </td>
                        <td>
                            Scale, %:
                        </td>
                        <td>
                            <input type="text" name="scale" value="100" />
                        </td>
                    </tr>
                </table>
                <table id="bezier_settings" class="input" hidden>
                    <tr>
                        <td>
                            Draw anchor points:
                        </td>
                        <td>
                            <input type="checkbox" name="draw_anchor" value="True" />
                        </td>
                    </tr>
                </table>
                <table>
                    <tr>
                        <td>
                            <input id="graph" type="radio" name="task_type" value="graph"> Graph</input>
                        </td>
                        <td>
                            <input id="bezier" type="radio" name="task_type" value="bezier"> Bezier</input>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <button type="button" id="add_btn" hidden></button>
                        </td>
                        <td>
                            <input type="submit" id="send_btn" value="Preview" hidden/>
                        </td>
                    </tr>
                </table>
            </form>
            <button id="help_btn">Help</button>
            <div id="help_div" hidden></div>
        </body>
        </html>
""")
