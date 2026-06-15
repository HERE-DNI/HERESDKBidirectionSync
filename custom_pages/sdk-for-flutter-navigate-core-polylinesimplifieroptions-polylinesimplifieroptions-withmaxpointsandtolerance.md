---
title: "PolylineSimplifierOptions.withMaxPointsAndTolerance constructor"
slug: "sdk-for-flutter-navigate-core-polylinesimplifieroptions-polylinesimplifieroptions-withmaxpointsandtolerance"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- PolylineSimplifierOptions.withMaxPointsAndTolerance.html -->


<div>
<h1>PolylineSimplifierOptions.withMaxPointsAndTolerance constructor</h1></div>

PolylineSimplifierOptions.withMaxPointsAndTolerance(<ol class="parameter-list single-line"> <li>int maxPoints, </li>
<li>int simplificationToleranceInMeters</li>
</ol>)
    

<p>Creates options with explicitly specified <a href="sdk-for-flutter-navigate-core-polylinesimplifieroptions-maxpoints">PolylineSimplifierOptions.maxPoints</a> and <a href="sdk-for-flutter-navigate-core-polylinesimplifieroptions-simplificationtoleranceinmeters">PolylineSimplifierOptions.simplificationToleranceInMeters</a>.</p>
<ul>
<li><code>maxPoints</code> Sets the upper limit on the resulting collection for
the <a href="sdk-for-flutter-navigate-core-polylinesimplifier-simplify">PolylineSimplifier.simplify</a>. Lower
value results in the lower accuracy of the resulting
polyline. If <code>maxPoints</code> is less than <code>2</code>
then resulting polyline will not have an upper limit
on the size and only <a href="sdk-for-flutter-navigate-core-polylinesimplifieroptions-simplificationtoleranceinmeters">PolylineSimplifierOptions.simplificationToleranceInMeters</a>
will be considered. When <code>maxPoints</code> is greater than
size of the passed polyline then simplification algorithm
will take into account only <a href="sdk-for-flutter-navigate-core-polylinesimplifieroptions-simplificationtoleranceinmeters">PolylineSimplifierOptions.simplificationToleranceInMeters</a>.</li>
<li><code>simplificationToleranceInMeters</code> Sets the accuracy limit for the <a href="sdk-for-flutter-navigate-core-polylinesimplifier-simplify">PolylineSimplifier.simplify</a>:</li>
<li>higher tolerance results in more simplification (fewer points);</li>
<li>lower tolerance keeps the line closer to its original shape.</li>
</ul>
<p>If removing a point produces polyline, which deviates from the
original one more than <code>simplificationToleranceInMeters</code>, then
this point is left in the collection.</p>
<p>If specified tolerance will not allow to create a polyline
conforming to <a href="sdk-for-flutter-navigate-core-polylinesimplifieroptions-maxpoints">PolylineSimplifierOptions.maxPoints</a>, then <code>simplificationToleranceInMeters</code>
is ignored.</p>
<p>Default value is equal to <a href="sdk-for-flutter-navigate-core-polylinesimplifieroptions-simplificationinmeters14zoomlevel">PolylineSimplifierOptions.simplificationInMeters14ZoomLevel</a>.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">PolylineSimplifierOptions.withMaxPointsAndTolerance(this.maxPoints, this.simplificationToleranceInMeters);</code></pre>

 



</div>
`
}</HTMLBlock>
