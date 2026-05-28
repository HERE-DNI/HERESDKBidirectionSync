---
title: "MapData"
slug: "sdk-for-ios-navigate-api-reference-mapdata"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Section/MapData"></a>
<a title="MapData  Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="img/carat.png"/>
        MapData  Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>MapData</h1>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19AdministrativeRulesV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/AdministrativeRules"></a>
<a class="token" href="#/s:7heresdk19AdministrativeRulesV">AdministrativeRules</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents a set of administrative rules for a country or a state.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-administrativerules">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">AdministrativeRules</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25AdministrativeRulesLoaderC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/AdministrativeRulesLoader"></a>
<a class="token" href="#/s:7heresdk25AdministrativeRulesLoaderC">AdministrativeRulesLoader</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Provides the protocol for the access to the administrative rules available
for a country or a state in the local OCM map. Please be aware that the methods within this
classload map data synchronously. In the event of absent data in the disk cache, the data
will be retrieved from the remote server. To mitigate the potential freezing of the calling
thread, it is advisable to proactively prefetch map data around the working area.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-classes-administrativerulesloader">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">AdministrativeRulesLoader</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">AdministrativeRulesLoader</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">AdministrativeRulesLoader</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21AllowedTransportModesV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/AllowedTransportModes"></a>
<a class="token" href="#/s:7heresdk21AllowedTransportModesV">AllowedTransportModes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies which transport modes are allowed in a particular direction.</p>
<p><strong>Note:</strong> This struct specifies a general restriction to that transport mode,
but additional restriction are possible.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-allowedtransportmodes">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">AllowedTransportModes</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24BloodAlcoholContentLimitV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/BloodAlcoholContentLimit"></a>
<a class="token" href="#/s:7heresdk24BloodAlcoholContentLimitV">BloodAlcoholContentLimit</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents the rules regarding alcohol in blood content limit in a country or state for
all types of drivers.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-bloodalcoholcontentlimit">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">BloodAlcoholContentLimit</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12ConnectivityV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/Connectivity"></a>
<a class="token" href="#/s:7heresdk12ConnectivityV">Connectivity</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A struct that provides information about link id and accessibility.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-connectivity">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">Connectivity</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20DirectedOCMSegmentIdV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/DirectedOCMSegmentId"></a>
<a class="token" href="#/s:7heresdk20DirectedOCMSegmentIdV">DirectedOCMSegmentId</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>OCM Segment ID with travel direction of segment.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-directedocmsegmentid">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">DirectedOCMSegmentId</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22DownloadingFileOptionsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/DownloadingFileOptions"></a>
<a class="token" href="#/s:7heresdk22DownloadingFileOptionsV">DownloadingFileOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A struct which identifies the configuration when downloading a file reference.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-downloadingfileoptions">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">DownloadingFileOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11DrivingSideO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/DrivingSide"></a>
<a class="token" href="#/s:7heresdk11DrivingSideO">DrivingSide</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The side of the road on which the driving is done.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-enums-drivingside">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">DrivingSide</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13FileReferenceV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/FileReference"></a>
<a class="token" href="#/s:7heresdk13FileReferenceV">FileReference</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A struct that provides information for a file reference.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-filereference">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">FileReference</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17FileReferenceTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/FileReferenceType"></a>
<a class="token" href="#/s:7heresdk17FileReferenceTypeO">FileReferenceType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Type of reference file.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-enums-filereferencetype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">FileReferenceType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21HeadlightsRequirementO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/HeadlightsRequirement"></a>
<a class="token" href="#/s:7heresdk21HeadlightsRequirementO">HeadlightsRequirement</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The situations in which headlights are required to be turned on.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-enums-headlightsrequirement">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">HeadlightsRequirement</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13LaneAttributeV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/LaneAttribute"></a>
<a class="token" href="#/s:7heresdk13LaneAttributeV">LaneAttribute</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A struct that describes attributes assigned to a specific section of a lane.
It includes lane markings, allowed travel directions, tolling info, access restrictions, and optional lane type.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-laneattribute">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">LaneAttribute</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23LocalRoadCharacteristicO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/LocalRoadCharacteristic"></a>
<a class="token" href="#/s:7heresdk23LocalRoadCharacteristicO">LocalRoadCharacteristic</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies the local road characteristics: frontage, parking lot road, poi access.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-enums-localroadcharacteristic">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">LocalRoadCharacteristic</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18MapDataLoaderErrora"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/MapDataLoaderError"></a>
<a class="token" href="#/s:7heresdk18MapDataLoaderErrora">MapDataLoaderError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Error occurred during obtaining data form the map. <code><a href="sdk-for-ios-navigate-api-reference-enums-mapdataloadererrorcode">MapDataLoaderErrorCode</a></code> represents possible errors.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">MapDataLoaderError</span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-mapdataloadererrorcode">MapDataLoaderErrorCode</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22MapDataLoaderErrorCodeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/MapDataLoaderErrorCode"></a>
<a class="token" href="#/s:7heresdk22MapDataLoaderErrorCodeO">MapDataLoaderErrorCode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies possible errors from map data accessing.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-enums-mapdataloadererrorcode">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">MapDataLoaderErrorCode</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapDataLoaderErrorCode</span> <span class="p">:</span> <span class="kt">Error</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12OCMSegmentIdV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/OCMSegmentId"></a>
<a class="token" href="#/s:7heresdk12OCMSegmentIdV">OCMSegmentId</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>OCM Segment ID of particular matched <code><a href="sdk-for-ios-navigate-api-reference-structs-segmentreference">SegmentReference</a></code> from OCM map,
represented in form: Tile + Local ID’s .</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-ocmsegmentid">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">OCMSegmentId</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21ParkingSideRegulationO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/ParkingSideRegulation"></a>
<a class="token" href="#/s:7heresdk21ParkingSideRegulationO">ParkingSideRegulation</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The regulations for parking on the side of the road.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-enums-parkingsideregulation">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">ParkingSideRegulation</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18PhysicalAttributesV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/PhysicalAttributes"></a>
<a class="token" href="#/s:7heresdk18PhysicalAttributesV">PhysicalAttributes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Physical attributes of the segment.</p>
<p><strong><em>Note</em></strong> a road can have more than one attribute at the same time.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-physicalattributes">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">PhysicalAttributes</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15PreTripPlanningV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/PreTripPlanning"></a>
<a class="token" href="#/s:7heresdk15PreTripPlanningV">PreTripPlanning</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents the legal requirements to be considered before a trip for all vehicles types.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-pretripplanning">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">PreTripPlanning</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15RailwayCrossingV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/RailwayCrossing"></a>
<a class="token" href="#/s:7heresdk15RailwayCrossingV">RailwayCrossing</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Identifies the presence and the location of railway corssings.
Included in <code><a href="sdk-for-ios-navigate-api-reference-classes-segmentdata">SegmentData</a></code> only if <code><a href="Structs/SegmentDataLoaderOptions.html#/s:7heresdk24SegmentDataLoaderOptionsV20loadRailwayCrossingsSbvp">SegmentDataLoaderOptions.loadRailwayCrossings</a></code> is set to <code>true</code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-railwaycrossing">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RailwayCrossing</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19RailwayCrossingTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/RailwayCrossingType"></a>
<a class="token" href="#/s:7heresdk19RailwayCrossingTypeO">RailwayCrossingType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Type of railway crossing.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-enums-railwaycrossingtype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">RailwayCrossingType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11RoadDividerO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/RoadDivider"></a>
<a class="token" href="#/s:7heresdk11RoadDividerO">RoadDivider</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A physical structure or painted road marking intended to legally prohibit
left turns in right-side driving countries, right turns in left-side driving countries,
and U-turns at divided intersections or in the middle of divided segments.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-enums-roaddivider">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">RoadDivider</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10RoadUsagesV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/RoadUsages"></a>
<a class="token" href="#/s:7heresdk10RoadUsagesV">RoadUsages</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Road Usages of the segment.</p>
<p><strong><em>Note</em></strong> a road can have more than one attribute at the same time.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-roadusages">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RoadUsages</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21SegmentConnectivitiesV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/SegmentConnectivities"></a>
<a class="token" href="#/s:7heresdk21SegmentConnectivitiesV">SegmentConnectivities</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A struct that provides information about segment one direction source and target connectivities.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-segmentconnectivities">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">SegmentConnectivities</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11SegmentDataC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/SegmentData"></a>
<a class="token" href="#/s:7heresdk11SegmentDataC">SegmentData</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Contains the requested information for a segment</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-classes-segmentdata">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">SegmentData</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">SegmentData</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">SegmentData</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17SegmentDataLoaderC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/SegmentDataLoader"></a>
<a class="token" href="#/s:7heresdk17SegmentDataLoaderC">SegmentDataLoader</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Provides the protocol for the access to the
segments data available in the local OCM map. Please be aware that the methods within this class
load map data synchronously. In the event of absent data in the disk cache, the data will be
retrieved from the remote server. To mitigate the potential freezing of the calling thread,
it is advisable to proactively prefetch map data around the working area.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-classes-segmentdataloader">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">SegmentDataLoader</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">SegmentDataLoader</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">SegmentDataLoader</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24SegmentDataLoaderOptionsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/SegmentDataLoaderOptions"></a>
<a class="token" href="#/s:7heresdk24SegmentDataLoaderOptionsV">SegmentDataLoaderOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies which data should be loaded by the <code><a href="Classes/SegmentDataLoader.html#/s:7heresdk17SegmentDataLoaderC04loadC07segment7optionsAA0bC0CAA12OCMSegmentIdV_AA0bcD7OptionsVtKF">SegmentDataLoader.loadData(...)</a></code> or <code><a href="Classes/SegmentDataLoader.html#/s:7heresdk17SegmentDataLoaderC012loadDirectedbC07segment7optionsAA0bC0CAA0F12OCMSegmentIdV_AA0bcD7OptionsVtKF">SegmentDataLoader.loadDirectedSegmentData(...)</a></code> function.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-segmentdataloaderoptions">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">SegmentDataLoaderOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25SegmentReferenceConverterC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/SegmentReferenceConverter"></a>
<a class="token" href="#/s:7heresdk25SegmentReferenceConverterC">SegmentReferenceConverter</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A SegmentReferenceConverter provides possibility to convert mapmatched instances of
<code><a href="sdk-for-ios-navigate-api-reference-structs-segmentreference">SegmentReference</a></code> to corresponding instances of <code><a href="sdk-for-ios-navigate-api-reference-structs-directedocmsegmentid">DirectedOCMSegmentId</a></code>.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-classes-segmentreferenceconverter">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">SegmentReferenceConverter</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">SegmentReferenceConverter</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">SegmentReferenceConverter</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15SegmentSpanDataC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/SegmentSpanData"></a>
<a class="token" href="#/s:7heresdk15SegmentSpanDataC">SegmentSpanData</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Contains attributes that are not necessarily constant on a full segment.
A Span is a portion of a Segment where the requested attributes are constant.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-classes-segmentspandata">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">SegmentSpanData</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">SegmentSpanData</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">SegmentSpanData</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk28SegmentSpecialSpeedSituationV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/SegmentSpecialSpeedSituation"></a>
<a class="token" href="#/s:7heresdk28SegmentSpecialSpeedSituationV">SegmentSpecialSpeedSituation</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A special speed situation indicates a speed that exists under special circumstances. It can be used to further refine
the estimation of traversal times, route calculation and calculation of route guidance timing.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-segmentspecialspeedsituation">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">SegmentSpecialSpeedSituation</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17SegmentSpeedLimitV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/SegmentSpeedLimit"></a>
<a class="token" href="#/s:7heresdk17SegmentSpeedLimitV">SegmentSpeedLimit</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Describes the posted speed limit on the segment span.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-segmentspeedlimit">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">SegmentSpeedLimit</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16SpecialSpeedTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/SpecialSpeedType"></a>
<a class="token" href="#/s:7heresdk16SpecialSpeedTypeO">SpecialSpeedType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents the speed situation type.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-enums-specialspeedtype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">SpecialSpeedType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8TollCostV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TollCost"></a>
<a class="token" href="#/s:7heresdk8TollCostV">TollCost</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Contains informations about the toll costs for a specific vehicle profile.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-tollcost">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TollCost</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9TollPointV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TollPoint"></a>
<a class="token" href="#/s:7heresdk9TollPointV">TollPoint</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A struct to represent the toll point attributes of a segment.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-tollpoint">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TollPoint</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13TollStructureV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TollStructure"></a>
<a class="token" href="#/s:7heresdk13TollStructureV">TollStructure</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A struct that defines tolling configuration for a lane.
It describes which types of toll structures apply and the acceptable payment methods.
This information can be used to guide drivers through toll roads based on their preferences or vehicle capabilities.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-tollstructure">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TollStructure</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21TollStructureManeuverV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TollStructureManeuver"></a>
<a class="token" href="#/s:7heresdk21TollStructureManeuverV">TollStructureManeuver</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A struct that provides information for a toll structure at a toll point.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-tollstructuremaneuver">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TollStructureManeuver</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17TollStructureTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/TollStructureType"></a>
<a class="token" href="#/s:7heresdk17TollStructureTypeO">TollStructureType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This enum defines the type of toll structure used on a road segment or lane.
Each value represents a different tolling mechanism used in road infrastructure.
This enum helps in providing detailed tolling information for routing and navigation.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-enums-tollstructuretype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">TollStructureType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10TollSystemV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TollSystem"></a>
<a class="token" href="#/s:7heresdk10TollSystemV">TollSystem</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Contains informations about a toll system.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-tollsystem">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TollSystem</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13TrafficSignalV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TrafficSignal"></a>
<a class="token" href="#/s:7heresdk13TrafficSignalV">TrafficSignal</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Identifies the presence and the location of traffic lights at an intersection</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-trafficsignal">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TrafficSignal</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21TrafficSignalLocationO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/TrafficSignalLocation"></a>
<a class="token" href="#/s:7heresdk21TrafficSignalLocationO">TrafficSignalLocation</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates the location of a traffic signal.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-enums-trafficsignallocation">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">TrafficSignalLocation</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19TurnOnRedRegulationO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/TurnOnRedRegulation"></a>
<a class="token" href="#/s:7heresdk19TurnOnRedRegulationO">TurnOnRedRegulation</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The regulations for turning on the red color of the traffic light.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-enums-turnonredregulation">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">TurnOnRedRegulation</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
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
}</HTMLBlock>
