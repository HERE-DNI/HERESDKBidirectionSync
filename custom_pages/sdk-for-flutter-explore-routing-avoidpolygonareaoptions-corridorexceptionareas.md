---
title: "corridorExceptionAreas property"
slug: "sdk-for-flutter-explore-routing-avoidpolygonareaoptions-corridorexceptionareas"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- corridorExceptionAreas.html -->


<div>
<h1>corridorExceptionAreas property</h1></div>

        
        List&lt;<a href="sdk-for-flutter-explore-core-geocorridor-class">GeoCorridor</a>&gt;
corridorExceptionAreas
<div class="features">getter/setter pair</div>


<p>Areas of corridor shape to exclude from avoidance.
<strong>Note:</strong>
Even though <code>GeoCorridor.half_width_in_meters</code> is an optional property in case of exception areas it is mandatory.
Otherwise route calculation will fail with an <code>sdk.routing.RoutingError.INVALID_PARAMETER</code> error.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;GeoCorridor&gt; corridorExceptionAreas;</code></pre>

 



</div>
`
}</HTMLBlock>
