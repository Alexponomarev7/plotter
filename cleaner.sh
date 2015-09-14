#!/bin/bash
find `dirname $0`/{img,tasks,cnc}/* -mmin +30 -exec rm -f {} \;
