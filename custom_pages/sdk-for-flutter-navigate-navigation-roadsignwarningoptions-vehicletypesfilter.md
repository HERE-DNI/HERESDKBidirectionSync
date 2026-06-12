---
title: "vehicleTypesFilter property"
slug: "sdk-for-flutter-navigate-navigation-roadsignwarningoptions-vehicletypesfilter"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- vehicleTypesFilter.html -->


<div>
<h1>vehicleTypesFilter property</h1></div>

        
        List&lt;<a href="/sdk-for-flutter-navigate-navigation-roadsignvehicletype">RoadSignVehicleType</a>&gt;
vehicleTypesFilter
<div class="features">getter/setter pair</div>


<p>The list of road sign vehicle types for which a warning will be given. If the list is empty,
road signs are not filtered by vehicle type, which means that you get road sign warnings for all vehicle types.</p>
<p><strong>Example:</strong> For a filter that contains only bus and trucks you will only receive specific road sign warnings for
bus and trucks - you will not get signs for the other types, such as heavy trucks or motorhomes.
Furthermore, you will <em>not</em> get any signs that are generally applicable for all vehicles. For example,
you cannot set a filter that allows to get signs for trucks <em>and</em> cars. If you want to get signs for standard vehicles
like cars, then the only option is to set an empty list as filter.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;RoadSignVehicleType&gt; vehicleTypesFilter;</code></pre>

 



</div>
`
}</HTMLBlock>
