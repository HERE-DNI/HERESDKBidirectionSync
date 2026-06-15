---
title: "Isoline constructor"
slug: "sdk-for-flutter-explore-routing-isoline-isoline"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- Isoline.html -->


<div>
<h1>Isoline constructor</h1></div>

Isoline(<ol class="parameter-list"> <li><a href="sdk-for-flutter-explore-routing-isolinerangetype">IsolineRangeType</a> rangeType, </li>
<li>double rangeValue, </li>
<li><a href="sdk-for-flutter-explore-routing-mapmatchedcoordinates-class">MapMatchedCoordinates</a> center, </li>
<li>List&lt;<a href="sdk-for-flutter-explore-core-geopolygon-class">GeoPolygon</a>&gt; polygons, </li>
</ol>)
    

<p>Constructs an isoline instance.</p>
<p>This instance is provided by the
<a href="sdk-for-flutter-explore-routing-calculateisolinecallback">CalculateIsolineCallback</a>.</p>
<ul>
<li>
<p><code>rangeType</code> Specifies the range type of the provided <code>Isoline.Isoline().rangeValue</code> list.</p>
</li>
<li>
<p><code>rangeValue</code> A list of range values. At least one value must be set.</p>
</li>
<li>
<p><code>center</code> The center of the isoline.</p>
</li>
<li>
<p><code>polygons</code> A list of polygons that belong to this isoline. At least one value must be set.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory Isoline(IsolineRangeType rangeType, double rangeValue, MapMatchedCoordinates center, List&lt;GeoPolygon&gt; polygons) =&gt; $prototype.make(rangeType, rangeValue, center, polygons);</code></pre>

 



</div>
`
}</HTMLBlock>
