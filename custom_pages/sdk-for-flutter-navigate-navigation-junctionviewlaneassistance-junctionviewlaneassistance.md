---
title: "JunctionViewLaneAssistance constructor"
slug: "sdk-for-flutter-navigate-navigation-junctionviewlaneassistance-junctionviewlaneassistance"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- JunctionViewLaneAssistance.html -->


<div>
<h1>JunctionViewLaneAssistance constructor</h1></div>

JunctionViewLaneAssistance(<ol class="parameter-list single-line"> <li>List&lt;<a href="sdk-for-flutter-navigate-navigation-lane-class">Lane</a>&gt; lanesForNextJunction, </li>
<li>double distanceToJunctionInMeters</li>
</ol>)
    

<p>Creates a new instance.</p>
<ul>
<li><code>lanesForNextJunction</code> A list of lanes on the next complex junction.
The lanes are sorted from left to right: The lane at index 0 represents the leftmost lane and
the last index represents the rightmost lane. This is valid for right-hand and left-hand driving
countries. An empty list means that the complex junction has been passed and that the lane information is not
valid anymore. Exactly one event with a non-empty list is delivered before reaching a complex junction and
one event with an empty list afterwards.</li>
</ul>
<p><strong>Note:</strong> Lanes going in opposite direction are not included in the list.</p>
<ul>
<li><code>distanceToJunctionInMeters</code> Distance to the next complex junction in meters.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">JunctionViewLaneAssistance(this.lanesForNextJunction, this.distanceToJunctionInMeters);</code></pre>

 



</div>
`
}</HTMLBlock>
