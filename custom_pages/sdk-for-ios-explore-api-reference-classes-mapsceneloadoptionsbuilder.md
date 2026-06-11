---
title: "MapSceneLoadOptionsBuilder"
slug: "sdk-for-ios-explore-api-reference-classes-mapsceneloadoptionsbuilder"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapSceneLoadOptionsBuilder"></a>
<a title="MapSceneLoadOptionsBuilder Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>

<a href="sdk-for-ios-explore-api-reference-maps">Maps</a>

        MapSceneLoadOptionsBuilder Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>MapSceneLoadOptionsBuilder</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapSceneLoadOptionsBuilder</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapSceneLoadOptionsBuilder</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapSceneLoadOptionsBuilder</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">InstantiationError</span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-mapsceneloadoptionsbuilder-instantiationerrordetails">InstantiationErrorDetails</a></span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">()</span></code></pre>
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
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-mapsceneloadoptionsbuilder-instantiationerrorcode">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">InstantiationErrorCode</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
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
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-mapsceneloadoptionsbuilder-instantiationerrordetails">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">InstantiationErrorDetails</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-mapsceneloadoptionsbuilder">MapSceneLoadOptionsBuilder</a></span><span class="o">.</span><span class="kt">InstantiationErrorDetails</span> <span class="p">:</span> <span class="kt">Error</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">withMapScheme</span><span class="p">(</span><span class="nv">mapScheme</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-mapscheme">MapScheme</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">MapSceneLoadOptionsBuilder</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">withConfigurationFile</span><span class="p">(</span><span class="nv">configurationFile</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">MapSceneLoadOptionsBuilder</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">withEnabledFeatures</span><span class="p">(</span><span class="nv">enabledFeatures</span><span class="p">:</span> <span class="p">[</span><span class="kt">String</span> <span class="p">:</span> <span class="kt">String</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kt">MapSceneLoadOptionsBuilder</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">withDisabledFeatures</span><span class="p">(</span><span class="nv">disabledFeatures</span><span class="p">:</span> <span class="p">[</span><span class="kt">String</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kt">MapSceneLoadOptionsBuilder</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">withWatermarkStyle</span><span class="p">(</span><span class="nv">watermarkStyle</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-watermarkstyle">WatermarkStyle</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">MapSceneLoadOptionsBuilder</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">withOverridingMapStyle</span><span class="p">(</span><span class="nv">overridingMapStyle</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-style">Style</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">MapSceneLoadOptionsBuilder</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">build</span><span class="p">()</span> <span class="k">throws</span> <span class="o">-&gt;</span> <span class="kt"><a href="../Maps.html#/s:7heresdk19MapSceneLoadOptionsC">MapSceneLoadOptions</a></span></code></pre>
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
</body>
</html>

`
}</HTMLBlock>
