# Weekly report 6

23-24.2.2023

I worked on a slider entity for the UI. Working on the component kinda taught me the importance of separating each component into its own class.
It makes the code much more re-usable i.e right now I can just create as many sliders as I want to (each with different size, value, text if needed).
I believe the buttons should be their own class as well, so if I get the time, I will try to refactor that the code a bit. However,
there is still so much work to do so I am not sure if I will get to it (finishing the actual project has much higher priority). I also made the UI a little bit
more readable and worked on performance testing. I will probably attempt to generate a combined biome/dungeon map if I have enough time.

Additionally, I did some research on how could I make the application run faster. One big issue is the usage of nested loops, apparently, it would be wise
to replace the standard library loops/list with NumPy arrays. This would be a huge performance boost for the application (as shown here: https://medium.com/@z.arderne/numpy-array-vs-nested-list-622b95d12761). Something to consider for future projects.

# What have I done this week?

Cleaned up a few classes and wrote code for UI slider. Added sliders to adjust the room sizes as well as the number of random walk steps. Wrote the peer-review.

## What have I learned?

More about how Pygame works, I am still not comfortable in using it, though. I also learned that I should have used numpy arrays instead of regular nested loops, but I wanna focus on implementing other things for now.

## Problems

No problems this week.

## What will I do next?

I will try to make the UI look nicer (especially the font since I received feedback on it and I kinda agree that it looks rough). Implement other fixes suggested in peer-reviews. Maybe add tests. MAYBE combined dungeon if I have time before the demo.

## Conclusion

I feel like I could improve and work on this project forever, but I think it is already in a passing state.

Time spent: around 10 hours in total
