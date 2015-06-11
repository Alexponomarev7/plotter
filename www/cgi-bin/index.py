#! /usr/bin/env python3
import time

print("Set-cookie: seed=", time.time(), sep='')
print("Content-type: text/html\n")

print("""<!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8" />
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
<!--            <link href="/css/style.css" rel="stylesheet" /> -->
            <title>Plotter</title>
        </head>
        <body>
            <script src="/js/index.js"></script>
            <h1>XY Plotter v0.1</h1>
            <h2>Send a request: </h2>
            <form action="/cgi-bin/preview.py">
                <table id="texts">
                <tr>
                    <td>
                        <input type="text" name="formula0" />
                    </td>
                    <td>
                        <button type="button" class="rm_button">Remove</button>
                    </td>
                </tr>
                </table>
                <table>
                    <tr>
                        <td>
                            <input id="graph" type="radio" name="img_type" value="graph" checked> Graph</input>
                        </td>
                        <td>
                            <input id="bezier" type="radio" name="img_type" value="bezier"> Bezier</input>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <button type="button" id="add">Add text field</button>
                        </td>
                        <td>
                            <input type="submit" />
                        </td>
                    </tr>
                </table>
            </form>
            <a href="/help.html">Help</a>
        </body>
        </html>
""")

