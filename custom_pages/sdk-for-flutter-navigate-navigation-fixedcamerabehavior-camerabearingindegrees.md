---
title: "cameraBearingInDegrees property"
slug: "sdk-for-flutter-navigate-navigation-fixedcamerabehavior-camerabearingindegrees"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- cameraBearingInDegrees.html -->


<div>
<h1>cameraBearingInDegrees property</h1></div>
<section id="getter">

double?
cameraBearingInDegrees


<p>Camera bearing in degrees.
Optional fixed bearing, from true North (0 degrees) in clockwise direction. The valid range
is [0, 360].
If set, it will prevent the map from rotating to the direction of travel. For example, a
value of zero results in "north up" mode.
Defaults to <code>null</code>, which means the camera derives the bearing from the <a href="sdk-for-flutter-navigate-core-location-class">Location</a>,
so that it points to the direction of travel.
If this property is <code>null</code> and the device does not provide bearing, the last known value is
used or zero otherwise.
Gets the currently set fixed bearing.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">double? get cameraBearingInDegrees;</code></pre>

</section>
<section id="setter">

void
cameraBearingInDegrees=(double? value)


<p>Camera bearing in degrees.
Optional fixed bearing, from true North (0 degrees) in clockwise direction. The valid range
is [0, 360].
If set, it will prevent the map from rotating to the direction of travel. For example, a
value of zero results in "north up" mode.
Defaults to <code>null</code>, which means the camera derives the bearing from the <a href="sdk-for-flutter-navigate-core-location-class">Location</a>,
so that it points to the direction of travel.
If this property is <code>null</code> and the device does not provide bearing, the last known value is
used or zero otherwise.
Sets an optional fixed bearing value, from true North (0 degrees) in clockwise direction.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set cameraBearingInDegrees(double? value);</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
