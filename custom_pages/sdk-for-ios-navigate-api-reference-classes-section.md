---
title: "Untitled"
slug: "sdk-for-ios-navigate-api-reference-classes-section"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- Section.html -->
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/Section"></a>
<a title="Section Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-routing">Routing</a>
<img alt="" id="carat" src="../img/carat.png"/>
        Section Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>Section</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">Section</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Section</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Section</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>A section is a part of the route between two stopovers.
A stopover is a location on the route where a stop is made.</p>
<p><strong>Note:</strong> A section contains a list of <code><a href="sdk-for-ios-navigate-api-reference-..-structs-sectionnotice">SectionNotice</a></code> objects that describe
<em>potential issues</em> after the route was calculated. If the list is non-empty, it
is recommended to evaluate possible violations against the requested route options
and reject the route if deemed necessary.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7SectionC8geometryAA11GeoPolylineVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/geometry"></a>
<a class="token" href="#/s:7heresdk7SectionC8geometryAA11GeoPolylineVvp">geometry</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The <code><a href="sdk-for-ios-navigate-api-reference-..-structs-geopolyline">GeoPolyline</a></code> object representing the polyline of this section.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">private(set)</span> <span class="kd">lazy</span> <span class="k">var</span> <span class="nv">geometry</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-geopolyline">GeoPolyline</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7SectionC5spansSayAA4SpanCGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/spans"></a>
<a class="token" href="#/s:7heresdk7SectionC5spansSayAA4SpanCGvp">spans</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The <code><a href="sdk-for-ios-navigate-api-reference-..-classes-span">Span</a></code>‘s that constitute this section.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">private(set)</span> <span class="kd">lazy</span> <span class="k">var</span> <span class="nv">spans</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-span">Span</a></span><span class="p">]</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7SectionC9maneuversSayAA8ManeuverCGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maneuvers"></a>
<a class="token" href="#/s:7heresdk7SectionC9maneuversSayAA8ManeuverCGvp">maneuvers</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The maneuvers for this section.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">private(set)</span> <span class="kd">lazy</span> <span class="k">var</span> <span class="nv">maneuvers</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-maneuver">Maneuver</a></span><span class="p">]</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7SectionC11boundingBoxAA03GeoD0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/boundingBox"></a>
<a class="token" href="#/s:7heresdk7SectionC11boundingBoxAA03GeoD0Vvp">boundingBox</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The closest rectangular area where this section fits in.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">boundingBox</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-geobox">GeoBox</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7SectionC14lengthInMeterss5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/lengthInMeters"></a>
<a class="token" href="#/s:7heresdk7SectionC14lengthInMeterss5Int32Vvp">lengthInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The length of this section in meters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">lengthInMeters</span><span class="p">:</span> <span class="kt">Int32</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7SectionC20sectionTransportModeAA0bdE0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/sectionTransportMode"></a>
<a class="token" href="#/s:7heresdk7SectionC20sectionTransportModeAA0bdE0Ovp">sectionTransportMode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The transport mode of this section.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">sectionTransportMode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-sectiontransportmode">SectionTransportMode</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7SectionC14departurePlaceAA05RouteD0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/departurePlace"></a>
<a class="token" href="#/s:7heresdk7SectionC14departurePlaceAA05RouteD0Vvp">departurePlace</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Describes the departure place.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">departurePlace</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-routeplace">RoutePlace</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7SectionC12arrivalPlaceAA05RouteD0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/arrivalPlace"></a>
<a class="token" href="#/s:7heresdk7SectionC12arrivalPlaceAA05RouteD0Vvp">arrivalPlace</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The arrival place.
Describes the arrival place.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">arrivalPlace</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-routeplace">RoutePlace</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7SectionC21departureLocationTimeAA0dE0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/departureLocationTime"></a>
<a class="token" href="#/s:7heresdk7SectionC21departureLocationTimeAA0dE0VSgvp">departureLocationTime</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The departure location time of this section.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">departureLocationTime</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-locationtime">LocationTime</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7SectionC19arrivalLocationTimeAA0dE0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/arrivalLocationTime"></a>
<a class="token" href="#/s:7heresdk7SectionC19arrivalLocationTimeAA0dE0VSgvp">arrivalLocationTime</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The arrival location time of this section.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">arrivalLocationTime</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-locationtime">LocationTime</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7SectionC10preActionsSayAA9PreActionVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/preActions"></a>
<a class="token" href="#/s:7heresdk7SectionC10preActionsSayAA9PreActionVGvp">preActions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The preceding actions that must be done prior to departure at the beginning of the section.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">private(set)</span> <span class="kd">lazy</span> <span class="k">var</span> <span class="nv">preActions</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-preaction">PreAction</a></span><span class="p">]</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7SectionC11postActionsSayAA10PostActionVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/postActions"></a>
<a class="token" href="#/s:7heresdk7SectionC11postActionsSayAA10PostActionVGvp">postActions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The post actions that must be done after the arrival at the end of the section.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">private(set)</span> <span class="kd">lazy</span> <span class="k">var</span> <span class="nv">postActions</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-postaction">PostAction</a></span><span class="p">]</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7SectionC14sectionNoticesSayAA0B6NoticeVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/sectionNotices"></a>
<a class="token" href="#/s:7heresdk7SectionC14sectionNoticesSayAA0B6NoticeVGvp">sectionNotices</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The notices which explain the issues encountered during processing of this section.
For example, while the scooter transport mode is selected, if no reasonable alternative route is
possible except violating controlled-access to highway rule for the section, one notice is generated
for the violation. The user must judge all the notices carefully before proceeding.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">private(set)</span> <span class="kd">lazy</span> <span class="k">var</span> <span class="nv">sectionNotices</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-sectionnotice">SectionNotice</a></span><span class="p">]</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7SectionC06indoorB7DetailsAA06IndoorbD0CSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/indoorSectionDetails"></a>
<a class="token" href="#/s:7heresdk7SectionC06indoorB7DetailsAA06IndoorbD0CSgvp">indoorSectionDetails</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indoor routing section information.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">indoorSectionDetails</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-indoorsectiondetails">IndoorSectionDetails</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7SectionC26consumptionInKilowattHoursSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/consumptionInKilowattHours"></a>
<a class="token" href="#/s:7heresdk7SectionC26consumptionInKilowattHoursSdSgvp">consumptionInKilowattHours</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Estimated net energy consumption (in kWh) if the transportation mode used for this route
is an electric vehicle. Note that it can be negative due to energy recuperation.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">consumptionInKilowattHours</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7SectionC14transitDetailsAA07TransitbD0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/transitDetails"></a>
<a class="token" href="#/s:7heresdk7SectionC14transitDetailsAA07TransitbD0VSgvp">transitDetails</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The transit details which are avilable for transit sections of a route.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">transitDetails</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-transitsectiondetails">TransitSectionDetails</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7SectionC5tollsSayAA4TollVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/tolls"></a>
<a class="token" href="#/s:7heresdk7SectionC5tollsSayAA4TollVGvp">tolls</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>All the tolls for this section.
Note that tolls are found depending on the transport mode.
For example, if pedestrian or bicycle transport mode specified, route sections have no tolls. Indoor
route sections have no tolls, too.
<strong>Note</strong>: If you’re using the <code><a href="sdk-for-ios-navigate-api-reference-..-classes-offlineroutingengine">OfflineRoutingEngine</a></code>, be aware that this feature is
currently in <strong>beta</strong>. As a result, there may be some bugs or unexpected behaviors.
Additionally, this feature and related APIs may be updated in future releases
without going through the deprecation process. Note that the <code><a href="sdk-for-ios-navigate-api-reference-..-classes-offlineroutingengine">OfflineRoutingEngine</a></code>
is only available with the Navigate license. If you’re using the
<code><a href="sdk-for-ios-navigate-api-reference-..-classes-routingengine">RoutingEngine</a></code>, this feature is considered to be stable.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">private(set)</span> <span class="kd">lazy</span> <span class="k">var</span> <span class="nv">tolls</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-toll">Toll</a></span><span class="p">]</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7SectionC16trafficIncidentsSayAA22TrafficIncidentOnRouteCGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/trafficIncidents"></a>
<a class="token" href="#/s:7heresdk7SectionC16trafficIncidentsSayAA22TrafficIncidentOnRouteCGvp">trafficIncidents</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of traffic incidents that are found on the section.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">private(set)</span> <span class="kd">lazy</span> <span class="k">var</span> <span class="nv">trafficIncidents</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-trafficincidentonroute">TrafficIncidentOnRoute</a></span><span class="p">]</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7SectionC8durationSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/duration"></a>
<a class="token" href="#/s:7heresdk7SectionC8durationSdvp">duration</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The estimated time in seconds needed to travel along this section, including
real-time traffic delays if available.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">duration</span><span class="p">:</span> <span class="kt">TimeInterval</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7SectionC12trafficDelaySdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/trafficDelay"></a>
<a class="token" href="#/s:7heresdk7SectionC12trafficDelaySdvp">trafficDelay</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The estimated extra time in seconds spent due to traffic delays along this section. Negative values
indicate that the route can be traversed faster than usual.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">trafficDelay</span><span class="p">:</span> <span class="kt">TimeInterval</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7SectionC20passthroughWaypointsSayAA19PassThroughWaypointVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/passthroughWaypoints"></a>
<a class="token" href="#/s:7heresdk7SectionC20passthroughWaypointsSayAA19PassThroughWaypointVGvp">passthroughWaypoints</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of passthrough waypoints in this section.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">passthroughWaypoints</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-passthroughwaypoint">PassThroughWaypoint</a></span><span class="p">]</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7SectionC21noThroughRestrictionsSayAA19ViolatedRestrictionVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/noThroughRestrictions"></a>
<a class="token" href="#/s:7heresdk7SectionC21noThroughRestrictionsSayAA19ViolatedRestrictionVGvp">noThroughRestrictions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of no through restriction
The no through restriction area is part of the road network that do not allow through traffic.
For example the <code>Resident only</code> sign indicates that vehicles are only allowed to enter this area if they are making a stop.
This area will be set only if <code>origin</code>, <code>destination</code> or <code>via</code> waypoint will be requested within the area.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">noThroughRestrictions</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-violatedrestriction">ViolatedRestriction</a></span><span class="p">]</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
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

</div>
`
}</HTMLBlock>
