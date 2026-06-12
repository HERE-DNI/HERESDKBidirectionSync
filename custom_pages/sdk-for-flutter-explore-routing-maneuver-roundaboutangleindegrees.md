---
title: "roundaboutAngleInDegrees property"
slug: "sdk-for-flutter-explore-routing-maneuver-roundaboutangleindegrees"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- roundaboutAngleInDegrees.html -->


<div>
<h1>roundaboutAngleInDegrees property</h1></div>
<section id="getter">

double?
roundaboutAngleInDegrees


<p>The angle is estimated between the incoming and outgoing route parts before entering the actual roundabout.
This is done to provide a better orientation for drivers. For better results, the incoming and outcoming route
parts can be around 50 meters in length. In addition, these parts lie usually around 30 meters away from
the actual roundabout. Therefore, the resulting arc does not necessarily represent the exact curved path a
vehicle has to follow within a roundabout from the point of entry to the point of exit. Instead, it reflects
the route path before and after the roundabout to highlight the directional change along the route. The angle can have a value from -360.0 to 360.0, and it is positive
in right-hand side driving country, and negative in left-hand side countries.
Note that the value is available for both the enter roundabout actions and the exit roundabout
actions. Both maneuvers have the same value. When the incoming or outgoing route parts are curvy or when the
roundabout itself is not representing a perfect circle, then the accuracy of the angle may be
compromised.
<strong>Note:</strong> These attributes are only available for the Navigate license.
The angle is estimated between the incoming and outgoing route parts before entering the actual roundabout.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">double? get roundaboutAngleInDegrees;</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
