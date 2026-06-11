---
title: "RoadSignWarning"
slug: "sdk-for-ios-navigate-api-reference-structs-roadsignwarning"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/RoadSignWarning"></a>
<a title="RoadSignWarning Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-navigation">Navigation</a>

        RoadSignWarning Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>RoadSignWarning</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RoadSignWarning</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>A road sign. The main field describing the sign is <code><a href="../Structs/RoadSignWarning.html#/s:7heresdk15RoadSignWarningV4typeAA0bC4TypeOvp">RoadSignWarning.type</a></code>. Some road types are standardized, others can be country specific.
A valid road sign contains known <code><a href="../Structs/RoadSignWarning.html#/s:7heresdk15RoadSignWarningV4typeAA0bC4TypeOvp">RoadSignWarning.type</a></code> or <code><a href="../Structs/RoadSignWarning.html#/s:7heresdk15RoadSignWarningV8categoryAA0bC8CategoryOvp">RoadSignWarning.category</a></code>.
Use <code>RoadSignWarningListener</code> to get notifications with current road signs.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15RoadSignWarningV2ids5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/id"></a>
<a class="token" href="#/s:7heresdk15RoadSignWarningV2ids5Int32Vvp">id</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Unique identifier for this specific road sign warning instance.
Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace.
Use this ID to track, update, or dismiss individual warning instances of this type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">id</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15RoadSignWarningV010distanceTobC8InMetersSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/distanceToRoadSignInMeters"></a>
<a class="token" href="#/s:7heresdk15RoadSignWarningV010distanceTobC8InMetersSdvp">distanceToRoadSignInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Distance to the road sign in meters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">distanceToRoadSignInMeters</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15RoadSignWarningV4typeAA0bC4TypeOvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/type"></a>
<a class="token" href="#/s:7heresdk15RoadSignWarningV4typeAA0bC4TypeOvp">type</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Type of the road sign.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">type</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-roadsigntype">RoadSignType</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15RoadSignWarningV8categoryAA0bC8CategoryOvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/category"></a>
<a class="token" href="#/s:7heresdk15RoadSignWarningV8categoryAA0bC8CategoryOvp">category</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The main category to which the road sign belongs.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">category</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-roadsigncategory">RoadSignCategory</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15RoadSignWarningV07generalD4TypeAA07GeneraldbcF0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/generalWarningType"></a>
<a class="token" href="#/s:7heresdk15RoadSignWarningV07generalD4TypeAA07GeneraldbcF0Ovp">generalWarningType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies the general warning to which the road sign belongs.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">generalWarningType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-generalwarningroadsigntype">GeneralWarningRoadSignType</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15RoadSignWarningV010isPriorityC0Sbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isPrioritySign"></a>
<a class="token" href="#/s:7heresdk15RoadSignWarningV010isPriorityC0Sbvp">isPrioritySign</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Flag indicating if the road sign is a priority sign.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isPrioritySign</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15RoadSignWarningV12vehicleTypesSayAA0bC11VehicleTypeOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/vehicleTypes"></a>
<a class="token" href="#/s:7heresdk15RoadSignWarningV12vehicleTypesSayAA0bC11VehicleTypeOGvp">vehicleTypes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies a list of vehicle types for which the road sign is applicable.
The list will be empty when the road sign is applicable for all vehicles including cars.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">vehicleTypes</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-roadsignvehicletype">RoadSignVehicleType</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15RoadSignWarningV11weatherTypeAA07WeatherF0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/weatherType"></a>
<a class="token" href="#/s:7heresdk15RoadSignWarningV11weatherTypeAA07WeatherF0Ovp">weatherType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies the weather type for which the sign is applicable. If weather type is <code><a href="../Enums/WeatherType.html#/s:7heresdk11WeatherTypeO7unknownyA2CmF">WeatherType.unknown</a></code>, the sign is actual for all weather types.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">weatherType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-weathertype">WeatherType</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15RoadSignWarningV9signValueAA13LocalizedTextVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/signValue"></a>
<a class="token" href="#/s:7heresdk15RoadSignWarningV9signValueAA13LocalizedTextVSgvp">signValue</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Optional value visible on the main sign related to specific road sign types, as it is printed on the local road sign.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">signValue</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-localizedtext">LocalizedText</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15RoadSignWarningV03preD0AA13LocalizedTextVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/preWarning"></a>
<a class="token" href="#/s:7heresdk15RoadSignWarningV03preD0AA13LocalizedTextVSgvp">preWarning</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Optional pre-warning in terms of distance, of the upcoming warning or regulation.
The pre-warning information is given as printed on the local road sign.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">preWarning</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-localizedtext">LocalizedText</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15RoadSignWarningV8durationAA13LocalizedTextVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/duration"></a>
<a class="token" href="#/s:7heresdk15RoadSignWarningV8durationAA13LocalizedTextVSgvp">duration</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Optional length information during which the warning is applicable.
Usually, this information is shown on a separate shield below the main shield.
For example, a sign may warn on playing children for a length of 100 m, starting from
the location of the warning sign.
The length information (most likely with units) is given as printed on the local road sign.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">duration</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-localizedtext">LocalizedText</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15RoadSignWarningV12validityTimeAA13LocalizedTextVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/validityTime"></a>
<a class="token" href="#/s:7heresdk15RoadSignWarningV12validityTimeAA13LocalizedTextVSgvp">validityTime</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Optional text visible on the supplemental sign indicating specific
time(s) at which the road sign is applicable.
The time information is given as printed on the local road sign.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">validityTime</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-localizedtext">LocalizedText</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15RoadSignWarningV04roadC7SegmentAA0F9ReferenceVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/roadSignSegment"></a>
<a class="token" href="#/s:7heresdk15RoadSignWarningV04roadC7SegmentAA0F9ReferenceVvp">roadSignSegment</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The reference to the segment where the road sign is located. It can be used to identify the
location of the road sign.
It allows to compare the road sign location with the <code>MapMatchedLocation.segment_reference</code>
provided by the <code>NavigableLocationListener</code> or with the <code><a href="../Classes/Span.html#/s:7heresdk4SpanC16segmentReferenceAA07SegmentD0Vvp">Span.segmentReference</a></code>
available in the Route’s Span.
By combining it with the geometry of the segment, that can be loaded using
<code><a href="sdk-for-ios-navigate-api-reference-classes-segmentdataloader">SegmentDataLoader</a></code>, it is possible to identify the road sign’s coordinates.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">roadSignSegment</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-segmentreference">SegmentReference</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15RoadSignWarningV12distanceTypeAA08DistanceF0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/distanceType"></a>
<a class="token" href="#/s:7heresdk15RoadSignWarningV12distanceTypeAA08DistanceF0Ovp">distanceType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The distance type for the warning, e.g. a warning for a new road sign ahead or a warning for
passing a road sign. Since the road sign warning is given relative to a single position on
the route, <code><a href="../Enums/DistanceType.html#/s:7heresdk12DistanceTypeO7reachedyA2CmF">DistanceType.reached</a></code> will never be given for this warning.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">distanceType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-distancetype">DistanceType</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15RoadSignWarningV2id010distanceTobC8InMeters4type8category07generalD4Type010isPriorityC012vehicleTypes07weatherM09signValue03preD08duration12validityTime04roadC7Segment0fM0ACs5Int32V_SdAA0bcM0OAA0bC8CategoryOAA07GeneraldbcM0OSbSayAA0bc7VehicleM0OGAA07WeatherM0OAA13LocalizedTextVSgA5_A5_A5_AA0Z9ReferenceVAA08DistanceM0Otcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(id:distanceToRoadSignInMeters:type:category:generalWarningType:isPrioritySign:vehicleTypes:weatherType:signValue:preWarning:duration:validityTime:roadSignSegment:distanceType:)"></a>
<a class="token" href="#/s:7heresdk15RoadSignWarningV2id010distanceTobC8InMeters4type8category07generalD4Type010isPriorityC012vehicleTypes07weatherM09signValue03preD08duration12validityTime04roadC7Segment0fM0ACs5Int32V_SdAA0bcM0OAA0bC8CategoryOAA07GeneraldbcM0OSbSayAA0bc7VehicleM0OGAA07WeatherM0OAA13LocalizedTextVSgA5_A5_A5_AA0Z9ReferenceVAA08DistanceM0Otcfc">init(id:<wbr/>distanceToRoadSignInMeters:<wbr/>type:<wbr/>category:<wbr/>generalWarningType:<wbr/>isPrioritySign:<wbr/>vehicleTypes:<wbr/>weatherType:<wbr/>signValue:<wbr/>preWarning:<wbr/>duration:<wbr/>validityTime:<wbr/>roadSignSegment:<wbr/>distanceType:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">id</span><span class="p">:</span> <span class="kt">Int32</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nv">distanceToRoadSignInMeters</span><span class="p">:</span> <span class="kt">Double</span><span class="p">,</span> <span class="nv">type</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-roadsigntype">RoadSignType</a></span><span class="p">,</span> <span class="nv">category</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-roadsigncategory">RoadSignCategory</a></span><span class="p">,</span> <span class="nv">generalWarningType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-generalwarningroadsigntype">GeneralWarningRoadSignType</a></span><span class="p">,</span> <span class="nv">isPrioritySign</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">,</span> <span class="nv">vehicleTypes</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-roadsignvehicletype">RoadSignVehicleType</a></span><span class="p">],</span> <span class="nv">weatherType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-weathertype">WeatherType</a></span><span class="p">,</span> <span class="nv">signValue</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-localizedtext">LocalizedText</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">preWarning</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-localizedtext">LocalizedText</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">duration</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-localizedtext">LocalizedText</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">validityTime</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-localizedtext">LocalizedText</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">roadSignSegment</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-segmentreference">SegmentReference</a></span><span class="p">,</span> <span class="nv">distanceType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-distancetype">DistanceType</a></span><span class="p">)</span></code></pre>
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
