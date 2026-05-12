---
title: "RouteOptions Structure Reference"
slug: "sdk-for-ios-explore-api-reference-structs-routeoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- RouteOptions.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/RouteOptions"></a>
<a title="RouteOptions Structure Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="../index.html">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="../index.html">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="../Routing.html">Routing</a>
<img alt="" id="carat" src="../img/carat.png"/>
        RouteOptions Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct RouteOptions : Hashable</code></pre>
</div>
</div>
<p>The options to specify how the route will be calculated.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RouteOptionsV16optimizationModeAA012OptimizationE0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/optimizationMode"></a>
<a class="token" href="#/s:7heresdk12RouteOptionsV16optimizationModeAA012OptimizationE0Ovp">optimizationMode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The optimization mode to be used for route calculation. By default, it is <code><a href="../Enums/OptimizationMode.html#/s:7heresdk16OptimizationModeO7fastestyA2CmF">OptimizationMode.fastest</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var optimizationMode: OptimizationMode</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RouteOptionsV12alternativess5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/alternatives"></a>
<a class="token" href="#/s:7heresdk12RouteOptionsV12alternativess5Int32Vvp">alternatives</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Maximum number of alternative routes that will be calculated, in addition
to the best one. The provided value must be in the range [0, 6].
Alternative routes can be unavailable, thus they are not guaranteed to be returned.
The order of routes is from the best to the worst, as evaluated by the route calculation
algorithm and according to the given input parameters.
Defaults to 0, which means there are no alternatives, i.e. only the best route is returned.
Must be 0 for isoline calculation.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var alternatives: Int32</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RouteOptionsV13departureTime10Foundation4DateVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/departureTime"></a>
<a class="token" href="#/s:7heresdk12RouteOptionsV13departureTime10Foundation4DateVSgvp">departureTime</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Optional time when travel is expected to start. Traffic speed and
incidents shall be taken into account in the calculation of the route, per <code><a href="../Structs/RouteOptions.html#/s:7heresdk12RouteOptionsV23trafficOptimizationModeAA07TrafficeF0Ovp">RouteOptions.trafficOptimizationMode</a></code>.
By default, the time is not set.
If the time is not set, the current time will be used internally, i.e. now.
Therefore, by default, a time-aware route request is initiated including traffic.</p>
<p><strong>Note</strong>:</p>
<ul>
<li>Both departure time and <code><a href="../Structs/RouteOptions.html#/s:7heresdk12RouteOptionsV11arrivalTime10Foundation4DateVSgvp">RouteOptions.arrivalTime</a></code> cannot be set at the same time.</li>
<li>This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset
when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var departureTime: Date?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RouteOptionsV11arrivalTime10Foundation4DateVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/arrivalTime"></a>
<a class="token" href="#/s:7heresdk12RouteOptionsV11arrivalTime10Foundation4DateVSgvp">arrivalTime</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Optional time when travel is expected to end. Traffic speed and
incidents shall be taken into account in the calculation of the route, per <code><a href="../Structs/RouteOptions.html#/s:7heresdk12RouteOptionsV23trafficOptimizationModeAA07TrafficeF0Ovp">RouteOptions.trafficOptimizationMode</a></code>.
By default, the time is not set.
If the time is not set, the current time will be used internally, to predict the arrival time.
Therefore, by default, a time-aware route request is initiated including traffic.</p>
<p><strong>Note</strong>:</p>
<ul>
<li>Both <code><a href="../Structs/RouteOptions.html#/s:7heresdk12RouteOptionsV13departureTime10Foundation4DateVSgvp">RouteOptions.departureTime</a></code> and arrival time cannot be set at the same time.</li>
<li>This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset
when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var arrivalTime: Date?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RouteOptionsV25speedCapInMetersPerSecondSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/speedCapInMetersPerSecond"></a>
<a class="token" href="#/s:7heresdk12RouteOptionsV25speedCapInMetersPerSecondSdSgvp">speedCapInMetersPerSecond</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies the maximum speed in meters per second, which the user wishes not to exceed.
The valid range is [1, 70] meters per second. Note that it is valid only for <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code>,
<code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO5truckyA2CmF">TransportMode.truck</a></code> and <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO7scooteryA2CmF">TransportMode.scooter</a></code> transport modes.
For car, truck and scooter transport modes, it will affect <code><a href="../Classes/Route.html#/s:7heresdk5RouteC8durationSdvp">Route.duration</a></code> of
the route. Only for scooter transport mode, it may affect the route geometry. Defaults to <code>nil</code>,
which means that no speed cap is set.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var speedCapInMetersPerSecond: Double?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RouteOptionsV06enableB6HandleSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/enableRouteHandle"></a>
<a class="token" href="#/s:7heresdk12RouteOptionsV06enableB6HandleSbvp">enableRouteHandle</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A flag that indicates whether the resulting route should contain a <code><a href="../Structs/RouteHandle.html">RouteHandle</a></code>.
Defaults to <code>false</code>.
Note that a <code><a href="../Structs/RouteHandle.html">RouteHandle</a></code> generated by the online <code><a href="../Classes/RoutingEngine.html">RoutingEngine</a></code> is not compatible with the <code>OfflineRoutingEngine</code> and vice versa.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var enableRouteHandle: Bool</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RouteOptionsV23trafficOptimizationModeAA07TrafficeF0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/trafficOptimizationMode"></a>
<a class="token" href="#/s:7heresdk12RouteOptionsV23trafficOptimizationModeAA07TrafficeF0Ovp">trafficOptimizationMode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The traffic optimization mode to be used for route calculation. By default, it is <code><a href="../Enums/TrafficOptimizationMode.html#/s:7heresdk23TrafficOptimizationModeO13timeDependentyA2CmF">TrafficOptimizationMode.timeDependent</a></code>, which enables traffic-aware routing.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var trafficOptimizationMode: TrafficOptimizationMode</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RouteOptionsV11enableTollsSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/enableTolls"></a>
<a class="token" href="#/s:7heresdk12RouteOptionsV11enableTollsSbvp">enableTolls</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A flag that indicates whether the resulting route <code><a href="../Classes/Section.html#/s:7heresdk7SectionC5tollsSayAA4TollVGvp">Section.tolls</a></code> properties should contain
tolls data. Defaults to <code>false</code>.</p>
<p><strong>Note:</strong> When a route calculation request asks tolls, a pricing scheme with higher rates might be applied.
Consult your HERE representative to get more information on the related pricing schemes.</p>
<p><strong>Note:</strong> For users of the <code>OfflineRoutingEngine</code> this is a beta release of this feature,
so there could be a few bugs and unexpected behaviors. The <code>OfflineRoutingEngine</code> is only available for the Navigate license. For users of the <code><a href="../Classes/RoutingEngine.html">RoutingEngine</a></code> the feature is stable.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var enableTolls: Bool</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RouteOptionsV22optimizeWaypointsOrderSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/optimizeWaypointsOrder"></a>
<a class="token" href="#/s:7heresdk12RouteOptionsV22optimizeWaypointsOrderSbvp">optimizeWaypointsOrder</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A flag that indicates whether the order of waypoints that is passed to <code>calculateRoute()</code> should be optimized in the best order.
The best order is calculated by the same metrics that are used during regular calculation, e.g. <code><a href="../Enums/OptimizationMode.html">OptimizationMode</a></code>.
The starting and destination <code><a href="../Structs/Waypoint.html">Waypoint</a></code> are not reordered.
If the whole number of waypoints is fewer than 4 - the flag doesn’t affect the resulting route (nothing to optimize).
The resulting order of waypoints can be identified by their waypoint indices in the route sections
(see <code><a href="../Classes/Route.html#/s:7heresdk5RouteC8sectionsSayAA7SectionCGvp">Route.sections</a></code>, <code><a href="../Classes/Section.html#/s:7heresdk7SectionC14departurePlaceAA05RouteD0Vvp">Section.departurePlace</a></code>, <code><a href="../Classes/Section.html#/s:7heresdk7SectionC12arrivalPlaceAA05RouteD0Vvp">Section.arrivalPlace</a></code>, <code><a href="../Structs/RoutePlace.html#/s:7heresdk10RoutePlaceV13waypointIndexs5Int32VSgvp">RoutePlace.waypointIndex</a></code>).
Currently, the waypoints order optimization is available only when using the <code>OfflineRoutingEngine</code> (only available for the Navigate license).
Defaults to <code>false</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var optimizeWaypointsOrder: Bool</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RouteOptionsV06enableB6LabelsSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/enableRouteLabels"></a>
<a class="token" href="#/s:7heresdk12RouteOptionsV06enableB6LabelsSbvp">enableRouteLabels</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies whether route labels should be included in the route response.
Route labels identify major highways or road names along the route.
By default, this is set to <code>false</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var enableRouteLabels: Bool</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12RouteOptionsV16optimizationMode12alternatives13departureTime07arrivalH025speedCapInMetersPerSecond06enableB6Handle019trafficOptimizationE00P5Tolls22optimizeWaypointsOrder0pB6LabelsAcA0sE0O_s5Int32V10Foundation4DateVSgAUSdSgSbAA07TrafficsE0OS3btcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(optimizationMode:alternatives:departureTime:arrivalTime:speedCapInMetersPerSecond:enableRouteHandle:trafficOptimizationMode:enableTolls:optimizeWaypointsOrder:enableRouteLabels:)"></a>
<a class="token" href="#/s:7heresdk12RouteOptionsV16optimizationMode12alternatives13departureTime07arrivalH025speedCapInMetersPerSecond06enableB6Handle019trafficOptimizationE00P5Tolls22optimizeWaypointsOrder0pB6LabelsAcA0sE0O_s5Int32V10Foundation4DateVSgAUSdSgSbAA07TrafficsE0OS3btcfc">init(optimizationMode:<wbr/>alternatives:<wbr/>departureTime:<wbr/>arrivalTime:<wbr/>speedCapInMetersPerSecond:<wbr/>enableRouteHandle:<wbr/>trafficOptimizationMode:<wbr/>enableTolls:<wbr/>optimizeWaypointsOrder:<wbr/>enableRouteLabels:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance.</p>
<ul>
<li><p>Parameters</p>
<ul>
<li>optimizationMode: The optimization mode to be used for route calculation. By default, it is <code><a href="../Enums/OptimizationMode.html#/s:7heresdk16OptimizationModeO7fastestyA2CmF">OptimizationMode.fastest</a></code>.</li>
<li>alternatives: Maximum number of alternative routes that will be calculated, in addition
to the best one. The provided value must be in the range [0, 6].
Alternative routes can be unavailable, thus they are not guaranteed to be returned.
The order of routes is from the best to the worst, as evaluated by the route calculation
algorithm and according to the given input parameters.
Defaults to 0, which means there are no alternatives, i.e. only the best route is returned.
Must be 0 for isoline calculation.</li>
<li>departureTime: Optional time when travel is expected to start. Traffic speed and
incidents shall be taken into account in the calculation of the route, per <code><a href="../Structs/RouteOptions.html#/s:7heresdk12RouteOptionsV23trafficOptimizationModeAA07TrafficeF0Ovp">RouteOptions.trafficOptimizationMode</a></code>.
By default, the time is not set.
If the time is not set, the current time will be used internally, i.e. now.
Therefore, by default, a time-aware route request is initiated including traffic.</li>
</ul>
<p><strong>Note</strong>:</p>
<ul>
<li>Both departure time and <code><a href="../Structs/RouteOptions.html#/s:7heresdk12RouteOptionsV11arrivalTime10Foundation4DateVSgvp">RouteOptions.arrivalTime</a></code> cannot be set at the same time.</li>
<li>This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset
  when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00

<ul>
<li>arrivalTime: Optional time when travel is expected to end. Traffic speed and
incidents shall be taken into account in the calculation of the route, per <code><a href="../Structs/RouteOptions.html#/s:7heresdk12RouteOptionsV23trafficOptimizationModeAA07TrafficeF0Ovp">RouteOptions.trafficOptimizationMode</a></code>.
By default, the time is not set.
If the time is not set, the current time will be used internally, to predict the arrival time.
Therefore, by default, a time-aware route request is initiated including traffic.</li>
</ul></li>
</ul>
<p><strong>Note</strong>:</p>
<ul>
<li>Both <code><a href="../Structs/RouteOptions.html#/s:7heresdk12RouteOptionsV13departureTime10Foundation4DateVSgvp">RouteOptions.departureTime</a></code> and arrival time cannot be set at the same time.</li>
<li>This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset
  when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00

<ul>
<li>speedCapInMetersPerSecond: Specifies the maximum speed in meters per second, which the user wishes not to exceed.
The valid range is [1, 70] meters per second. Note that it is valid only for <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code>,
<code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO5truckyA2CmF">TransportMode.truck</a></code> and <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO7scooteryA2CmF">TransportMode.scooter</a></code> transport modes.
For car, truck and scooter transport modes, it will affect <code><a href="../Classes/Route.html#/s:7heresdk5RouteC8durationSdvp">Route.duration</a></code> of
the route. Only for scooter transport mode, it may affect the route geometry. Defaults to <code>nil</code>,
which means that no speed cap is set.</li>
<li>enableRouteHandle: A flag that indicates whether the resulting route should contain a <code><a href="../Structs/RouteHandle.html">RouteHandle</a></code>.
Defaults to <code>false</code>.
Note that a <code><a href="../Structs/RouteHandle.html">RouteHandle</a></code> generated by the online <code><a href="../Classes/RoutingEngine.html">RoutingEngine</a></code> is not compatible with the <code>OfflineRoutingEngine</code> and vice versa.</li>
<li>trafficOptimizationMode: The traffic optimization mode to be used for route calculation. By default, it is <code><a href="../Enums/TrafficOptimizationMode.html#/s:7heresdk23TrafficOptimizationModeO13timeDependentyA2CmF">TrafficOptimizationMode.timeDependent</a></code>, which enables traffic-aware routing.</li>
<li>enableTolls: A flag that indicates whether the resulting route <code><a href="../Classes/Section.html#/s:7heresdk7SectionC5tollsSayAA4TollVGvp">Section.tolls</a></code> properties should contain
tolls data. Defaults to <code>false</code>.</li>
</ul></li>
</ul>
<p><strong>Note:</strong> When a route calculation request asks tolls, a pricing scheme with higher rates might be applied.
  Consult your HERE representative to get more information on the related pricing schemes.</p>
<p><strong>Note:</strong> For users of the <code>OfflineRoutingEngine</code> this is a beta release of this feature,
  so there could be a few bugs and unexpected behaviors. The <code>OfflineRoutingEngine</code> is only available for the Navigate license. For users of the <code><a href="../Classes/RoutingEngine.html">RoutingEngine</a></code> the feature is stable.</p>
<ul>
<li>optimizeWaypointsOrder: A flag that indicates whether the order of waypoints that is passed to <code>calculateRoute()</code> should be optimized in the best order.
The best order is calculated by the same metrics that are used during regular calculation, e.g. <code><a href="../Enums/OptimizationMode.html">OptimizationMode</a></code>.
The starting and destination <code><a href="../Structs/Waypoint.html">Waypoint</a></code> are not reordered.
If the whole number of waypoints is fewer than 4 - the flag doesn’t affect the resulting route (nothing to optimize).
The resulting order of waypoints can be identified by their waypoint indices in the route sections
(see <code><a href="../Classes/Route.html#/s:7heresdk5RouteC8sectionsSayAA7SectionCGvp">Route.sections</a></code>, <code><a href="../Classes/Section.html#/s:7heresdk7SectionC14departurePlaceAA05RouteD0Vvp">Section.departurePlace</a></code>, <code><a href="../Classes/Section.html#/s:7heresdk7SectionC12arrivalPlaceAA05RouteD0Vvp">Section.arrivalPlace</a></code>, <code><a href="../Structs/RoutePlace.html#/s:7heresdk10RoutePlaceV13waypointIndexs5Int32VSgvp">RoutePlace.waypointIndex</a></code>).
Currently, the waypoints order optimization is available only when using the <code>OfflineRoutingEngine</code> (only available for the Navigate license).
Defaults to <code>false</code>.</li>
<li>enableRouteLabels: Specifies whether route labels should be included in the route response.
Route labels identify major highways or road names along the route.
By default, this is set to <code>false</code>.</li>
</ul></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public init(optimizationMode: OptimizationMode = OptimizationMode.fastest, alternatives: Int32 = 0, departureTime: Date? = nil, arrivalTime: Date? = nil, speedCapInMetersPerSecond: Double? = nil, enableRouteHandle: Bool = false, trafficOptimizationMode: TrafficOptimizationMode = TrafficOptimizationMode.timeDependent, enableTolls: Bool = false, optimizeWaypointsOrder: Bool = false, enableRouteLabels: Bool = false)</code></pre>
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



</div>
`
}</HTMLBlock>
