#! /usr/bin/env python3
import driver

driver.start_document("test.cnc")
polygon = [(50, 50), (100, 50), (100, 100), (50, 100)]
driver.draw_polygon(polygon)
driver.draw_circle(75, 75, 25)
driver.end_document()
