---
title: "headingInDegrees property"
slug: "sdk-for-flutter-explore-routing-waypoint-headingindegrees"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- headingInDegrees.html -->


<div>
<h1>headingInDegrees property</h1></div>

        
        double?
        headingInDegrees
<div class="features">getter/setter pair</div>


<p>Optional heading angle referenced by true North, clockwise specifying
the direction of travel. The heading direction may help the routing algorithm to select
the best direction, for example, when multiple directions are possible at a road junction.
North is 0 degrees, East is 90 degrees, South is 180 degrees, and West is 270 degrees.
The value must be in the range [0, 360] when specified. By default, or when <code>null</code> is set,
heading is ignored for route calculation.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">double? headingInDegrees;</code></pre>

 



</div>
`
}</HTMLBlock>
