---
title: "MapPolyline.withRepresentation constructor"
slug: "sdk-for-flutter-navigate-mapview-mappolyline-mappolyline-withrepresentation"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapPolyline.withRepresentation.html -->


<div>
<h1>MapPolyline.withRepresentation constructor</h1></div>

MapPolyline.withRepresentation(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-core-geopolyline-class">GeoPolyline</a> geometry, </li>
<li><a href="/sdk-for-flutter-navigate-mapview-mappolylinerepresentation-class">MapPolylineRepresentation</a> representation</li>
</ol>)
    

<p>Creates a new <code>MapPolyline</code> instance with a specified visual representation.</p>
<p>Altitude component of <code>GeoPolyline</code>'s vertices is ignored.</p>
<p>After creating a <code>MapPolyline</code> with this representation, the deprecated <code>MapPolyline</code>
properties do not work and any change to them will be ignored. Any modifications to polyline's
appearance must be done with <a href="/sdk-for-flutter-navigate-mapview-mappolyline-setrepresentation">MapPolyline.setRepresentation</a>.</p>
<ul>
<li>
<p><code>geometry</code> The list of vertices representing the polyline.</p>
</li>
<li>
<p><code>representation</code> The styling properties of the polyline.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory MapPolyline.withRepresentation(GeoPolyline geometry, MapPolylineRepresentation representation) =&gt; $prototype.withRepresentation(geometry, representation);</code></pre>

 



</div>
`
}</HTMLBlock>
