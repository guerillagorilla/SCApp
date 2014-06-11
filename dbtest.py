#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

location = 'test10'
manufacturer = 'Accuver'
serialnum= 'MY002'

con = lite.connect('testdb')

with con:    
    
    cur = con.cursor()    
    cur.execute("UPDATE products SET location=? WHERE products.manufacturer=? AND products.serialnum=?", (location, manufacturer, serialnum))

    con.commit()
    
    #print "Number of rows updated: %d" % cur.rowcount
    print "product %s updated to location %s" % (serialnum, location)
