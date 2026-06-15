---
title: "GeoCorridor constructor"
slug: "sdk-for-flutter-explore-core-geocorridor-geocorridor"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- GeoCorridor.html -->


<div>
<h1>GeoCorridor constructor</h1></div>

GeoCorridor(<ol class="parameter-list single-line"> <li>List&lt;<a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a>&gt; polyline, </li>
<li>int halfWidthInMeters</li>
</ol>)
    

<p>Constructs a GeoCorridor from the provided polyline and half-width in meters.</p>
<ul>
<li>
<p><code>polyline</code> The polyline passing through the middle of the corridor.</p>
</li>
<li>
<p><code>halfWidthInMeters</code> The shortest distance from any point on the polyline to the border of the corridor.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory GeoCorridor(List&lt;GeoCoordinates&gt; polyline, int halfWidthInMeters) =&gt; $prototype.$init(polyline, halfWidthInMeters);</code></pre>

 



</div>
`
}</HTMLBlock>
