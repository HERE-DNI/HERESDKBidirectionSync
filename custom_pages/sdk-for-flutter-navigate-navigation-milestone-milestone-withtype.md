---
title: "Milestone.withType constructor"
slug: "sdk-for-flutter-navigate-navigation-milestone-milestone-withtype"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- Milestone.withType.html -->


<div>
<h1>Milestone.withType constructor</h1></div>

Milestone.withType(<ol class="parameter-list"> <li>int sectionIndex, </li>
<li>int? waypointIndex, </li>
<li><a href="/sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a>? originalCoordinates, </li>
<li><a href="/sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a> mapMatchedCoordinates, </li>
<li><a href="/sdk-for-flutter-navigate-navigation-milestonetype">MilestoneType</a> type, </li>
</ol>)
    

<p>Creates a new instance.</p>
<ul>
<li><code>sectionIndex</code> Index of the section on the route.</li>
<li><code>waypointIndex</code> If present, this index corresponds to the waypoint in the original
user-defined waypoint list. Otherwise this waypoint was added during
route calculation by the system.</li>
<li><code>originalCoordinates</code> User-defined geographic coordinates. If not available, this waypoint was
added during route calculation.</li>
<li><code>mapMatchedCoordinates</code> Map-matched geographic coordinates.</li>
<li><code>type</code> Type of this Milestone</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">Milestone.withType(this.sectionIndex, this.waypointIndex, this.originalCoordinates, this.mapMatchedCoordinates, this.type);</code></pre>

 



</div>
`
}</HTMLBlock>
