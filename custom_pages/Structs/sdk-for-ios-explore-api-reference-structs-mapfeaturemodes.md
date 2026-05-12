---
title: "MapFeatureModes Structure Reference"
slug: "sdk-for-ios-explore-api-reference-structs-mapfeaturemodes"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- MapFeatureModes.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/MapFeatureModes"></a>
<a title="MapFeatureModes Structure Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="../index.html">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="../index.html">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="../Maps.html">Maps</a>
<img alt="" id="carat" src="../img/carat.png"/>
        MapFeatureModes Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct MapFeatureModes</code></pre>
</div>
</div>
<p>Holds constants for map feature modes, to be used with <code><a href="../Classes/MapScene.html#/s:7heresdk8MapSceneC14enableFeaturesyySDyS2SGF">MapScene.enableFeatures(...)</a></code>.</p>
<p>Use <code><a href="../Structs/MapFeatureModes.html#/s:7heresdk15MapFeatureModesV11defaultModeSSvpZ">MapFeatureModes.defaultMode</a></code> to enable a feature with its default mode.</p>
<p>Note: The default mode is defined by the currently loaded map scene configuration and
may vary per <code><a href="../Enums/MapScheme.html">MapScheme</a></code>. The currently active features and modes can be inspected
using <code><a href="../Classes/MapScene.html#/s:7heresdk8MapSceneC17getActiveFeaturesSDyS2SGyF">MapScene.getActiveFeatures(...)</a></code> after the scene is loaded.</p>
<p>See <code><a href="../Structs/MapFeatures.html">MapFeatures</a></code> for constants representing the feature names.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15MapFeatureModesV11defaultModeSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/defaultMode"></a>
<a class="token" href="#/s:7heresdk15MapFeatureModesV11defaultModeSSvpZ">defaultMode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Enables the default mode of a map feature. Can be used with any map feature.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let defaultMode: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15MapFeatureModesV21buildingFootprintsAllSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/buildingFootprintsAll"></a>
<a class="token" href="#/s:7heresdk15MapFeatureModesV21buildingFootprintsAllSSvpZ">buildingFootprintsAll</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>All building footprints are shown.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let buildingFootprintsAll: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15MapFeatureModesV18congestionZonesAllSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/congestionZonesAll"></a>
<a class="token" href="#/s:7heresdk15MapFeatureModesV18congestionZonesAllSSvpZ">congestionZonesAll</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>All congestion zones are shown.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let congestionZonesAll: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15MapFeatureModesV20extrudedBuildingsAllSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/extrudedBuildingsAll"></a>
<a class="token" href="#/s:7heresdk15MapFeatureModesV20extrudedBuildingsAllSSvpZ">extrudedBuildingsAll</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>All extruded buildings are shown.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let extrudedBuildingsAll: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15MapFeatureModesV21environmentalZonesAllSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/environmentalZonesAll"></a>
<a class="token" href="#/s:7heresdk15MapFeatureModesV21environmentalZonesAllSSvpZ">environmentalZonesAll</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>All environmental zones are shown.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let environmentalZonesAll: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15MapFeatureModesV16lowSpeedZonesAllSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/lowSpeedZonesAll"></a>
<a class="token" href="#/s:7heresdk15MapFeatureModesV16lowSpeedZonesAllSSvpZ">lowSpeedZonesAll</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>All low speed zones are shown.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let lowSpeedZonesAll: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15MapFeatureModesV027trafficFlowJapanWithoutFreeF0SSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/trafficFlowJapanWithoutFreeFlow"></a>
<a class="token" href="#/s:7heresdk15MapFeatureModesV027trafficFlowJapanWithoutFreeF0SSvpZ">trafficFlowJapanWithoutFreeFlow</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Only available when Japan map is used.</p>
<p>Traffic flow shows green lines depending on the region.</p>
<p>In Japan green lines will not be shown,
as if the <code><a href="../Structs/MapFeatureModes.html#/s:7heresdk15MapFeatureModesV022trafficFlowWithoutFreeF0SSvpZ">MapFeatureModes.trafficFlowWithoutFreeFlow</a></code> were used.</p>
<p>In rest of the world, green lines will be shown, as if
the <code><a href="../Structs/MapFeatureModes.html#/s:7heresdk15MapFeatureModesV019trafficFlowWithFreeF0SSvpZ">MapFeatureModes.trafficFlowWithFreeFlow</a></code> were used.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let trafficFlowJapanWithoutFreeFlow: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15MapFeatureModesV019trafficFlowWithFreeF0SSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/trafficFlowWithFreeFlow"></a>
<a class="token" href="#/s:7heresdk15MapFeatureModesV019trafficFlowWithFreeF0SSvpZ">trafficFlowWithFreeFlow</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Traffic flow shows green lines when there is no traffic congestion.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let trafficFlowWithFreeFlow: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15MapFeatureModesV022trafficFlowWithoutFreeF0SSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/trafficFlowWithoutFreeFlow"></a>
<a class="token" href="#/s:7heresdk15MapFeatureModesV022trafficFlowWithoutFreeF0SSvpZ">trafficFlowWithoutFreeFlow</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Traffic flow does not show green lines when there is no traffic congestion.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let trafficFlowWithoutFreeFlow: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15MapFeatureModesV19trafficIncidentsAllSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/trafficIncidentsAll"></a>
<a class="token" href="#/s:7heresdk15MapFeatureModesV19trafficIncidentsAllSSvpZ">trafficIncidentsAll</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>All available traffic incidents are shown.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let trafficIncidentsAll: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15MapFeatureModesV16trafficLightsAllSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/trafficLightsAll"></a>
<a class="token" href="#/s:7heresdk15MapFeatureModesV16trafficLightsAllSSvpZ">trafficLightsAll</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>All available traffic lights are shown.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let trafficLightsAll: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15MapFeatureModesV25roadExitLabelsNumbersOnlySSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/roadExitLabelsNumbersOnly"></a>
<a class="token" href="#/s:7heresdk15MapFeatureModesV25roadExitLabelsNumbersOnlySSvpZ">roadExitLabelsNumbersOnly</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Road exit labels are shown with numbers, if available.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let roadExitLabelsNumbersOnly: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15MapFeatureModesV17roadExitLabelsAllSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/roadExitLabelsAll"></a>
<a class="token" href="#/s:7heresdk15MapFeatureModesV17roadExitLabelsAllSSvpZ">roadExitLabelsAll</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Road exit labels are shown with numbers and names, if available.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let roadExitLabelsAll: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15MapFeatureModesV10shadowsAllSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/shadowsAll"></a>
<a class="token" href="#/s:7heresdk15MapFeatureModesV10shadowsAllSSvpZ">shadowsAll</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Shadows are shown for extruded buildings and landmarks.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let shadowsAll: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15MapFeatureModesV19ambientOcclusionAllSSvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/ambientOcclusionAll"></a>
<a class="token" href="#/s:7heresdk15MapFeatureModesV19ambientOcclusionAllSSvpZ">ambientOcclusionAll</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Ambient occlusion effect is shown for extruded buildings and landmarks.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static let ambientOcclusionAll: String</code></pre>
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
