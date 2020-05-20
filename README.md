# Ugliest Orca

This is a script written in [Orca](https://100r.co/site/orca.html) generating "pattern free music" using [Costas arrays](https://en.wikipedia.org/wiki/Costas_array) and is inspired by Scott Rickard's ["The World's Ugliest Music"](https://www.youtube.com/watch?v=RENk9PK06AQ)

![screenshot of the Orca script, it kinda looks like a kangaroo](screenshots/screenshot-ugliest-orca.png)

Due to the limitations of the Orca language, having base 36 one digit numbers only, the maximum order of costas array which can be generated using this script is `p = 13` using the primitive root `g = 2`, since the largest possible remainder (`16`) of the next larger prime `p = 17` multiplied with its lowest primitive root `g = 3` would cause the multiplication operator to overflow (`16 * 3 = 48 > 36`).


