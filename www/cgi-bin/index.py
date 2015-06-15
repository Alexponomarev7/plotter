#! /usr/bin/env python3
import time

print("Set-cookie: seed=", time.time(), sep='')
print("Content-type: text/html\n")

print("""<!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8" />
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
            <link rel="shortcut icon" href="/favicon.ico" type="image/x-icon" />
<!--            <link href="/css/style.css" rel="stylesheet" /> -->
            <title>Plotter</title>
        </head>
        <body>
            <script src="/js/index.js"></script>
            <h1>XY Plotter v1.0</h1>
            <h2>Send a request: </h2>
            <form action="/cgi-bin/preview.py">
                <table id="functions" class="input" hidden>
                </table>
                <table id="points" class="input" hidden>
                </table>
                <table id="graph_settings" class="input" hidden>
                    <tr>
                        <td>
                           X coordinate in center:
                        </td>
                        <td>
                            <input type="text" name="_x_pos" value="0" />
                        </td>
                        <td>
                            Y coordinate in center:
                        </td>
                        <td>
                            <input type="text" name="_y_pos" value="0" />
                        </td>
                        <td>
                            Scale, cm:
                        </td>
                        <td>
                            <input type="text" name="_scale" value="1" />
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
            <a href="/help.html">Help</a>
        </body>
        </html>
""")

