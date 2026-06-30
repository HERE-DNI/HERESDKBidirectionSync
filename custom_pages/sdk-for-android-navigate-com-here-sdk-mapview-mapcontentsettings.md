---
title: "MapContentSettings (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mapcontentsettings"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- MapContentSettings.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.mapview.MapContentSettings</div>
</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">MapContentSettings</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>Provides settings regarding map data which are applied globally to all map views. The settings
 can already be changed before a map view instance is created.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">

<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static enum </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontentsettings.trafficrefreshperioderrorcode" title="enum class in com.here.sdk.mapview">MapContentSettings.TrafficRefreshPeriodErrorCode</a></code></div>
<div class="col-last even-row-color">
<div class="block">Traffic refresh period error code</div>
</div>
<div class="col-first odd-row-color"><code>static final class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontentsettings.trafficrefreshperiodexception" title="class in com.here.sdk.mapview">MapContentSettings.TrafficRefreshPeriodException</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Traffic refresh period error exception</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontentsettings#configureVehicleRestrictionFilter(com.here.sdk.transport.TransportMode,com.here.sdk.transport.TruckSpecifications,java.util.List,com.here.sdk.transport.TunnelCategory)">configureVehicleRestrictionFilter</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-transport-transportmode" title="enum class in com.here.sdk.transport">TransportMode</a> transportMode,
 <a href="sdk-for-android-navigate-com-here-sdk-transport-truckspecifications" title="class in com.here.sdk.transport">TruckSpecifications</a> truckSpecifications,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-transport-hazardousmaterial" title="enum class in com.here.sdk.transport">HazardousMaterial</a>&gt; hazardousMaterials,
 <a href="sdk-for-android-navigate-com-here-sdk-transport-tunnelcategory" title="enum class in com.here.sdk.transport">TunnelCategory</a> tunnelCategory)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.28.0, use <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontentsettings#configureVehicleRestrictionFilter(com.here.sdk.transport.TransportSpecification)"><code>configureVehicleRestrictionFilter(TransportSpecification)</code></a> instead.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontentsettings#configureVehicleRestrictionFilter(com.here.sdk.transport.TransportSpecification)">configureVehicleRestrictionFilter</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-transport-transportspecification" title="class in com.here.sdk.transport">TransportSpecification</a> transportSpecs)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Configures a filter for <a href="sdk-for-android-navigate-mapfeatures#VEHICLE_RESTRICTIONS"><code>MapFeatures.VEHICLE_RESTRICTIONS</code></a> to show only the restrictions
 matching the transport specifications when the feature is enabled.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontentsettings#filterTrafficIncidents(java.util.List)">filterTrafficIncidents</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincidenttype" title="enum class in com.here.sdk.traffic">TrafficIncidentType</a>&gt; trafficIncidents)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Filters the displayed traffic incidents so that only the ones applicable to the specified
 criteria are shown when general display of traffic incidents is enabled.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontentsettings#resetPoiCategoriesVisibility()">resetPoiCategoriesVisibility</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Resets POI categories visibility to their default state.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontentsettings#resetTrafficIncidentFilter()">resetTrafficIncidentFilter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes all filters regarding Traffic Incidents so that all incidents will be displayed,
 when the display of Traffic Incidents is enabled using <a href="sdk-for-android-navigate-mapscene#enableFeatures(java.util.Map)"><code>MapScene.enableFeatures(java.util.Map&lt;java.lang.String, java.lang.String&gt;)</code></a> with
 <a href="sdk-for-android-navigate-mapfeatures#TRAFFIC_INCIDENTS"><code>MapFeatures.TRAFFIC_INCIDENTS</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontentsettings#resetTrafficRefreshPeriod()">resetTrafficRefreshPeriod</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Resets the traffic data (both flow and incidents) refresh period so the default traffic information
 validity time and the refresh period derived from the refresh period of the traffic server is used.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontentsettings#resetVehicleRestrictionFilter()">resetVehicleRestrictionFilter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Removes all filters regarding vehicle restrictions so that all restrictions will be displayed,
 when the display of vehicle restrictions is enabled by enabling feature
 using <a href="sdk-for-android-navigate-mapscene#enableFeatures(java.util.Map)"><code>MapScene.enableFeatures(java.util.Map&lt;java.lang.String, java.lang.String&gt;)</code></a> with <a href="sdk-for-android-navigate-mapfeatures#VEHICLE_RESTRICTIONS"><code>MapFeatures.VEHICLE_RESTRICTIONS</code></a> and setting layer
 visibility using <a href="sdk-for-android-navigate-mapscene#setLayerVisibility(java.lang.String,com.here.sdk.mapview.VisibilityState)"><code>MapScene.setLayerVisibility(java.lang.String, com.here.sdk.mapview.VisibilityState)</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontentsettings#setPoiCategoriesVisibility(java.util.List,com.here.sdk.mapview.VisibilityState)">setPoiCategoriesVisibility</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; categoryIds,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-visibilitystate" title="enum class in com.here.sdk.mapview">VisibilityState</a> visibility)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets visibility for embedded carto POI categories (points of interest that are visible on the
 map, by default).</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontentsettings#setTrafficRefreshPeriod(com.here.time.Duration)">setTrafficRefreshPeriod</a><wbr/>(<a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Sets the traffic data refresh period for both <a href="sdk-for-android-navigate-mapfeatures#TRAFFIC_FLOW"><code>MapFeatures.TRAFFIC_FLOW</code></a> and
 <a href="sdk-for-android-navigate-mapfeatures#TRAFFIC_INCIDENTS"><code>MapFeatures.TRAFFIC_INCIDENTS</code></a>.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="configureVehicleRestrictionFilter(com.here.sdk.transport.TransportMode,com.here.sdk.transport.TruckSpecifications,java.util.List,com.here.sdk.transport.TunnelCategory)">
<h3>configureVehicleRestrictionFilter</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">configureVehicleRestrictionFilter</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-transport-transportmode" title="enum class in com.here.sdk.transport">TransportMode</a> transportMode,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-transport-truckspecifications" title="class in com.here.sdk.transport">TruckSpecifications</a> truckSpecifications,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-transport-hazardousmaterial" title="enum class in com.here.sdk.transport">HazardousMaterial</a>&gt; hazardousMaterials,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-transport-tunnelcategory" title="enum class in com.here.sdk.transport">TunnelCategory</a> tunnelCategory)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0, use <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontentsettings#configureVehicleRestrictionFilter(com.here.sdk.transport.TransportSpecification)"><code>configureVehicleRestrictionFilter(TransportSpecification)</code></a> instead.</p></div>
</div>
<div class="block"><p>Configure a filter for <a href="sdk-for-android-navigate-mapfeatures#VEHICLE_RESTRICTIONS"><code>MapFeatures.VEHICLE_RESTRICTIONS</code></a> to show only the restrictions
 matching the specified criteria when the feature is enabled.
 
Only restrictions applicable to the supplied truck specifications will be shown.
 Examples:
 <ul>
<li>If the height in <code>truckSpecifications</code> is set to 200 cm, then height restrictions
 with a height greater than 200 cm will not be displayed.</li>
<li>If the trailer count in <code>truckSpecifications</code> is set to 2, then trailer
 restrictions for a count greater than 2 will not be displayed.</li>
</ul>

Only restrictions applicable to specified hazardous materials will be shown.
 If at least one hazardous material of any type is present in the list, all available
 tunnel category restrictions will be displayed. In order to filter-out non-applicable
 tunnel categories, a tunnel category, that applies to the vehicle, can be specified
 additionally.
 Examples:
 <ul>
<li>If the <code>hazardousMaterials</code> contains <a href="sdk-for-android-navigate-hazardousmaterial#POISON"><code>HazardousMaterial.POISON</code></a>
 and <a href="sdk-for-android-navigate-hazardousmaterial#GAS"><code>HazardousMaterial.GAS</code></a>, then only material restrictions
 for poison and gas will be displayed.</li>
<li>If the <code>hazardousMaterials</code> list is empty, then no material restrictions
 will be shown.</li>
<li>If the <code>hazardousMaterials</code> list is not supplied at all (is <code>null</code>), then
 no material restrictions will be shown.</li>
<li>If the <code>hazardousMaterials</code> contains at least one hazardous material of any
 type and <code>tunnelCategory</code> is <code>null</code>, then only corresponding material
 restrictions will be displayed together with all available tunnel categories.</li>
</ul>

Tunnel categories are labeled and rated based on the level of restriction they provide.
 The lowest level of restriction is <a href="sdk-for-android-navigate-tunnelcategory#B"><code>TunnelCategory.B</code></a>, the highest and most
 restrictive one is <a href="sdk-for-android-navigate-tunnelcategory#E"><code>TunnelCategory.E</code></a>.
 Specifying tunnel category means that:
 <ul>
<li>The truck carries goods which could cause only the additional dangerous effects
 described in specified tunnel category and other categories below it with lower level
 of restriction.</li>
<li>The truck does not carry goods that could cause the dangerous effects described in
 tunnel categories above with higher restriction levels than the one specified.</li>
</ul>
Tunnel categories are closely related to hazardous materials.
 Since the type of hazardous material alone does not define the exact level of danger,
 to ensure comprehensive coverage; the HERE SDK follows:
 <ul>
<li>If at least one hazardous material is specified but no <code>tunnelCategory</code> is provided,
 the SDK enables and displays <strong>all tunnel category restrictions</strong> to ensure that no relevant
 restrictions are omitted.</li>
<li>If both hazardous materials and a <code>tunnelCategory</code> are specified, the SDK
 <strong>strictly follows the given tunnel category parameter</strong> and displays only the
 applicable restrictions.</li>
</ul>
Example:
 If <code>tunnelCategory</code> is set to <a href="sdk-for-android-navigate-tunnelcategory#D"><code>TunnelCategory.D</code></a>, then restrictions for
 tunnel category <a href="sdk-for-android-navigate-tunnelcategory#E"><code>TunnelCategory.E</code></a> and <a href="sdk-for-android-navigate-tunnelcategory#D"><code>TunnelCategory.D</code></a>
 will be displayed, but not the categories <a href="sdk-for-android-navigate-tunnelcategory#B"><code>TunnelCategory.B</code></a> and
 <a href="sdk-for-android-navigate-tunnelcategory#C"><code>TunnelCategory.C</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>transportMode</code> - <p>Specifies the current transport type. Currently, it's used to distinguish
     between truck and other transport modes. This distinction ensures consistency
     between the routing logic and the information displayed on the map.
     At present, this is primarily used to suppress the generic truck restriction icon.</p></dd>
<dd><code>truckSpecifications</code> - <p>The size, weight, type and trailer count specifications to filter for, so that only
     restrictions which are relevant for the given specifications are displayed.</p></dd>
<dd><code>hazardousMaterials</code> - <p>The hazardous materials to filter for, so that only applicable restrictions are
     displayed. When the list is <code>null</code> or empty, then no material restrictions
     will be displayed.</p></dd>
<dd><code>tunnelCategory</code> - <p>The tunnel category to filter for, so that only applicable restrictions are
     displayed. If <code>null</code>, then no tunnel category restrictions will be
     displayed.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="configureVehicleRestrictionFilter(com.here.sdk.transport.TransportSpecification)">
<h3>configureVehicleRestrictionFilter</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">configureVehicleRestrictionFilter</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-transport-transportspecification" title="class in com.here.sdk.transport">TransportSpecification</a> transportSpecs)</span></div>
<div class="block"><p>Configures a filter for <a href="sdk-for-android-navigate-mapfeatures#VEHICLE_RESTRICTIONS"><code>MapFeatures.VEHICLE_RESTRICTIONS</code></a> to show only the restrictions
 matching the transport specifications when the feature is enabled.
 This method provides a unified way to configure vehicle restriction filters using
 a single <a href="sdk-for-android-navigate-com-here-sdk-transport-transportspecification" title="class in com.here.sdk.transport"><code>TransportSpecification</code></a> parameter. This allows you to use the same
 transport configuration for both routing and map rendering, ensuring consistency between
 route calculation and the restrictions displayed on the map.
 The method extracts the transport mode, vehicle specifications, hazardous materials, and
 tunnel category from the <code>transportSpecs</code> parameter and applies filtering according to
 the same rules described below.
 
The transport mode is used to distinguish between truck and other transport modes.
 This distinction ensures consistency between the routing logic and the information
 displayed on the map. At present, this is primarily used to suppress the generic
 truck restriction icon for non-truck modes.
 Currently, only vehicle-related restrictions are supported. For pedestrian, scooter,
 or taxi transport modes, the transport mode information is used, but no additional
 vehicle-specific restrictions are applied.
 
Only restrictions applicable to the vehicle specifications will be shown.
 The vehicle specifications include dimensions (height, width, length), weights
 (gross weight, weight per axle), and trailer count.
 Examples:
 <ul>
<li>If the height in vehicle specifications is set to 200 cm, then height restrictions
 with a height greater than 200 cm will not be displayed.</li>
<li>If the trailer count in vehicle specifications is set to 2, then trailer
 restrictions for a count greater than 2 will not be displayed.</li>
</ul>

Only restrictions applicable to specified hazardous materials will be shown.
 Hazardous materials are specified within the <a href="sdk-for-android-navigate-com-here-sdk-transport-vehiclespecification" title="class in com.here.sdk.transport"><code>VehicleSpecification</code></a>
 contained in the <code>transportSpecs</code> parameter.
 If at least one hazardous material of any type is present in the list, all available
 tunnel category restrictions will be displayed. In order to filter-out non-applicable
 tunnel categories, a tunnel category that applies to the vehicle can be specified
 additionally.
 Examples:
 <ul>
<li>If the hazardous materials list contains <a href="sdk-for-android-navigate-hazardousmaterial#POISON"><code>HazardousMaterial.POISON</code></a>
 and <a href="sdk-for-android-navigate-hazardousmaterial#GAS"><code>HazardousMaterial.GAS</code></a>, then only material restrictions
 for poison and gas will be displayed.</li>
<li>If the hazardous materials list is empty, then no material restrictions
 will be shown.</li>
<li>If the hazardous materials list is not supplied at all (is <code>null</code>), then
 no material restrictions will be shown.</li>
<li>If the hazardous materials list contains at least one hazardous material of any
 type and tunnel category is <code>null</code>, then only corresponding material
 restrictions will be displayed together with all available tunnel categories.</li>
</ul>

Tunnel categories are labeled and rated based on the level of restriction they provide.
 The lowest level of restriction is <a href="sdk-for-android-navigate-tunnelcategory#B"><code>TunnelCategory.B</code></a>, the highest and most
 restrictive one is <a href="sdk-for-android-navigate-tunnelcategory#E"><code>TunnelCategory.E</code></a>.
 The tunnel category is specified within the <a href="sdk-for-android-navigate-com-here-sdk-transport-vehiclespecification" title="class in com.here.sdk.transport"><code>VehicleSpecification</code></a>
 contained in the <code>transportSpecs</code> parameter.
 Specifying tunnel category means that:
 <ul>
<li>The vehicle carries goods which could cause only the additional dangerous effects
 described in specified tunnel category and other categories below it with lower level
 of restriction.</li>
<li>The vehicle does not carry goods that could cause the dangerous effects described in
 tunnel categories above with higher restriction levels than the one specified.</li>
</ul>
Tunnel categories are closely related to hazardous materials.
 Since the type of hazardous material alone does not define the exact level of danger,
 to ensure comprehensive coverage; the HERE SDK follows:
 <ul>
<li>If at least one hazardous material is specified but no tunnel category is provided,
 the SDK enables and displays <strong>all tunnel category restrictions</strong> to ensure that no relevant
 restrictions are omitted.</li>
<li>If both hazardous materials and a tunnel category are specified, the SDK
 <strong>strictly follows the given tunnel category parameter</strong> and displays only the
 applicable restrictions.</li>
</ul>
Example:
 If tunnel category is set to <a href="sdk-for-android-navigate-tunnelcategory#D"><code>TunnelCategory.D</code></a>, then restrictions for
 tunnel category <a href="sdk-for-android-navigate-tunnelcategory#E"><code>TunnelCategory.E</code></a> and <a href="sdk-for-android-navigate-tunnelcategory#D"><code>TunnelCategory.D</code></a>
 will be displayed, but not the categories <a href="sdk-for-android-navigate-tunnelcategory#B"><code>TunnelCategory.B</code></a> and
 <a href="sdk-for-android-navigate-tunnelcategory#C"><code>TunnelCategory.C</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>transportSpecs</code> - <p>The transport specification containing the transport mode and vehicle specifications.
     For vehicle modes (car, truck, bus), the <a href="sdk-for-android-navigate-com-here-sdk-transport-vehiclespecification" title="class in com.here.sdk.transport"><code>VehicleSpecification</code></a> within
     this parameter provides dimensions, weights, hazardous materials, and tunnel category
     information used for filtering. The same <a href="sdk-for-android-navigate-com-here-sdk-transport-transportspecification" title="class in com.here.sdk.transport"><code>TransportSpecification</code></a> object
     can be used for both routing configuration and map rendering to ensure consistency.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="resetVehicleRestrictionFilter()">
<h3>resetVehicleRestrictionFilter</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">resetVehicleRestrictionFilter</span>()</div>
<div class="block"><p>Removes all filters regarding vehicle restrictions so that all restrictions will be displayed,
 when the display of vehicle restrictions is enabled by enabling feature
 using <a href="sdk-for-android-navigate-mapscene#enableFeatures(java.util.Map)"><code>MapScene.enableFeatures(java.util.Map&lt;java.lang.String, java.lang.String&gt;)</code></a> with <a href="sdk-for-android-navigate-mapfeatures#VEHICLE_RESTRICTIONS"><code>MapFeatures.VEHICLE_RESTRICTIONS</code></a> and setting layer
 visibility using <a href="sdk-for-android-navigate-mapscene#setLayerVisibility(java.lang.String,com.here.sdk.mapview.VisibilityState)"><code>MapScene.setLayerVisibility(java.lang.String, com.here.sdk.mapview.VisibilityState)</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="setPoiCategoriesVisibility(java.util.List,com.here.sdk.mapview.VisibilityState)">
<h3>setPoiCategoriesVisibility</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setPoiCategoriesVisibility</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; categoryIds,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-visibilitystate" title="enum class in com.here.sdk.mapview">VisibilityState</a> visibility)</span></div>
<div class="block"><p>Sets visibility for embedded carto POI categories (points of interest that are visible on the
 map, by default). For HERE standard map schemes all available POI categories are visible by
 default for each selected map scheme. Note that not all POI categories are available for
 all map schemes.
 Based on the given list of categories the number of shown carto POIs can be reduced.
 To find all possible POI category strings look into <code>here.sdk.search.PlaceCategory</code>.
 Note that it is enough to hide a main category like "100" (eat-and-drink) to also affect
 sub categories such as "100-1000" (eat-and-drink-restaurant)
 and "100-1100" (eat-and-drink-coffee-tea). To enable a sub category, also the related
 main categories need have the <code>VISIBLE</code> state.
 The POI visibility is a property of the map data itself. Once set it will be applied to
 all HERE standard map schemes and the selected categories will remain even when
 switching a map scheme.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>categoryIds</code> - <p>A list of POI categories that a visibility state is set for.</p></dd>
<dd><code>visibility</code> - <p>A selected visibility for specified POI categories.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="resetPoiCategoriesVisibility()">
<h3>resetPoiCategoriesVisibility</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">resetPoiCategoriesVisibility</span>()</div>
<div class="block"><p>Resets POI categories visibility to their default state.</p></div>
</section>
</li>
<li>
<section class="detail" id="filterTrafficIncidents(java.util.List)">
<h3>filterTrafficIncidents</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">filterTrafficIncidents</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincidenttype" title="enum class in com.here.sdk.traffic">TrafficIncidentType</a>&gt; trafficIncidents)</span></div>
<div class="block"><p>Filters the displayed traffic incidents so that only the ones applicable to the specified
 criteria are shown when general display of traffic incidents is enabled.
 The display of traffic incidents can be enabled using <a href="sdk-for-android-navigate-mapscene#enableFeatures(java.util.Map)"><code>MapScene.enableFeatures(java.util.Map&lt;java.lang.String, java.lang.String&gt;)</code></a> with
 <a href="sdk-for-android-navigate-mapfeatures#TRAFFIC_INCIDENTS"><code>MapFeatures.TRAFFIC_INCIDENTS</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>trafficIncidents</code> - <p>The traffic incidents to filter for, so that only applicable incidents are displayed.
     When the list is empty, then all traffic incidents will be displayed.
     If the <code>trafficIncidents</code> contains <a href="sdk-for-android-navigate-trafficincidenttype#UNKNOWN"><code>TrafficIncidentType.UNKNOWN</code></a>, then the
     traffic filter will be applied ignoring this element.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="resetTrafficIncidentFilter()">
<h3>resetTrafficIncidentFilter</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">resetTrafficIncidentFilter</span>()</div>
<div class="block"><p>Removes all filters regarding Traffic Incidents so that all incidents will be displayed,
 when the display of Traffic Incidents is enabled using <a href="sdk-for-android-navigate-mapscene#enableFeatures(java.util.Map)"><code>MapScene.enableFeatures(java.util.Map&lt;java.lang.String, java.lang.String&gt;)</code></a> with
 <a href="sdk-for-android-navigate-mapfeatures#TRAFFIC_INCIDENTS"><code>MapFeatures.TRAFFIC_INCIDENTS</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="setTrafficRefreshPeriod(com.here.time.Duration)">
<h3>setTrafficRefreshPeriod</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">setTrafficRefreshPeriod</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a> value)</span>
                                    throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontentsettings.trafficrefreshperiodexception" title="class in com.here.sdk.mapview">MapContentSettings.TrafficRefreshPeriodException</a></span></div>
<div class="block"><p>Sets the traffic data refresh period for both <a href="sdk-for-android-navigate-mapfeatures#TRAFFIC_FLOW"><code>MapFeatures.TRAFFIC_FLOW</code></a> and
 <a href="sdk-for-android-navigate-mapfeatures#TRAFFIC_INCIDENTS"><code>MapFeatures.TRAFFIC_INCIDENTS</code></a>. By default, the traffic information
 validity time and the refresh period is derived from the refresh period of HERE's traffic server.
 The period set by this function will override the server's default setting for
 upcoming traffic data requests.
 Defaults to 60 seconds.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Traffic data refresh period in seconds. Valid range is [60, 300] seconds.
     The shortest refresh period that can be set is 60 seconds. This means that the traffic
     data shown on a map view will be refreshed every minute.
     The longest refresh period that can be set is 300 seconds. This means that the traffic
     data shown on the current map view will be refreshed every 5 minutes
     if the viewport does not change.
     Note that when a viewport change occurs, new traffic data may be requested
     regardless of the set refresh period. For example, during turn-by-turn navigation,
     frequent viewport changes can result in missing traffic data, causing new requests
     to be made more often.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontentsettings.trafficrefreshperiodexception" title="class in com.here.sdk.mapview">MapContentSettings.TrafficRefreshPeriodException</a></code> - <p><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontentsettings.trafficrefreshperiodexception" title="class in com.here.sdk.mapview"><code>MapContentSettings.TrafficRefreshPeriodException</code></a> indicates what went wrong.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="resetTrafficRefreshPeriod()">
<h3>resetTrafficRefreshPeriod</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">resetTrafficRefreshPeriod</span>()</div>
<div class="block"><p>Resets the traffic data (both flow and incidents) refresh period so the default traffic information
 validity time and the refresh period derived from the refresh period of the traffic server is used.</p></div>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->






</div>
`
}</HTMLBlock>
