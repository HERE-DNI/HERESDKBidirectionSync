---
title: "RoutePlace"
slug: "sdk-for-ios-navigate-api-reference-structs-routeplace"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/RoutePlace"></a>
<a title="RoutePlace Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-routing">Routing</a>

        RoutePlace Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>RoutePlace</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RoutePlace</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>The location information.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10RoutePlaceV4typeAA0bC4TypeOvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/type"></a>
<a class="token" href="#/s:7heresdk10RoutePlaceV4typeAA0bC4TypeOvp">type</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The type of the route place.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">type</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-routeplacetype">RoutePlaceType</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10RoutePlaceV13waypointIndexs5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/waypointIndex"></a>
<a class="token" href="#/s:7heresdk10RoutePlaceV13waypointIndexs5Int32VSgvp">waypointIndex</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>If available, this index corresponds to the waypoint in the original
user-defined waypoint list. Otherwise, this waypoint was added during
route calculation by the system.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">waypointIndex</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10RoutePlaceV19originalCoordinatesAA03GeoE0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/originalCoordinates"></a>
<a class="token" href="#/s:7heresdk10RoutePlaceV19originalCoordinatesAA03GeoE0VSgvp">originalCoordinates</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>User-defined geographic coordinates. If not available, it means this place
was added during route calculation.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">originalCoordinates</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geocoordinates">GeoCoordinates</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10RoutePlaceV21mapMatchedCoordinatesAA03GeoF0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/mapMatchedCoordinates"></a>
<a class="token" href="#/s:7heresdk10RoutePlaceV21mapMatchedCoordinatesAA03GeoF0Vvp">mapMatchedCoordinates</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Map-matched geographic coordinates.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">mapMatchedCoordinates</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geocoordinates">GeoCoordinates</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10RoutePlaceV18displayCoordinatesAA03GeoE0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/displayCoordinates"></a>
<a class="token" href="#/s:7heresdk10RoutePlaceV18displayCoordinatesAA03GeoE0VSgvp">displayCoordinates</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Location of the Points of Interest (PoI) to be displayed in the visualization.
In the map data, PoI have a set of display coordinates as well as a set of access/routing coordinates.
While the access/routing coordinates specify the nearest accessible road network location
that can be apart from actual location of the PoI,
the display coordinates specify the location of the PoI to be displayed accurately in the visualization.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">displayCoordinates</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geocoordinates">GeoCoordinates</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10RoutePlaceV21chargeInKilowattHoursSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/chargeInKilowattHours"></a>
<a class="token" href="#/s:7heresdk10RoutePlaceV21chargeInKilowattHoursSdSgvp">chargeInKilowattHours</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Estimated battery charge in kWh for electric vehicles when leaving this place.
Available only if the route was calculated with <code><a href="../Structs/ElectricVehicleOptions.html#/s:7heresdk22ElectricVehicleOptionsV18ensureReachabilitySbvp">ElectricVehicleOptions.ensureReachability</a></code> = <code>true</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">chargeInKilowattHours</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10RoutePlaceV15chargingStationAA08ChargingE0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/chargingStation"></a>
<a class="token" href="#/s:7heresdk10RoutePlaceV15chargingStationAA08ChargingE0VSgvp">chargingStation</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Charging station data for electric vehicles.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">chargingStation</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-chargingstation">ChargingStation</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10RoutePlaceV4nameSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/name"></a>
<a class="token" href="#/s:7heresdk10RoutePlaceV4nameSSSgvp">name</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Name of a public transit place if available.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">name</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10RoutePlaceV2idSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/id"></a>
<a class="token" href="#/s:7heresdk10RoutePlaceV2idSSSgvp">id</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Identifier of a public transit place if available.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">id</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10RoutePlaceV8platformSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/platform"></a>
<a class="token" href="#/s:7heresdk10RoutePlaceV8platformSSSgvp">platform</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Platform name or number of a public transit place if available.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">platform</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10RoutePlaceV17sideOfDestinationAA04SideeF0OSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/sideOfDestination"></a>
<a class="token" href="#/s:7heresdk10RoutePlaceV17sideOfDestinationAA04SideeF0OSgvp">sideOfDestination</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Side of destination: left, right or undefined.
<code>nil</code> for transit sections and for origin points.
<code>UNDEFINED</code> if <code><a href="../Structs/RoutePlace.html#/s:7heresdk10RoutePlaceV19originalCoordinatesAA03GeoE0VSgvp">originalCoordinates</a></code> are not identified or too close to the road.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">sideOfDestination</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-sideofdestination">SideOfDestination</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10RoutePlaceV9isOffRoadSbyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/isOffRoad()"></a>
<a class="token" href="#/s:7heresdk10RoutePlaceV9isOffRoadSbyF">isOffRoad()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Checks whether the <code>RoutePlace</code> is off-road or not.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">isOffRoad</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p><code>true</code> if the <code>RoutePlace</code> is off-road, <code>false</code> otherwise.</p>
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
