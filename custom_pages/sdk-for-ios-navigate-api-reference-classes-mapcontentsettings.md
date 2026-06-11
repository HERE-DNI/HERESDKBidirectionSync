---
title: "sdk-for-ios-navigate-api-reference-classes-mapcontentsettings"
slug: "sdk-for-ios-navigate-api-reference-classes-mapcontentsettings"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapContentSettings"></a>
<a title="MapContentSettings Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-maps">Maps</a>
<img alt="" id="carat" src="/carat.png"/>
        MapContentSettings Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>MapContentSettings</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapContentSettings</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapContentSettings</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapContentSettings</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Provides settings regarding map data which are applied globally to all map views. The settings
can already be changed before a map view instance is created.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18MapContentSettingsC25TrafficRefreshPeriodErrora"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/TrafficRefreshPeriodError"></a>
<a class="token" href="#/s:7heresdk18MapContentSettingsC25TrafficRefreshPeriodErrora">TrafficRefreshPeriodError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Traffic refresh period error exception</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">TrafficRefreshPeriodError</span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapcontentsettings-trafficrefreshperioderrorcode">TrafficRefreshPeriodErrorCode</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18MapContentSettingsC29TrafficRefreshPeriodErrorCodeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/TrafficRefreshPeriodErrorCode"></a>
<a class="token" href="#/s:7heresdk18MapContentSettingsC29TrafficRefreshPeriodErrorCodeO">TrafficRefreshPeriodErrorCode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Traffic refresh period error code</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-classes-mapcontentsettings-trafficrefreshperioderrorcode">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">TrafficRefreshPeriodErrorCode</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapcontentsettings">MapContentSettings</a></span><span class="o">.</span><span class="kt">TrafficRefreshPeriodErrorCode</span> <span class="p">:</span> <span class="kt">Error</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18MapContentSettingsC33configureVehicleRestrictionFilter13transportMode19truckSpecifications18hazardousMaterials14tunnelCategoryyAA09TransportJ0O_AA05TruckL0VSayAA17HazardousMaterialOGSgAA06TunnelP0OSgtFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/configureVehicleRestrictionFilter(transportMode:truckSpecifications:hazardousMaterials:tunnelCategory:)"></a>
<a class="token" href="#/s:7heresdk18MapContentSettingsC33configureVehicleRestrictionFilter13transportMode19truckSpecifications18hazardousMaterials14tunnelCategoryyAA09TransportJ0O_AA05TruckL0VSayAA17HazardousMaterialOGSgAA06TunnelP0OSgtFZ">configureVehicleRestrictionFilter(transportMode:<wbr/>truckSpecifications:<wbr/>hazardousMaterials:<wbr/>tunnelCategory:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Configure a filter for <code><a href="../Structs/MapFeatures.html#/s:7heresdk11MapFeaturesV19vehicleRestrictionsSSvpZ">MapFeatures.vehicleRestrictions</a></code> to show only the restrictions
matching the specified criteria when the feature is enabled.</p>
<h1 class="heading" id="filtering-rules-for-truck-specifications">Filtering rules for truck specifications</h1>
<p>Only restrictions applicable to the supplied truck specifications will be shown.</p>
<p>Examples:</p>
<ul>
<li>If the height in <code>MapContentSettings.configureVehicleRestrictionFilter(TransportMode, TruckSpecifications, [HazardousMaterial]?, TunnelCategory?).truckSpecifications</code> is set to 200 cm, then height restrictions
with a height greater than 200 cm will not be displayed.</li>
<li>If the trailer count in <code>MapContentSettings.configureVehicleRestrictionFilter(TransportMode, TruckSpecifications, [HazardousMaterial]?, TunnelCategory?).truckSpecifications</code> is set to 2, then trailer
restrictions for a count greater than 2 will not be displayed.</li>
</ul>
<h1 class="heading" id="filtering-rules-for-hazardous-materials">Filtering rules for hazardous materials</h1>
<p>Only restrictions applicable to specified hazardous materials will be shown.
If at least one hazardous material of any type is present in the list, all available
tunnel category restrictions will be displayed. In order to filter-out non-applicable
tunnel categories, a tunnel category, that applies to the vehicle, can be specified
additionally.</p>
<p>Examples:</p>
<ul>
<li>If the <code>MapContentSettings.configureVehicleRestrictionFilter(TransportMode, TruckSpecifications, [HazardousMaterial]?, TunnelCategory?).hazardousMaterials</code> contains <code><a href="../Enums/HazardousMaterial.html#/s:7heresdk17HazardousMaterialO6poisonyA2CmF">HazardousMaterial.poison</a></code>
and <code><a href="../Enums/HazardousMaterial.html#/s:7heresdk17HazardousMaterialO3gasyA2CmF">HazardousMaterial.gas</a></code>, then only material restrictions
for poison and gas will be displayed.</li>
<li>If the <code>MapContentSettings.configureVehicleRestrictionFilter(TransportMode, TruckSpecifications, [HazardousMaterial]?, TunnelCategory?).hazardousMaterials</code> list is empty, then no material restrictions
will be shown.</li>
<li>If the <code>MapContentSettings.configureVehicleRestrictionFilter(TransportMode, TruckSpecifications, [HazardousMaterial]?, TunnelCategory?).hazardousMaterials</code> list is not supplied at all (is <code>nil</code>), then
no material restrictions will be shown.</li>
<li>If the <code>MapContentSettings.configureVehicleRestrictionFilter(TransportMode, TruckSpecifications, [HazardousMaterial]?, TunnelCategory?).hazardousMaterials</code> contains at least one hazardous material of any
type and <code>MapContentSettings.configureVehicleRestrictionFilter(TransportMode, TruckSpecifications, [HazardousMaterial]?, TunnelCategory?).tunnelCategory</code> is <code>nil</code>, then only corresponding material
restrictions will be displayed together with all available tunnel categories.</li>
</ul>
<h1 class="heading" id="filtering-rules-for-tunnel-category">Filtering rules for tunnel category</h1>
<p>Tunnel categories are labeled and rated based on the level of restriction they provide.
The lowest level of restriction is <code><a href="../Enums/TunnelCategory.html#/s:7heresdk14TunnelCategoryO1byA2CmF">TunnelCategory.b</a></code>, the highest and most
restrictive one is <code><a href="../Enums/TunnelCategory.html#/s:7heresdk14TunnelCategoryO1eyA2CmF">TunnelCategory.e</a></code>.</p>
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
<li>If at least one hazardous material is specified but no <code>MapContentSettings.configureVehicleRestrictionFilter(TransportMode, TruckSpecifications, [HazardousMaterial]?, TunnelCategory?).tunnelCategory</code> is provided,
the SDK enables and displays <strong>all tunnel category restrictions</strong> to ensure that no relevant
restrictions are omitted.</li>
<li>If both hazardous materials and a <code>MapContentSettings.configureVehicleRestrictionFilter(TransportMode, TruckSpecifications, [HazardousMaterial]?, TunnelCategory?).tunnelCategory</code> are specified, the SDK
<strong>strictly follows the given tunnel category parameter</strong> and displays only the
applicable restrictions.</li>
</ul>
<p>Example:
If <code>MapContentSettings.configureVehicleRestrictionFilter(TransportMode, TruckSpecifications, [HazardousMaterial]?, TunnelCategory?).tunnelCategory</code> is set to <code><a href="../Enums/TunnelCategory.html#/s:7heresdk14TunnelCategoryO1dyA2CmF">TunnelCategory.d</a></code>, then restrictions for
tunnel category <code><a href="../Enums/TunnelCategory.html#/s:7heresdk14TunnelCategoryO1eyA2CmF">TunnelCategory.e</a></code> and <code><a href="../Enums/TunnelCategory.html#/s:7heresdk14TunnelCategoryO1dyA2CmF">TunnelCategory.d</a></code>
will be displayed, but not the categories <code><a href="../Enums/TunnelCategory.html#/s:7heresdk14TunnelCategoryO1byA2CmF">TunnelCategory.b</a></code> and
<code><a href="../Enums/TunnelCategory.html#/s:7heresdk14TunnelCategoryO1cyA2CmF">TunnelCategory.c</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0, use MapContentSettings.configureVehicleRestrictionFilter(TransportSpecification﹚ instead.")</span>
<span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">configureVehicleRestrictionFilter</span><span class="p">(</span><span class="nv">transportMode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-transportmode">TransportMode</a></span><span class="p">,</span> <span class="nv">truckSpecifications</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-truckspecifications">TruckSpecifications</a></span><span class="p">,</span> <span class="nv">hazardousMaterials</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-hazardousmaterial">HazardousMaterial</a></span><span class="p">]?,</span> <span class="nv">tunnelCategory</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-tunnelcategory">TunnelCategory</a></span><span class="p">?)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>transportMode</em>
</code>
</td>
<td>
<div>
<p>Specifies the current transport type. Currently, it’s used to distinguish
between truck and other transport modes. This distinction ensures consistency
between the routing logic and the information displayed on the map.
At present, this is primarily used to suppress the generic truck restriction icon.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>truckSpecifications</em>
</code>
</td>
<td>
<div>
<p>The size, weight, type and trailer count specifications to filter for, so that only
restrictions which are relevant for the given specifications are displayed.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>hazardousMaterials</em>
</code>
</td>
<td>
<div>
<p>The hazardous materials to filter for, so that only applicable restrictions are
displayed. When the list is <code>nil</code> or empty, then no material restrictions
will be displayed.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>tunnelCategory</em>
</code>
</td>
<td>
<div>
<p>The tunnel category to filter for, so that only applicable restrictions are
displayed. If <code>nil</code>, then no tunnel category restrictions will be
displayed.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18MapContentSettingsC33configureVehicleRestrictionFilter14transportSpecsyAA22TransportSpecificationV_tFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/configureVehicleRestrictionFilter(transportSpecs:)"></a>
<a class="token" href="#/s:7heresdk18MapContentSettingsC33configureVehicleRestrictionFilter14transportSpecsyAA22TransportSpecificationV_tFZ">configureVehicleRestrictionFilter(transportSpecs:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Configures a filter for <code><a href="../Structs/MapFeatures.html#/s:7heresdk11MapFeaturesV19vehicleRestrictionsSSvpZ">MapFeatures.vehicleRestrictions</a></code> to show only the restrictions
matching the transport specifications when the feature is enabled.</p>
<p>This method provides a unified way to configure vehicle restriction filters using
a single <code><a href="sdk-for-ios-navigate-api-reference-structs-transportspecification">TransportSpecification</a></code> parameter. This allows you to use the same
transport configuration for both routing and map rendering, ensuring consistency between
route calculation and the restrictions displayed on the map.</p>
<p>The method extracts the transport mode, vehicle specifications, hazardous materials, and
tunnel category from the <code>MapContentSettings.configureVehicleRestrictionFilter(TransportSpecification).transportSpecs</code> parameter and applies filtering according to
the same rules described below.</p>
<h1 class="heading" id="filtering-rules-for-transport-mode">Filtering rules for transport mode</h1>
<p>The transport mode is used to distinguish between truck and other transport modes.
This distinction ensures consistency between the routing logic and the information
displayed on the map. At present, this is primarily used to suppress the generic
truck restriction icon for non-truck modes.</p>
<p>Currently, only vehicle-related restrictions are supported. For pedestrian, scooter,
or taxi transport modes, the transport mode information is used, but no additional
vehicle-specific restrictions are applied.</p>
<h1 class="heading" id="filtering-rules-for-vehicle-specifications">Filtering rules for vehicle specifications</h1>
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
<h1 class="heading" id="filtering-rules-for-hazardous-materials">Filtering rules for hazardous materials</h1>
<p>Only restrictions applicable to specified hazardous materials will be shown.
Hazardous materials are specified within the <code><a href="sdk-for-ios-navigate-api-reference-structs-vehiclespecification">VehicleSpecification</a></code>
contained in the <code>MapContentSettings.configureVehicleRestrictionFilter(TransportSpecification).transportSpecs</code> parameter.</p>
<p>If at least one hazardous material of any type is present in the list, all available
tunnel category restrictions will be displayed. In order to filter-out non-applicable
tunnel categories, a tunnel category that applies to the vehicle can be specified
additionally.</p>
<p>Examples:</p>
<ul>
<li>If the hazardous materials list contains <code><a href="../Enums/HazardousMaterial.html#/s:7heresdk17HazardousMaterialO6poisonyA2CmF">HazardousMaterial.poison</a></code>
and <code><a href="../Enums/HazardousMaterial.html#/s:7heresdk17HazardousMaterialO3gasyA2CmF">HazardousMaterial.gas</a></code>, then only material restrictions
for poison and gas will be displayed.</li>
<li>If the hazardous materials list is empty, then no material restrictions
will be shown.</li>
<li>If the hazardous materials list is not supplied at all (is <code>nil</code>), then
no material restrictions will be shown.</li>
<li>If the hazardous materials list contains at least one hazardous material of any
type and tunnel category is <code>nil</code>, then only corresponding material
restrictions will be displayed together with all available tunnel categories.</li>
</ul>
<h1 class="heading" id="filtering-rules-for-tunnel-category">Filtering rules for tunnel category</h1>
<p>Tunnel categories are labeled and rated based on the level of restriction they provide.
The lowest level of restriction is <code><a href="../Enums/TunnelCategory.html#/s:7heresdk14TunnelCategoryO1byA2CmF">TunnelCategory.b</a></code>, the highest and most
restrictive one is <code><a href="../Enums/TunnelCategory.html#/s:7heresdk14TunnelCategoryO1eyA2CmF">TunnelCategory.e</a></code>.</p>
<p>The tunnel category is specified within the <code><a href="sdk-for-ios-navigate-api-reference-structs-vehiclespecification">VehicleSpecification</a></code>
contained in the <code>MapContentSettings.configureVehicleRestrictionFilter(TransportSpecification).transportSpecs</code> parameter.</p>
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
If tunnel category is set to <code><a href="../Enums/TunnelCategory.html#/s:7heresdk14TunnelCategoryO1dyA2CmF">TunnelCategory.d</a></code>, then restrictions for
tunnel category <code><a href="../Enums/TunnelCategory.html#/s:7heresdk14TunnelCategoryO1eyA2CmF">TunnelCategory.e</a></code> and <code><a href="../Enums/TunnelCategory.html#/s:7heresdk14TunnelCategoryO1dyA2CmF">TunnelCategory.d</a></code>
will be displayed, but not the categories <code><a href="../Enums/TunnelCategory.html#/s:7heresdk14TunnelCategoryO1byA2CmF">TunnelCategory.b</a></code> and
<code><a href="../Enums/TunnelCategory.html#/s:7heresdk14TunnelCategoryO1cyA2CmF">TunnelCategory.c</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">configureVehicleRestrictionFilter</span><span class="p">(</span><span class="nv">transportSpecs</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-transportspecification">TransportSpecification</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>transportSpecs</em>
</code>
</td>
<td>
<div>
<p>The transport specification containing the transport mode and vehicle specifications.
For vehicle modes (car, truck, bus), the <code><a href="sdk-for-ios-navigate-api-reference-structs-vehiclespecification">VehicleSpecification</a></code> within
this parameter provides dimensions, weights, hazardous materials, and tunnel category
information used for filtering. The same <code><a href="sdk-for-ios-navigate-api-reference-structs-transportspecification">TransportSpecification</a></code> object
can be used for both routing configuration and map rendering to ensure consistency.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18MapContentSettingsC29resetVehicleRestrictionFilteryyFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/resetVehicleRestrictionFilter()"></a>
<a class="token" href="#/s:7heresdk18MapContentSettingsC29resetVehicleRestrictionFilteryyFZ">resetVehicleRestrictionFilter()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes all filters regarding vehicle restrictions so that all restrictions will be displayed,
when the display of vehicle restrictions is enabled by enabling feature
using <code><a href="../Classes/MapScene.html#/s:7heresdk8MapSceneC14enableFeaturesyySDyS2SGF">MapScene.enableFeatures(...)</a></code> with <code><a href="../Structs/MapFeatures.html#/s:7heresdk11MapFeaturesV19vehicleRestrictionsSSvpZ">MapFeatures.vehicleRestrictions</a></code> and setting layer
visibility using <code><a href="../Classes/MapScene.html#/s:7heresdk8MapSceneC18setLayerVisibility9layerName10visibilityySS_AA0F5StateOtF">MapScene.setLayerVisibility(...)</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">resetVehicleRestrictionFilter</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18MapContentSettingsC26setPoiCategoriesVisibility11categoryIds10visibilityySaySSG_AA0H5StateOtFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setPoiCategoriesVisibility(categoryIds:visibility:)"></a>
<a class="token" href="#/s:7heresdk18MapContentSettingsC26setPoiCategoriesVisibility11categoryIds10visibilityySaySSG_AA0H5StateOtFZ">setPoiCategoriesVisibility(categoryIds:<wbr/>visibility:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets visibility for embedded carto POI categories (points of interest that are visible on the
map, by default). For HERE standard map schemes all available POI categories are visible by
default for each selected map scheme. Note that not all POI categories are available for
all map schemes.</p>
<p>Based on the given list of categories the number of shown carto POIs can be reduced.
To find all possible POI category strings look into <code>here.sdk.search.PlaceCategory</code>.
Note that it is enough to hide a main category like “100” (eat-and-drink) to also affect
sub categories such as “100-1000” (eat-and-drink-restaurant)
and “100-1100” (eat-and-drink-coffee-tea). To enable a sub category, also the related
main categories need have the <code>VISIBLE</code> state.</p>
<p>The POI visibility is a property of the map data itself. Once set it will be applied to
all HERE standard map schemes and the selected categories will remain even when
switching a map scheme.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">setPoiCategoriesVisibility</span><span class="p">(</span><span class="nv">categoryIds</span><span class="p">:</span> <span class="p">[</span><span class="kt">String</span><span class="p">],</span> <span class="nv">visibility</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-visibilitystate">VisibilityState</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>categoryIds</em>
</code>
</td>
<td>
<div>
<p>A list of POI categories that a visibility state is set for.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>visibility</em>
</code>
</td>
<td>
<div>
<p>A selected visibility for specified POI categories.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18MapContentSettingsC28resetPoiCategoriesVisibilityyyFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/resetPoiCategoriesVisibility()"></a>
<a class="token" href="#/s:7heresdk18MapContentSettingsC28resetPoiCategoriesVisibilityyyFZ">resetPoiCategoriesVisibility()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Resets POI categories visibility to their default state.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">resetPoiCategoriesVisibility</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18MapContentSettingsC22filterTrafficIncidents07trafficG0ySayAA0F12IncidentTypeOG_tFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/filterTrafficIncidents(trafficIncidents:)"></a>
<a class="token" href="#/s:7heresdk18MapContentSettingsC22filterTrafficIncidents07trafficG0ySayAA0F12IncidentTypeOG_tFZ">filterTrafficIncidents(trafficIncidents:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Filters the displayed traffic incidents so that only the ones applicable to the specified
criteria are shown when general display of traffic incidents is enabled.
The display of traffic incidents can be enabled using <code><a href="../Classes/MapScene.html#/s:7heresdk8MapSceneC14enableFeaturesyySDyS2SGF">MapScene.enableFeatures(...)</a></code> with
<code><a href="../Structs/MapFeatures.html#/s:7heresdk11MapFeaturesV16trafficIncidentsSSvpZ">MapFeatures.trafficIncidents</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">filterTrafficIncidents</span><span class="p">(</span><span class="nv">trafficIncidents</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-trafficincidenttype">TrafficIncidentType</a></span><span class="p">])</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>trafficIncidents</em>
</code>
</td>
<td>
<div>
<p>The traffic incidents to filter for, so that only applicable incidents are displayed.
When the list is empty, then all traffic incidents will be displayed.
If the <code>MapContentSettings.filterTrafficIncidents(...).trafficIncidents</code> contains <code><a href="../Enums/TrafficIncidentType.html#/s:7heresdk19TrafficIncidentTypeO7unknownyA2CmF">TrafficIncidentType.unknown</a></code>, then the
traffic filter will be applied ignoring this element.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18MapContentSettingsC26resetTrafficIncidentFilteryyFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/resetTrafficIncidentFilter()"></a>
<a class="token" href="#/s:7heresdk18MapContentSettingsC26resetTrafficIncidentFilteryyFZ">resetTrafficIncidentFilter()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes all filters regarding Traffic Incidents so that all incidents will be displayed,
when the display of Traffic Incidents is enabled using <code><a href="../Classes/MapScene.html#/s:7heresdk8MapSceneC14enableFeaturesyySDyS2SGF">MapScene.enableFeatures(...)</a></code> with
<code><a href="../Structs/MapFeatures.html#/s:7heresdk11MapFeaturesV16trafficIncidentsSSvpZ">MapFeatures.trafficIncidents</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">resetTrafficIncidentFilter</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18MapContentSettingsC23setTrafficRefreshPeriodyySdKFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setTrafficRefreshPeriod(_:)"></a>
<a class="token" href="#/s:7heresdk18MapContentSettingsC23setTrafficRefreshPeriodyySdKFZ">setTrafficRefreshPeriod(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the traffic data refresh period for both <code><a href="../Structs/MapFeatures.html#/s:7heresdk11MapFeaturesV11trafficFlowSSvpZ">MapFeatures.trafficFlow</a></code> and
<code><a href="../Structs/MapFeatures.html#/s:7heresdk11MapFeaturesV16trafficIncidentsSSvpZ">MapFeatures.trafficIncidents</a></code>. By default, the traffic information
validity time and the refresh period is derived from the refresh period of HERE’s traffic server.
The period set by this function will override the server’s default setting for
upcoming traffic data requests.
Defaults to 60 seconds.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Classes/MapContentSettings.html#/s:7heresdk18MapContentSettingsC25TrafficRefreshPeriodErrora">MapContentSettings.TrafficRefreshPeriodError</a></code> <code><a href="../Classes/MapContentSettings.html#/s:7heresdk18MapContentSettingsC25TrafficRefreshPeriodErrora">MapContentSettings.TrafficRefreshPeriodError</a></code> indicates what went wrong.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">setTrafficRefreshPeriod</span><span class="p">(</span><span class="n">_</span> <span class="nv">value</span><span class="p">:</span> <span class="kt">TimeInterval</span><span class="p">)</span> <span class="k">throws</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>value</em>
</code>
</td>
<td>
<div>
<p>Traffic data refresh period in seconds. Valid range is [60, 300] seconds.
The shortest refresh period that can be set is 60 seconds. This means that the traffic
data shown on a map view will be refreshed every minute.
The longest refresh period that can be set is 300 seconds. This means that the traffic
data shown on the current map view will be refreshed every 5 minutes
if the viewport does not change.
Note that when a viewport change occurs, new traffic data may be requested
regardless of the set refresh period. For example, during turn-by-turn navigation,
frequent viewport changes can result in missing traffic data, causing new requests
to be made more often.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18MapContentSettingsC25resetTrafficRefreshPeriodyyFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/resetTrafficRefreshPeriod()"></a>
<a class="token" href="#/s:7heresdk18MapContentSettingsC25resetTrafficRefreshPeriodyyFZ">resetTrafficRefreshPeriod()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Resets the traffic data (both flow and incidents) refresh period so the default traffic information
validity time and the refresh period derived from the refresh period of the traffic server is used.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">resetTrafficRefreshPeriod</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
</ul>
</div>
</section>
</section>
<section id="footer">
<p>© 2026 <a class="link" href="" rel="external noopener" target="_blank"></a>. All rights reserved. (Last updated: 2026-04-14)</p>
<p>Generated by <a class="link" href="https://github.com/realm/jazzy" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a class="link" href="https://realm.io" rel="external noopener" target="_blank">Realm</a> project.</p>
</section>
</article>
</div>
</body>
</html>

`
}</HTMLBlock>
