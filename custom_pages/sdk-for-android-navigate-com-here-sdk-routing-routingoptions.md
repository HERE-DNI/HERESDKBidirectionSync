---
title: "RoutingOptions (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-routing-routingoptions"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- RoutingOptions.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.routing</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.routing.RoutingOptions</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">RoutingOptions</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>The options defines how a route should be calculated.
 The options are used for all transport modes and engines.
 ** Electric vehicle specific requirements **
 Electric vehicle consumption are estimated when at least one consumption model is defined.
 Currently two models are supported:
 <ul>
<li>PhysicalConsumptionModel
 Aside from the values in PhysicalConsumptionModel additionally these values needs to be defined:
 <ul>
<li><a href="sdk-for-android-navigate-vehiclespecification#currentWeightInKilograms"><code>VehicleSpecification.currentWeightInKilograms</code></a> from <a href="sdk-for-android-navigate-transportspecification#vehicleSpecification"><code>TransportSpecification.vehicleSpecification</code></a>
 from <a href="sdk-for-android-navigate-com-here-sdk-routing-routingoptions#transportSpecification"><code>transportSpecification</code></a></li>
<li>Additionally <a href="sdk-for-android-navigate-waypoint#currentWeightChangeInKilograms"><code>Waypoint.currentWeightChangeInKilograms</code></a> can be defined.</li>
</ul>
</li>
<li>EmpiricalConsumptionModel</li>
</ul>
By setting <a href="sdk-for-android-navigate-electricvehicleoptions#ensureReachability"><code>ElectricVehicleOptions.ensureReachability</code></a> the <code>RoutingEngine</code> inserts additional charging stations
 to reach the waypoints.
 This feature requires setting the <a href="sdk-for-android-navigate-com-here-sdk-routing-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a>.
 By default a vehicle might not reach the waypoint, when the initial charge is not enough to reach all waypoints.
 See the parameter description below for more details.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-routing-allowoptions" title="class in com.here.sdk.routing">AllowOptions</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routingoptions#allowOptions">allowOptions</a></code></div>
<div className="col-last even-row-color">
<div className="block">The options explicitly allowed by user for route calculations.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-routing-avoidanceoptions" title="class in com.here.sdk.routing">AvoidanceOptions</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routingoptions#avoidanceOptions">avoidanceOptions</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Options to specify restrictions for route calculations.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-routing-electricvehicleoptions" title="class in com.here.sdk.routing">ElectricVehicleOptions</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routingoptions#evOptions">evOptions</a></code></div>
<div className="col-last even-row-color">
<div className="block">Defines the electric vehicle (EV) related parameters to calculate the consumption and reachability.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-maxspeedonsegment" title="class in com.here.sdk.routing">MaxSpeedOnSegment</a>&gt;</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routingoptions#maxSpeedOnSegments">maxSpeedOnSegments</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Segments with restriction on maximum <a href="sdk-for-android-navigate-dynamicspeedinfo#baseSpeedInMetersPerSecond"><code>DynamicSpeedInfo.baseSpeedInMetersPerSecond</code></a>.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions" title="class in com.here.sdk.routing">RouteOptions</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routingoptions#routeOptions">routeOptions</a></code></div>
<div className="col-last even-row-color">
<div className="block">Specifies the common route calculation options.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-routing-routetextoptions" title="class in com.here.sdk.routing">RouteTextOptions</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routingoptions#textOptions">textOptions</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Customize textual content returned from the route calculation, such
 as localization, format, and unit system.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-routing-tolloptions" title="class in com.here.sdk.routing">TollOptions</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routingoptions#tollOptions">tollOptions</a></code></div>
<div className="col-last even-row-color">
<div className="block">Options to specify how the tolls should be calculated,
 such as transponders, vehicle category, and emission type.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-transport-transportspecification" title="class in com.here.sdk.transport">TransportSpecification</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routingoptions#transportSpecification">transportSpecification</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Defines the transport specification which contains the transport mode and the vehicle specifications
 for the transport mode chosen.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routingoptions#%3Cinit%3E()">RoutingOptions</a>()</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section className="field-details" id="field-detail">

<ul className="member-list">
<li>
<section className="detail" id="transportSpecification">
<h3>transportSpecification</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-transport-transportspecification" title="class in com.here.sdk.transport">TransportSpecification</a></span> <span className="element-name">transportSpecification</span></div>
<div className="block"><p>Defines the transport specification which contains the transport mode and the vehicle specifications
 for the transport mode chosen.
 <strong>Notes:</strong>
<ul>
<li>The transport mode <a href="sdk-for-android-navigate-transportmode#PUBLIC_TRANSIT"><code>TransportMode.PUBLIC_TRANSIT</code></a> is not supported.</li>
<li>By default all vehicle specifications from <a href="sdk-for-android-navigate-com-here-sdk-routing-routingoptions#transportSpecification"><code>transportSpecification</code></a> are set to <code>null</code> and the
 <a href="sdk-for-android-navigate-transportspecification#transportMode"><code>TransportSpecification.transportMode</code></a> from <a href="sdk-for-android-navigate-com-here-sdk-routing-routingoptions#transportSpecification"><code>transportSpecification</code></a> is set to <a href="sdk-for-android-navigate-transportmode#CAR"><code>TransportMode.CAR</code></a>.</li>
<li>A route can be calculated with only the <a href="sdk-for-android-navigate-transportspecification#transportMode"><code>TransportSpecification.transportMode</code></a> from <a href="sdk-for-android-navigate-com-here-sdk-routing-routingoptions#transportSpecification"><code>transportSpecification</code></a> set.</li>
<li>It is highly recommended to define the <a href="sdk-for-android-navigate-com-here-sdk-transport-truckcategory" title="enum class in com.here.sdk.transport"><code>TruckCategory</code></a> that is being used in <a href="sdk-for-android-navigate-vehiclespecification#truckCategory"><code>VehicleSpecification.truckCategory</code></a> from
 <a href="sdk-for-android-navigate-transportspecification#vehicleSpecification"><code>TransportSpecification.vehicleSpecification</code></a> from <a href="sdk-for-android-navigate-com-here-sdk-routing-routingoptions#transportSpecification"><code>transportSpecification</code></a>, if the
 <a href="sdk-for-android-navigate-transportspecification#transportMode"><code>TransportSpecification.transportMode</code></a> from <a href="sdk-for-android-navigate-com-here-sdk-routing-routingoptions#transportSpecification"><code>transportSpecification</code></a> is set to <a href="sdk-for-android-navigate-transportmode#TRUCK"><code>TransportMode.TRUCK</code></a>.</li>
<li>The <a href="sdk-for-android-navigate-vehiclespecification#occupancy"><code>VehicleSpecification.occupancy</code></a> from <a href="sdk-for-android-navigate-transportspecification#vehicleSpecification"><code>TransportSpecification.vehicleSpecification</code></a> won't have effect
 if HOV and/or HOT lane usage is not allowed using <a href="sdk-for-android-navigate-evtruckoptions#allowOptions"><code>EVTruckOptions.allowOptions</code></a>.</li>
<li>The <a href="sdk-for-android-navigate-pedestrianspecification#walkingSpeedInMetersPerSecond"><code>PedestrianSpecification.walkingSpeedInMetersPerSecond</code></a> from <a href="sdk-for-android-navigate-transportspecification#pedestrianSpecification"><code>TransportSpecification.pedestrianSpecification</code></a>
 if present, will be used by the service as the walking speed for pedestrian routing. It influences the duration of walking
 along the route. The provided value must be in the range [0.5, 2.0]. When the value is outside this
 range, an invalid parameter error is raised. Refer to <a href="sdk-for-android-navigate-com-here-sdk-routing-routingerror" title="enum class in com.here.sdk.routing"><code>RoutingError</code></a> for details. The
 default speed is 1 meter per second.</li>
</ul></p></div>
</section>
</li>
<li>
<section className="detail" id="routeOptions">
<h3>routeOptions</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-routeoptions" title="class in com.here.sdk.routing">RouteOptions</a></span> <span className="element-name">routeOptions</span></div>
<div className="block"><p>Specifies the common route calculation options.</p></div>
</section>
</li>
<li>
<section className="detail" id="textOptions">
<h3>textOptions</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-routetextoptions" title="class in com.here.sdk.routing">RouteTextOptions</a></span> <span className="element-name">textOptions</span></div>
<div className="block"><p>Customize textual content returned from the route calculation, such
 as localization, format, and unit system.</p></div>
</section>
</li>
<li>
<section className="detail" id="avoidanceOptions">
<h3>avoidanceOptions</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-avoidanceoptions" title="class in com.here.sdk.routing">AvoidanceOptions</a></span> <span className="element-name">avoidanceOptions</span></div>
<div className="block"><p>Options to specify restrictions for route calculations.
 By default no restrictions are applied.</p></div>
</section>
</li>
<li>
<section className="detail" id="allowOptions">
<h3>allowOptions</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-allowoptions" title="class in com.here.sdk.routing">AllowOptions</a></span> <span className="element-name">allowOptions</span></div>
<div className="block"><p>The options explicitly allowed by user for route calculations.
 By default no options are opt in.</p></div>
</section>
</li>
<li>
<section className="detail" id="tollOptions">
<h3>tollOptions</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-tolloptions" title="class in com.here.sdk.routing">TollOptions</a></span> <span className="element-name">tollOptions</span></div>
<div className="block"><p>Options to specify how the tolls should be calculated,
 such as transponders, vehicle category, and emission type.
 <strong>Note</strong> Not used for offline calculations.</p></div>
</section>
</li>
<li>
<section className="detail" id="maxSpeedOnSegments">
<h3>maxSpeedOnSegments</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-maxspeedonsegment" title="class in com.here.sdk.routing">MaxSpeedOnSegment</a>&gt;</span> <span className="element-name">maxSpeedOnSegments</span></div>
<div className="block"><p>Segments with restriction on maximum <a href="sdk-for-android-navigate-dynamicspeedinfo#baseSpeedInMetersPerSecond"><code>DynamicSpeedInfo.baseSpeedInMetersPerSecond</code></a>.
 <strong>Note</strong> Not used for offline calculations.</p></div>
</section>
</li>
<li>
<section className="detail" id="evOptions">
<h3>evOptions</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-electricvehicleoptions" title="class in com.here.sdk.routing">ElectricVehicleOptions</a></span> <span className="element-name">evOptions</span></div>
<div className="block"><p>Defines the electric vehicle (EV) related parameters to calculate the consumption and reachability.
 When no EV options are defined an internal combustion engine is assumed.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section className="constructor-details" id="constructor-detail">

<ul className="member-list">
<li>
<section className="detail" id="&lt;init&gt;()">
<h3>RoutingOptions</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">RoutingOptions</span>()</div>
<div className="block"><p>Creates a new instance.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">equals</span><wbr/><span className="parameters">(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<dl className="notes">
<dt>Overrides:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="hashCode()">
<h3>hashCode</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">hashCode</span>()</div>
<dl className="notes">
<dt>Overrides:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="fromDefaultParameterConfiguration()">
<h3>fromDefaultParameterConfiguration</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-routingoptions" title="class in com.here.sdk.routing">RoutingOptions</a></span> <span className="element-name">fromDefaultParameterConfiguration</span>()</div>
<div className="block"><p>Returns the default configuration for the transport specification selected in <a href="sdk-for-android-navigate-parameterconfiguration#transportSpecification"><code>ParameterConfiguration.transportSpecification</code></a>
 from <a href="sdk-for-android-navigate-sdknativeengine#getParameterConfig()"><code>SDKNativeEngine.getParameterConfig()</code></a>.
 <strong>Note</strong> By default, the [sdk.core.ParameterConfiguration.transport_specification] from [sdk.core.engine.SDKNativeEngine.parameter_config]
 will return a valid <a href="sdk-for-android-navigate-com-here-sdk-transport-transportspecification" title="class in com.here.sdk.transport"><code>TransportSpecification</code></a> object with the [sdk.transport.TransportSpecification.transport_mode]
 set to <a href="sdk-for-android-navigate-transportmode#CAR"><code>TransportMode.CAR</code></a>.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-com-here-sdk-routing-routingoptions" title="class in com.here.sdk.routing"><code>RoutingOptions</code></a> object with the default configuration for the transport specification selected in
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
</div>



</div>
`
}</HTMLBlock>
