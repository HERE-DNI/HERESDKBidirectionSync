---
title: "RefreshRouteParameters"
slug: "sdk-for-ios-explore-structs-refreshrouteparameters"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/RefreshRouteParameters"></a>
<a title="RefreshRouteParameters Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-index">heresdk</a>

<a href="sdk-for-ios-explore-other%20structs">Other Structures</a>

        RefreshRouteParameters Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>RefreshRouteParameters</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RefreshRouteParameters</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>This struct provides the necessary information for refreshing a route from a
specific location on it.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22RefreshRouteParametersV11routeHandleAA0cF0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/routeHandle"></a>
<a class="token" href="#/s:7heresdk22RefreshRouteParametersV11routeHandleAA0cF0Vvp">routeHandle</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The route handle holding the route to be refreshed.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">routeHandle</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-structs-routehandle">RouteHandle</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22RefreshRouteParametersV13startingPointAA8WaypointVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/startingPoint"></a>
<a class="token" href="#/s:7heresdk22RefreshRouteParametersV13startingPointAA8WaypointVSgvp">startingPoint</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Identify the new starting point of the route. It should be of type <code><a href="../Enums/WaypointType.html#/s:7heresdk12WaypointTypeO8stopoveryA2CmF">WaypointType.stopover</a></code>.
Otherwise, an <code><a href="../Enums/RoutingError.html#/s:7heresdk12RoutingErrorO16invalidParameteryA2CmF">RoutingError.invalidParameter</a></code> error is generated. Moreover, it should be very close to the
original route specified with the <code><a href="sdk-for-ios-explore-structs-routehandle">RouteHandle</a></code>. The location of this waypoint may by provided,
for example, by a <code>RouteProgress</code> event. Since the new starting point is expected to be
along the original route, the original route geometry is used to reach the remaining waypoints. The new route
will not include the <code><a href="sdk-for-ios-explore-structs-waypoint">Waypoint</a></code> items that lie behind the new starting point (i.e. the path that
was already traveled). Plus, <code><a href="../Classes/Route.html#/s:7heresdk5RouteC14lengthInMeterss5Int32Vvp">Route.lengthInMeters</a></code>, <code><a href="../Classes/Route.html#/s:7heresdk5RouteC8durationSdvp">Route.duration</a></code>, and similar
values are from the new starting point to the destination. If the new waypoint is too far off the original
route, the route refresh may fail and an <code><a href="../Enums/RoutingError.html#/s:7heresdk12RoutingErrorO19couldNotMatchOriginyA2CmF">RoutingError.couldNotMatchOrigin</a></code> error is triggered.
In that case, an application may decide to calculate a new route from scratch.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">startingPoint</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-structs-waypoint">Waypoint</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22RefreshRouteParametersV20startingSectionIndexs5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/startingSectionIndex"></a>
<a class="token" href="#/s:7heresdk22RefreshRouteParametersV20startingSectionIndexs5Int32VSgvp">startingSectionIndex</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates the index of the last traveled route section. When it is provided, the previous sections are discarded
from the refreshed route and the starting point is searched in the provided section. If the starting point
is not found in that section an <code><a href="../Enums/RoutingError.html#/s:7heresdk12RoutingErrorO19couldNotMatchOriginyA2CmF">RoutingError.couldNotMatchOrigin</a></code> error is triggered.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">startingSectionIndex</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22RefreshRouteParametersV41traveledDistanceOnStartingSectionInMeterss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/traveledDistanceOnStartingSectionInMeters"></a>
<a class="token" href="#/s:7heresdk22RefreshRouteParametersV41traveledDistanceOnStartingSectionInMeterss5Int32VSgvp">traveledDistanceOnStartingSectionInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Provides an indication on how much of the starting section is already traveled. The refresh route function
would ignore the first part of the section. If it is provided with an invalid starting section index, an
<code><a href="../Enums/RoutingError.html#/s:7heresdk12RoutingErrorO16invalidParameteryA2CmF">RoutingError.invalidParameter</a></code> error is generated.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">traveledDistanceOnStartingSectionInMeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22RefreshRouteParametersV11routeHandle13startingPointAcA0cF0V_AA8WaypointVtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(routeHandle:startingPoint:)"></a>
<a class="token" href="#/s:7heresdk22RefreshRouteParametersV11routeHandle13startingPointAcA0cF0V_AA8WaypointVtcfc">init(routeHandle:<wbr/>startingPoint:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Create a new instance of <code>RefreshRouteParameters</code> with the new starting point on the route.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">routeHandle</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-structs-routehandle">RouteHandle</a></span><span class="p">,</span> <span class="nv">startingPoint</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-structs-waypoint">Waypoint</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>routeHandle</em>
</code>
</td>
<td>
<div>
<p>The route handle holding the route to be refreshed.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>startingPoint</em>
</code>
</td>
<td>
<div>
<p>Identify the new starting point of the route.</p>
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
<a name="/s:7heresdk22RefreshRouteParametersV11routeHandle20startingSectionIndex026traveledDistanceOnStartingH8InMetersAcA0cF0V_s5Int32VAJtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(routeHandle:startingSectionIndex:traveledDistanceOnStartingSectionInMeters:)"></a>
<a class="token" href="#/s:7heresdk22RefreshRouteParametersV11routeHandle20startingSectionIndex026traveledDistanceOnStartingH8InMetersAcA0cF0V_s5Int32VAJtcfc">init(routeHandle:<wbr/>startingSectionIndex:<wbr/>traveledDistanceOnStartingSectionInMeters:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Create a new instance of <code>RefreshRouteParameters</code> with the point on the section of the route as a new starting point.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">routeHandle</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-structs-routehandle">RouteHandle</a></span><span class="p">,</span> <span class="nv">startingSectionIndex</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">,</span> <span class="nv">traveledDistanceOnStartingSectionInMeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>routeHandle</em>
</code>
</td>
<td>
<div>
<p>The route handle holding the route to be refreshed.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>startingSectionIndex</em>
</code>
</td>
<td>
<div>
<p>Indicates the index of the last traveled route section.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>traveledDistanceOnStartingSectionInMeters</em>
</code>
</td>
<td>
<div>
<p>Provides an indication on how much of the starting section is already traveled.</p>
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
<a name="/s:7heresdk22RefreshRouteParametersV11routeHandle13startingPoint0G12SectionIndex026traveledDistanceOnStartingI8InMetersAcA0cF0V_AA8WaypointVs5Int32VAMtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(routeHandle:startingPoint:startingSectionIndex:traveledDistanceOnStartingSectionInMeters:)"></a>
<a class="token" href="#/s:7heresdk22RefreshRouteParametersV11routeHandle13startingPoint0G12SectionIndex026traveledDistanceOnStartingI8InMetersAcA0cF0V_AA8WaypointVs5Int32VAMtcfc">init(routeHandle:<wbr/>startingPoint:<wbr/>startingSectionIndex:<wbr/>traveledDistanceOnStartingSectionInMeters:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Create a new instance of <code>RefreshRouteParameters</code> with the new starting point and the section position on the route.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">routeHandle</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-structs-routehandle">RouteHandle</a></span><span class="p">,</span> <span class="nv">startingPoint</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-structs-waypoint">Waypoint</a></span><span class="p">,</span> <span class="nv">startingSectionIndex</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">,</span> <span class="nv">traveledDistanceOnStartingSectionInMeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>routeHandle</em>
</code>
</td>
<td>
<div>
<p>The route handle holding the route to be refreshed.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>startingPoint</em>
</code>
</td>
<td>
<div>
<p>Identify the new starting point of the route.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>startingSectionIndex</em>
</code>
</td>
<td>
<div>
<p>Indicates the index of the last traveled route section.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>traveledDistanceOnStartingSectionInMeters</em>
</code>
</td>
<td>
<div>
<p>Provides an indication on how much of the starting section is already traveled.</p>
</div>
</td>
</tr>
</tbody>
</table>
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
