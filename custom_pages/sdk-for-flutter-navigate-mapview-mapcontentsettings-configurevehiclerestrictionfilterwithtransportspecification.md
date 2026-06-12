---
title: "configureVehicleRestrictionFilterWithTransportSpecification static method"
slug: "sdk-for-flutter-navigate-mapview-mapcontentsettings-configurevehiclerestrictionfilterwithtransportspecification"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- configureVehicleRestrictionFilterWithTransportSpecification.html -->


<div>
<h1>configureVehicleRestrictionFilterWithTransportSpecification static method</h1></div>

void
configureVehicleRestrictionFilterWithTransportSpecification(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-transport-transportspecification-class">TransportSpecification</a> transportSpecs</li>
</ol>)

      

    

<p>Configures a filter for <a href="/sdk-for-flutter-navigate-mapview-mapfeatures-vehiclerestrictions">MapFeatures.vehicleRestrictions</a> to show only the restrictions
matching the transport specifications when the feature is enabled.</p>
<p>This method provides a unified way to configure vehicle restriction filters using
a single <a href="/sdk-for-flutter-navigate-transport-transportspecification-class">TransportSpecification</a> parameter. This allows you to use the same
transport configuration for both routing and map rendering, ensuring consistency between
route calculation and the restrictions displayed on the map.</p>
<p>The method extracts the transport mode, vehicle specifications, hazardous materials, and
tunnel category from the <code>MapContentSettings.configureVehicleRestrictionFilterWithTransportSpecification.transportSpecs</code> parameter and applies filtering according to
the same rules described below.</p>
<h1 id="filtering-rules-for-transport-mode">Filtering rules for transport mode</h1>
<p>The transport mode is used to distinguish between truck and other transport modes.
This distinction ensures consistency between the routing logic and the information
displayed on the map. At present, this is primarily used to suppress the generic
truck restriction icon for non-truck modes.</p>
<p>Currently, only vehicle-related restrictions are supported. For pedestrian, scooter,
or taxi transport modes, the transport mode information is used, but no additional
vehicle-specific restrictions are applied.</p>
<h1 id="filtering-rules-for-vehicle-specifications">Filtering rules for vehicle specifications</h1>
<p>Only restrictions applicable to the vehicle specifications will be shown.
The vehicle specifications include dimensions (height, width, length), weights
(gross weight, weight per axle), and trailer count.</p>
<p>Examples:</p>
<ul>
<li>If the height in vehicle specifications is set to 200 cm, then height restrictions
with a height greater than 200 cm will not be displayed.</li>
<li>If the trailer count in vehicle specifications is set to 2, then trailer
restrictions for a count greater than 2 will not be displayed.</li>
</ul>
<h1 id="filtering-rules-for-hazardous-materials">Filtering rules for hazardous materials</h1>
<p>Only restrictions applicable to specified hazardous materials will be shown.
Hazardous materials are specified within the <a href="/sdk-for-flutter-navigate-transport-vehiclespecification-class">VehicleSpecification</a>
contained in the <code>MapContentSettings.configureVehicleRestrictionFilterWithTransportSpecification.transportSpecs</code> parameter.</p>
<p>If at least one hazardous material of any type is present in the list, all available
tunnel category restrictions will be displayed. In order to filter-out non-applicable
tunnel categories, a tunnel category that applies to the vehicle can be specified
additionally.</p>
<p>Examples:</p>
<ul>
<li>If the hazardous materials list contains <a href="/sdk-for-flutter-navigate-transport-hazardousmaterial">HazardousMaterial.poison</a>
and <a href="/sdk-for-flutter-navigate-transport-hazardousmaterial">HazardousMaterial.gas</a>, then only material restrictions
for poison and gas will be displayed.</li>
<li>If the hazardous materials list is empty, then no material restrictions
will be shown.</li>
<li>If the hazardous materials list is not supplied at all (is <code>null</code>), then
no material restrictions will be shown.</li>
<li>If the hazardous materials list contains at least one hazardous material of any
type and tunnel category is <code>null</code>, then only corresponding material
restrictions will be displayed together with all available tunnel categories.</li>
</ul>
<h1 id="filtering-rules-for-tunnel-category">Filtering rules for tunnel category</h1>
<p>Tunnel categories are labeled and rated based on the level of restriction they provide.
The lowest level of restriction is <a href="/sdk-for-flutter-navigate-transport-tunnelcategory">TunnelCategory.b</a>, the highest and most
restrictive one is <a href="/sdk-for-flutter-navigate-transport-tunnelcategory">TunnelCategory.e</a>.</p>
<p>The tunnel category is specified within the <a href="/sdk-for-flutter-navigate-transport-vehiclespecification-class">VehicleSpecification</a>
contained in the <code>MapContentSettings.configureVehicleRestrictionFilterWithTransportSpecification.transportSpecs</code> parameter.</p>
<p>Specifying tunnel category means that:</p>
<ul>
<li>The vehicle carries goods which could cause only the additional dangerous effects
described in specified tunnel category and other categories below it with lower level
of restriction.</li>
<li>The vehicle does not carry goods that could cause the dangerous effects described in
tunnel categories above with higher restriction levels than the one specified.</li>
</ul>
<p>Tunnel categories are closely related to hazardous materials.</p>
<p>Since the type of hazardous material alone does not define the exact level of danger,
to ensure comprehensive coverage; the HERE SDK follows:</p>
<ul>
<li>If at least one hazardous material is specified but no tunnel category is provided,
the SDK enables and displays <strong>all tunnel category restrictions</strong> to ensure that no relevant
restrictions are omitted.</li>
<li>If both hazardous materials and a tunnel category are specified, the SDK
<strong>strictly follows the given tunnel category parameter</strong> and displays only the
applicable restrictions.</li>
</ul>
<p>Example:
If tunnel category is set to <a href="/sdk-for-flutter-navigate-transport-tunnelcategory">TunnelCategory.d</a>, then restrictions for
tunnel category <a href="/sdk-for-flutter-navigate-transport-tunnelcategory">TunnelCategory.e</a> and <a href="/sdk-for-flutter-navigate-transport-tunnelcategory">TunnelCategory.d</a>
will be displayed, but not the categories <a href="/sdk-for-flutter-navigate-transport-tunnelcategory">TunnelCategory.b</a> and
<a href="/sdk-for-flutter-navigate-transport-tunnelcategory">TunnelCategory.c</a>.</p>
<ul>
<li><code>transportSpecs</code> The transport specification containing the transport mode and vehicle specifications.
For vehicle modes (car, truck, bus), the <a href="/sdk-for-flutter-navigate-transport-vehiclespecification-class">VehicleSpecification</a> within
this parameter provides dimensions, weights, hazardous materials, and tunnel category
information used for filtering. The same <a href="/sdk-for-flutter-navigate-transport-transportspecification-class">TransportSpecification</a> object
can be used for both routing configuration and map rendering to ensure consistency.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static void configureVehicleRestrictionFilterWithTransportSpecification(TransportSpecification transportSpecs) =&gt; $prototype.configureVehicleRestrictionFilterWithTransportSpecification(transportSpecs);</code></pre>

 



</div>
`
}</HTMLBlock>
