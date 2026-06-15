---
title: "principalPoint property"
slug: "sdk-for-flutter-explore-mapview-mapcamera-principalpoint"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- principalPoint.html -->


<div>
<h1>principalPoint property</h1></div>
<section id="getter">

<a href="sdk-for-flutter-explore-core-point2d-class">Point2D</a>
principalPoint


<p>Determines the pixel point where the target is placed within the map view. Setting a new
principal point instantly moves the map to render the current target coordinates
at the new principal point.
Gets the pixel point that determines where the target is placed within the map view.
By default, the principal point is located at the center of the map view.</p>
<p>The value of the principal point is adjusted when the dimensions of the
map view change, so that it stays in the same point relative to width
and height. Meaning that when a principal point it set to bottom
middle of the map view, it will stay in the bottom middle regardless
of the changes to dimensions and orientation of the view.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">Point2D get principalPoint;</code></pre>

</section>
<section id="setter">

void
principalPoint=(<a href="sdk-for-flutter-explore-core-point2d-class">Point2D</a> value)


<p>Determines the pixel point where the target is placed within the map view. Setting a new
principal point instantly moves the map to render the current target coordinates
at the new principal point.
Sets the pixel point that determines where the target appears within the map view.
This instantly moves the map to render the current target coordinates
at the new principal point.</p>
<p>By default, the principal point is located at the center of the map view.
It is set in pixels relative to the map view's origin top-left (0, 0).
Values outside the map view's dimensions (x &lt; 0 || x &gt; width, y &lt; 0 || y &gt; height)
will be rejected silently and the current principal point is kept.</p>
<p>The value of the principal point is adjusted when the dimensions of the
map view change, so that it stays in the same point relative to width
and height. Meaning that when a principal point it set to bottom
middle of the map view, it will stay in the bottom middle regardless
of the changes to dimensions and orientation of the view.</p>
<p>Note: The principal point affects all programmatical map transformations (rotate, orbit, tilt and zoom)
and the two-finger-pan gesture to tilt the map. Other gestures, like pinch-rotate,
are not affected.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set principalPoint(Point2D value);</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
