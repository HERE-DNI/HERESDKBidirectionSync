---
title: "spanIndex property"
slug: "sdk-for-flutter-explore-routing-maneuver-spanindex"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- spanIndex.html -->


<div>
<h1>spanIndex property</h1></div>
<section id="getter">

int
spanIndex


<p>Index over <a href="sdk-for-flutter-explore-routing-section-spans">Section.spans</a> indicating the first span after the maneuver point.
<strong>Note:</strong> The span index for the last maneuvers (those maneuvers with maneuver action set to
<a href="sdk-for-flutter-explore-routing-maneuveraction">ManeuverAction.arrive</a>) cannot be used, since these maneuvers are placed after the last span of the route and
the span index for them would be greater than the span list size.
Gets the index over <a href="sdk-for-flutter-explore-routing-section-spans">Section.spans</a> indicating the first span after the maneuver point.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">int get spanIndex;</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
