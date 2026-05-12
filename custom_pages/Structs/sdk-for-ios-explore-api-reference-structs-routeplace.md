---
title: "RoutePlace Structure Reference"
slug: "sdk-for-ios-explore-api-reference-structs-routeplace"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- RoutePlace.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/RoutePlace"></a>
<a title="RoutePlace Structure Reference"></a>
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
        RoutePlace Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct RoutePlace : Hashable</code></pre>
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
<pre><code>public var type: RoutePlaceType</code></pre>
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
<pre><code>public var waypointIndex: Int32?</code></pre>
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
<pre><code>public var originalCoordinates: GeoCoordinates?</code></pre>
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
<pre><code>public var mapMatchedCoordinates: GeoCoordinates</code></pre>
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
<pre><code>public var displayCoordinates: GeoCoordinates?</code></pre>
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
<pre><code>public var chargeInKilowattHours: Double?</code></pre>
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
<pre><code>public var chargingStation: ChargingStation?</code></pre>
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
<pre><code>public var name: String?</code></pre>
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
<pre><code>public var id: String?</code></pre>
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
<pre><code>public var platform: String?</code></pre>
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
<pre><code>public var sideOfDestination: SideOfDestination?</code></pre>
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
<pre><code>public func isOffRoad() -&gt; Bool</code></pre>
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



</div>
`
}</HTMLBlock>
