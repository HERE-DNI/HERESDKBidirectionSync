---
title: "MapData / SegmentData"
slug: "sdk-for-ios-navigate-api-reference-classes-segmentdata"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/SegmentData"></a>
<a title="SegmentData Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-mapdata">MapData</a>
<img alt="" id="carat" src="../img/carat.png"/>
        SegmentData Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>SegmentData</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">SegmentData</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">SegmentData</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">SegmentData</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Contains the requested information for a segment</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11SegmentDataC03ocmB2IdAA010OCMSegmentE0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/ocmSegmentId"></a>
<a class="token" href="#/s:7heresdk11SegmentDataC03ocmB2IdAA010OCMSegmentE0Vvp">ocmSegmentId</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The <code><a href="sdk-for-ios-navigate-api-reference-..-structs-ocmsegmentid">OCMSegmentId</a></code> object representing the segment</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">ocmSegmentId</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-ocmsegmentid">OCMSegmentId</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11SegmentDataC16segmentReferenceAA0bE0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/segmentReference"></a>
<a class="token" href="#/s:7heresdk11SegmentDataC16segmentReferenceAA0bE0Vvp">segmentReference</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The <code><a href="sdk-for-ios-navigate-api-reference-..-structs-segmentreference">SegmentReference</a></code> object representing the segment</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">segmentReference</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-segmentreference">SegmentReference</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11SegmentDataC8polylineAA11GeoPolylineVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/polyline"></a>
<a class="token" href="#/s:7heresdk11SegmentDataC8polylineAA11GeoPolylineVvp">polyline</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The <code><a href="sdk-for-ios-navigate-api-reference-..-structs-geopolyline">GeoPolyline</a></code> object representing the polyline of this segment.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">private(set)</span> <span class="kd">lazy</span> <span class="k">var</span> <span class="nv">polyline</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-geopolyline">GeoPolyline</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11SegmentDataC14lengthInMeterss5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/lengthInMeters"></a>
<a class="token" href="#/s:7heresdk11SegmentDataC14lengthInMeterss5Int32Vvp">lengthInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The length of this segment in meters. This information is based on map data.
It can differ from the length of <code><a href="../Classes/SegmentData.html#/s:7heresdk11SegmentDataC8polylineAA11GeoPolylineVvp">SegmentData.polyline</a></code> due to
approximations of the polyline.</p>
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
<a name="/s:7heresdk11SegmentDataC5spansSayAA0b4SpanC0CGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/spans"></a>
<a class="token" href="#/s:7heresdk11SegmentDataC5spansSayAA0b4SpanC0CGvp">spans</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of <code><a href="sdk-for-ios-navigate-api-reference-..-classes-segmentspandata">SegmentSpanData</a></code> of the given segment for the
requested attributes
<strong>Note:</strong> If no span attributes is requested, the list will be empty.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">spans</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-segmentspandata">SegmentSpanData</a></span><span class="p">]</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11SegmentDataC14trafficSignalsSayAA13TrafficSignalVGSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/trafficSignals"></a>
<a class="token" href="#/s:7heresdk11SegmentDataC14trafficSignalsSayAA13TrafficSignalVGSgvp">trafficSignals</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of <code><a href="sdk-for-ios-navigate-api-reference-..-structs-trafficsignal">TrafficSignal</a></code> of the given segment.
Returns an empty list if no data is found.
Returns <code>nil</code> if <code><a href="../Structs/SegmentDataLoaderOptions.html#/s:7heresdk24SegmentDataLoaderOptionsV18loadTrafficSignalsSbvp">SegmentDataLoaderOptions.loadTrafficSignals</a></code> is set to <code>false</code>.
The <code><a href="sdk-for-ios-navigate-api-reference-..-enums-trafficsignallocation">TrafficSignalLocation</a></code> indicates the location of a single traffic signal, which can be any combination of left, right and overhead.
The <code><a href="../Structs/TrafficSignal.html#/s:7heresdk13TrafficSignalV14offsetInMeterss5Int32Vvp">TrafficSignal.offsetInMeters</a></code> is the location along the segment,
while the traffic signal location have details on how the traffic signal is display/deploy in that specific location in the segment.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">trafficSignals</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-trafficsignal">TrafficSignal</a></span><span class="p">]?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11SegmentDataC9roadSignsSayAA8RoadSignVGSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/roadSigns"></a>
<a class="token" href="#/s:7heresdk11SegmentDataC9roadSignsSayAA8RoadSignVGSgvp">roadSigns</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of <code><a href="sdk-for-ios-navigate-api-reference-..-structs-roadsign">RoadSign</a></code> of the given segment.
Returns <code>nil</code> if <code><a href="../Structs/SegmentDataLoaderOptions.html#/s:7heresdk24SegmentDataLoaderOptionsV13loadRoadSignsSbvp">SegmentDataLoaderOptions.loadRoadSigns</a></code> is set to <code>false</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">roadSigns</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-roadsign">RoadSign</a></span><span class="p">]?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11SegmentDataC16railwayCrossingsSayAA15RailwayCrossingVGSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/railwayCrossings"></a>
<a class="token" href="#/s:7heresdk11SegmentDataC16railwayCrossingsSayAA15RailwayCrossingVGSgvp">railwayCrossings</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of <code><a href="sdk-for-ios-navigate-api-reference-..-structs-railwaycrossing">RailwayCrossing</a></code> of the given segment.
Returns an empty list if no data is found.
Returns <code>nil</code> if <code><a href="../Structs/SegmentDataLoaderOptions.html#/s:7heresdk24SegmentDataLoaderOptionsV20loadRailwayCrossingsSbvp">SegmentDataLoaderOptions.loadRailwayCrossings</a></code> is set to <code>false</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">railwayCrossings</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-railwaycrossing">RailwayCrossing</a></span><span class="p">]?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11SegmentDataC10tollPointsSayAA9TollPointVGSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/tollPoints"></a>
<a class="token" href="#/s:7heresdk11SegmentDataC10tollPointsSayAA9TollPointVGSgvp">tollPoints</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of <code><a href="sdk-for-ios-navigate-api-reference-..-structs-tollpoint">TollPoint</a></code> of the given segment.
Returns an empty list if no data is found.
Returns <code>nil</code> if <code><a href="../Structs/SegmentDataLoaderOptions.html#/s:7heresdk24SegmentDataLoaderOptionsV14loadTollPointsSbvp">SegmentDataLoaderOptions.loadTollPoints</a></code> is set to <code>false</code>
or the <code>SegmentData</code> is not initialized using <code><a href="../Classes/SegmentDataLoader.html#/s:7heresdk17SegmentDataLoaderC012loadDirectedbC07segment7optionsAA0bC0CAA0F12OCMSegmentIdV_AA0bcD7OptionsVtKF">SegmentDataLoader.loadDirectedSegmentData(...)</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">tollPoints</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-tollpoint">TollPoint</a></span><span class="p">]?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
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
