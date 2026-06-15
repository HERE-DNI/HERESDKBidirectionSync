---
title: "avoidPolygonArea property"
slug: "sdk-for-flutter-explore-routing-avoidpolygonareaoptions-avoidpolygonarea"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- avoidPolygonArea.html -->


<div>
<h1>avoidPolygonArea property</h1></div>

<a href="sdk-for-flutter-explore-core-geopolygon-class">GeoPolygon</a>
avoidPolygonArea
<div class="features">getter/setter pair</div>


<p>Area of polygon shape which routes must not cross. Strictly enforced.
Violations are reported as <a href="sdk-for-flutter-explore-routing-sectionnoticecode">SectionNoticeCode.violatedBlockedRoad</a>.
<strong>Note:</strong> This avoidance option is not supported for <code>IsolineOptions</code>. If it is defined for isoline calculation then an <code>sdk.routing.RoutingError.INVALID_PARAMETER</code> error is generated.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">GeoPolygon avoidPolygonArea;</code></pre>

 



</div>
`
}</HTMLBlock>
