---
title: "withGeometry abstract method"
slug: "sdk-for-flutter-explore-mapview-datasource-linedatabuilder-withgeometry"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- withGeometry.html -->


<div>
<h1>withGeometry abstract method</h1></div>

<a href="sdk-for-flutter-explore-mapview-datasource-linedatabuilder-class">LineDataBuilder</a>
withGeometry(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-explore-core-geopolyline-class">GeoPolyline</a> geometry</li>
</ol>)

      

    

<p>Configures the builder with geometry for line to be created.</p>
<ul>
<li><code>geometry</code> Geometry of the polyline. Each vertex defines two line segments: one
with a previous vertex and one with a next vertex. First and last vertices don't have
resp. previous and next vertices and thus belong to single line segments.
Consecutive duplicate vertices are ignored.
Altitude of polyline vertices is ignored.</li>
</ul>
<p>Returns <a href="sdk-for-flutter-explore-mapview-datasource-linedatabuilder-class">LineDataBuilder</a>. The builder.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">LineDataBuilder withGeometry(GeoPolyline geometry);</code></pre>

 



</div>
`
}</HTMLBlock>
