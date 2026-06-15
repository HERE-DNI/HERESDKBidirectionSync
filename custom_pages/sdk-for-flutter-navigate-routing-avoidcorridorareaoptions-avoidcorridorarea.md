---
title: "avoidCorridorArea property"
slug: "sdk-for-flutter-navigate-routing-avoidcorridorareaoptions-avoidcorridorarea"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- avoidCorridorArea.html -->


<div>
<h1>avoidCorridorArea property</h1></div>

<a href="sdk-for-flutter-navigate-core-geocorridor-class">GeoCorridor</a>
avoidCorridorArea
<div class="features">getter/setter pair</div>


<p>Area of corridor shape which routes must not cross. Strictly enforced.
Violations are reported as <a href="sdk-for-flutter-navigate-routing-sectionnoticecode">SectionNoticeCode.violatedBlockedRoad</a>.
<strong>Note:</strong>
This avoidance option is not supported for <code>IsolineOptions</code>. If it is defined for isoline calculation then an <code>sdk.routing.RoutingError.INVALID_PARAMETER</code> error is generated.
Even though <code>GeoCorridor.half_width_in_meters</code> is an optional property in case of exception areas it is mandatory.
Otherwise route calculation will fail with an <code>sdk.routing.RoutingError.INVALID_PARAMETER</code> error.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">GeoCorridor avoidCorridorArea;</code></pre>

 



</div>
`
}</HTMLBlock>
