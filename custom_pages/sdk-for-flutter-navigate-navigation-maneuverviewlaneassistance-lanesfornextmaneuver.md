---
title: "lanesForNextManeuver property"
slug: "sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-lanesfornextmaneuver"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- lanesForNextManeuver.html -->


<div>
<h1>lanesForNextManeuver property</h1></div>

        
        List&lt;<a href="sdk-for-flutter-navigate-navigation-lane-class">Lane</a>&gt;
lanesForNextManeuver
<div class="features">getter/setter pair</div>


<p>A list of lanes on the current road that leads to the upcoming maneuver.
The lanes are sorted from left to right: The lane at index 0 represents the leftmost lane and
the last index represents the rightmost lane.
This is valid for both right-hand and left-hand driving countries.
Contraflow lanes are not included in the list.
The list is guaranteed to be non-empty.
<a href="sdk-for-flutter-navigate-navigation-roadattributes-isrightdrivingside">RoadAttributes.isRightDrivingSide</a> indicates if this is a left-hand driving country or not.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;Lane&gt; lanesForNextManeuver;</code></pre>

 



</div>
`
}</HTMLBlock>
