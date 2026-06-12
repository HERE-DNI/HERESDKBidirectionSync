---
title: "initialAzimuthInDegrees property"
slug: "sdk-for-flutter-navigate-navigation-spatialnotificationdetails-initialazimuthindegrees"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- initialAzimuthInDegrees.html -->


<div>
<h1>initialAzimuthInDegrees property</h1></div>

        
        double
        initialAzimuthInDegrees
<div class="features">getter/setter pair</div>


<p>Initial desired angular position of the upcoming audio cue. For example, for a maneuver such as
"Turn right on" (<code>ManeuverAction.RightTurn</code>) we want to create a spatial audio arc trajectory
from the front to the right, mimicking the maneuver geometry.
In this case, it is good practice to start the trajectory from an initial azimuth that is located
slightly on the opposite direction of the maneuver (e.g. slightly starting from "front-left")
and terminate the trajectory fully on the right side. The initial azimuth angle of such
a trajectory would be, for example, -5.0 (slightly front-left).
This azimuth value is needed to set the position of the audio renderer before starting to play
the audio cue to avoid unwanted audio "jumps".
The orientation in space for <a href="/sdk-for-flutter-navigate-navigation-spatialnotificationdetails-initialazimuthindegrees">SpatialNotificationDetails.initialAzimuthInDegrees</a> can be represented by the
following angular values:</p>
<table>
<thead>
<tr>
<th align="center">Front</th>
<th align="center">Right</th>
<th align="center">Rear</th>
<th align="center">Left</th>
</tr>
</thead>
<tbody>
<tr>
<td align="center">0°</td>
<td align="center">+90°</td>
<td align="center">+- 180</td>
<td align="center">-90°</td>
</tr>
</tbody>
</table>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">double initialAzimuthInDegrees;</code></pre>

 



</div>
`
}</HTMLBlock>
