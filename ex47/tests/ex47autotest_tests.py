# from nose.tools import *
# import ex47autotest

# def setup():
    # print "SETUP!"
    
# def teardown():
    # print "TEAR DOWN"
    
# def test_basic():
    # print "I RAN!"

from nose.tools import *
from game import Room

def test_room():
    print "Going into Gold room"
    gold = Room("Gold Room", 
                """This room has gold in it you can grab. There's a 
                door to the north.""")
    assert_equal(gold.name, "Gold Room")
    assert_equal(gold.paths, {})
    
def test_room_paths():
    print "Going Center"
    center = Room("Center", "Test room in the center.")
    north = Room("North", "Test room in the north.")
    south = Room("South", "Test room in the south.")
    
    center.add_paths({'north': north, 'south': south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)
    
def test_map():
    print "Starting the game"
    start = Room("Start", "You can go west and down a hole.")
    west = Room("Trees", "There are trees here, you can go east.")
    down = Room("Dungeon", "It's dark down here, you can go up.")
    
    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})
    
    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)