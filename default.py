'''UrbanDictionary app by gauravssnl
Contact: gaurav.ssnl@gmail.com'''
__author__ = 'gauravssnl'
__version__ = '1.00.00'
# pyS60 v2.0(python 2.5.4) app

import urbandict
import Console
import appuifw
import e32
import globalui

app_lock = e32.Ao_lock()
ru = lambda text : text.decode('utf-8' , 'ignore')
ur = lambda text : text.encode('utf-8' , 'ignore')

def quit():
    q = appuifw.query( ru( 'Do you really want to exit' ), 'query' )
    if q :
        app_lock.signal()
        
def UI():
    appuifw.app.title = ru('Urban Dictionary')
    global console
    console = Console.Console( True )
    appuifw.app.body = console.text
    appuifw.app.screen = 'normal'
    initialize()
    console.text.font = 'title',18
    appuifw.app.menu = [( ru( 'Search' ) , search ) ,( ru( 'About' ) ,about ) ]
    

def initialize():
    global console
    console.text.font = 'title',22
    console.text.color = 255,0,0
    console.write( 'UrbanDictionary App by gauravssnl\n' )
    console.text.font = 'title',20
    console.text.color = 0,0,200
    console.write( 'Dictionary based on urbandictionary.com\n' )
    console.text.font = 'title',20
    console.text.color = 0,0,0
    console.write( '-' * 35)
    console.write('\n')
    
    
    
def search():
    global console
    qw = appuifw.query( ru( 'Enter word to search meaning' ) , 'text' )
    if qw :
        
        console.write('WORD : ')
        e32.ao_sleep(0.005)
        console.text.color = 0,0,255
        console.write( qw)
        console.write('\n')
        qw = ur(qw).rstrip()
        res = urbandict.define( ( qw ) )
        for dicts in res:
            #console.write( dicts[ 'word' ] )
            console.text.color = 255,0,255
            console.write( dicts[ 'def' ])
            console.text.color = 0,0,255
    
            console.write( dicts[ 'example' ] )
            console.write('\n')
            console.text.color = 0,0,0
    
    
def about():
    globalui.global_msg_query( ru( 'UrbanDictionary app by gauravssnl\nDictionary based on urbandictionary.com\nThanks:Roman Bogrodskiy(Author: urbandict module)\n' ) , ru( 'UrbanDictionary' ) )
    
            
    
    
    
    
            
    
e32.ao_yield()    
UI()
app_lock.wait()            



