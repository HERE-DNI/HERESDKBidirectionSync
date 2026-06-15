---
title: "configureVehicleRestrictionFilter static method"
slug: "sdk-for-flutter-navigate-mapview-mapcontentsettings-configurevehiclerestrictionfilter"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- configureVehicleRestrictionFilter.html -->


<div>
<h1>configureVehicleRestrictionFilter static method</h1></div>

<div>
<ol class="annotation-list">
<li>@Deprecated("Will be removed in v4.28.0, use [MapContentSettings.configureVehicleRestrictionFilterWithTransportSpecification] instead.")</li>
</ol>
</div>
void
configureVehicleRestrictionFilter(<ol class="parameter-list"> <li><a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode</a> transportMode, </li>
<li><a class="deprecated" href="sdk-for-flutter-navigate-transport-truckspecifications-class">TruckSpecifications</a> truckSpecifications, </li>
<li>List&lt;<a href="sdk-for-flutter-navigate-transport-hazardousmaterial">HazardousMaterial</a>&gt;? hazardousMaterials, </li>
<li><a href="sdk-for-flutter-navigate-transport-tunnelcategory">TunnelCategory</a>? tunnelCategory, </li>
</ol>)

      

    

<p>Configure a filter for <a href="sdk-for-flutter-navigate-mapview-mapfeatures-vehiclerestrictions">MapFeatures.vehicleRestrictions</a> to show only the restrictions
matching the specified criteria when the feature is enabled.</p>
<h1 id="filtering-rules-for-truck-specifications">Filtering rules for truck specifications</h1>
<p>Only restrictions applicable to the supplied truck specifications will be shown.</p>
<p>Examples:</p>
<ul>
<li>If the height in <code>MapContentSettings.configureVehicleRestrictionFilter.truckSpecifications</code> is set to 200 cm, then height restrictions
with a height greater than 200 cm will not be displayed.</li>
<li>If the trailer count in <code>MapContentSettings.configureVehicleRestrictionFilter.truckSpecifications</code> is set to 2, then trailer
restrictions for a count greater than 2 will not be displayed.</li>
</ul>
<h1 id="filtering-rules-for-hazardous-materials">Filtering rules for hazardous materials</h1>
<p>Only restrictions applicable to specified hazardous materials will be shown.
If at least one hazardous material of any type is present in the list, all available
tunnel category restrictions will be displayed. In order to filter-out non-applicable
tunnel categories, a tunnel category, that applies to the vehicle, can be specified
additionally.</p>
<p>Examples:</p>
<ul>
<li>If the <code>MapContentSettings.configureVehicleRestrictionFilter.hazardousMaterials</code> contains <a href="sdk-for-flutter-navigate-transport-hazardousmaterial">HazardousMaterial.poison</a>
and <a href="sdk-for-flutter-navigate-transport-hazardousmaterial">HazardousMaterial.gas</a>, then only material restrictions
for poison and gas will be displayed.</li>
<li>If the <code>MapContentSettings.configureVehicleRestrictionFilter.hazardousMaterials</code> list is empty, then no material restrictions
will be shown.</li>
<li>If the <code>MapContentSettings.configureVehicleRestrictionFilter.hazardousMaterials</code> list is not supplied at all (is <code>null</code>), then
no material restrictions will be shown.</li>
<li>If the <code>MapContentSettings.configureVehicleRestrictionFilter.hazardousMaterials</code> contains at least one hazardous material of any
type and <code>MapContentSettings.configureVehicleRestrictionFilter.tunnelCategory</code> is <code>null</code>, then only corresponding material
restrictions will be displayed together with all available tunnel categories.</li>
</ul>
<h1 id="filtering-rules-for-tunnel-category">Filtering rules for tunnel category</h1>
<p>Tunnel categories are labeled and rated based on the level of restriction they provide.
The lowest level of restriction is <a href="sdk-for-flutter-navigate-transport-tunnelcategory">TunnelCategory.b</a>, the highest and most
restrictive one is <a href="sdk-for-flutter-navigate-transport-tunnelcategory">TunnelCategory.e</a>.</p>
<p>Specifying tunnel category means that:</p>
<ul>
<li>The truck carries goods which could cause only the additional dangerous effects
described in specified tunnel category and other categories below it with lower level
of restriction.</li>
<li>The truck does not carry goods that could cause the dangerous effects described in
tunnel categories above with higher restriction levels than the one specified.</li>
</ul>
<p>Tunnel categories are closely related to hazardous materials.</p>
<p>Since the type of hazardous material alone does not define the exact level of danger,
to ensure comprehensive coverage; the HERE SDK follows:</p>
<ul>
<li>If at least one hazardous material is specified but no <code>MapContentSettings.configureVehicleRestrictionFilter.tunnelCategory</code> is provided,
the SDK enables and displays <strong>all tunnel category restrictions</strong> to ensure that no relevant
restrictions are omitted.</li>
<li>If both hazardous materials and a <code>MapContentSettings.configureVehicleRestrictionFilter.tunnelCategory</code> are specified, the SDK
<strong>strictly follows the given tunnel category parameter</strong> and displays only the
applicable restrictions.</li>
</ul>
<p>Example:
If <code>MapContentSettings.configureVehicleRestrictionFilter.tunnelCategory</code> is set to <a href="sdk-for-flutter-navigate-transport-tunnelcategory">TunnelCategory.d</a>, then restrictions for
tunnel category <a href="sdk-for-flutter-navigate-transport-tunnelcategory">TunnelCategory.e</a> and <a href="sdk-for-flutter-navigate-transport-tunnelcategory">TunnelCategory.d</a>
will be displayed, but not the categories <a href="sdk-for-flutter-navigate-transport-tunnelcategory">TunnelCategory.b</a> and
<a href="sdk-for-flutter-navigate-transport-tunnelcategory">TunnelCategory.c</a>.</p>
<ul>
<li>
<p><code>transportMode</code> Specifies the current transport type. Currently, it's used to distinguish
between truck and other transport modes. This distinction ensures consistency
between the routing logic and the information displayed on the map.
At present, this is primarily used to suppress the generic truck restriction icon.</p>
</li>
<li>
<p><code>truckSpecifications</code> The size, weight, type and trailer count specifications to filter for, so that only
restrictions which are relevant for the given specifications are displayed.</p>
</li>
<li>
<p><code>hazardousMaterials</code> The hazardous materials to filter for, so that only applicable restrictions are
displayed. When the list is <code>null</code> or empty, then no material restrictions
will be displayed.</p>
</li>
<li>
<p><code>tunnelCategory</code> The tunnel category to filter for, so that only applicable restrictions are
displayed. If <code>null</code>, then no tunnel category restrictions will be
displayed.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">@Deprecated("Will be removed in v4.28.0, use [MapContentSettings.configureVehicleRestrictionFilterWithTransportSpecification] instead.")

static void configureVehicleRestrictionFilter(TransportMode transportMode, TruckSpecifications truckSpecifications, List&lt;HazardousMaterial&gt;? hazardousMaterials, TunnelCategory? tunnelCategory) =&gt; $prototype.configureVehicleRestrictionFilter(transportMode, truckSpecifications, hazardousMaterials, tunnelCategory);</code></pre>

 



</div>
`
}</HTMLBlock>
