---
title: "turnAngleInDegrees property"
slug: "sdk-for-flutter-navigate-routing-maneuver-turnangleindegrees"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- turnAngleInDegrees.html -->


<div>
<h1>turnAngleInDegrees property</h1></div>
<section id="getter">

double?
turnAngleInDegrees


<p>The angle of the turn component of the maneuver.
The angle increases clockwise and small values are used for going straight, i.e. a positive number
means there is a right turn and a negative number is a left turn.
Some maneuvers like Depart, Arrive and Roundabout pass doesn't have a well defined angle, so the value
is omitted.
<strong>Note:</strong> These attributes are only available for the Navigate license.
Gets the angle of the turn component of the maneuver. The value is in degrees and from -180 to 180.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">double? get turnAngleInDegrees;</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
