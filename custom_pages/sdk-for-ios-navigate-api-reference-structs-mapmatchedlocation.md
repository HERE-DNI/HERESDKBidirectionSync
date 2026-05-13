---
title: "Untitled"
slug: "sdk-for-ios-navigate-api-reference-structs-mapmatchedlocation"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- MapMatchedLocation.html -->
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/MapMatchedLocation"></a>
<a title="MapMatchedLocation Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-navigation">Navigation</a>
<img alt="" id="carat" src="../img/carat.png"/>
        MapMatchedLocation Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>MapMatchedLocation</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">MapMatchedLocation</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Describes a map-matched location in the world at a given time.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18MapMatchedLocationV11coordinatesAA14GeoCoordinatesVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/coordinates"></a>
<a class="token" href="#/s:7heresdk18MapMatchedLocationV11coordinatesAA14GeoCoordinatesVvp">coordinates</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The geographic coordinates of the map-matched location.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">coordinates</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-geocoordinates">GeoCoordinates</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18MapMatchedLocationV16bearingInDegreesSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/bearingInDegrees"></a>
<a class="token" href="#/s:7heresdk18MapMatchedLocationV16bearingInDegreesSdSgvp">bearingInDegrees</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The bearing orientation points to the direction of travel, and has the same angle as the
street where it is matched to. Therefore, it must not necessarily be the same as the
bearing of a location source.
Starts at 0 in the geographic north and rotates in a clockwise direction around the
compass. It means that for going north it’s equal to 0, for northeast it’s equal to 45,
for east it’s equal to 90, and so on.
If it cannot be determined, the value is <code>nil</code>. Otherwise, it is guaranteed to be in the
range [0, 360).</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">bearingInDegrees</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18MapMatchedLocationV16segmentReferenceAA07SegmentF0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/segmentReference"></a>
<a class="token" href="#/s:7heresdk18MapMatchedLocationV16segmentReferenceAA07SegmentF0Vvp">segmentReference</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Reference to the current segment.
The ratio of <code><a href="../Structs/MapMatchedLocation.html#/s:7heresdk18MapMatchedLocationV26segmentOffsetInCentimeterss6UInt32Vvp">MapMatchedLocation.segmentOffsetInCentimeters</a></code> to the segment length is
between <code><a href="../Structs/SegmentReference.html#/s:7heresdk16SegmentReferenceV11offsetStartSdvp">SegmentReference.offsetStart</a></code> and <code><a href="../Structs/SegmentReference.html#/s:7heresdk16SegmentReferenceV9offsetEndSdvp">SegmentReference.offsetEnd</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">segmentReference</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-segmentreference">SegmentReference</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18MapMatchedLocationV26segmentOffsetInCentimeterss6UInt32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/segmentOffsetInCentimeters"></a>
<a class="token" href="#/s:7heresdk18MapMatchedLocationV26segmentOffsetInCentimeterss6UInt32Vvp">segmentOffsetInCentimeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Offset from start of segment in centimeters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">segmentOffsetInCentimeters</span><span class="p">:</span> <span class="kt">UInt32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18MapMatchedLocationV10confidenceSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/confidence"></a>
<a class="token" href="#/s:7heresdk18MapMatchedLocationV10confidenceSdvp">confidence</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Confidence level (between 0 and 1) of the matched location.
A low confidence value means that the map-matched vehicle location is not reliable and it may
not be clear which part of the road the vehicle has taken. This can happen when the accuracy
or frequency of the provided location updates is poor. If the confidence level is too small
then, for example, overspeed warnings may be also inaccurate.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">confidence</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18MapMatchedLocationV22isDrivingInTheWrongWaySbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isDrivingInTheWrongWay"></a>
<a class="token" href="#/s:7heresdk18MapMatchedLocationV22isDrivingInTheWrongWaySbvp">isDrivingInTheWrongWay</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Determines if the travel direction on a one-way street is against the allowed traffic direction.
For two-way streets, this value is always <code>false</code>.
This feature is supported in tracking mode and when deviating from a route.
Note that the travel direction is determined based on the map-matched location.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isDrivingInTheWrongWay</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18MapMatchedLocationV26horizontalAccuracyInMetersSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/horizontalAccuracyInMeters"></a>
<a class="token" href="#/s:7heresdk18MapMatchedLocationV26horizontalAccuracyInMetersSdSgvp">horizontalAccuracyInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Horizontal accuracy measure of location.
Estimated based on accuracy of input location and confidence of this map-matched location.
Currently this value is not being provided by the Navigator.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">horizontalAccuracyInMeters</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18MapMatchedLocationV22speedInMetersPerSecondSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/speedInMetersPerSecond"></a>
<a class="token" href="#/s:7heresdk18MapMatchedLocationV22speedInMetersPerSecondSdSgvp">speedInMetersPerSecond</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Speed in meters per second.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">speedInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18MapMatchedLocationV9timestamp10Foundation4DateVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/timestamp"></a>
<a class="token" href="#/s:7heresdk18MapMatchedLocationV9timestamp10Foundation4DateVSgvp">timestamp</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Timestamp of the map matched position.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">timestamp</span><span class="p">:</span> <span class="kt">Date</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18MapMatchedLocationV11coordinates16bearingInDegrees16segmentReference0i6OffsetG11Centimeters10confidence09isDrivingG11TheWrongWay018horizontalAccuracyG6Meters05speedgU9PerSecond9timestampAcA14GeoCoordinatesV_SdSgAA07SegmentJ0Vs6UInt32VSdSbA2O10Foundation4DateVSgtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(coordinates:bearingInDegrees:segmentReference:segmentOffsetInCentimeters:confidence:isDrivingInTheWrongWay:horizontalAccuracyInMeters:speedInMetersPerSecond:timestamp:)"></a>
<a class="token" href="#/s:7heresdk18MapMatchedLocationV11coordinates16bearingInDegrees16segmentReference0i6OffsetG11Centimeters10confidence09isDrivingG11TheWrongWay018horizontalAccuracyG6Meters05speedgU9PerSecond9timestampAcA14GeoCoordinatesV_SdSgAA07SegmentJ0Vs6UInt32VSdSbA2O10Foundation4DateVSgtcfc">init(coordinates:<wbr/>bearingInDegrees:<wbr/>segmentReference:<wbr/>segmentOffsetInCentimeters:<wbr/>confidence:<wbr/>isDrivingInTheWrongWay:<wbr/>horizontalAccuracyInMeters:<wbr/>speedInMetersPerSecond:<wbr/>timestamp:<wbr/>)</a>
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
<li>coordinates: The geographic coordinates of the map-matched location.</li>
<li>bearingInDegrees: The bearing orientation points to the direction of travel, and has the same angle as the
street where it is matched to. Therefore, it must not necessarily be the same as the
bearing of a location source.
Starts at 0 in the geographic north and rotates in a clockwise direction around the
compass. It means that for going north it’s equal to 0, for northeast it’s equal to 45,
for east it’s equal to 90, and so on.
If it cannot be determined, the value is <code>nil</code>. Otherwise, it is guaranteed to be in the
range [0, 360).</li>
<li>segmentReference: Reference to the current segment.
The ratio of <code><a href="../Structs/MapMatchedLocation.html#/s:7heresdk18MapMatchedLocationV26segmentOffsetInCentimeterss6UInt32Vvp">MapMatchedLocation.segmentOffsetInCentimeters</a></code> to the segment length is
between <code><a href="../Structs/SegmentReference.html#/s:7heresdk16SegmentReferenceV11offsetStartSdvp">SegmentReference.offsetStart</a></code> and <code><a href="../Structs/SegmentReference.html#/s:7heresdk16SegmentReferenceV9offsetEndSdvp">SegmentReference.offsetEnd</a></code>.</li>
<li>segmentOffsetInCentimeters: Offset from start of segment in centimeters.</li>
<li>confidence: Confidence level (between 0 and 1) of the matched location.
A low confidence value means that the map-matched vehicle location is not reliable and it may
not be clear which part of the road the vehicle has taken. This can happen when the accuracy
or frequency of the provided location updates is poor. If the confidence level is too small
then, for example, overspeed warnings may be also inaccurate.</li>
<li>isDrivingInTheWrongWay: Determines if the travel direction on a one-way street is against the allowed traffic direction.
For two-way streets, this value is always <code>false</code>.
This feature is supported in tracking mode and when deviating from a route.
Note that the travel direction is determined based on the map-matched location.</li>
<li>horizontalAccuracyInMeters: Horizontal accuracy measure of location.
Estimated based on accuracy of input location and confidence of this map-matched location.
Currently this value is not being provided by the Navigator.</li>
<li>speedInMetersPerSecond: Speed in meters per second.</li>
</ul>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
  behaviors. Related APIs may change for new releases without a deprecation process.</p>
<ul>
<li>timestamp: Timestamp of the map matched position.</li>
</ul>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
  behaviors. Related APIs may change for new releases without a deprecation process.</p></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">coordinates</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-geocoordinates">GeoCoordinates</a></span><span class="p">,</span> <span class="nv">bearingInDegrees</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">segmentReference</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-segmentreference">SegmentReference</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-segmentreference">SegmentReference</a></span><span class="p">(),</span> <span class="nv">segmentOffsetInCentimeters</span><span class="p">:</span> <span class="kt">UInt32</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nv">confidence</span><span class="p">:</span> <span class="kt">Double</span> <span class="o">=</span> <span class="mf">0.0</span><span class="p">,</span> <span class="nv">isDrivingInTheWrongWay</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">horizontalAccuracyInMeters</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">speedInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">timestamp</span><span class="p">:</span> <span class="kt">Date</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
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
