---
title: "RoutingOptions (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-routing-routingoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- RoutingOptions.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.routing.RoutingOptions</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">RoutingOptions</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>The options defines how a route should be calculated.
 </p><p>The options are used for all transport modes and engines.
 </p><p>** Electric vehicle specific requirements **
 Electric vehicle consumption are estimated when at least one consumption model is defined.
 Currently two models are supported:
 <ul>
<li>PhysicalConsumptionModel
 Aside from the values in PhysicalConsumptionModel additionally these values needs to be defined:
 <ul>
<li><a href="sdk-for-android-navigate-vehiclespecification#currentWeightInKilograms"><code>VehicleSpecification.currentWeightInKilograms</code></a> from <a href="sdk-for-android-navigate-transportspecification#vehicleSpecification"><code>TransportSpecification.vehicleSpecification</code></a>
 from <a href="sdk-for-android-navigate-index#transportSpecification"><code>transportSpecification</code></a></li>
<li>Additionally <a href="sdk-for-android-navigate-waypoint#currentWeightChangeInKilograms"><code>Waypoint.currentWeightChangeInKilograms</code></a> can be defined.</li>
</ul>
</li>
<li>EmpiricalConsumptionModel</li>
</ul>
</p><p>By setting <a href="sdk-for-android-navigate-electricvehicleoptions#ensureReachability"><code>ElectricVehicleOptions.ensureReachability</code></a> the <code>RoutingEngine</code> inserts additional charging stations
 to reach the waypoints.
 This feature requires setting the <a href="sdk-for-android-navigate-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a>.
 By default a vehicle might not reach the waypoint, when the initial charge is not enough to reach all waypoints.
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#allowOptions">allowOptions</a></code></div>
<div class="col-last even-row-color">
<div class="block">The options explicitly allowed by user for route calculations.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-avoidanceoptions" title="class in com.here.sdk.routing">AvoidanceOptions</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#avoidanceOptions">avoidanceOptions</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Options to specify restrictions for route calculations.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-electricvehicleoptions" title="class in com.here.sdk.routing">ElectricVehicleOptions</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#evOptions">evOptions</a></code></div>
<div class="col-last even-row-color">
<div class="block">Defines the electric vehicle (EV) related parameters to calculate the consumption and reachability.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-maxspeedonsegment" title="class in com.here.sdk.routing">MaxSpeedOnSegment</a>&gt;</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#maxSpeedOnSegments">maxSpeedOnSegments</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Segments with restriction on maximum <a href="sdk-for-android-navigate-dynamicspeedinfo#baseSpeedInMetersPerSecond"><code>DynamicSpeedInfo.baseSpeedInMetersPerSecond</code></a>.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-routeoptions" title="class in com.here.sdk.routing">RouteOptions</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#routeOptions">routeOptions</a></code></div>
<div class="col-last even-row-color">
<div class="block">Specifies the common route calculation options.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-routetextoptions" title="class in com.here.sdk.routing">RouteTextOptions</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#textOptions">textOptions</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Customize textual content returned from the route calculation, such
 as localization, format, and unit system.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-tolloptions" title="class in com.here.sdk.routing">TollOptions</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#tollOptions">tollOptions</a></code></div>
<div class="col-last even-row-color">
<div class="block">Options to specify how the tolls should be calculated,
 such as transponders, vehicle category, and emission type.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-transportspecification" title="class in com.here.sdk.transport">TransportSpecification</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#transportSpecification">transportSpecification</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Defines the transport specification which contains the transport mode and the vehicle specifications
 for the transport mode chosen.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#%3Cinit%3E()">RoutingOptions</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>

<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-navigate-routingoptions" title="class in com.here.sdk.routing">RoutingOptions</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#fromDefaultParameterConfiguration()">fromDefaultParameterConfiguration</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the default configuration for the transport specification selected in <a href="sdk-for-android-navigate-parameterconfiguration#transportSpecification"><code>ParameterConfiguration.transportSpecification</code></a>
 from <a href="sdk-for-android-navigate-sdknativeengine#getParameterConfig()"><code>SDKNativeEngine.getParameterConfig()</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#hashCode()">hashCode</a>()</code></div>

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
<section class="detail" id="transportSpecification">
<h3>transportSpecification</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-transportspecification" title="class in com.here.sdk.transport">TransportSpecification</a></span> <span class="element-name">transportSpecification</span></div>
<div class="block"><p>Defines the transport specification which contains the transport mode and the vehicle specifications
 for the transport mode chosen.
 <strong>Notes:</strong>
<ul>
<li>The transport mode <a href="sdk-for-android-navigate-transportmode#PUBLIC_TRANSIT"><code>TransportMode.PUBLIC_TRANSIT</code></a> is not supported.</li>
<li>By default all vehicle specifications from <a href="sdk-for-android-navigate-index#transportSpecification"><code>transportSpecification</code></a> are set to <code>null</code> and the
 <a href="sdk-for-android-navigate-transportspecification#transportMode"><code>TransportSpecification.transportMode</code></a> from <a href="sdk-for-android-navigate-index#transportSpecification"><code>transportSpecification</code></a> is set to <a href="sdk-for-android-navigate-transportmode#CAR"><code>TransportMode.CAR</code></a>.</li>
<li>A route can be calculated with only the <a href="sdk-for-android-navigate-transportspecification#transportMode"><code>TransportSpecification.transportMode</code></a> from <a href="sdk-for-android-navigate-index#transportSpecification"><code>transportSpecification</code></a> set.</li>
<li>It is highly recommended to define the <a href="sdk-for-android-navigate-truckcategory" title="enum class in com.here.sdk.transport"><code>TruckCategory</code></a> that is being used in <a href="sdk-for-android-navigate-vehiclespecification#truckCategory"><code>VehicleSpecification.truckCategory</code></a> from
 <a href="sdk-for-android-navigate-transportspecification#vehicleSpecification"><code>TransportSpecification.vehicleSpecification</code></a> from <a href="sdk-for-android-navigate-index#transportSpecification"><code>transportSpecification</code></a>, if the
 <a href="sdk-for-android-navigate-transportspecification#transportMode"><code>TransportSpecification.transportMode</code></a> from <a href="sdk-for-android-navigate-index#transportSpecification"><code>transportSpecification</code></a> is set to <a href="sdk-for-android-navigate-transportmode#TRUCK"><code>TransportMode.TRUCK</code></a>.</li>
<li>The <a href="sdk-for-android-navigate-vehiclespecification#occupancy"><code>VehicleSpecification.occupancy</code></a> from <a href="sdk-for-android-navigate-transportspecification#vehicleSpecification"><code>TransportSpecification.vehicleSpecification</code></a> won't have effect
 if HOV and/or HOT lane usage is not allowed using <a href="sdk-for-android-navigate-evtruckoptions#allowOptions"><code>EVTruckOptions.allowOptions</code></a>.</li>
<li>The <a href="sdk-for-android-navigate-pedestrianspecification#walkingSpeedInMetersPerSecond"><code>PedestrianSpecification.walkingSpeedInMetersPerSecond</code></a> from <a href="sdk-for-android-navigate-transportspecification#pedestrianSpecification"><code>TransportSpecification.pedestrianSpecification</code></a>
 if present, will be used by the service as the walking speed for pedestrian routing. It influences the duration of walking
 along the route. The provided value must be in the range [0.5, 2.0]. When the value is outside this
 range, an invalid parameter error is raised. Refer to <a href="sdk-for-android-navigate-routingerror" title="enum class in com.here.sdk.routing"><code>RoutingError</code></a> for details. The
 default speed is 1 meter per second.</li>
</ul></p></div>
</section>
</li>
<li>
<section class="detail" id="routeOptions">
<h3>routeOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-routeoptions" title="class in com.here.sdk.routing">RouteOptions</a></span> <span class="element-name">routeOptions</span></div>
<div class="block"><p>Specifies the common route calculation options.</p></div>
</section>
</li>
<li>
<section class="detail" id="textOptions">
<h3>textOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-routetextoptions" title="class in com.here.sdk.routing">RouteTextOptions</a></span> <span class="element-name">textOptions</span></div>
<div class="block"><p>Customize textual content returned from the route calculation, such
 as localization, format, and unit system.</p></div>
</section>
</li>
<li>
<section class="detail" id="avoidanceOptions">
<h3>avoidanceOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-avoidanceoptions" title="class in com.here.sdk.routing">AvoidanceOptions</a></span> <span class="element-name">avoidanceOptions</span></div>
<div class="block"><p>Options to specify restrictions for route calculations.
 By default no restrictions are applied.</p></div>
</section>
</li>
<li>
<section class="detail" id="allowOptions">
<h3>allowOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-allowoptions" title="class in com.here.sdk.routing">AllowOptions</a></span> <span class="element-name">allowOptions</span></div>
<div class="block"><p>The options explicitly allowed by user for route calculations.
 By default no options are opt in.</p></div>
</section>
</li>
<li>
<section class="detail" id="tollOptions">
<h3>tollOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-tolloptions" title="class in com.here.sdk.routing">TollOptions</a></span> <span class="element-name">tollOptions</span></div>
<div class="block"><p>Options to specify how the tolls should be calculated,
 such as transponders, vehicle category, and emission type.
 <strong>Note</strong> Not used for offline calculations.</p></div>
</section>
</li>
<li>
<section class="detail" id="maxSpeedOnSegments">
<h3>maxSpeedOnSegments</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-maxspeedonsegment" title="class in com.here.sdk.routing">MaxSpeedOnSegment</a>&gt;</span> <span class="element-name">maxSpeedOnSegments</span></div>
<div class="block"><p>Segments with restriction on maximum <a href="sdk-for-android-navigate-dynamicspeedinfo#baseSpeedInMetersPerSecond"><code>DynamicSpeedInfo.baseSpeedInMetersPerSecond</code></a>.
 <strong>Note</strong> Not used for offline calculations.</p></div>
</section>
</li>
<li>
<section class="detail" id="evOptions">
<h3>evOptions</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-electricvehicleoptions" title="class in com.here.sdk.routing">ElectricVehicleOptions</a></span> <span class="element-name">evOptions</span></div>
<div class="block"><p>Defines the electric vehicle (EV) related parameters to calculate the consumption and reachability.
 When no EV options are defined an internal combustion engine is assumed.</p></div>
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
<h3>RoutingOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RoutingOptions</span>()</div>
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
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="fromDefaultParameterConfiguration()">
<h3>fromDefaultParameterConfiguration</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-routingoptions" title="class in com.here.sdk.routing">RoutingOptions</a></span> <span class="element-name">fromDefaultParameterConfiguration</span>()</div>
<div class="block"><p>Returns the default configuration for the transport specification selected in <a href="sdk-for-android-navigate-parameterconfiguration#transportSpecification"><code>ParameterConfiguration.transportSpecification</code></a>
 from <a href="sdk-for-android-navigate-sdknativeengine#getParameterConfig()"><code>SDKNativeEngine.getParameterConfig()</code></a>.
 <strong>Note</strong> By default, the [sdk.core.ParameterConfiguration.transport_specification] from [sdk.core.engine.SDKNativeEngine.parameter_config]
 will return a valid <a href="sdk-for-android-navigate-transportspecification" title="class in com.here.sdk.transport"><code>TransportSpecification</code></a> object with the [sdk.transport.TransportSpecification.transport_mode]
 set to <a href="sdk-for-android-navigate-transportmode#CAR"><code>TransportMode.CAR</code></a>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-routingoptions" title="class in com.here.sdk.routing"><code>RoutingOptions</code></a> object with the default configuration for the transport specification selected in
     <a href="sdk-for-android-navigate-parameterconfiguration#transportSpecification"><code>ParameterConfiguration.transportSpecification</code></a> from <a href="sdk-for-android-navigate-sdknativeengine#getParameterConfig()"><code>SDKNativeEngine.getParameterConfig()</code></a>.</p></dd>
</dl>
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
