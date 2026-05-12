---
title: "MapSceneLoadOptionsBuilder Class Reference"
slug: "sdk-for-ios-explore-api-reference-classes-mapsceneloadoptionsbuilder"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- MapSceneLoadOptionsBuilder.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Class/MapSceneLoadOptionsBuilder"></a>
<a title="MapSceneLoadOptionsBuilder Class Reference"></a>
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
        MapSceneLoadOptionsBuilder Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public class MapSceneLoadOptionsBuilder</code></pre>
<pre><code>extension MapSceneLoadOptionsBuilder: NativeBase</code></pre>
<pre><code>extension MapSceneLoadOptionsBuilder: Hashable</code></pre>
</div>
</div>
<p>Builder for creating <code><a href="../Maps.html#/s:7heresdk19MapSceneLoadOptionsC">MapSceneLoadOptions</a></code> instances.
This builder ensures that either a MapScheme or a configuration file is set, but not both.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk26MapSceneLoadOptionsBuilderC18InstantiationErrora"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/InstantiationError"></a>
<a class="token" href="#/s:7heresdk26MapSceneLoadOptionsBuilderC18InstantiationErrora">InstantiationError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Thrown when failing to build a <code><a href="../Maps.html#/s:7heresdk19MapSceneLoadOptionsC">MapSceneLoadOptions</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public typealias InstantiationError = InstantiationErrorDetails</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk26MapSceneLoadOptionsBuilderCACycfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init()"></a>
<a class="token" href="#/s:7heresdk26MapSceneLoadOptionsBuilderCACycfc">init()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new builder instance.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public init()</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk26MapSceneLoadOptionsBuilderC22InstantiationErrorCodeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/InstantiationErrorCode"></a>
<a class="token" href="#/s:7heresdk26MapSceneLoadOptionsBuilderC22InstantiationErrorCodeO">InstantiationErrorCode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Describes a reason for failing to build a <code><a href="../Maps.html#/s:7heresdk19MapSceneLoadOptionsC">MapSceneLoadOptions</a></code>.</p>
<a class="slightly-smaller" href="../Classes/MapSceneLoadOptionsBuilder/InstantiationErrorCode.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum InstantiationErrorCode : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk26MapSceneLoadOptionsBuilderC25InstantiationErrorDetailsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/InstantiationErrorDetails"></a>
<a class="token" href="#/s:7heresdk26MapSceneLoadOptionsBuilderC25InstantiationErrorDetailsV">InstantiationErrorDetails</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Describes the reason for failing to build a <code><a href="../Maps.html#/s:7heresdk19MapSceneLoadOptionsC">MapSceneLoadOptions</a></code>.</p>
<a class="slightly-smaller" href="../Classes/MapSceneLoadOptionsBuilder/InstantiationErrorDetails.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct InstantiationErrorDetails</code></pre>
<pre><code>extension MapSceneLoadOptionsBuilder.InstantiationErrorDetails : Error</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk26MapSceneLoadOptionsBuilderC04withB6Scheme03mapH0AcA0bH0O_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withMapScheme(mapScheme:)"></a>
<a class="token" href="#/s:7heresdk26MapSceneLoadOptionsBuilderC04withB6Scheme03mapH0AcA0bH0O_tF">withMapScheme(mapScheme:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the map scheme to load.
Any configuration file set through <code><a href="../Classes/MapSceneLoadOptionsBuilder.html#/s:7heresdk26MapSceneLoadOptionsBuilderC21withConfigurationFile013configurationI0ACSS_tF">MapSceneLoadOptionsBuilder.withConfigurationFile(...)</a></code> will be discarded.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func withMapScheme(mapScheme: MapScheme) -&gt; MapSceneLoadOptionsBuilder</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>mapScheme</em>
</code>
</td>
<td>
<div>
<p>Map scheme to load.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>This class instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk26MapSceneLoadOptionsBuilderC21withConfigurationFile013configurationI0ACSS_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withConfigurationFile(configurationFile:)"></a>
<a class="token" href="#/s:7heresdk26MapSceneLoadOptionsBuilderC21withConfigurationFile013configurationI0ACSS_tF">withConfigurationFile(configurationFile:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the configuration file path to load.
Any map scheme set through <code><a href="../Classes/MapSceneLoadOptionsBuilder.html#/s:7heresdk26MapSceneLoadOptionsBuilderC04withB6Scheme03mapH0AcA0bH0O_tF">MapSceneLoadOptionsBuilder.withMapScheme(...)</a></code> will be discarded.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func withConfigurationFile(configurationFile: String) -&gt; MapSceneLoadOptionsBuilder</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>configurationFile</em>
</code>
</td>
<td>
<div>
<p>Configuration file path to load.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>This class instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk26MapSceneLoadOptionsBuilderC19withEnabledFeatures07enabledI0ACSDyS2SG_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withEnabledFeatures(enabledFeatures:)"></a>
<a class="token" href="#/s:7heresdk26MapSceneLoadOptionsBuilderC19withEnabledFeatures07enabledI0ACSDyS2SG_tF">withEnabledFeatures(enabledFeatures:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the features to enable in the new configuration.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func withEnabledFeatures(enabledFeatures: [String : String]) -&gt; MapSceneLoadOptionsBuilder</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>enabledFeatures</em>
</code>
</td>
<td>
<div>
<p>Features to enable. Key = feature name, value = mode name.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>This class instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk26MapSceneLoadOptionsBuilderC20withDisabledFeatures08disabledI0ACSaySSG_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withDisabledFeatures(disabledFeatures:)"></a>
<a class="token" href="#/s:7heresdk26MapSceneLoadOptionsBuilderC20withDisabledFeatures08disabledI0ACSaySSG_tF">withDisabledFeatures(disabledFeatures:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the features to disable in the new configuration.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func withDisabledFeatures(disabledFeatures: [String]) -&gt; MapSceneLoadOptionsBuilder</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>disabledFeatures</em>
</code>
</td>
<td>
<div>
<p>Features to disable.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>This class instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk26MapSceneLoadOptionsBuilderC18withWatermarkStyle09watermarkI0AcA0hI0O_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withWatermarkStyle(watermarkStyle:)"></a>
<a class="token" href="#/s:7heresdk26MapSceneLoadOptionsBuilderC18withWatermarkStyle09watermarkI0AcA0hI0O_tF">withWatermarkStyle(watermarkStyle:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the watermark style.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func withWatermarkStyle(watermarkStyle: WatermarkStyle) -&gt; MapSceneLoadOptionsBuilder</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>watermarkStyle</em>
</code>
</td>
<td>
<div>
<p>Watermark style to use.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>This class instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk26MapSceneLoadOptionsBuilderC014withOverridingB5Style010overridingbI0AcA0I0C_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withOverridingMapStyle(overridingMapStyle:)"></a>
<a class="token" href="#/s:7heresdk26MapSceneLoadOptionsBuilderC014withOverridingB5Style010overridingbI0AcA0I0C_tF">withOverridingMapStyle(overridingMapStyle:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the style to override what is defined in the scene configuration.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func withOverridingMapStyle(overridingMapStyle: Style) -&gt; MapSceneLoadOptionsBuilder</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>overridingMapStyle</em>
</code>
</td>
<td>
<div>
<p>Map style to override the scene configuration.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>This class instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk26MapSceneLoadOptionsBuilderC5buildAA0bcdE0CyKF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/build()"></a>
<a class="token" href="#/s:7heresdk26MapSceneLoadOptionsBuilderC5buildAA0bcdE0CyKF">build()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Builds the <code><a href="../Maps.html#/s:7heresdk19MapSceneLoadOptionsC">MapSceneLoadOptions</a></code> instance.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Classes/MapSceneLoadOptionsBuilder.html#/s:7heresdk26MapSceneLoadOptionsBuilderC18InstantiationErrora">MapSceneLoadOptionsBuilder.InstantiationError</a></code> Indicates an instantiation issue.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func build() throws -&gt; MapSceneLoadOptions</code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>A new MapSceneLoadOptions instance.</p>
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
