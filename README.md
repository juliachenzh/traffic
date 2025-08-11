this is a simple “traffic wave” app that uses Python to simulate and visualise the effects of vehicle distribution and reaction time on traffic delays.

The idea to build this app hit me after a Sydney-to-Wollongong road trip (via Engadine and Stanwell Tops) that turned into a 4-hour drive instead of a quick 1.5-hour cruise.

Using turtles (cars) and kangaroos (obstacles), I played with variables like reaction time, car spacing, and acceleration to see the jam form in real time. 

Sure, it’s been modelled before, but I wanted to use it as an opportunity to play around with velocity/acceleration functions and also animations.

To make the simulation feel real, I factored in both ***human quirks*** — like reaction time and personal comfort zones for following distance — and ***mechanical limits**,* like how quickly a car can accelerate or slow down.

Below is just the visuals from phase one. Paired with the visual is a dashboard of “summary stats” (with metrics such as Aggregate Time Delayed in Traffic). The next step is modelling multi-lane mayhem…

![a2okfe](https://github.com/user-attachments/assets/ae7914e1-3c9d-497b-b9a4-d750a651dc8a)

Here’s the basic animation playback.

***Legend***

**Green** = normal speed

**Yellow** = slowing down

**Red** = stopped

**Blue** = accelerating

Actions: When the user presses a button, the kangaroo jumps in front of the cars.
