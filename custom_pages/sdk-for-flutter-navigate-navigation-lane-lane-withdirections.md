---
title: "Lane.withDirections constructor"
slug: "sdk-for-flutter-navigate-navigation-lane-lane-withdirections"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- Lane.withDirections.html -->


<div>
<h1>Lane.withDirections constructor</h1></div>

Lane.withDirections(<ol class="parameter-list"> <li><a href="sdk-for-flutter-navigate-navigation-lanetype-class">LaneType</a> type, </li>
<li><a href="sdk-for-flutter-navigate-navigation-laneaccess-class">LaneAccess</a> access, </li>
<li><a href="sdk-for-flutter-navigate-navigation-lanemarkings-class">LaneMarkings</a> laneMarkings, </li>
<li>List&lt;<a href="sdk-for-flutter-navigate-navigation-lanedirection">LaneDirection</a>&gt; directions, </li>
<li>List&lt;<a href="sdk-for-flutter-navigate-navigation-lanedirection">LaneDirection</a>&gt; directionsOnRoute, </li>
</ol>)
    

<p>Creates a new instance.</p>
<ul>
<li><code>type</code> Indicates the properties of this lane.
For example, it indicates whether parking is allowed, if it is an acceleration lane,
an express lane, or other attributes.</li>
<li><code>access</code> Indicates which vehicle types can access this lane.</li>
<li><code>laneMarkings</code> Indicates the lane markings between the lanes.</li>
<li><code>directions</code> Indicates all the lane directions that are available for this lane.</li>
<li><code>directionsOnRoute</code> Indicates the lane directions that are on the route.
Following these directions keeps the driver on the route.
This is a subset of <a href="sdk-for-flutter-navigate-navigation-lane-directions">Lane.directions</a>.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">Lane.withDirections(this.type, this.access, this.laneMarkings, this.directions, this.directionsOnRoute)
    : recommendationState = LaneRecommendationState.notRecommended;</code></pre>

 



</div>
`
}</HTMLBlock>
