# Weekly report 3

30.1.2023

I had a brain blast this morning, and I think that my current approach is completely wrong. The root of the BSP Tree should be the size of the whole map, and
from there, I should divide the map into smaller sections (within the bounds). At least my current data structures are not completely wrong. I am fairly sure that the information held by nodes is enough. I can use the split nodes (or areas, planes) to hold a room, as long as the room size is within the bounds of the area. Now that I have a better grasp of what I am doing, things should go more smoothly this week. Changing the recursion of BSP Tree will be the first thing on the list (I will work extra time this week to make sure everything works).

2.2.2023

I restructured pretty much everything. The biggest problem was the fact that it was hard to determine what was actually happening without
any form of visualization. Now the BSP tree works, but the split still needs more randomization to make the room locations more interesting. The
main issue is that the first room is currently created in an almost fixed location (top left). The UI is ugly, too. It is going
to take a lot of coding to make it look pretty (and I had no experience with Pygame prior to this project which is generating even more problems).
I feel like I underestimated the size of the project, but its been fun so far.

3.3.2023

Managed to write A Star algorithm for pathfinding. The rooms seem to connect without any of them isolating, but the generation does not look
very appealing. The paths usually form a square. This is something I will have to work on if I find the time. Other than that, I am happy
with the progress so far. Also need to do more testing! Code might need refactoring too i.e maybe it would make sense to have A Star on its
own module? I am not sure yet.

## What have I done this week?

Worked on BSP Tree partitions and A star search algorithm. Wrote bunch of tests.

## What have I learned?

Much better understanding on how to partition areas using the BSP Tree. I learned how to use A star to find the shortest paths
between nodes.

## Problems

Right now A star finds too many paths and I have no idea how I can improve it. It is also hard to figure out what the threshold should be
(i.e too low and nothing connects, too high and you get even more paths). Paths often start at edges of the rooms as well, which makes sense
since I am using the node x,y coordinates, but it makes the dungeons look a bit ugly.

## What will I do next?

Start working on random walk to generate biomes. It should be a lot easier to figure out than BSP / A Star. Improve UI and try to wiggle with parameters to
make the dungeons look visually better.

## Conclusion

Made a ton of progress, but it is still hard to make dungeons that are visually appealing. Also: thank you for the
link you sent me on email, using height/width ratios for partitions makes sense!

Time used: 25-30 hours. I neglected other courses to make room for this project.
