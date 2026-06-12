---
title: "weightPerAxleGroup property"
slug: "sdk-for-flutter-explore-transport-truckspecifications-weightperaxlegroup"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- weightPerAxleGroup.html -->


<div>
<h1>weightPerAxleGroup property</h1></div>

<a href="/sdk-for-flutter-explore-transport-weightperaxlegroup-class">WeightPerAxleGroup</a>?
        weightPerAxleGroup
<div class="features">getter/setter pair</div>


<p>Allows specification of axle weights in a more fine-grained way than <code>weight_per_axle_in_kilograms</code>.
This is relevant in countries with signs and regulations that specify different limits for different axle groups, like the USA and Sweden.
By default is not set.
<strong>Note:</strong> <code>weight_per_axle_in_kilograms</code> and <code>weight_per_axle_group</code> are incompatible.
When available for your edition, if both attributes are set, during online RoutingEngine an <code>sdk.routing.RoutingError.INVALID_PARAMETER</code> error is generated.
Otherwise, when offline RoutingEngine is in place, both parameters are evaluated and the maximum value between them will be used.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">WeightPerAxleGroup? weightPerAxleGroup;</code></pre>

 



</div>
`
}</HTMLBlock>
