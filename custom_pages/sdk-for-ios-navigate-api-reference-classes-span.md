---
title: "sdk-for-ios-navigate-api-reference-classes-span"
slug: "sdk-for-ios-navigate-api-reference-classes-span"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/Span"></a>
<a title="Span Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-routing">Routing</a>
<img alt="" id="carat" src="/carat.png"/>
        Span Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>Span</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">Span</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Span</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Span</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>A span is a part of the <code><a href="sdk-for-ios-navigate-api-reference-classes-section">Section</a></code> which is traversable or navigable. Each span
usually has some geometry associated with it.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk4SpanC8geometryAA11GeoPolylineVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/geometry"></a>
<a class="token" href="#/s:7heresdk4SpanC8geometryAA11GeoPolylineVvp">geometry</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The <code><a href="sdk-for-ios-navigate-api-reference-structs-geopolyline">GeoPolyline</a></code> object representing the polyline of this span.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">geometry</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geopolyline">GeoPolyline</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk4SpanC14lengthInMeterss5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/lengthInMeters"></a>
<a class="token" href="#/s:7heresdk4SpanC14lengthInMeterss5Int32Vvp">lengthInMeters</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">lengthInMeters</span><span class="p">:</span> <span class="kt">Int32</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk4SpanC13noticeIndexesSays5Int32VGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/noticeIndexes"></a>
<a class="token" href="#/s:7heresdk4SpanC13noticeIndexesSays5Int32VGvp">noticeIndexes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of indexes to <code><a href="../Classes/Section.html#/s:7heresdk7SectionC14sectionNoticesSayAA0B6NoticeVGvp">Section.sectionNotices</a></code> the parent section owns.
In case the list is not empty, the user must judge all the indexed <code><a href="sdk-for-ios-navigate-api-reference-structs-sectionnotice">SectionNotice</a></code>s
carefully before proceeding.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">noticeIndexes</span><span class="p">:</span> <span class="p">[</span><span class="kt">Int32</span><span class="p">]</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk4SpanC16segmentReferenceAA07SegmentD0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/segmentReference"></a>
<a class="token" href="#/s:7heresdk4SpanC16segmentReferenceAA07SegmentD0Vvp">segmentReference</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The segment reference of this span.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">segmentReference</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-segmentreference">SegmentReference</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk4SpanC22trafficIncidentIndexesSays5Int32VGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/trafficIncidentIndexes"></a>
<a class="token" href="#/s:7heresdk4SpanC22trafficIncidentIndexesSays5Int32VGvp">trafficIncidentIndexes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The indexes of traffic incidents from the field <code><a href="../Classes/Section.html#/s:7heresdk7SectionC16trafficIncidentsSayAA22TrafficIncidentOnRouteCGvp">Section.trafficIncidents</a></code> of the parent <code><a href="sdk-for-ios-navigate-api-reference-classes-section">Section</a></code>.
Each matching incident takes at least a whole <code><a href="../Classes/Span.html#/s:7heresdk4SpanC8geometryAA11GeoPolylineVvp">Span.geometry</a></code>.
The same incident can take other spans and an area out of the built route as well.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">trafficIncidentIndexes</span><span class="p">:</span> <span class="p">[</span><span class="kt">Int32</span><span class="p">]</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk4SpanC21sectionPolylineOffsets5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/sectionPolylineOffset"></a>
<a class="token" href="#/s:7heresdk4SpanC21sectionPolylineOffsets5Int32Vvp">sectionPolylineOffset</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The position of the span inside the section’s geometry, given as an offset. The span geometry starts from
this offset and ends on the offset of the next span, both start offset point and end offset point being
included in the span, because the spans’ geometry share a point in the section’s geometry.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">sectionPolylineOffset</span><span class="p">:</span> <span class="kt">Int32</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk4SpanC16dynamicSpeedInfoAA07DynamicdE0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/dynamicSpeedInfo"></a>
<a class="token" href="#/s:7heresdk4SpanC16dynamicSpeedInfoAA07DynamicdE0VSgvp">dynamicSpeedInfo</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The dynamic speed information on the span.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">dynamicSpeedInfo</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-dynamicspeedinfo">DynamicSpeedInfo</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk4SpanC16streetAttributesSayAA06StreetD0OGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/streetAttributes"></a>
<a class="token" href="#/s:7heresdk4SpanC16streetAttributesSayAA06StreetD0OGvp">streetAttributes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of street attributes on the span.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">streetAttributes</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-streetattributes">StreetAttributes</a></span><span class="p">]</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk4SpanC13carAttributesSayAA06AccessD0OGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/carAttributes"></a>
<a class="token" href="#/s:7heresdk4SpanC13carAttributesSayAA06AccessD0OGvp">carAttributes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of car access attributes on the span.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">carAttributes</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-accessattributes">AccessAttributes</a></span><span class="p">]</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk4SpanC15truckAttributesSayAA06AccessD0OGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/truckAttributes"></a>
<a class="token" href="#/s:7heresdk4SpanC15truckAttributesSayAA06AccessD0OGvp">truckAttributes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of truck access attributes on the span.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">truckAttributes</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-accessattributes">AccessAttributes</a></span><span class="p">]</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk4SpanC17scooterAttributesSayAA06AccessD0OGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/scooterAttributes"></a>
<a class="token" href="#/s:7heresdk4SpanC17scooterAttributesSayAA06AccessD0OGvp">scooterAttributes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of scooter access attributes on the span.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">scooterAttributes</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-accessattributes">AccessAttributes</a></span><span class="p">]</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk4SpanC14walkAttributesSayAA04WalkD0OGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/walkAttributes"></a>
<a class="token" href="#/s:7heresdk4SpanC14walkAttributesSayAA04WalkD0OGvp">walkAttributes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of walk attributes on the span.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">walkAttributes</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-walkattributes">WalkAttributes</a></span><span class="p">]</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk4SpanC11streetNamesAA14LocalizedTextsVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/streetNames"></a>
<a class="token" href="#/s:7heresdk4SpanC11streetNamesAA14LocalizedTextsVvp">streetNames</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The street names on the span.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">streetNames</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-localizedtexts">LocalizedTexts</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk4SpanC11roadNumbersAA013LocalizedRoadD0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/roadNumbers"></a>
<a class="token" href="#/s:7heresdk4SpanC11roadNumbersAA013LocalizedRoadD0Vvp">roadNumbers</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The road numbers on the span enriched with information specific to <em>route numbers</em>
of a road such as I-10, US-50, or A3, and cardinal direction, if available, and a road level classification (<code><a href="sdk-for-ios-navigate-api-reference-enums-routetype">RouteType</a></code>).</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">roadNumbers</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-localizedroadnumbers">LocalizedRoadNumbers</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk4SpanC27speedLimitInMetersPerSecondSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/speedLimitInMetersPerSecond"></a>
<a class="token" href="#/s:7heresdk4SpanC27speedLimitInMetersPerSecondSdSgvp">speedLimitInMetersPerSecond</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The speed limit in meters per second on the span.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">speedLimitInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk4SpanC26consumptionInKilowattHoursSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/consumptionInKilowattHours"></a>
<a class="token" href="#/s:7heresdk4SpanC26consumptionInKilowattHoursSdSgvp">consumptionInKilowattHours</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The power consumption in kilowatt per hour necessary to traverse the span.</p>
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
<a name="/s:7heresdk4SpanC19functionalRoadClassAA010FunctionaldE0OSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/functionalRoadClass"></a>
<a class="token" href="#/s:7heresdk4SpanC19functionalRoadClassAA010FunctionaldE0OSgvp">functionalRoadClass</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The functional road class of the span.</p>
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
<a name="/s:7heresdk4SpanC8durationSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/duration"></a>
<a class="token" href="#/s:7heresdk4SpanC8durationSdvp">duration</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The time duration necessary to traverse the span, using the speed provided
in <code><a href="../Classes/Span.html#/s:7heresdk4SpanC16dynamicSpeedInfoAA07DynamicdE0VSgvp">Span.dynamicSpeedInfo</a></code>. This duration takes also into
consideration the delays caused by the traffic.</p>
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
<a name="/s:7heresdk4SpanC12baseDurationSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/baseDuration"></a>
<a class="token" href="#/s:7heresdk4SpanC12baseDurationSdvp">baseDuration</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The time duration necessary to traverse the span, using the speed provided
in <code><a href="../Classes/Span.html#/s:7heresdk4SpanC16dynamicSpeedInfoAA07DynamicdE0VSgvp">Span.dynamicSpeedInfo</a></code> without taking into consideration
the delays caused by the traffic.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">baseDuration</span><span class="p">:</span> <span class="kt">TimeInterval</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk4SpanC11countryCodeSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/countryCode"></a>
<a class="token" href="#/s:7heresdk4SpanC11countryCodeSSSgvp">countryCode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The country code of the span. The value is <code>nil</code> when no data is available.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">countryCode</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk4SpanC9stateCodeSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/stateCode"></a>
<a class="token" href="#/s:7heresdk4SpanC9stateCodeSSSgvp">stateCode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The state code of the span. State code is available in some countries to denote principal
subdivisions(provinces or states), e.g. in the United States, AK stands for Alaska and OH stands for Ohio.
The format of state code can vary for different countries, take the United States as example,
it consists of two alphabet letters.
The value is <code>nil</code> when no data is available.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">stateCode</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk4SpanC28noThroughRestrictionsIndexesSays5Int32VGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/noThroughRestrictionsIndexes"></a>
<a class="token" href="#/s:7heresdk4SpanC28noThroughRestrictionsIndexesSays5Int32VGvp">noThroughRestrictionsIndexes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of indexes to <code><a href="../Classes/Section.html#/s:7heresdk7SectionC21noThroughRestrictionsSayAA19ViolatedRestrictionVGvp">Section.noThroughRestrictions</a></code> the parent section owns.
In case the list is not empty, the user must judge all the indexed sdk routing noThroughRestriction’s
carefully before proceeding.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">noThroughRestrictionsIndexes</span><span class="p">:</span> <span class="p">[</span><span class="kt">Int32</span><span class="p">]</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk4SpanC13getShieldText10roadNumberSSAA013LocalizedRoadG0V_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getShieldText(roadNumber:)"></a>
<a class="token" href="#/s:7heresdk4SpanC13getShieldText10roadNumberSSAA013LocalizedRoadG0V_tF">getShieldText(roadNumber:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Converts full route number to the value to be displayed on the road shield.
The results are based on country code and state code of <code>Span</code> object and route type of passed <code>road_number</code> argument.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getShieldText</span><span class="p">(</span><span class="nv">roadNumber</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-localizedroadnumber">LocalizedRoadNumber</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">String</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>roadNumber</em>
</code>
</td>
<td>
<div>
<p>Route number to convert to shield text.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Text on the road shield to display.</p>
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
