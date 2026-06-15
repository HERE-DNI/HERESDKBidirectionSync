---
title: "withGeometry abstract method"
slug: "sdk-for-flutter-explore-mapview-datasource-polygondatabuilder-withgeometry"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- withGeometry.html -->


<div>
<h1>withGeometry abstract method</h1></div>

<a href="sdk-for-flutter-explore-mapview-datasource-polygondatabuilder-class">PolygonDataBuilder</a>
withGeometry(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-explore-core-geopolygon-class">GeoPolygon</a> geometry</li>
</ol>)

      

    

<p>Configures the builder with geometry for the polygon to be created.</p>
<ul>
<li><code>geometry</code> Geometry of the polygon.
The outer boundary has to be ordered clockwise and closed.
Any inner boundary has to be ordered counterclockwise and closed.
Altitude of boundary vertices is ignored.
The visual behaviour for self-intersecting outer boundary is undefined.</li>
</ul>
<p>Returns <a href="sdk-for-flutter-explore-mapview-datasource-polygondatabuilder-class">PolygonDataBuilder</a>. The builder.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">PolygonDataBuilder withGeometry(GeoPolygon geometry);</code></pre>

 



</div>
`
}</HTMLBlock>
