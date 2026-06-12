---
title: "GeoPolygon.withInnerBoundaries constructor"
slug: "sdk-for-flutter-explore-core-geopolygon-geopolygon-withinnerboundaries"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- GeoPolygon.withInnerBoundaries.html -->


<div>
<h1>GeoPolygon.withInnerBoundaries constructor</h1></div>

GeoPolygon.withInnerBoundaries(<ol class="parameter-list single-line"> <li>List&lt;<a href="/sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a>&gt; vertices, </li>
<li>List&lt;List&lt;<a href="/sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a>&gt;&gt; innerBoundaries</li>
</ol>)
    

<p>Constructs an instance of this class from the provided vertices and inner boundaries (holes).</p>
<p>Throws InstantiationError if the number of vertices is less than three.</p>
<ul>
<li>
<p><code>vertices</code> List of vertices representing the polygon outer boundary in clockwise order.</p>
</li>
<li>
<p><code>innerBoundaries</code> List of polygon inner boundaries (holes), each in counterclockwise order.</p>
</li>
</ul>
<p>Throws <a href="/sdk-for-flutter-explore-core-errors-instantiationexception-class">InstantiationException</a>. Instantiation error.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory GeoPolygon.withInnerBoundaries(List&lt;GeoCoordinates&gt; vertices, List&lt;List&lt;GeoCoordinates&gt;&gt; innerBoundaries) =&gt; $prototype.withInnerBoundaries(vertices, innerBoundaries);</code></pre>

 



</div>
`
}</HTMLBlock>
