---
title: "PolylineSimplificationCallback typedef"
slug: "sdk-for-flutter-navigate-core-polylinesimplificationcallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- PolylineSimplificationCallback.html -->


<div>
<h1>PolylineSimplificationCallback typedef</h1></div>

PolylineSimplificationCallback =
     void Function(<a href="/sdk-for-flutter-navigate-core-polylinesimplificationerror">PolylineSimplificationError</a>? queryError, List&lt;<a href="/sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a>&gt;? result)


<p>The method will be called on the main thread when
<a href="/sdk-for-flutter-navigate-core-polylinesimplifier-simplify">PolylineSimplifier.simplify</a> is finished.</p>
<ul>
<li>
<p><code>queryError</code> The optional error, which occurred during
simplification.</p>
</li>
<li>
<p><code>result</code> The simplified polyline with number of
points less or equal to the input polyline
of <a href="/sdk-for-flutter-navigate-core-polylinesimplifier-simplify">PolylineSimplifier.simplify</a>.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">typedef PolylineSimplificationCallback = void Function(PolylineSimplificationError? queryError, List&lt;GeoCoordinates&gt;? result);</code></pre>

 



</div>
`
}</HTMLBlock>
