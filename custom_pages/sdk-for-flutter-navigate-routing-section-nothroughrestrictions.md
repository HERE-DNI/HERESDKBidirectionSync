---
title: "noThroughRestrictions property"
slug: "sdk-for-flutter-navigate-routing-section-nothroughrestrictions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- noThroughRestrictions.html -->


<div>
<h1>noThroughRestrictions property</h1></div>
<section id="getter">

List&lt;<a href="/sdk-for-flutter-navigate-routing-violatedrestriction-class">ViolatedRestriction</a>&gt;
noThroughRestrictions


<p>The list of no through restriction
The no through restriction area is part of the road network that do not allow through traffic.
For example the <code>Resident only</code> sign indicates that vehicles are only allowed to enter this area if they are making a stop.
This area will be set only if <code>origin</code>, <code>destination</code> or <code>via</code> waypoint will be requested within the area.
list of no through restriction.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;ViolatedRestriction&gt; get noThroughRestrictions;</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
