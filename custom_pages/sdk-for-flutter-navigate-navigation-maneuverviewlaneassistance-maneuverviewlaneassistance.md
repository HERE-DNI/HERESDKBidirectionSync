---
title: "ManeuverViewLaneAssistance constructor"
slug: "sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-maneuverviewlaneassistance"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ManeuverViewLaneAssistance.html -->


<div>
<h1>ManeuverViewLaneAssistance constructor</h1></div>

ManeuverViewLaneAssistance(<ol class="parameter-list single-line"> <li>List&lt;<a href="sdk-for-flutter-navigate-navigation-lane-class">Lane</a>&gt; lanesForNextManeuver, </li>
<li>List&lt;<a href="sdk-for-flutter-navigate-navigation-lane-class">Lane</a>&gt; lanesForNextNextManeuver</li>
</ol>)
    

<p>Creates a new instance.</p>
<ul>
<li><code>lanesForNextManeuver</code> A list of lanes on the current road that leads to the upcoming maneuver.
The lanes are sorted from left to right: The lane at index 0 represents the leftmost lane and
the last index represents the rightmost lane.
This is valid for both right-hand and left-hand driving countries.
Contraflow lanes are not included in the list.
The list is guaranteed to be non-empty.
<a href="sdk-for-flutter-navigate-navigation-roadattributes-isrightdrivingside">RoadAttributes.isRightDrivingSide</a> indicates if this is a left-hand driving country or not.</li>
<li><code>lanesForNextNextManeuver</code> A list of lanes on the road that leads to the maneuver after the upcoming maneuver.
The lanes are sorted from left to right: The lane at index 0 represents the leftmost lane and
the last index represents the rightmost lane.
This is valid for both right-hand and left-hand driving countries.
Contraflow lanes are not included in the list.
<a href="sdk-for-flutter-navigate-navigation-roadattributes-isrightdrivingside">RoadAttributes.isRightDrivingSide</a> indicates if this is a left-hand driving country or not.
By default, this list is empty. It will be filled when the next two maneuvers are too
close to each other, or when the next two maneuvers are roundabout maneuvers.
Note: This notification is delivered at the same time as the <a href="sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-lanesfornextmaneuver">ManeuverViewLaneAssistance.lanesForNextManeuver</a>.
There is no separate maneuver notification on the second maneuver when two maneuvers are
are too close to each other.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">ManeuverViewLaneAssistance(this.lanesForNextManeuver, this.lanesForNextNextManeuver);</code></pre>

 



</div>
`
}</HTMLBlock>
