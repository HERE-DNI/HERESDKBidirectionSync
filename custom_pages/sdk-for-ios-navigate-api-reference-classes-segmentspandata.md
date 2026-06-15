---
title: "SegmentSpanData"
slug: "sdk-for-ios-navigate-api-reference-classes-segmentspandata"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/SegmentSpanData"></a>
<a title="SegmentSpanData Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-mapdata">MapData</a>

        SegmentSpanData Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>SegmentSpanData</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">SegmentSpanData</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">SegmentSpanData</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">SegmentSpanData</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Contains attributes that are not necessarily constant on a full segment.
A Span is a portion of a Segment where the requested attributes are constant.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15SegmentSpanDataC19startOffsetInMeterss5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/startOffsetInMeters"></a>
<a class="token" href="#/s:7heresdk15SegmentSpanDataC19startOffsetInMeterss5Int32Vvp">startOffsetInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Start offset.
The offset in meters from the beginning of the segment to the start of the span
in positive direction or from the end of the segment to the start of the span in negative direction.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">startOffsetInMeters</span><span class="p">:</span> <span class="kt">Int32</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15SegmentSpanDataC18spanLengthInMeterss5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/spanLengthInMeters"></a>
<a class="token" href="#/s:7heresdk15SegmentSpanDataC18spanLengthInMeterss5Int32Vvp">spanLengthInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The length of this span in meters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">spanLengthInMeters</span><span class="p">:</span> <span class="kt">Int32</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15SegmentSpanDataC15travelDirectionAA06TravelF0OSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/travelDirection"></a>
<a class="token" href="#/s:7heresdk15SegmentSpanDataC15travelDirectionAA06TravelF0OSgvp">travelDirection</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The <code><a href="sdk-for-ios-navigate-api-reference-enums-traveldirection">TravelDirection</a></code> object representing the allowed travel directions.
Gets the <code><a href="sdk-for-ios-navigate-api-reference-enums-traveldirection">TravelDirection</a></code> object for the portion of the segment.
Returns <code>nil</code> if <code><a href="../Structs/SegmentDataLoaderOptions.html#/s:7heresdk24SegmentDataLoaderOptionsV19loadTravelDirectionSbvp">SegmentDataLoaderOptions.loadTravelDirection</a></code> is set to <code>false</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">travelDirection</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-traveldirection">TravelDirection</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15SegmentSpanDataC21allowedTransportModesAA07AllowedfG0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/allowedTransportModes"></a>
<a class="token" href="#/s:7heresdk15SegmentSpanDataC21allowedTransportModesAA07AllowedfG0VSgvp">allowedTransportModes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The <code><a href="sdk-for-ios-navigate-api-reference-structs-allowedtransportmodes">AllowedTransportModes</a></code> object representing the allowed transport modes.
Returns <code>nil</code> if <code><a href="../Structs/SegmentDataLoaderOptions.html#/s:7heresdk24SegmentDataLoaderOptionsV24loadTransportModesAccessSbvp">SegmentDataLoaderOptions.loadTransportModesAccess</a></code> is set to <code>false</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">allowedTransportModes</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-allowedtransportmodes">AllowedTransportModes</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15SegmentSpanDataC19functionalRoadClassAA010FunctionalfG0OSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/functionalRoadClass"></a>
<a class="token" href="#/s:7heresdk15SegmentSpanDataC19functionalRoadClassAA010FunctionalfG0OSgvp">functionalRoadClass</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The <code><a href="sdk-for-ios-navigate-api-reference-enums-functionalroadclass">FunctionalRoadClass</a></code> object representing the polyline of this segment.
Returns <code>nil</code> if <code><a href="../Structs/SegmentDataLoaderOptions.html#/s:7heresdk24SegmentDataLoaderOptionsV23loadFunctionalRoadClassSbvp">SegmentDataLoaderOptions.loadFunctionalRoadClass</a></code> is set to <code>false</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">functionalRoadClass</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-functionalroadclass">FunctionalRoadClass</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15SegmentSpanDataC27positiveDirectionSpeedLimitAA0bgH0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/positiveDirectionSpeedLimit"></a>
<a class="token" href="#/s:7heresdk15SegmentSpanDataC27positiveDirectionSpeedLimitAA0bgH0VSgvp">positiveDirectionSpeedLimit</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The <code><a href="sdk-for-ios-navigate-api-reference-structs-segmentspeedlimit">SegmentSpeedLimit</a></code> object representing the speed limit of this segment span in the positive
tavel direction.
Returns <code>nil</code> if <code><a href="../Structs/SegmentDataLoaderOptions.html#/s:7heresdk24SegmentDataLoaderOptionsV15loadSpeedLimitsSbvp">SegmentDataLoaderOptions.loadSpeedLimits</a></code> is set to <code>false</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">positiveDirectionSpeedLimit</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-segmentspeedlimit">SegmentSpeedLimit</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15SegmentSpanDataC27negativeDirectionSpeedLimitAA0bgH0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/negativeDirectionSpeedLimit"></a>
<a class="token" href="#/s:7heresdk15SegmentSpanDataC27negativeDirectionSpeedLimitAA0bgH0VSgvp">negativeDirectionSpeedLimit</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The <code><a href="sdk-for-ios-navigate-api-reference-structs-segmentspeedlimit">SegmentSpeedLimit</a></code> object representing the speed limit of this segment span in the negative
travel direction.
Returns <code>nil</code> if <code><a href="../Structs/SegmentDataLoaderOptions.html#/s:7heresdk24SegmentDataLoaderOptionsV15loadSpeedLimitsSbvp">SegmentDataLoaderOptions.loadSpeedLimits</a></code> is set to <code>false</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">negativeDirectionSpeedLimit</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-segmentspeedlimit">SegmentSpeedLimit</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15SegmentSpanDataC10speedLimitAA0b5SpeedF0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/speedLimit"></a>
<a class="token" href="#/s:7heresdk15SegmentSpanDataC10speedLimitAA0b5SpeedF0VSgvp">speedLimit</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The <code><a href="sdk-for-ios-navigate-api-reference-structs-segmentspeedlimit">SegmentSpeedLimit</a></code> object representing the speed limit of this segment span.
Will be loaded if <code><a href="../Structs/SegmentDataLoaderOptions.html#/s:7heresdk24SegmentDataLoaderOptionsV15loadSpeedLimitsSbvp">SegmentDataLoaderOptions.loadSpeedLimits</a></code> is <code>true</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">speedLimit</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-segmentspeedlimit">SegmentSpeedLimit</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15SegmentSpanDataC43positiveDirectionBaseSpeedInMetersPerSecondSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/positiveDirectionBaseSpeedInMetersPerSecond"></a>
<a class="token" href="#/s:7heresdk15SegmentSpanDataC43positiveDirectionBaseSpeedInMetersPerSecondSdSgvp">positiveDirectionBaseSpeedInMetersPerSecond</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The average speed expected for this segment in positive direction with a car or a similar
vehicle.
Returns <code>nil</code> if <code><a href="../Structs/SegmentDataLoaderOptions.html#/s:7heresdk24SegmentDataLoaderOptionsV14loadBaseSpeedsSbvp">SegmentDataLoaderOptions.loadBaseSpeeds</a></code> is set to <code>false</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">positiveDirectionBaseSpeedInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15SegmentSpanDataC43negativeDirectionBaseSpeedInMetersPerSecondSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/negativeDirectionBaseSpeedInMetersPerSecond"></a>
<a class="token" href="#/s:7heresdk15SegmentSpanDataC43negativeDirectionBaseSpeedInMetersPerSecondSdSgvp">negativeDirectionBaseSpeedInMetersPerSecond</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The average speed expected for this segment in negative direction with a car or a similar
vehicle.
Returns <code>nil</code> if <code><a href="../Structs/SegmentDataLoaderOptions.html#/s:7heresdk24SegmentDataLoaderOptionsV14loadBaseSpeedsSbvp">SegmentDataLoaderOptions.loadBaseSpeeds</a></code> is set to <code>false</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">negativeDirectionBaseSpeedInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15SegmentSpanDataC26baseSpeedInMetersPerSecondSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/baseSpeedInMetersPerSecond"></a>
<a class="token" href="#/s:7heresdk15SegmentSpanDataC26baseSpeedInMetersPerSecondSdSgvp">baseSpeedInMetersPerSecond</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The average speed expected for this segment span with a car or a similar vehicle.
Will be loaded if <code><a href="../Structs/SegmentDataLoaderOptions.html#/s:7heresdk24SegmentDataLoaderOptionsV14loadBaseSpeedsSbvp">SegmentDataLoaderOptions.loadBaseSpeeds</a></code> is <code>true</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">baseSpeedInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15SegmentSpanDataC24localRoadCharacteristicsSayAA05LocalF14CharacteristicOGSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/localRoadCharacteristics"></a>
<a class="token" href="#/s:7heresdk15SegmentSpanDataC24localRoadCharacteristicsSayAA05LocalF14CharacteristicOGSgvp">localRoadCharacteristics</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The local road characteristics of the segment: frontage, parking lot road, or POI access road.
Returns <code>nil</code> if <code><a href="../Structs/SegmentDataLoaderOptions.html#/s:7heresdk24SegmentDataLoaderOptionsV28loadLocalRoadCharacteristicsSbvp">SegmentDataLoaderOptions.loadLocalRoadCharacteristics</a></code> is set to <code>false</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">localRoadCharacteristics</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-localroadcharacteristic">LocalRoadCharacteristic</a></span><span class="p">]?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15SegmentSpanDataC11streetNamesAA14LocalizedTextsVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/streetNames"></a>
<a class="token" href="#/s:7heresdk15SegmentSpanDataC11streetNamesAA14LocalizedTextsVSgvp">streetNames</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The street names on the span.
Returns <code>nil</code> if <code><a href="../Structs/SegmentDataLoaderOptions.html#/s:7heresdk24SegmentDataLoaderOptionsV29loadStreetNamesAndRoadNumbersSbvp">SegmentDataLoaderOptions.loadStreetNamesAndRoadNumbers</a></code> is set to <code>false</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">streetNames</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-localizedtexts">LocalizedTexts</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15SegmentSpanDataC11roadNumbersAA013LocalizedRoadF0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/roadNumbers"></a>
<a class="token" href="#/s:7heresdk15SegmentSpanDataC11roadNumbersAA013LocalizedRoadF0VSgvp">roadNumbers</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The road numbers on the span enriched with information specific to <em>route numbers</em>
of a road such as I-10, US-50, or A3.
Returns <code>nil</code> if <code><a href="../Structs/SegmentDataLoaderOptions.html#/s:7heresdk24SegmentDataLoaderOptionsV29loadStreetNamesAndRoadNumbersSbvp">SegmentDataLoaderOptions.loadStreetNamesAndRoadNumbers</a></code> is set to <code>false</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">roadNumbers</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-localizedroadnumbers">LocalizedRoadNumbers</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15SegmentSpanDataC18physicalAttributesAA08PhysicalF0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/physicalAttributes"></a>
<a class="token" href="#/s:7heresdk15SegmentSpanDataC18physicalAttributesAA08PhysicalF0VSgvp">physicalAttributes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The physical attributes of the segment.
Returns <code>nil</code> if <code><a href="../Structs/SegmentDataLoaderOptions.html#/s:7heresdk24SegmentDataLoaderOptionsV18loadRoadAttributesSbvp">SegmentDataLoaderOptions.loadRoadAttributes</a></code> is set to <code>false</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">physicalAttributes</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-physicalattributes">PhysicalAttributes</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15SegmentSpanDataC10roadUsagesAA04RoadF0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/roadUsages"></a>
<a class="token" href="#/s:7heresdk15SegmentSpanDataC10roadUsagesAA04RoadF0VSgvp">roadUsages</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The road usages of the segment.
Returns <code>nil</code> if <code><a href="../Structs/SegmentDataLoaderOptions.html#/s:7heresdk24SegmentDataLoaderOptionsV18loadRoadAttributesSbvp">SegmentDataLoaderOptions.loadRoadAttributes</a></code> is set to <code>false</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">roadUsages</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-roadusages">RoadUsages</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15SegmentSpanDataC19administrativeRulesAA014AdministrativeF0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/administrativeRules"></a>
<a class="token" href="#/s:7heresdk15SegmentSpanDataC19administrativeRulesAA014AdministrativeF0VSgvp">administrativeRules</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The <code><a href="sdk-for-ios-navigate-api-reference-structs-administrativerules">AdministrativeRules</a></code> for the segment, containing information
about country code, state code, unit system, tolls, pre-trip planning and other
administrative information.
Returns <code>nil</code> if <code><a href="../Structs/SegmentDataLoaderOptions.html#/s:7heresdk24SegmentDataLoaderOptionsV23loadAdministrativeRulesSbvp">SegmentDataLoaderOptions.loadAdministrativeRules</a></code> is set to <code>false</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">administrativeRules</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-administrativerules">AdministrativeRules</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15SegmentSpanDataC7isUrbanSbSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isUrban"></a>
<a class="token" href="#/s:7heresdk15SegmentSpanDataC7isUrbanSbSgvp">isUrban</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The urban attribute of the segment.
Returns <code>nil</code> if <code><a href="../Structs/SegmentDataLoaderOptions.html#/s:7heresdk24SegmentDataLoaderOptionsV9loadUrbanSbvp">SegmentDataLoaderOptions.loadUrban</a></code> is set to <code>false</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isUrban</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15SegmentSpanDataC22specialSpeedSituationsSayAA0b7SpecialF9SituationVGSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/specialSpeedSituations"></a>
<a class="token" href="#/s:7heresdk15SegmentSpanDataC22specialSpeedSituationsSayAA0b7SpecialF9SituationVGSgvp">specialSpeedSituations</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The special speed situations of the segment.
Will be loaded if <code><a href="../Structs/SegmentDataLoaderOptions.html#/s:7heresdk24SegmentDataLoaderOptionsV26loadSpecialSpeedSituationsSbvp">SegmentDataLoaderOptions.loadSpecialSpeedSituations</a></code> is <code>true</code>.
<strong>Note:</strong> To get timezone offset and daylight saving time values for TimeRule, [sdk.mapdata.SegmentDataLoaderOptions.load_administrative_rules] must also be set to <code>true</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">specialSpeedSituations</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-segmentspecialspeedsituation">SegmentSpecialSpeedSituation</a></span><span class="p">]?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
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
