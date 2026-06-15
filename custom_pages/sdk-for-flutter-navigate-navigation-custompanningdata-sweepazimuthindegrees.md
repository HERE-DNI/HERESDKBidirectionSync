---
title: "sweepAzimuthInDegrees property"
slug: "sdk-for-flutter-navigate-navigation-custompanningdata-sweepazimuthindegrees"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- sweepAzimuthInDegrees.html -->


<div>
<h1>sweepAzimuthInDegrees property</h1></div>

        
        double?
        sweepAzimuthInDegrees
<div class="features">getter/setter pair</div>


<p>Sweep angle of the upcoming audio cue. For example, for a maneuver such as "Turn right on"
(i.e. <code>ManeuverAction.RightTurn</code>),
within an <code>initial_azimuth_in_degrees</code> of -5 degrees, we want to create a spatial audio arc
trajectory from the front to the right, mimicking the maneuver geometry.
In this case, the desired final angle would be +90 degrees, and therefore, a sweep angle of
+95 degrees would be required.
On the other hand, when the desired spatialization is to the left side
(i.e. <code>ManeuverAction.LeftTurn</code>), the <code>initial_azimuth_in_degrees</code> could be set to +5 degrees
and the <code>sweep_azimuth_in_degrees</code> to -95 degrees</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">double? sweepAzimuthInDegrees;</code></pre>

 



</div>
`
}</HTMLBlock>
