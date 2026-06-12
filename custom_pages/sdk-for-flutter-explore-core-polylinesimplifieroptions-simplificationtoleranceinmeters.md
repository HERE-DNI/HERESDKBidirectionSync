---
title: "simplificationToleranceInMeters property"
slug: "sdk-for-flutter-explore-core-polylinesimplifieroptions-simplificationtoleranceinmeters"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- simplificationToleranceInMeters.html -->


<div>
<h1>simplificationToleranceInMeters property</h1></div>

        
        int
        simplificationToleranceInMeters
<div class="features">getter/setter pair</div>


<p>Sets the accuracy limit for the <a href="/sdk-for-flutter-explore-core-polylinesimplifier-simplify">PolylineSimplifier.simplify</a>:</p>
<ul>
<li>higher tolerance results in more simplification (fewer points);</li>
<li>lower tolerance keeps the line closer to its original shape.</li>
</ul>
<p>If removing a point produces polyline, which deviates from the
original one more than <code>simplificationToleranceInMeters</code>, then
this point is left in the collection.</p>
<p>If specified tolerance will not allow to create a polyline
conforming to <a href="/sdk-for-flutter-explore-core-polylinesimplifieroptions-maxpoints">PolylineSimplifierOptions.maxPoints</a>, then <code>simplificationToleranceInMeters</code>
is ignored.</p>
<p>Default value is equal to <a href="/sdk-for-flutter-explore-core-polylinesimplifieroptions-simplificationinmeters14zoomlevel">PolylineSimplifierOptions.simplificationInMeters14ZoomLevel</a>.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">int simplificationToleranceInMeters;</code></pre>

 



</div>
`
}</HTMLBlock>
