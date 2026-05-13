---
title: "MapFeatures Structure Reference"
slug: "sdk-for-ios-explore-api-reference-structs-mapfeatures"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- MapFeatures.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/MapFeatures"></a>
<a title="MapFeatures Structure Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="sdk-for-ios-explore-api-reference-..-index">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-maps">Maps</a>
<img alt="" id="carat" src="../img/carat.png"/>
        MapFeatures Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct MapFeatures</code></pre>
</div>
</div>
<p>Holds constants for map features, to be used with
<code><a href="../Classes/MapScene.html#/s:7heresdk8MapSceneC14enableFeaturesyySDyS2SGF">MapScene.enableFeatures(...)</a></code> and <code><a href="../Classes/MapScene.html#/s:7heresdk8MapSceneC15disableFeaturesyySaySSGF">MapScene.disableFeatures(...)</a></code>.</p>
<p>See <code><a href="sdk-for-ios-explore-api-reference-..-structs-mapfeaturemodes">MapFeatureModes</a></code> for constants representing feature modes.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapFeaturesV17extrudedBuildingsSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/extrudedBuildings"></a>
<a class="token" href="#/s:7heresdk11MapFeaturesV17extrudedBuildingsSSvpZ">extrudedBuildings</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Simple 3D representation of buildings.</p>
<p>Supports only one mode: <code><a href="../Structs/MapFeatureModes.html#/s:7heresdk15MapFeatureModesV20extrudedBuildingsAllSSvpZ">MapFeatureModes.extrudedBuildingsAll</a></code>.</p>
<p>Not supported for <code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO9satelliteyA2CmF">MapScheme.satellite</a></code>, <code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO14roadNetworkDayyA2CmF">MapScheme.roadNetworkDay</a></code>,
<code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO16roadNetworkNightyA2CmF">MapScheme.roadNetworkNight</a></code> and all hybrid schemes: <code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO9hybridDayyA2CmF">MapScheme.hybridDay</a></code>
<code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO11hybridNightyA2CmF">MapScheme.hybridNight</a></code>, <code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO13liteHybridDayyA2CmF">MapScheme.liteHybridDay</a></code>
<code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO15liteHybridNightyA2CmF">MapScheme.liteHybridNight</a></code>, <code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO18logisticsHybridDayyA2CmF">MapScheme.logisticsHybridDay</a></code> and
<code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO20logisticsHybridNightyA2CmF">MapScheme.logisticsHybridNight</a></code>.</p>
<p>By default, extruded buildings are enabled on all compatible map schemes.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let extrudedBuildings: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapFeaturesV18buildingFootprintsSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/buildingFootprints"></a>
<a class="token" href="#/s:7heresdk11MapFeaturesV18buildingFootprintsSSvpZ">buildingFootprints</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The 2D footprint of buildings.</p>
<p>Supports only one mode: <code><a href="../Structs/MapFeatureModes.html#/s:7heresdk15MapFeatureModesV21buildingFootprintsAllSSvpZ">MapFeatureModes.buildingFootprintsAll</a></code>.</p>
<p>Not supported for <code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO9satelliteyA2CmF">MapScheme.satellite</a></code>, <code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO14roadNetworkDayyA2CmF">MapScheme.roadNetworkDay</a></code>,
<code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO16roadNetworkNightyA2CmF">MapScheme.roadNetworkNight</a></code> and all hybrid schemes: <code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO9hybridDayyA2CmF">MapScheme.hybridDay</a></code>
<code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO11hybridNightyA2CmF">MapScheme.hybridNight</a></code>, <code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO13liteHybridDayyA2CmF">MapScheme.liteHybridDay</a></code>
<code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO15liteHybridNightyA2CmF">MapScheme.liteHybridNight</a></code>, <code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO18logisticsHybridDayyA2CmF">MapScheme.logisticsHybridDay</a></code> and
<code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO20logisticsHybridNightyA2CmF">MapScheme.logisticsHybridNight</a></code>.</p>
<p>By default, building footprints are enabled on all compatible map schemes.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let buildingFootprints: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapFeaturesV11trafficFlowSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/trafficFlow"></a>
<a class="token" href="#/s:7heresdk11MapFeaturesV11trafficFlowSSvpZ">trafficFlow</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Traffic flow speed. An online connection is required for the traffic
flow to be shown.</p>
<p>If the offline-mode is enabled for offline maps usage,
the live traffic flow can still be shown in offline mode by enabling
pass-through feature for traffic flow on <code>sdk.core.engine.SDKNativeEngine</code>.
See <code>sdk.core.engine.SDKNativeEngine.pass_through_features</code> for details.</p>
<p>Supported modes:</p>
<ul>
<li><code><a href="../Structs/MapFeatureModes.html#/s:7heresdk15MapFeatureModesV027trafficFlowJapanWithoutFreeF0SSvpZ">MapFeatureModes.trafficFlowJapanWithoutFreeFlow</a></code>,</li>
<li><code><a href="../Structs/MapFeatureModes.html#/s:7heresdk15MapFeatureModesV019trafficFlowWithFreeF0SSvpZ">MapFeatureModes.trafficFlowWithFreeFlow</a></code>,</li>
<li><code><a href="../Structs/MapFeatureModes.html#/s:7heresdk15MapFeatureModesV022trafficFlowWithoutFreeF0SSvpZ">MapFeatureModes.trafficFlowWithoutFreeFlow</a></code>.</li>
</ul>
<p>Default mode is <code><a href="../Structs/MapFeatureModes.html#/s:7heresdk15MapFeatureModesV019trafficFlowWithFreeF0SSvpZ">MapFeatureModes.trafficFlowWithFreeFlow</a></code>.</p>
<p>Not supported for <code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO9satelliteyA2CmF">MapScheme.satellite</a></code>, <code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO14roadNetworkDayyA2CmF">MapScheme.roadNetworkDay</a></code>
and <code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO16roadNetworkNightyA2CmF">MapScheme.roadNetworkNight</a></code>.
By default, this map feature is not enabled.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let trafficFlow: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapFeaturesV16trafficIncidentsSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/trafficIncidents"></a>
<a class="token" href="#/s:7heresdk11MapFeaturesV16trafficIncidentsSSvpZ">trafficIncidents</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Traffic incidents. An online connection is required for the traffic
incidents to be shown.</p>
<p>If the offline-mode is enabled for offline maps usage,
the live traffic incidents can still be shown in offline mode by enabling
pass-through feature for traffic incidents on <code>sdk.core.engine.SDKNativeEngine</code>.
See <code>sdk.core.engine.SDKNativeEngine.pass_through_features</code> for details.</p>
<p>Supports only one mode: <code><a href="../Structs/MapFeatureModes.html#/s:7heresdk15MapFeatureModesV19trafficIncidentsAllSSvpZ">MapFeatureModes.trafficIncidentsAll</a></code>.</p>
<p>Not supported for <code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO9satelliteyA2CmF">MapScheme.satellite</a></code>, <code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO14roadNetworkDayyA2CmF">MapScheme.roadNetworkDay</a></code>
and <code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO16roadNetworkNightyA2CmF">MapScheme.roadNetworkNight</a></code>.
By default, this map feature is not enabled.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let trafficIncidents: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapFeaturesV13trafficLightsSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/trafficLights"></a>
<a class="token" href="#/s:7heresdk11MapFeaturesV13trafficLightsSSvpZ">trafficLights</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Traffic lights.</p>
<p>Supports only one mode: <code><a href="../Structs/MapFeatureModes.html#/s:7heresdk15MapFeatureModesV16trafficLightsAllSSvpZ">MapFeatureModes.trafficLightsAll</a></code></p>
<p>Not supported for <code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO9satelliteyA2CmF">MapScheme.satellite</a></code>, <code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO14roadNetworkDayyA2CmF">MapScheme.roadNetworkDay</a></code>
and <code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO16roadNetworkNightyA2CmF">MapScheme.roadNetworkNight</a></code>.</p>
<p>By default, traffic lights are enabled on all compatible map schemes.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let trafficLights: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapFeaturesV18environmentalZonesSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/environmentalZones"></a>
<a class="token" href="#/s:7heresdk11MapFeaturesV18environmentalZonesSSvpZ">environmentalZones</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>City areas designated as environmental zones, which empose limitations
on the type of vehicles that are allowed to enter such areas.</p>
<p>Supports only one mode: <code><a href="../Structs/MapFeatureModes.html#/s:7heresdk15MapFeatureModesV21environmentalZonesAllSSvpZ">MapFeatureModes.environmentalZonesAll</a></code>.</p>
<p>Not supported for <code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO9satelliteyA2CmF">MapScheme.satellite</a></code>, <code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO14roadNetworkDayyA2CmF">MapScheme.roadNetworkDay</a></code>
and <code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO16roadNetworkNightyA2CmF">MapScheme.roadNetworkNight</a></code>.
By default, this map feature is not enabled.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let environmentalZones: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapFeaturesV15congestionZonesSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/congestionZones"></a>
<a class="token" href="#/s:7heresdk11MapFeaturesV15congestionZonesSSvpZ">congestionZones</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>City areas designated as congestion zones (or congestion charge zones),
which impose fees on entering such areas.</p>
<p>Supports only one mode: <code><a href="../Structs/MapFeatureModes.html#/s:7heresdk15MapFeatureModesV18congestionZonesAllSSvpZ">MapFeatureModes.congestionZonesAll</a></code>.</p>
<p>Not supported for <code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO9satelliteyA2CmF">MapScheme.satellite</a></code>, <code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO14roadNetworkDayyA2CmF">MapScheme.roadNetworkDay</a></code>
and <code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO16roadNetworkNightyA2CmF">MapScheme.roadNetworkNight</a></code>.
By default, this map feature is not enabled.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let congestionZones: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapFeaturesV13lowSpeedZonesSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/lowSpeedZones"></a>
<a class="token" href="#/s:7heresdk11MapFeaturesV13lowSpeedZonesSSvpZ">lowSpeedZones</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>City areas designated as low speed zones.
Only available when Japan map is used.</p>
<p>Supports only one mode: <code><a href="../Structs/MapFeatureModes.html#/s:7heresdk15MapFeatureModesV16lowSpeedZonesAllSSvpZ">MapFeatureModes.lowSpeedZonesAll</a></code>.</p>
<p>Not supported for <code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO9satelliteyA2CmF">MapScheme.satellite</a></code>, <code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO14roadNetworkDayyA2CmF">MapScheme.roadNetworkDay</a></code>
and <code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO16roadNetworkNightyA2CmF">MapScheme.roadNetworkNight</a></code>.
By default, this map feature is not enabled.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let lowSpeedZones: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapFeaturesV14roadExitLabelsSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/roadExitLabels"></a>
<a class="token" href="#/s:7heresdk11MapFeaturesV14roadExitLabelsSSvpZ">roadExitLabels</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Show or hide road exit labels, if available.</p>
<p>Supported modes: <code><a href="../Structs/MapFeatureModes.html#/s:7heresdk15MapFeatureModesV25roadExitLabelsNumbersOnlySSvpZ">MapFeatureModes.roadExitLabelsNumbersOnly</a></code>,
<code><a href="../Structs/MapFeatureModes.html#/s:7heresdk15MapFeatureModesV17roadExitLabelsAllSSvpZ">MapFeatureModes.roadExitLabelsAll</a></code></p>
<p>Default mode is <code><a href="../Structs/MapFeatureModes.html#/s:7heresdk15MapFeatureModesV25roadExitLabelsNumbersOnlySSvpZ">MapFeatureModes.roadExitLabelsNumbersOnly</a></code>.</p>
<p>Road exit labels are enabled by default with <code><a href="../Structs/MapFeatureModes.html#/s:7heresdk15MapFeatureModesV25roadExitLabelsNumbersOnlySSvpZ">MapFeatureModes.roadExitLabelsNumbersOnly</a></code>
on normal, lite and topo schemes and with <code><a href="../Structs/MapFeatureModes.html#/s:7heresdk15MapFeatureModesV17roadExitLabelsAllSSvpZ">MapFeatureModes.roadExitLabelsAll</a></code> on logistics
schemes. Note that topo schemes are only available in the HERE SDK Navigate variant.</p>
<p>Not supported for <code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO9satelliteyA2CmF">MapScheme.satellite</a></code>, <code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO14roadNetworkDayyA2CmF">MapScheme.roadNetworkDay</a></code>
and <code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO16roadNetworkNightyA2CmF">MapScheme.roadNetworkNight</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let roadExitLabels: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapFeaturesV7shadowsSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/shadows"></a>
<a class="token" href="#/s:7heresdk11MapFeaturesV7shadowsSSvpZ">shadows</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Shadows for all building types (extruded buildings and landmarks).</p>
<p>Supports only one mode: <code><a href="../Structs/MapFeatureModes.html#/s:7heresdk15MapFeatureModesV10shadowsAllSSvpZ">MapFeatureModes.shadowsAll</a></code>.</p>
<p>A <code><a href="sdk-for-ios-explore-api-reference-..-enums-shadowquality">ShadowQuality</a></code> must be set on the MapContext through a MapView or the feature has no
effect.</p>
<p>Shadows have a performance impact and should be considered only for devices with
sufficient performance.</p>
<p>Not supported for <code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO9satelliteyA2CmF">MapScheme.satellite</a></code>, <code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO14roadNetworkDayyA2CmF">MapScheme.roadNetworkDay</a></code>,
<code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO16roadNetworkNightyA2CmF">MapScheme.roadNetworkNight</a></code> and all hybrid schemes: <code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO9hybridDayyA2CmF">MapScheme.hybridDay</a></code>
<code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO11hybridNightyA2CmF">MapScheme.hybridNight</a></code>, <code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO13liteHybridDayyA2CmF">MapScheme.liteHybridDay</a></code>
<code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO15liteHybridNightyA2CmF">MapScheme.liteHybridNight</a></code>, <code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO18logisticsHybridDayyA2CmF">MapScheme.logisticsHybridDay</a></code> and
<code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO20logisticsHybridNightyA2CmF">MapScheme.logisticsHybridNight</a></code>.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.
By default, this map feature is not enabled.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let shadows: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapFeaturesV16ambientOcclusionSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/ambientOcclusion"></a>
<a class="token" href="#/s:7heresdk11MapFeaturesV16ambientOcclusionSSvpZ">ambientOcclusion</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Ambient occlusion effect for 3D geometries (extruded buildings and landmarks).</p>
<p>Supports only one mode: <code><a href="../Structs/MapFeatureModes.html#/s:7heresdk15MapFeatureModesV19ambientOcclusionAllSSvpZ">MapFeatureModes.ambientOcclusionAll</a></code>.</p>
<p>This visual effect has a performance impact and should be considered only for devices with
sufficient performance.</p>
<p>Not supported for <code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO9satelliteyA2CmF">MapScheme.satellite</a></code>, <code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO14roadNetworkDayyA2CmF">MapScheme.roadNetworkDay</a></code>,
<code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO16roadNetworkNightyA2CmF">MapScheme.roadNetworkNight</a></code> and all hybrid schemes: <code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO9hybridDayyA2CmF">MapScheme.hybridDay</a></code>
<code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO11hybridNightyA2CmF">MapScheme.hybridNight</a></code>, <code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO13liteHybridDayyA2CmF">MapScheme.liteHybridDay</a></code>
<code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO15liteHybridNightyA2CmF">MapScheme.liteHybridNight</a></code>, <code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO18logisticsHybridDayyA2CmF">MapScheme.logisticsHybridDay</a></code> and
<code><a href="../Enums/MapScheme.html#/s:7heresdk9MapSchemeO20logisticsHybridNightyA2CmF">MapScheme.logisticsHybridNight</a></code>.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.
By default, this map feature is not enabled.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let ambientOcclusion: String</code></pre>
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



</div>
`
}</HTMLBlock>
