---
title: "lanes property"
slug: "sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceview-lanes"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- lanes.html -->


<div>
<h1>lanes property</h1></div>

        
        List&lt;<a href="sdk-for-flutter-navigate-navigation-currentsituationlaneview-class">CurrentSituationLaneView</a>&gt;
lanes
<div class="features">getter/setter pair</div>


<p>A list of lanes on the current road.
The lanes are sorted from left to right: The lane at index 0 represents the leftmost lane and
the last index represents the rightmost lane. This is valid for right-hand and left-hand driving
countries. Empty list means unavailability of lane data for the current location.</p>
<p>The left to right order is in the travel direction.
Only the lanes for the current driving direction are included.</p>
<p><strong>Note:</strong> Lanes going in opposite direction are not included in the list.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;CurrentSituationLaneView&gt; lanes;</code></pre>

 



</div>
`
}</HTMLBlock>
