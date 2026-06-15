---
title: "RouteOptions"
slug: "sdk-for-ios-navigate-api-reference-structs-routeoptions"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/RouteOptions"></a>
<a title="RouteOptions Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-routing">Routing</a>

        RouteOptions Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>RouteOptions</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RouteOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">optimizationMode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-optimizationmode">OptimizationMode</a></span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">alternatives</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">departureTime</span><span class="p">:</span> <span class="kt">Date</span><span class="p">?</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">arrivalTime</span><span class="p">:</span> <span class="kt">Date</span><span class="p">?</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">speedCapInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span></code></pre>
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
<p>A flag that indicates whether the resulting route should contain a <code><a href="sdk-for-ios-navigate-api-reference-structs-routehandle">RouteHandle</a></code>.
Defaults to <code>false</code>.
Note that a <code><a href="sdk-for-ios-navigate-api-reference-structs-routehandle">RouteHandle</a></code> generated by the online <code><a href="sdk-for-ios-navigate-api-reference-classes-routingengine">RoutingEngine</a></code> is not compatible with the <code><a href="sdk-for-ios-navigate-api-reference-classes-offlineroutingengine">OfflineRoutingEngine</a></code> and vice versa.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">enableRouteHandle</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">trafficOptimizationMode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-trafficoptimizationmode">TrafficOptimizationMode</a></span></code></pre>
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
<p><strong>Note:</strong> For users of the <code><a href="sdk-for-ios-navigate-api-reference-classes-offlineroutingengine">OfflineRoutingEngine</a></code> this is a beta release of this feature,
so there could be a few bugs and unexpected behaviors. The <code><a href="sdk-for-ios-navigate-api-reference-classes-offlineroutingengine">OfflineRoutingEngine</a></code> is only available for the Navigate license. For users of the <code><a href="sdk-for-ios-navigate-api-reference-classes-routingengine">RoutingEngine</a></code> the feature is stable.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">enableTolls</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
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
The best order is calculated by the same metrics that are used during regular calculation, e.g. <code><a href="sdk-for-ios-navigate-api-reference-enums-optimizationmode">OptimizationMode</a></code>.
The starting and destination <code><a href="sdk-for-ios-navigate-api-reference-structs-waypoint">Waypoint</a></code> are not reordered.
If the whole number of waypoints is fewer than 4 - the flag doesn’t affect the resulting route (nothing to optimize).
The resulting order of waypoints can be identified by their waypoint indices in the route sections
(see <code><a href="../Classes/Route.html#/s:7heresdk5RouteC8sectionsSayAA7SectionCGvp">Route.sections</a></code>, <code><a href="../Classes/Section.html#/s:7heresdk7SectionC14departurePlaceAA05RouteD0Vvp">Section.departurePlace</a></code>, <code><a href="../Classes/Section.html#/s:7heresdk7SectionC12arrivalPlaceAA05RouteD0Vvp">Section.arrivalPlace</a></code>, <code><a href="../Structs/RoutePlace.html#/s:7heresdk10RoutePlaceV13waypointIndexs5Int32VSgvp">RoutePlace.waypointIndex</a></code>).
Currently, the waypoints order optimization is available only when using the <code><a href="sdk-for-ios-navigate-api-reference-classes-offlineroutingengine">OfflineRoutingEngine</a></code> (only available for the Navigate license).
Defaults to <code>false</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">optimizeWaypointsOrder</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">enableRouteLabels</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
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
<li>enableRouteHandle: A flag that indicates whether the resulting route should contain a <code><a href="sdk-for-ios-navigate-api-reference-structs-routehandle">RouteHandle</a></code>.
Defaults to <code>false</code>.
Note that a <code><a href="sdk-for-ios-navigate-api-reference-structs-routehandle">RouteHandle</a></code> generated by the online <code><a href="sdk-for-ios-navigate-api-reference-classes-routingengine">RoutingEngine</a></code> is not compatible with the <code><a href="sdk-for-ios-navigate-api-reference-classes-offlineroutingengine">OfflineRoutingEngine</a></code> and vice versa.</li>
<li>trafficOptimizationMode: The traffic optimization mode to be used for route calculation. By default, it is <code><a href="../Enums/TrafficOptimizationMode.html#/s:7heresdk23TrafficOptimizationModeO13timeDependentyA2CmF">TrafficOptimizationMode.timeDependent</a></code>, which enables traffic-aware routing.</li>
<li>enableTolls: A flag that indicates whether the resulting route <code><a href="../Classes/Section.html#/s:7heresdk7SectionC5tollsSayAA4TollVGvp">Section.tolls</a></code> properties should contain
tolls data. Defaults to <code>false</code>.</li>
</ul></li>
</ul>
<p><strong>Note:</strong> When a route calculation request asks tolls, a pricing scheme with higher rates might be applied.
  Consult your HERE representative to get more information on the related pricing schemes.</p>
<p><strong>Note:</strong> For users of the <code><a href="sdk-for-ios-navigate-api-reference-classes-offlineroutingengine">OfflineRoutingEngine</a></code> this is a beta release of this feature,
  so there could be a few bugs and unexpected behaviors. The <code><a href="sdk-for-ios-navigate-api-reference-classes-offlineroutingengine">OfflineRoutingEngine</a></code> is only available for the Navigate license. For users of the <code><a href="sdk-for-ios-navigate-api-reference-classes-routingengine">RoutingEngine</a></code> the feature is stable.</p>
<ul>
<li>optimizeWaypointsOrder: A flag that indicates whether the order of waypoints that is passed to <code>calculateRoute()</code> should be optimized in the best order.
The best order is calculated by the same metrics that are used during regular calculation, e.g. <code><a href="sdk-for-ios-navigate-api-reference-enums-optimizationmode">OptimizationMode</a></code>.
The starting and destination <code><a href="sdk-for-ios-navigate-api-reference-structs-waypoint">Waypoint</a></code> are not reordered.
If the whole number of waypoints is fewer than 4 - the flag doesn’t affect the resulting route (nothing to optimize).
The resulting order of waypoints can be identified by their waypoint indices in the route sections
(see <code><a href="../Classes/Route.html#/s:7heresdk5RouteC8sectionsSayAA7SectionCGvp">Route.sections</a></code>, <code><a href="../Classes/Section.html#/s:7heresdk7SectionC14departurePlaceAA05RouteD0Vvp">Section.departurePlace</a></code>, <code><a href="../Classes/Section.html#/s:7heresdk7SectionC12arrivalPlaceAA05RouteD0Vvp">Section.arrivalPlace</a></code>, <code><a href="../Structs/RoutePlace.html#/s:7heresdk10RoutePlaceV13waypointIndexs5Int32VSgvp">RoutePlace.waypointIndex</a></code>).
Currently, the waypoints order optimization is available only when using the <code><a href="sdk-for-ios-navigate-api-reference-classes-offlineroutingengine">OfflineRoutingEngine</a></code> (only available for the Navigate license).
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">optimizationMode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-optimizationmode">OptimizationMode</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-optimizationmode">OptimizationMode</a></span><span class="o">.</span><span class="n">fastest</span><span class="p">,</span> <span class="nv">alternatives</span><span class="p">:</span> <span class="kt">Int32</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nv">departureTime</span><span class="p">:</span> <span class="kt">Date</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">arrivalTime</span><span class="p">:</span> <span class="kt">Date</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">speedCapInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">enableRouteHandle</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">trafficOptimizationMode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-trafficoptimizationmode">TrafficOptimizationMode</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-trafficoptimizationmode">TrafficOptimizationMode</a></span><span class="o">.</span><span class="n">timeDependent</span><span class="p">,</span> <span class="nv">enableTolls</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">optimizeWaypointsOrder</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">enableRouteLabels</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">)</span></code></pre>
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
} </HTMLBlock>
