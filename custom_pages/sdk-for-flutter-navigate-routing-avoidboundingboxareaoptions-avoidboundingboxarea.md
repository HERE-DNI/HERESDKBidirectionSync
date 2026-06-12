---
title: "avoidBoundingBoxArea property"
slug: "sdk-for-flutter-navigate-routing-avoidboundingboxareaoptions-avoidboundingboxarea"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- avoidBoundingBoxArea.html -->


<div>
<h1>avoidBoundingBoxArea property</h1></div>

<a href="/sdk-for-flutter-navigate-core-geobox-class">GeoBox</a>
avoidBoundingBoxArea
<div class="features">getter/setter pair</div>


<p>Area of rectangular shape which routes must not cross. Strictly enforced.
<strong>Note:</strong>
Violations are reported as <code>sdk.routing.SectionNoticeCode.VIOLATED_BLOCKED_ROAD</code>.
This avoidance option is not supported for <code>IsolineOptions</code>. If it is defined for isoline calculation then an <code>sdk.routing.RoutingError.INVALID_PARAMETER</code> error is generated.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">GeoBox avoidBoundingBoxArea;</code></pre>

 



</div>
`
}</HTMLBlock>
