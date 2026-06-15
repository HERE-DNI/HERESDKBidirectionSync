---
title: "initialAzimuthInDegrees property"
slug: "sdk-for-flutter-navigate-navigation-custompanningdata-initialazimuthindegrees"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- initialAzimuthInDegrees.html -->


<div>
<h1>initialAzimuthInDegrees property</h1></div>

        
        double?
        initialAzimuthInDegrees
<div class="features">getter/setter pair</div>


<p>Initial desired angular position of the upcoming audio cue. For example, for a maneuver such
as "Turn right on" (<code>ManeuverAction.RightTurn</code>) we want to create a spatial audio arc
from the front to the right, mimicking the maneuver geometry. In this case,
it is good practice to start the trajectory from an initial azimuth that is slightly located
on the opposite direction of the maneuver (e.g. slightly starting from "front-left")
and terminate the trajectory fully on the right side. The initial azimuth angle of such
a trajectory would be, for example, -5.0 (slightly front-left).
This azimuth value is needed to set the position of the audio renderer before starting
to play the audio cue to avoid unwanted audio "jumps".</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">double? initialAzimuthInDegrees;</code></pre>

 



</div>
`
}</HTMLBlock>
