---
title: "forbiddenHazardousGoods property"
slug: "sdk-for-flutter-explore-routing-violatedrestrictiondetails-forbiddenhazardousgoods"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- forbiddenHazardousGoods.html -->


<div>
<h1>forbiddenHazardousGoods property</h1></div>

        
        List&lt;<a href="/sdk-for-flutter-explore-transport-hazardousmaterial">HazardousMaterial</a>&gt;
forbiddenHazardousGoods
<div class="features">getter/setter pair</div>


<p>There are two lists for our trip: Hazardous goods restrictions applied during the trip, and the list used
for the route calculation provided using <a href="/sdk-for-flutter-explore-transport-vehiclespecification-hazardousmaterials">VehicleSpecification.hazardousMaterials</a> from
<a href="/sdk-for-flutter-explore-transport-transportspecification-vehiclespecification">TransportSpecification.vehicleSpecification</a> from <a href="/sdk-for-flutter-explore-routing-routingoptions-transportspecification">RoutingOptions.transportSpecification</a>.
This property is the intersection of the two lists.</p>
<p><strong>Note</strong> <code>RoadSignWarning</code> events and <code>RouteViolations</code> are only given for violations that are
indicated on a road sign. Additional legal restrictions might apply when transporting hazardous materials.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;HazardousMaterial&gt; forbiddenHazardousGoods;</code></pre>

 



</div>
`
}</HTMLBlock>
