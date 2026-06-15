---
title: "weightPerAxleInKilograms property"
slug: "sdk-for-flutter-navigate-transport-truckspecifications-weightperaxleinkilograms"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- weightPerAxleInKilograms.html -->


<div>
<h1>weightPerAxleInKilograms property</h1></div>

        
        int?
        weightPerAxleInKilograms
<div class="features">getter/setter pair</div>


<p>Heaviest weight per axle, regardless of axle type or axle group.
It is evaluated against all axle weight restrictions, including single axle and tandem axle weight restrictions.
The provided value must be greater or equal to 0.
By default, it is not set.
<strong>Note:</strong> <code>weight_per_axle_in_kilograms</code> and <code>weight_per_axle_group</code> are incompatible.
When available for your edition, if both attributes are set, during online RoutingEngine an <code>sdk.routing.RoutingError.INVALID_PARAMETER</code> error is generated.
Otherwise, when offline RoutingEngine is in place, both parameters are evaluated and the maximum value between them will be used.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">int? weightPerAxleInKilograms;</code></pre>

 



</div>
`
}</HTMLBlock>
