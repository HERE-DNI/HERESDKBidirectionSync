---
title: "sdk-for-ios-navigate-api-reference-structs-segmentdataloaderoptions"
slug: "sdk-for-ios-navigate-api-reference-structs-segmentdataloaderoptions"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/SegmentDataLoaderOptions"></a>
<a title="SegmentDataLoaderOptions Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-mapdata">MapData</a>
<img alt="" id="carat" src="/carat.png"/>
        SegmentDataLoaderOptions Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>SegmentDataLoaderOptions</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">SegmentDataLoaderOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Specifies which data should be loaded by the <code><a href="../Classes/SegmentDataLoader.html#/s:7heresdk17SegmentDataLoaderC04loadC07segment7optionsAA0bC0CAA12OCMSegmentIdV_AA0bcD7OptionsVtKF">SegmentDataLoader.loadData(...)</a></code> or <code><a href="../Classes/SegmentDataLoader.html#/s:7heresdk17SegmentDataLoaderC012loadDirectedbC07segment7optionsAA0bC0CAA0F12OCMSegmentIdV_AA0bcD7OptionsVtKF">SegmentDataLoader.loadDirectedSegmentData(...)</a></code> function.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24SegmentDataLoaderOptionsV19loadTravelDirectionSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/loadTravelDirection"></a>
<a class="token" href="#/s:7heresdk24SegmentDataLoaderOptionsV19loadTravelDirectionSbvp">loadTravelDirection</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>If it is true, the <code><a href="../Classes/SegmentSpanData.html#/s:7heresdk15SegmentSpanDataC15travelDirectionAA06TravelF0OSgvp">SegmentSpanData.travelDirection</a></code> will be loaded when <code><a href="../Classes/SegmentDataLoader.html#/s:7heresdk17SegmentDataLoaderC04loadC07segment7optionsAA0bC0CAA12OCMSegmentIdV_AA0bcD7OptionsVtKF">SegmentDataLoader.loadData(...)</a></code> or
<code><a href="../Classes/SegmentDataLoader.html#/s:7heresdk17SegmentDataLoaderC012loadDirectedbC07segment7optionsAA0bC0CAA0F12OCMSegmentIdV_AA0bcD7OptionsVtKF">SegmentDataLoader.loadDirectedSegmentData(...)</a></code> is called.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">loadTravelDirection</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24SegmentDataLoaderOptionsV23loadFunctionalRoadClassSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/loadFunctionalRoadClass"></a>
<a class="token" href="#/s:7heresdk24SegmentDataLoaderOptionsV23loadFunctionalRoadClassSbvp">loadFunctionalRoadClass</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>If it is true, the <code><a href="../Classes/SegmentSpanData.html#/s:7heresdk15SegmentSpanDataC19functionalRoadClassAA010FunctionalfG0OSgvp">SegmentSpanData.functionalRoadClass</a></code> will be loaded when <code><a href="../Classes/SegmentDataLoader.html#/s:7heresdk17SegmentDataLoaderC04loadC07segment7optionsAA0bC0CAA12OCMSegmentIdV_AA0bcD7OptionsVtKF">SegmentDataLoader.loadData(...)</a></code> or
<code><a href="../Classes/SegmentDataLoader.html#/s:7heresdk17SegmentDataLoaderC012loadDirectedbC07segment7optionsAA0bC0CAA0F12OCMSegmentIdV_AA0bcD7OptionsVtKF">SegmentDataLoader.loadDirectedSegmentData(...)</a></code> is called.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">loadFunctionalRoadClass</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24SegmentDataLoaderOptionsV24loadTransportModesAccessSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/loadTransportModesAccess"></a>
<a class="token" href="#/s:7heresdk24SegmentDataLoaderOptionsV24loadTransportModesAccessSbvp">loadTransportModesAccess</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>If it is true, <code><a href="../Classes/SegmentSpanData.html#/s:7heresdk15SegmentSpanDataC21allowedTransportModesAA07AllowedfG0VSgvp">SegmentSpanData.allowedTransportModes</a></code> will be loaded when <code><a href="../Classes/SegmentDataLoader.html#/s:7heresdk17SegmentDataLoaderC04loadC07segment7optionsAA0bC0CAA12OCMSegmentIdV_AA0bcD7OptionsVtKF">SegmentDataLoader.loadData(...)</a></code> or
<code><a href="../Classes/SegmentDataLoader.html#/s:7heresdk17SegmentDataLoaderC012loadDirectedbC07segment7optionsAA0bC0CAA0F12OCMSegmentIdV_AA0bcD7OptionsVtKF">SegmentDataLoader.loadDirectedSegmentData(...)</a></code> is called.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">loadTransportModesAccess</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24SegmentDataLoaderOptionsV15loadSpeedLimitsSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/loadSpeedLimits"></a>
<a class="token" href="#/s:7heresdk24SegmentDataLoaderOptionsV15loadSpeedLimitsSbvp">loadSpeedLimits</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>If it is true, <code><a href="../Classes/SegmentSpanData.html#/s:7heresdk15SegmentSpanDataC27positiveDirectionSpeedLimitAA0bgH0VSgvp">SegmentSpanData.positiveDirectionSpeedLimit</a></code>,
<code><a href="../Classes/SegmentSpanData.html#/s:7heresdk15SegmentSpanDataC27negativeDirectionSpeedLimitAA0bgH0VSgvp">SegmentSpanData.negativeDirectionSpeedLimit</a></code> and <code><a href="../Classes/SegmentSpanData.html#/s:7heresdk15SegmentSpanDataC10speedLimitAA0b5SpeedF0VSgvp">SegmentSpanData.speedLimit</a></code> will be loaded
when <code><a href="../Classes/SegmentDataLoader.html#/s:7heresdk17SegmentDataLoaderC04loadC07segment7optionsAA0bC0CAA12OCMSegmentIdV_AA0bcD7OptionsVtKF">SegmentDataLoader.loadData(...)</a></code> or <code><a href="../Classes/SegmentDataLoader.html#/s:7heresdk17SegmentDataLoaderC012loadDirectedbC07segment7optionsAA0bC0CAA0F12OCMSegmentIdV_AA0bcD7OptionsVtKF">SegmentDataLoader.loadDirectedSegmentData(...)</a></code> is called.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">loadSpeedLimits</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24SegmentDataLoaderOptionsV14loadBaseSpeedsSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/loadBaseSpeeds"></a>
<a class="token" href="#/s:7heresdk24SegmentDataLoaderOptionsV14loadBaseSpeedsSbvp">loadBaseSpeeds</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>If it is true, <code><a href="../Classes/SegmentSpanData.html#/s:7heresdk15SegmentSpanDataC43positiveDirectionBaseSpeedInMetersPerSecondSdSgvp">SegmentSpanData.positiveDirectionBaseSpeedInMetersPerSecond</a></code>,
<code><a href="../Classes/SegmentSpanData.html#/s:7heresdk15SegmentSpanDataC43negativeDirectionBaseSpeedInMetersPerSecondSdSgvp">SegmentSpanData.negativeDirectionBaseSpeedInMetersPerSecond</a></code> and <code><a href="../Classes/SegmentSpanData.html#/s:7heresdk15SegmentSpanDataC26baseSpeedInMetersPerSecondSdSgvp">SegmentSpanData.baseSpeedInMetersPerSecond</a></code> will be loaded when <code><a href="../Classes/SegmentDataLoader.html#/s:7heresdk17SegmentDataLoaderC04loadC07segment7optionsAA0bC0CAA12OCMSegmentIdV_AA0bcD7OptionsVtKF">SegmentDataLoader.loadData(...)</a></code> or
<code><a href="../Classes/SegmentDataLoader.html#/s:7heresdk17SegmentDataLoaderC012loadDirectedbC07segment7optionsAA0bC0CAA0F12OCMSegmentIdV_AA0bcD7OptionsVtKF">SegmentDataLoader.loadDirectedSegmentData(...)</a></code> is called.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">loadBaseSpeeds</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24SegmentDataLoaderOptionsV28loadLocalRoadCharacteristicsSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/loadLocalRoadCharacteristics"></a>
<a class="token" href="#/s:7heresdk24SegmentDataLoaderOptionsV28loadLocalRoadCharacteristicsSbvp">loadLocalRoadCharacteristics</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>If it is true, <code><a href="../Classes/SegmentSpanData.html#/s:7heresdk15SegmentSpanDataC24localRoadCharacteristicsSayAA05LocalF14CharacteristicOGSgvp">SegmentSpanData.localRoadCharacteristics</a></code> will be loaded when <code><a href="../Classes/SegmentDataLoader.html#/s:7heresdk17SegmentDataLoaderC04loadC07segment7optionsAA0bC0CAA12OCMSegmentIdV_AA0bcD7OptionsVtKF">SegmentDataLoader.loadData(...)</a></code> or
<code><a href="../Classes/SegmentDataLoader.html#/s:7heresdk17SegmentDataLoaderC012loadDirectedbC07segment7optionsAA0bC0CAA0F12OCMSegmentIdV_AA0bcD7OptionsVtKF">SegmentDataLoader.loadDirectedSegmentData(...)</a></code> is called.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">loadLocalRoadCharacteristics</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24SegmentDataLoaderOptionsV29loadStreetNamesAndRoadNumbersSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/loadStreetNamesAndRoadNumbers"></a>
<a class="token" href="#/s:7heresdk24SegmentDataLoaderOptionsV29loadStreetNamesAndRoadNumbersSbvp">loadStreetNamesAndRoadNumbers</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>If it is true, <code><a href="../Classes/SegmentSpanData.html#/s:7heresdk15SegmentSpanDataC11streetNamesAA14LocalizedTextsVSgvp">SegmentSpanData.streetNames</a></code> and <code><a href="../Classes/SegmentSpanData.html#/s:7heresdk15SegmentSpanDataC11roadNumbersAA013LocalizedRoadF0VSgvp">SegmentSpanData.roadNumbers</a></code> and will be loaded when <code><a href="../Classes/SegmentDataLoader.html#/s:7heresdk17SegmentDataLoaderC04loadC07segment7optionsAA0bC0CAA12OCMSegmentIdV_AA0bcD7OptionsVtKF">SegmentDataLoader.loadData(...)</a></code> or
<code><a href="../Classes/SegmentDataLoader.html#/s:7heresdk17SegmentDataLoaderC012loadDirectedbC07segment7optionsAA0bC0CAA0F12OCMSegmentIdV_AA0bcD7OptionsVtKF">SegmentDataLoader.loadDirectedSegmentData(...)</a></code> is called.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">loadStreetNamesAndRoadNumbers</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24SegmentDataLoaderOptionsV18loadRoadAttributesSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/loadRoadAttributes"></a>
<a class="token" href="#/s:7heresdk24SegmentDataLoaderOptionsV18loadRoadAttributesSbvp">loadRoadAttributes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>If it is true, <code><a href="../Classes/SegmentSpanData.html#/s:7heresdk15SegmentSpanDataC18physicalAttributesAA08PhysicalF0VSgvp">SegmentSpanData.physicalAttributes</a></code> and
<code><a href="../Classes/SegmentSpanData.html#/s:7heresdk15SegmentSpanDataC10roadUsagesAA04RoadF0VSgvp">SegmentSpanData.roadUsages</a></code> will be loaded when <code><a href="../Classes/SegmentDataLoader.html#/s:7heresdk17SegmentDataLoaderC04loadC07segment7optionsAA0bC0CAA12OCMSegmentIdV_AA0bcD7OptionsVtKF">SegmentDataLoader.loadData(...)</a></code> or
<code><a href="../Classes/SegmentDataLoader.html#/s:7heresdk17SegmentDataLoaderC012loadDirectedbC07segment7optionsAA0bC0CAA0F12OCMSegmentIdV_AA0bcD7OptionsVtKF">SegmentDataLoader.loadDirectedSegmentData(...)</a></code> is called.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">loadRoadAttributes</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24SegmentDataLoaderOptionsV18loadTrafficSignalsSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/loadTrafficSignals"></a>
<a class="token" href="#/s:7heresdk24SegmentDataLoaderOptionsV18loadTrafficSignalsSbvp">loadTrafficSignals</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>If it is true, <code><a href="../Classes/SegmentData.html#/s:7heresdk11SegmentDataC14trafficSignalsSayAA13TrafficSignalVGSgvp">SegmentData.trafficSignals</a></code> will be loaded when <code><a href="../Classes/SegmentDataLoader.html#/s:7heresdk17SegmentDataLoaderC04loadC07segment7optionsAA0bC0CAA12OCMSegmentIdV_AA0bcD7OptionsVtKF">SegmentDataLoader.loadData(...)</a></code> or <code><a href="../Classes/SegmentDataLoader.html#/s:7heresdk17SegmentDataLoaderC012loadDirectedbC07segment7optionsAA0bC0CAA0F12OCMSegmentIdV_AA0bcD7OptionsVtKF">SegmentDataLoader.loadDirectedSegmentData(...)</a></code> is called.
Defaults to <code>false</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">loadTrafficSignals</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24SegmentDataLoaderOptionsV13loadRoadSignsSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/loadRoadSigns"></a>
<a class="token" href="#/s:7heresdk24SegmentDataLoaderOptionsV13loadRoadSignsSbvp">loadRoadSigns</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>If it is true, <code><a href="../Classes/SegmentData.html#/s:7heresdk11SegmentDataC9roadSignsSayAA8RoadSignVGSgvp">SegmentData.roadSigns</a></code> will be loaded when <code><a href="../Classes/SegmentDataLoader.html#/s:7heresdk17SegmentDataLoaderC04loadC07segment7optionsAA0bC0CAA12OCMSegmentIdV_AA0bcD7OptionsVtKF">SegmentDataLoader.loadData(...)</a></code> or <code><a href="../Classes/SegmentDataLoader.html#/s:7heresdk17SegmentDataLoaderC012loadDirectedbC07segment7optionsAA0bC0CAA0F12OCMSegmentIdV_AA0bcD7OptionsVtKF">SegmentDataLoader.loadDirectedSegmentData(...)</a></code> is called.
Defaults to <code>false</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">loadRoadSigns</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24SegmentDataLoaderOptionsV23loadAdministrativeRulesSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/loadAdministrativeRules"></a>
<a class="token" href="#/s:7heresdk24SegmentDataLoaderOptionsV23loadAdministrativeRulesSbvp">loadAdministrativeRules</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>If it is true, <code><a href="../Classes/SegmentSpanData.html#/s:7heresdk15SegmentSpanDataC19administrativeRulesAA014AdministrativeF0VSgvp">SegmentSpanData.administrativeRules</a></code> will be loaded when <code><a href="../Classes/SegmentDataLoader.html#/s:7heresdk17SegmentDataLoaderC04loadC07segment7optionsAA0bC0CAA12OCMSegmentIdV_AA0bcD7OptionsVtKF">SegmentDataLoader.loadData(...)</a></code> or <code><a href="../Classes/SegmentDataLoader.html#/s:7heresdk17SegmentDataLoaderC012loadDirectedbC07segment7optionsAA0bC0CAA0F12OCMSegmentIdV_AA0bcD7OptionsVtKF">SegmentDataLoader.loadDirectedSegmentData(...)</a></code> is called.
Defaults to <code>false</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">loadAdministrativeRules</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24SegmentDataLoaderOptionsV20loadRailwayCrossingsSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/loadRailwayCrossings"></a>
<a class="token" href="#/s:7heresdk24SegmentDataLoaderOptionsV20loadRailwayCrossingsSbvp">loadRailwayCrossings</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>If it is true, <code><a href="../Classes/SegmentData.html#/s:7heresdk11SegmentDataC16railwayCrossingsSayAA15RailwayCrossingVGSgvp">SegmentData.railwayCrossings</a></code> will be loaded when <code><a href="../Classes/SegmentDataLoader.html#/s:7heresdk17SegmentDataLoaderC04loadC07segment7optionsAA0bC0CAA12OCMSegmentIdV_AA0bcD7OptionsVtKF">SegmentDataLoader.loadData(...)</a></code> or <code><a href="../Classes/SegmentDataLoader.html#/s:7heresdk17SegmentDataLoaderC012loadDirectedbC07segment7optionsAA0bC0CAA0F12OCMSegmentIdV_AA0bcD7OptionsVtKF">SegmentDataLoader.loadDirectedSegmentData(...)</a></code> is called.
Defaults to <code>false</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">loadRailwayCrossings</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24SegmentDataLoaderOptionsV9loadUrbanSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/loadUrban"></a>
<a class="token" href="#/s:7heresdk24SegmentDataLoaderOptionsV9loadUrbanSbvp">loadUrban</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>If it is true, <code><a href="../Classes/SegmentSpanData.html#/s:7heresdk15SegmentSpanDataC7isUrbanSbSgvp">SegmentSpanData.isUrban</a></code> will be loaded when <code><a href="../Classes/SegmentDataLoader.html#/s:7heresdk17SegmentDataLoaderC04loadC07segment7optionsAA0bC0CAA12OCMSegmentIdV_AA0bcD7OptionsVtKF">SegmentDataLoader.loadData(...)</a></code> is called.
Defaults to <code>false</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">loadUrban</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24SegmentDataLoaderOptionsV26loadSpecialSpeedSituationsSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/loadSpecialSpeedSituations"></a>
<a class="token" href="#/s:7heresdk24SegmentDataLoaderOptionsV26loadSpecialSpeedSituationsSbvp">loadSpecialSpeedSituations</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>If it is true, <code><a href="../Classes/SegmentSpanData.html#/s:7heresdk15SegmentSpanDataC22specialSpeedSituationsSayAA0b7SpecialF9SituationVGSgvp">SegmentSpanData.specialSpeedSituations</a></code> will be loaded when <code><a href="../Classes/SegmentDataLoader.html#/s:7heresdk17SegmentDataLoaderC04loadC07segment7optionsAA0bC0CAA12OCMSegmentIdV_AA0bcD7OptionsVtKF">SegmentDataLoader.loadData(...)</a></code> is called.
<strong>Note:</strong> To get timezone offset and daylight saving time values for TimeRule, [sdk.mapdata.SegmentDataLoaderOptions.load_administrative_rules] must also be set to <code>true</code>.
Defaults to <code>false</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">loadSpecialSpeedSituations</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24SegmentDataLoaderOptionsV14loadTollPointsSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/loadTollPoints"></a>
<a class="token" href="#/s:7heresdk24SegmentDataLoaderOptionsV14loadTollPointsSbvp">loadTollPoints</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>If it is true, <code><a href="../Classes/SegmentData.html#/s:7heresdk11SegmentDataC10tollPointsSayAA9TollPointVGSgvp">SegmentData.tollPoints</a></code> will be loaded when <code><a href="../Classes/SegmentDataLoader.html#/s:7heresdk17SegmentDataLoaderC012loadDirectedbC07segment7optionsAA0bC0CAA0F12OCMSegmentIdV_AA0bcD7OptionsVtKF">SegmentDataLoader.loadDirectedSegmentData(...)</a></code> is called.
Defaults to <code>false</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">loadTollPoints</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24SegmentDataLoaderOptionsV19loadTravelDirection0F19FunctionalRoadClass0F20TransportModesAccess0F11SpeedLimits0F10BaseSpeeds0f5LocalJ15Characteristics0f14StreetNamesAndJ7Numbers0fJ10Attributes0F14TrafficSignals0fJ5Signs0F19AdministrativeRules0F16RailwayCrossings0F5Urban0f7SpecialO10Situations0F10TollPointsACSb_S14btcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(loadTravelDirection:loadFunctionalRoadClass:loadTransportModesAccess:loadSpeedLimits:loadBaseSpeeds:loadLocalRoadCharacteristics:loadStreetNamesAndRoadNumbers:loadRoadAttributes:loadTrafficSignals:loadRoadSigns:loadAdministrativeRules:loadRailwayCrossings:loadUrban:loadSpecialSpeedSituations:loadTollPoints:)"></a>
<a class="token" href="#/s:7heresdk24SegmentDataLoaderOptionsV19loadTravelDirection0F19FunctionalRoadClass0F20TransportModesAccess0F11SpeedLimits0F10BaseSpeeds0f5LocalJ15Characteristics0f14StreetNamesAndJ7Numbers0fJ10Attributes0F14TrafficSignals0fJ5Signs0F19AdministrativeRules0F16RailwayCrossings0F5Urban0f7SpecialO10Situations0F10TollPointsACSb_S14btcfc">init(loadTravelDirection:<wbr/>loadFunctionalRoadClass:<wbr/>loadTransportModesAccess:<wbr/>loadSpeedLimits:<wbr/>loadBaseSpeeds:<wbr/>loadLocalRoadCharacteristics:<wbr/>loadStreetNamesAndRoadNumbers:<wbr/>loadRoadAttributes:<wbr/>loadTrafficSignals:<wbr/>loadRoadSigns:<wbr/>loadAdministrativeRules:<wbr/>loadRailwayCrossings:<wbr/>loadUrban:<wbr/>loadSpecialSpeedSituations:<wbr/>loadTollPoints:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">loadTravelDirection</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">loadFunctionalRoadClass</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">loadTransportModesAccess</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">loadSpeedLimits</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">loadBaseSpeeds</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">loadLocalRoadCharacteristics</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">loadStreetNamesAndRoadNumbers</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">loadRoadAttributes</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">loadTrafficSignals</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">loadRoadSigns</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">loadAdministrativeRules</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">loadRailwayCrossings</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">loadUrban</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">loadSpecialSpeedSituations</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">loadTollPoints</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">)</span></code></pre>
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
