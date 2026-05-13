---
title: "EVCarOptions (API Reference)"
slug: "sdk-for-android-navigate-navigate-com-here-sdk-routing-evcaroptions"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- EVCarOptions.html -->
<!DOCTYPE HTML>






<div class="flex-box">
<header class="flex-header" role="banner">
<nav role="navigation">
<!-- ========= START OF TOP NAVBAR ======= -->
<div class="top-nav" id="navbar-top">
<div class="skip-nav"><a href="#skip-navbar-top" title="Skip navigation links">Skip navigation links</a></div>
<ul class="nav-list" id="navbar-top-firstrow" title="Navigation">
<li><a href="sdk-for-android-navigate-..-..-..-..-index">Overview</a></li>
<li><a href="sdk-for-android-navigate-package-summary">Package</a></li>
<li class="nav-bar-cell1-rev">Class</li>
<li><a href="sdk-for-android-navigate-package-tree">Tree</a></li>
<li><a href="sdk-for-android-navigate-..-..-..-..-deprecated-list">Deprecated</a></li>
<li><a href="sdk-for-android-navigate-..-..-..-..-index-all">Index</a></li>
<li><a href="sdk-for-android-navigate-..-..-..-..-help-doc#class">Help</a></li>
</ul>
</div>
<div class="sub-nav">
<div>
<ul class="sub-nav-list">
<li>Summary: </li>
<li>Nested | </li>
<li><a href="#field-summary">Field</a> | </li>
<li><a href="#constructor-summary">Constr</a> | </li>
<li><a href="#method-summary">Method</a></li>
</ul>
<ul class="sub-nav-list">
<li>Detail: </li>
<li><a href="#field-detail">Field</a> | </li>
<li><a href="#constructor-detail">Constr</a> | </li>
<li><a href="#method-detail">Method</a></li>
</ul>
</div>

</div>
<!-- ========= END OF TOP NAVBAR ========= -->
<span class="skip-nav" id="skip-navbar-top"></span></nav>
</header>
<div class="flex-content">
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.routing</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.routing.EVCarOptions</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">EVCarOptions</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use <code>RoutingOptions</code> class instead.</p></div>
</div>
<div class="block"><p>All the options to specify how a route for an electric car should be calculated.
 At minimum, a valid <a href="sdk-for-android-navigate-evconsumptionmodel" title="class in com.here.sdk.routing"><code>EVConsumptionModel</code></a> must be set or the route calculation will fail.
 <br/>
 Note: <a href="#ensureReachability"><code>ensureReachability</code></a> must be <code>true</code> to make sure that all stopovers are reachable. For this,
 charging stations may be added to the route. If <a href="#ensureReachability"><code>ensureReachability</code></a> is true, you need to
 specify the required route options and battery specifications that include the current charge level
 of the battery (<a href="sdk-for-android-navigate-batteryspecifications#initialChargeInKilowattHours"><code>BatterySpecifications.initialChargeInKilowattHours</code></a>).
 See the parameter description below for more details.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">

<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-allowoptions" title="class in com.here.sdk.routing">AllowOptions</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#allowOptions">allowOptions</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">The options explicitly allowed by user for route calculations.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-avoidanceoptions" title="class in com.here.sdk.routing">AvoidanceOptions</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#avoidanceOptions">avoidanceOptions</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Options to specify restrictions for route calculations.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-batteryspecifications" title="class in com.here.sdk.routing">BatterySpecifications</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#batterySpecifications">batterySpecifications</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Parameters that describe the electric vehicle's battery.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-..-transport-carspecifications" title="class in com.here.sdk.transport">CarSpecifications</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#carSpecifications">carSpecifications</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Detailed car specifications such as dimensions and weight.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-evconsumptionmodel" title="class in com.here.sdk.routing">EVConsumptionModel</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#consumptionModel">consumptionModel</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Vehicle specific parameters, which are then used to calculate energy consumption
 for the vehicle on a given route.</div>
</div>
<div class="col-first odd-row-color"><code>boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#ensureReachability">ensureReachability</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Ensure that the vehicle does not run out of energy along the way.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-evmobilityserviceproviderpreferences" title="class in com.here.sdk.routing">EVMobilityServiceProviderPreferences</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#evMobilityServiceProviderPreferences">evMobilityServiceProviderPreferences</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Defines the preferred E-Mobility Service Providers.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#lastCharacterOfLicensePlate">lastCharacterOfLicensePlate</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Specifies the last character of a vehicle's license plate, typically used to
 evaluate traffic restrictions in certain environmental or low-emission zones.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-maxspeedonsegment" title="class in com.here.sdk.routing">MaxSpeedOnSegment</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#maxSpeedOnSegments">maxSpeedOnSegments</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Segments with restriction on maximum <a href="sdk-for-android-navigate-dynamicspeedinfo#baseSpeedInMetersPerSecond"><code>DynamicSpeedInfo.baseSpeedInMetersPerSecond</code></a>.</div>
</div>
<div class="col-first odd-row-color"><code>int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#occupantsNumber">occupantsNumber</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Specifies the number of occupants in the vehicle, including driver,
 can affect the vehicle's ability to use HOV/carpool restricted lanes.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-routeoptions" title="class in com.here.sdk.routing">RouteOptions</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#routeOptions">routeOptions</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Specifies the common route calculation options.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-routetextoptions" title="class in com.here.sdk.routing">RouteTextOptions</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#textOptions">textOptions</a></code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Customize textual content returned from the route calculation, such
 as localization, format, and unit system.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-tolloptions" title="class in com.here.sdk.routing">TollOptions</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#tollOptions">tollOptions</a></code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Options to specify how the tolls should be calculated,
 such as transponders, vehicle category, and emission type.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">EVCarOptions</a>()</code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Creates a new instance.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="#hashCode()">hashCode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
 </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">

<ul class="member-list">
<li>
<section class="detail" id="routeOptions">
<h3>routeOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-routeoptions" title="class in com.here.sdk.routing">RouteOptions</a></span> <span class="element-name">routeOptions</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block"><p>Specifies the common route calculation options.</p></div>
</section>
</li>
<li>
<section class="detail" id="textOptions">
<h3>textOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-routetextoptions" title="class in com.here.sdk.routing">RouteTextOptions</a></span> <span class="element-name">textOptions</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block"><p>Customize textual content returned from the route calculation, such
 as localization, format, and unit system.</p></div>
</section>
</li>
<li>
<section class="detail" id="avoidanceOptions">
<h3>avoidanceOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-avoidanceoptions" title="class in com.here.sdk.routing">AvoidanceOptions</a></span> <span class="element-name">avoidanceOptions</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block"><p>Options to specify restrictions for route calculations. By default
 no restrictions are applied.</p></div>
</section>
</li>
<li>
<section class="detail" id="tollOptions">
<h3>tollOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-tolloptions" title="class in com.here.sdk.routing">TollOptions</a></span> <span class="element-name">tollOptions</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block"><p>Options to specify how the tolls should be calculated,
 such as transponders, vehicle category, and emission type.</p></div>
</section>
</li>
<li>
<section class="detail" id="allowOptions">
<h3>allowOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-allowoptions" title="class in com.here.sdk.routing">AllowOptions</a></span> <span class="element-name">allowOptions</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block"><p>The options explicitly allowed by user for route calculations. By default
 no options are opt in.</p></div>
</section>
</li>
<li>
<section class="detail" id="occupantsNumber">
<h3>occupantsNumber</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">occupantsNumber</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block"><p>Specifies the number of occupants in the vehicle, including driver,
 can affect the vehicle's ability to use HOV/carpool restricted lanes.
 Shouldn't be less than 1 or greater than 255. Defaults to 1.
 </p><p><strong>Note:</strong> This parameter has no effect unless HOV and/or HOT lane usage is enabled via <a href="#allowOptions"><code>allowOptions</code></a> and such lanes are available in the selected country.</p></div>
</section>
</li>
<li>
<section class="detail" id="lastCharacterOfLicensePlate">
<h3>lastCharacterOfLicensePlate</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">lastCharacterOfLicensePlate</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block"><p>Specifies the last character of a vehicle's license plate, typically used to
 evaluate traffic restrictions in certain environmental or low-emission zones.
 In cities like Bogotá, Mexico City, or Jakarta, specific license plate digits may
 be restricted on certain days or in certain areas to reduce congestion and emissions.
 When this value is provided, the HERE SDK considers it during route calculation to
 avoid roads or areas where your vehicle may be restricted based on local regulations.
 Example usage: "7", when the license plate of a vehicle looks like "B-ET-182487".
 </p><p>If this value is not set, such license plate-based restrictions are ignored, and
 routing is performed without considering them.</p></div>
</section>
</li>
<li>
<section class="detail" id="maxSpeedOnSegments">
<h3>maxSpeedOnSegments</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-maxspeedonsegment" title="class in com.here.sdk.routing">MaxSpeedOnSegment</a>&gt;</span> <span class="element-name">maxSpeedOnSegments</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block"><p>Segments with restriction on maximum <a href="sdk-for-android-navigate-dynamicspeedinfo#baseSpeedInMetersPerSecond"><code>DynamicSpeedInfo.baseSpeedInMetersPerSecond</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="ensureReachability">
<h3>ensureReachability</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">ensureReachability</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block"><p>Ensure that the vehicle does not run out of energy along the way.
 Requires valid <a href="#batterySpecifications"><code>batterySpecifications</code></a>.
 It also requires that
 <a href="sdk-for-android-navigate-routeoptions#optimizationMode"><code>RouteOptions.optimizationMode</code></a> = <a href="sdk-for-android-navigate-optimizationmode#FASTEST"><code>OptimizationMode.FASTEST</code></a>,
 <a href="sdk-for-android-navigate-routeoptions#speedCapInMetersPerSecond"><code>RouteOptions.speedCapInMetersPerSecond</code></a> is not set, and
 <a href="sdk-for-android-navigate-avoidanceoptions" title="class in com.here.sdk.routing"><code>AvoidanceOptions</code></a> is empty. Otherwise, this object is considered invalid.
 Setting this flag enables calculation of a route optimized for electric vehicles.
 Charging stations may be added along the route to ensure that the vehicle does
 not run out of energy along the way.
 It is especially useful for longer routes, because after all, charging stations are much
 less common than petrol stations.
 <strong>Note</strong> An [sdk.routing.RoutingError.INVALID_PARAMETER] is generated when
 the [sdk.routing.EVCarOptions.ensure_reachability] is set to <code>true</code> in case [sdk.routing.RoutingEngine.import_route] is called.
 Defaults to <code>false</code>.</p></div>
</section>
</li>
<li>
<section class="detail" id="consumptionModel">
<h3>consumptionModel</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-evconsumptionmodel" title="class in com.here.sdk.routing">EVConsumptionModel</a></span> <span class="element-name">consumptionModel</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block"><p>Vehicle specific parameters, which are then used to calculate energy consumption
 for the vehicle on a given route.</p></div>
</section>
</li>
<li>
<section class="detail" id="batterySpecifications">
<h3>batterySpecifications</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-batteryspecifications" title="class in com.here.sdk.routing">BatterySpecifications</a></span> <span class="element-name">batterySpecifications</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block"><p>Parameters that describe the electric vehicle's battery.</p></div>
</section>
</li>
<li>
<section class="detail" id="carSpecifications">
<h3>carSpecifications</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-..-transport-carspecifications" title="class in com.here.sdk.transport">CarSpecifications</a></span> <span class="element-name">carSpecifications</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block"><p>Detailed car specifications such as dimensions and weight.</p></div>
</section>
</li>
<li>
<section class="detail" id="evMobilityServiceProviderPreferences">
<h3>evMobilityServiceProviderPreferences</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-evmobilityserviceproviderpreferences" title="class in com.here.sdk.routing">EVMobilityServiceProviderPreferences</a></span> <span class="element-name">evMobilityServiceProviderPreferences</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block"><p>Defines the preferred E-Mobility Service Providers.
 The The E-Mobility Service Provider Partner Ids can be received from
 https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-roamings.html
 An alternative way to get <code>partnerId</code> is the <code>eMobilityServiceProviders.partnerId</code> as part of <code>HERE SDK Search</code>.
 Maximum number of E-Mobility Service Providers is limited to 10.
 By default, all providers are used.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>EVCarOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">EVCarOptions</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block"><p>Creates a new instance.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hashCode()">
<h3>hashCode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()</div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>
</div>
</div>



</div>
`
}</HTMLBlock>
