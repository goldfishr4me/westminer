import time
import random
import states
import items
from world import World
from entities.miner import Miner
from entities.wife import Wife
from entities import MessageDispatcher

if __name__ == '__main__':
    world = World('westworld')
    dispatcho = MessageDispatcher(world)

    miner_wife = Wife(world,
                      'Deloris',
                      states.wife_global,
                      states.wake_up_and_make_coffee,
                      states.wake_up_and_make_coffee,
                      'home',
                      0,
                      0,
                      0,
                      0,
                      False)
    real_miner = Miner(world,
                       'Bob',
                       states.enter_mine_and_dig_for_nugget,
                       states.enter_mine_and_dig_for_nugget,
                       states.enter_mine_and_dig_for_nugget,
                       'home',
                       0,
                       0,
                       0,
                       0,
                       "bulky",
                       items.small_pickax,
                       miner_wife)
    miner_wife.husband = real_miner
    other_miner = Miner(world,
                        'Sam',
                        states.enter_mine_and_dig_for_nugget,
                        states.enter_mine_and_dig_for_nugget,
                        states.enter_mine_and_dig_for_nugget,
                        'home',
                        1,
                        10,
                        0,
                        0,
                        "lanky",
                        items.small_pickax)

    world.entities.extend([real_miner, other_miner, miner_wife])
    counter = 0
    while counter < 50:
        print("Game tick {}".format(counter))
        world.dispatcher.dispatch_delayed()
        world.update()
        time.sleep(0.5)
        counter += 1
