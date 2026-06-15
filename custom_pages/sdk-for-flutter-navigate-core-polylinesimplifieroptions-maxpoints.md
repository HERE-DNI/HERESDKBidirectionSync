---
title: "maxPoints property"
slug: "sdk-for-flutter-navigate-core-polylinesimplifieroptions-maxpoints"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- maxPoints.html -->


<div>
<h1>maxPoints property</h1></div>

        
        int
        maxPoints
<div class="features">getter/setter pair</div>


<p>Sets the upper limit on the resulting collection for
the <a href="sdk-for-flutter-navigate-core-polylinesimplifier-simplify">PolylineSimplifier.simplify</a>. Lower
value results in the lower accuracy of the resulting
polyline. If <code>maxPoints</code> is less than <code>2</code>
then resulting polyline will not have an upper limit
on the size and only <a href="sdk-for-flutter-navigate-core-polylinesimplifieroptions-simplificationtoleranceinmeters">PolylineSimplifierOptions.simplificationToleranceInMeters</a>
will be considered. When <code>maxPoints</code> is greater than
size of the passed polyline then simplification algorithm
will take into account only <a href="sdk-for-flutter-navigate-core-polylinesimplifieroptions-simplificationtoleranceinmeters">PolylineSimplifierOptions.simplificationToleranceInMeters</a>.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">int maxPoints;</code></pre>

 



</div>
`
}</HTMLBlock>
