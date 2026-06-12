---
title: "setGeometry abstract method"
slug: "sdk-for-flutter-navigate-mapview-datasource-polygondataaccessor-setgeometry"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setGeometry.html -->


<div>
<h1>setGeometry abstract method</h1></div>

void
setGeometry(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-core-geopolygon-class">GeoPolygon</a> geometry</li>
</ol>)

      

    

<p>Replaces polygon geometry.</p>
<p>The outer boundary has to be ordered clockwise and closed.</p>
<p>Altitude of the vertices is ignored.</p>
<p>The visual behaviour for self-intersecting outer boundary is undefined.</p>
<ul>
<li><code>geometry</code> Geometry of the polygon. The outer boundary has to be ordered clockwise and closed.
Altitude of the vertices is ignored.
The visual behaviour for self-intersecting outer boundary is undefined.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void setGeometry(GeoPolygon geometry);</code></pre>

 



</div>
`
}</HTMLBlock>
