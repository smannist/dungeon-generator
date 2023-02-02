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
