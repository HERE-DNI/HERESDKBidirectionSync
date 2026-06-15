---
title: "simplify abstract method"
slug: "sdk-for-flutter-navigate-core-polylinesimplifier-simplify"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- simplify.html -->


<div>
<h1>simplify abstract method</h1></div>

<a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>
simplify(<ol class="parameter-list single-line"> <li>List&lt;<a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a>&gt; polyline, </li>
<li><a href="sdk-for-flutter-navigate-core-polylinesimplifieroptions-class">PolylineSimplifierOptions</a> simplificationParameters, </li>
<li><a href="sdk-for-flutter-navigate-core-polylinesimplificationcallback">PolylineSimplificationCallback</a> callback</li>
</ol>)

      

    

<p>Reduces the number of points in the input polyline.</p>
<p>Does this by removing points which are not significant
according to the passed <a href="sdk-for-flutter-navigate-core-polylinesimplifieroptions-class">PolylineSimplifierOptions</a>.
Simplification process is performed on the device without
connecting to the network and is computationally intensive.</p>
<ul>
<li>
<p><code>polyline</code> Input polyline that should be reduced in size.</p>
</li>
<li>
<p><code>simplificationParameters</code> Strategy, that controls the behavior of the underlying algorithm.</p>
</li>
<li>
<p><code>callback</code> Callback, which will be invoked on the main thread,
when operation is finished.</p>
</li>
</ul>
<p>Returns <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Controls an asynchronous operation.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle simplify(List&lt;GeoCoordinates&gt; polyline, PolylineSimplifierOptions simplificationParameters, PolylineSimplificationCallback callback);</code></pre>

 



</div>
`
}</HTMLBlock>
