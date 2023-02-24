# Weekly report 6

23-24.2.2023

I worked on a slider entity for the UI. Working on the component kinda taught me the importance of separating each component into its own class.
It makes the code much more re-usable i.e right now I can just create as many sliders as I want to (each with different size, value, text if needed).
I believe the buttons should be their own class as well, so if I get the time, I will try to refactor that the code a bit. However,
there is still so much work to do so I am not sure if I will get to it (finishing the actual project has much higher priority). I also made the UI a little bit
more readable and worked on performance testing. I will probably attempt to generate a combined biome/dungeon map if I have enough time.

Additionally, I did some research on how could I make the application run faster. One big issues is the usage of nested loops, apparently, it would be wise
to replace the standard library loops/list with NumPy arrays, this would be a huge performance boost for the application (as shown here: https://medium.com/@z.arderne/numpy-array-vs-nested-list-622b95d12761). Something to consider for future projects.
