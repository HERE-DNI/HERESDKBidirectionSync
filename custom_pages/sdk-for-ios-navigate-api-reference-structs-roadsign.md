---
title: "sdk-for-ios-navigate-api-reference-structs-roadsign"
slug: "sdk-for-ios-navigate-api-reference-structs-roadsign"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/RoadSign"></a>
<a title="RoadSign Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-navigation">Navigation</a>
<img alt="" id="carat" src="/carat.png"/>
        RoadSign Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>RoadSign</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RoadSign</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Describes a road sign.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8RoadSignV14offsetInMeterss5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/offsetInMeters"></a>
<a class="token" href="#/s:7heresdk8RoadSignV14offsetInMeterss5Int32Vvp">offsetInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The offset in meters from the beginning of the segment to the location of the road sign
in positive direction.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">offsetInMeters</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8RoadSignV15travelDirectionAA06TravelE0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/travelDirection"></a>
<a class="token" href="#/s:7heresdk8RoadSignV15travelDirectionAA06TravelE0Ovp">travelDirection</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Segment direction which the road sign is applied.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">travelDirection</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-traveldirection">TravelDirection</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8RoadSignV04roadC4TypeAA0bcE0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/roadSignType"></a>
<a class="token" href="#/s:7heresdk8RoadSignV04roadC4TypeAA0bcE0Ovp">roadSignType</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">roadSignType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-roadsigntype">RoadSignType</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8RoadSignV04roadC8CategoryAA0bcE0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/roadSignCategory"></a>
<a class="token" href="#/s:7heresdk8RoadSignV04roadC8CategoryAA0bcE0Ovp">roadSignCategory</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">roadSignCategory</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-roadsigncategory">RoadSignCategory</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8RoadSignV010isPriorityC0Sbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isPrioritySign"></a>
<a class="token" href="#/s:7heresdk8RoadSignV010isPriorityC0Sbvp">isPrioritySign</a>
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
<a name="/s:7heresdk8RoadSignV18generalWarningTypeAA07GeneralebcF0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/generalWarningType"></a>
<a class="token" href="#/s:7heresdk8RoadSignV18generalWarningTypeAA07GeneralebcF0Ovp">generalWarningType</a>
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
<a name="/s:7heresdk8RoadSignV12vehicleTypesSayAA0bC11VehicleTypeOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/vehicleTypes"></a>
<a class="token" href="#/s:7heresdk8RoadSignV12vehicleTypesSayAA0bC11VehicleTypeOGvp">vehicleTypes</a>
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
<a name="/s:7heresdk8RoadSignV11weatherTypeAA07WeatherE0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/weatherType"></a>
<a class="token" href="#/s:7heresdk8RoadSignV11weatherTypeAA07WeatherE0Ovp">weatherType</a>
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
<a name="/s:7heresdk8RoadSignV09localizedC5ValueAA13LocalizedTextVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/localizedSignValue"></a>
<a class="token" href="#/s:7heresdk8RoadSignV09localizedC5ValueAA13LocalizedTextVSgvp">localizedSignValue</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">localizedSignValue</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-localizedtext">LocalizedText</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8RoadSignV19localizedPreWarningAA13LocalizedTextVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/localizedPreWarning"></a>
<a class="token" href="#/s:7heresdk8RoadSignV19localizedPreWarningAA13LocalizedTextVSgvp">localizedPreWarning</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">localizedPreWarning</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-localizedtext">LocalizedText</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8RoadSignV17localizedDurationAA13LocalizedTextVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/localizedDuration"></a>
<a class="token" href="#/s:7heresdk8RoadSignV17localizedDurationAA13LocalizedTextVSgvp">localizedDuration</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">localizedDuration</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-localizedtext">LocalizedText</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8RoadSignV21localizedValidityTimeAA13LocalizedTextVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/localizedValidityTime"></a>
<a class="token" href="#/s:7heresdk8RoadSignV21localizedValidityTimeAA13LocalizedTextVSgvp">localizedValidityTime</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">localizedValidityTime</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-localizedtext">LocalizedText</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8RoadSignV14offsetInMeters15travelDirection04roadC4Type0iC8Category010isPriorityC0014generalWarningJ012vehicleTypes07weatherJ009localizedC5Value0s3PreO00S8Duration0S12ValidityTimeACs5Int32V_AA06TravelH0OAA0bcJ0OAA0bcK0OSbAA07GeneralobcJ0OSayAA0bc7VehicleJ0OGAA07WeatherJ0OAA13LocalizedTextVSgA5_A5_A5_tcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(offsetInMeters:travelDirection:roadSignType:roadSignCategory:isPrioritySign:generalWarningType:vehicleTypes:weatherType:localizedSignValue:localizedPreWarning:localizedDuration:localizedValidityTime:)"></a>
<a class="token" href="#/s:7heresdk8RoadSignV14offsetInMeters15travelDirection04roadC4Type0iC8Category010isPriorityC0014generalWarningJ012vehicleTypes07weatherJ009localizedC5Value0s3PreO00S8Duration0S12ValidityTimeACs5Int32V_AA06TravelH0OAA0bcJ0OAA0bcK0OSbAA07GeneralobcJ0OSayAA0bc7VehicleJ0OGAA07WeatherJ0OAA13LocalizedTextVSgA5_A5_A5_tcfc">init(offsetInMeters:<wbr/>travelDirection:<wbr/>roadSignType:<wbr/>roadSignCategory:<wbr/>isPrioritySign:<wbr/>generalWarningType:<wbr/>vehicleTypes:<wbr/>weatherType:<wbr/>localizedSignValue:<wbr/>localizedPreWarning:<wbr/>localizedDuration:<wbr/>localizedValidityTime:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance with default values.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">offsetInMeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">,</span> <span class="nv">travelDirection</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-traveldirection">TravelDirection</a></span><span class="p">,</span> <span class="nv">roadSignType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-roadsigntype">RoadSignType</a></span><span class="p">,</span> <span class="nv">roadSignCategory</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-roadsigncategory">RoadSignCategory</a></span><span class="p">,</span> <span class="nv">isPrioritySign</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">,</span> <span class="nv">generalWarningType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-generalwarningroadsigntype">GeneralWarningRoadSignType</a></span><span class="p">,</span> <span class="nv">vehicleTypes</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-roadsignvehicletype">RoadSignVehicleType</a></span><span class="p">],</span> <span class="nv">weatherType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-weathertype">WeatherType</a></span><span class="p">,</span> <span class="nv">localizedSignValue</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-localizedtext">LocalizedText</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">localizedPreWarning</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-localizedtext">LocalizedText</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">localizedDuration</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-localizedtext">LocalizedText</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">localizedValidityTime</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-localizedtext">LocalizedText</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
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
