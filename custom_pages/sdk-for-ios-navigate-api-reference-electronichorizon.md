---
title: "ElectronicHorizon"
slug: "sdk-for-ios-navigate-api-reference-electronichorizon"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Section/ElectronicHorizon"></a>
<a title="ElectronicHorizon  Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

        ElectronicHorizon  Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>ElectronicHorizon</h1>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17ElectronicHorizonV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ElectronicHorizon"></a>
<a class="token" href="#/s:7heresdk17ElectronicHorizonV">ElectronicHorizon</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A struct containing the full set of available paths
predicted for the current vehicle state.</p>
<p>Represents a snapshot of the horizon estimation at the moment the update
was generated.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-electronichorizon">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ElectronicHorizon</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27ElectronicHorizonDataLoaderC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/ElectronicHorizonDataLoader"></a>
<a class="token" href="#/s:7heresdk27ElectronicHorizonDataLoaderC">ElectronicHorizonDataLoader</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Loads map data for segments that belong to the <code><a href="sdk-for-ios-navigate-api-reference-classes-electronichorizonengine">ElectronicHorizonEngine</a></code> paths.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
<p>Offline availability: This property is available online and offline.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-classes-electronichorizondataloader">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">ElectronicHorizonDataLoader</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">ElectronicHorizonDataLoader</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">ElectronicHorizonDataLoader</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk36ElectronicHorizonDataLoaderErrorCodeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/ElectronicHorizonDataLoaderErrorCode"></a>
<a class="token" href="#/s:7heresdk36ElectronicHorizonDataLoaderErrorCodeO">ElectronicHorizonDataLoaderErrorCode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents error codes that describe the result of the <code><a href="Classes/ElectronicHorizonDataLoader.html#/s:7heresdk27ElectronicHorizonDataLoaderC10getSegment9segmentIdAA0bcdE6ResultVAA018DirectedOCMSegmentI0V_tF">ElectronicHorizonDataLoader.getSegment(...)</a></code> method.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
<p>Offline availability: This property is available online and offline.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-enums-electronichorizondataloadererrorcode">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">ElectronicHorizonDataLoaderErrorCode</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk33ElectronicHorizonDataLoaderResultV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ElectronicHorizonDataLoaderResult"></a>
<a class="token" href="#/s:7heresdk33ElectronicHorizonDataLoaderResultV">ElectronicHorizonDataLoaderResult</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents the result of a data loading operation performed by <code><a href="sdk-for-ios-navigate-api-reference-classes-electronichorizondataloader">ElectronicHorizonDataLoader</a></code>.
The result contains either the loaded segment data or an error code.</p>
<p>Note: This is a <strong>beta</strong> release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-electronichorizondataloaderresult">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ElectronicHorizonDataLoaderResult</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk33ElectronicHorizonDataLoadedStatusO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/ElectronicHorizonDataLoadedStatus"></a>
<a class="token" href="#/s:7heresdk33ElectronicHorizonDataLoadedStatusO">ElectronicHorizonDataLoadedStatus</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents the status of data that was loaded by <code><a href="sdk-for-ios-navigate-api-reference-classes-electronichorizondataloader">ElectronicHorizonDataLoader</a></code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-enums-electronichorizondataloadedstatus">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">ElectronicHorizonDataLoadedStatus</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk41ElectronicHorizonDataLoaderStatusDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/ElectronicHorizonDataLoaderStatusDelegate"></a>
<a class="token" href="#/s:7heresdk41ElectronicHorizonDataLoaderStatusDelegateP">ElectronicHorizonDataLoaderStatusDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Provides a delegate for status updates from the <code><a href="Classes/ElectronicHorizonDataLoader.html#/s:7heresdk27ElectronicHorizonDataLoaderC04loadD0010electronicC6UpdateyAA0bcH0V_tF">ElectronicHorizonDataLoader.loadData(...)</a></code> method.
The listener receives the current state for different levels of the paths as <code><a href="sdk-for-ios-navigate-api-reference-enums-electronichorizondataloadedstatus">ElectronicHorizonDataLoadedStatus</a></code>.</p>
<p>Note: This is a <strong>beta</strong> release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<p>Offline availability: This property is available online and offline.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-protocols-electronichorizondataloaderstatusdelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">ElectronicHorizonDataLoaderStatusDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25ElectronicHorizonDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/ElectronicHorizonDelegate"></a>
<a class="token" href="#/s:7heresdk25ElectronicHorizonDelegateP">ElectronicHorizonDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Provides a delegate for receiving updates during execution of the <code><a href="Classes/ElectronicHorizonEngine.html#/s:7heresdk23ElectronicHorizonEngineC6update18mapMatchedLocationyAA03MapgH0V_tF">ElectronicHorizonEngine.update(...)</a></code> method.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
<p>Offline availability: This property is available online and offline.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-protocols-electronichorizondelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">ElectronicHorizonDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23ElectronicHorizonEngineC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/ElectronicHorizonEngine"></a>
<a class="token" href="#/s:7heresdk23ElectronicHorizonEngineC">ElectronicHorizonEngine</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Provides an electronic horizon engine that continuously predicts
the road network ahead of the vehicle by using detailed map data, including road topography that is
currently out of sight.
You can subscribe to electronic horizon updates based on position updates by using <code><a href="sdk-for-ios-navigate-api-reference-protocols-electronichorizondelegate">ElectronicHorizonDelegate</a></code>.
For more information about sub path levels, see <code><a href="Structs/ElectronicHorizonOptions.html#/s:7heresdk24ElectronicHorizonOptionsV26lookAheadDistancesInMetersSaySdGvp">ElectronicHorizonOptions.lookAheadDistancesInMeters</a></code>.</p>
<p>The electronic horizon engine uses map-matched locations and can optionally use a <code><a href="sdk-for-ios-navigate-api-reference-classes-route">Route</a></code>
to improve the most-preferred path (MPP).</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-classes-electronichorizonengine">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">ElectronicHorizonEngine</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">ElectronicHorizonEngine</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">ElectronicHorizonEngine</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk26ElectronicHorizonErrorCodeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/ElectronicHorizonErrorCode"></a>
<a class="token" href="#/s:7heresdk26ElectronicHorizonErrorCodeO">ElectronicHorizonErrorCode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents error codes that describe the result of the <code><a href="Classes/ElectronicHorizonEngine.html#/s:7heresdk23ElectronicHorizonEngineC6update18mapMatchedLocationyAA03MapgH0V_tF">ElectronicHorizonEngine.update(...)</a></code> method.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
<p>Offline availability: This property is available online and offline.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-enums-electronichorizonerrorcode">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">ElectronicHorizonErrorCode</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24ElectronicHorizonOptionsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ElectronicHorizonOptions"></a>
<a class="token" href="#/s:7heresdk24ElectronicHorizonOptionsV">ElectronicHorizonOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Provides options to configure <code><a href="sdk-for-ios-navigate-api-reference-classes-electronichorizonengine">ElectronicHorizonEngine</a></code>.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-electronichorizonoptions">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ElectronicHorizonOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21ElectronicHorizonPathV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ElectronicHorizonPath"></a>
<a class="token" href="#/s:7heresdk21ElectronicHorizonPathV">ElectronicHorizonPath</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents a single electronic horizon path.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-electronichorizonpath">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ElectronicHorizonPath</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25ElectronicHorizonPositionV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ElectronicHorizonPosition"></a>
<a class="token" href="#/s:7heresdk25ElectronicHorizonPositionV">ElectronicHorizonPosition</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Provides a position on an electronic horizon path with a reference to the current item in the <code><a href="sdk-for-ios-navigate-api-reference-structs-electronichorizon">ElectronicHorizon</a></code>.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-electronichorizonposition">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ElectronicHorizonPosition</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24ElectronicHorizonSegmentV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ElectronicHorizonSegment"></a>
<a class="token" href="#/s:7heresdk24ElectronicHorizonSegmentV">ElectronicHorizonSegment</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents a segment in an <code><a href="sdk-for-ios-navigate-api-reference-structs-electronichorizonpath">ElectronicHorizonPath</a></code>.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-electronichorizonsegment">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ElectronicHorizonSegment</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk31ElectronicHorizonSegmentChangesV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ElectronicHorizonSegmentChanges"></a>
<a class="token" href="#/s:7heresdk31ElectronicHorizonSegmentChangesV">ElectronicHorizonSegmentChanges</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A struct describing the set of changes in horizon segments
between two consecutive updates.
Includes lists of both newly added and removed segments.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-electronichorizonsegmentchanges">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ElectronicHorizonSegmentChanges</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk26ElectronicHorizonSegmentIdV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ElectronicHorizonSegmentId"></a>
<a class="token" href="#/s:7heresdk26ElectronicHorizonSegmentIdV">ElectronicHorizonSegmentId</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Identifies a segment in an <code><a href="sdk-for-ios-navigate-api-reference-structs-electronichorizonpath">ElectronicHorizonPath</a></code>.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-electronichorizonsegmentid">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ElectronicHorizonSegmentId</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23ElectronicHorizonUpdateV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ElectronicHorizonUpdate"></a>
<a class="token" href="#/s:7heresdk23ElectronicHorizonUpdateV">ElectronicHorizonUpdate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A struct representing a full update delivered via <code><a href="sdk-for-ios-navigate-api-reference-protocols-electronichorizondelegate">ElectronicHorizonDelegate</a></code> notifications.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-electronichorizonupdate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ElectronicHorizonUpdate</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
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
