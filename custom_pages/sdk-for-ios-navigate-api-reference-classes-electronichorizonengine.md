---
title: "sdk-for-ios-navigate-api-reference-classes-electronichorizonengine"
slug: "sdk-for-ios-navigate-api-reference-classes-electronichorizonengine"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/ElectronicHorizonEngine"></a>
<a title="ElectronicHorizonEngine Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-electronichorizon">ElectronicHorizon</a>
<img alt="" id="carat" src="/carat.png"/>
        ElectronicHorizonEngine Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>ElectronicHorizonEngine</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">ElectronicHorizonEngine</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">ElectronicHorizonEngine</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">ElectronicHorizonEngine</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Provides an electronic horizon engine that continuously predicts
the road network ahead of the vehicle by using detailed map data, including road topography that is
currently out of sight.
You can subscribe to electronic horizon updates based on position updates by using <code><a href="sdk-for-ios-navigate-api-reference-protocols-electronichorizondelegate">ElectronicHorizonDelegate</a></code>.
For more information about sub path levels, see <code><a href="../Structs/ElectronicHorizonOptions.html#/s:7heresdk24ElectronicHorizonOptionsV26lookAheadDistancesInMetersSaySdGvp">ElectronicHorizonOptions.lookAheadDistancesInMeters</a></code>.</p>
<p>The electronic horizon engine uses map-matched locations and can optionally use a <code><a href="sdk-for-ios-navigate-api-reference-classes-route">Route</a></code>
to improve the most-preferred path (MPP).</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23ElectronicHorizonEngineC03sdkD07options13transportMode5routeAcA09SDKNativeD0C_AA0bC7OptionsVAA09TransportH0OAA5RouteCSgtKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(sdkEngine:options:transportMode:route:)"></a>
<a class="token" href="#/s:7heresdk23ElectronicHorizonEngineC03sdkD07options13transportMode5routeAcA09SDKNativeD0C_AA0bC7OptionsVAA09TransportH0OAA5RouteCSgtKcfc">init(sdkEngine:<wbr/>options:<wbr/>transportMode:<wbr/>route:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance of <code>ElectronicHorizonEngine</code>.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Core.html#/s:7heresdk18InstantiationErrora">InstantiationError</a></code> <code><a href="../Core.html#/s:7heresdk18InstantiationErrora">InstantiationError</a></code> If the electronic horizon engine cannot be created.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">sdkEngine</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-sdknativeengine">SDKNativeEngine</a></span><span class="p">,</span> <span class="nv">options</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-electronichorizonoptions">ElectronicHorizonOptions</a></span><span class="p">,</span> <span class="nv">transportMode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-transportmode">TransportMode</a></span><span class="p">,</span> <span class="nv">route</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-route">Route</a></span><span class="p">?)</span> <span class="k">throws</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>sdkEngine</em>
</code>
</td>
<td>
<div>
<p>The <code><a href="sdk-for-ios-navigate-api-reference-classes-sdknativeengine">SDKNativeEngine</a></code> instance that provides shared services, such as networking and map data.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>options</em>
</code>
</td>
<td>
<div>
<p>The <code><a href="sdk-for-ios-navigate-api-reference-structs-electronichorizonoptions">ElectronicHorizonOptions</a></code> instance that configures how the electronic horizon is calculated, including look-ahead distances.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>transportMode</em>
</code>
</td>
<td>
<div>
<p>The <code><a href="sdk-for-ios-navigate-api-reference-enums-transportmode">TransportMode</a></code> that is used when building the electronic horizon paths.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>route</em>
</code>
</td>
<td>
<div>
<p>The <code><a href="sdk-for-ios-navigate-api-reference-classes-route">Route</a></code> that improves the calculation of the most-preferred path (MPP).
If <code>nil</code> is passed, the most-preferred path can deviate from the route.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23ElectronicHorizonEngineC5routeAA5RouteCSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/route"></a>
<a class="token" href="#/s:7heresdk23ElectronicHorizonEngineC5routeAA5RouteCSgvp">route</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The instance of <code><a href="sdk-for-ios-navigate-api-reference-classes-route">Route</a></code> that is being used by <code>ElectronicHorizonEngine</code>.
You can override this property to rebuild the electronic horizon based on a different route.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">route</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-route">Route</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23ElectronicHorizonEngineC6update18mapMatchedLocationyAA03MapgH0V_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/update(mapMatchedLocation:)"></a>
<a class="token" href="#/s:7heresdk23ElectronicHorizonEngineC6update18mapMatchedLocationyAA03MapgH0V_tF">update(mapMatchedLocation:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Updates the electronic horizon paths based on the provided map-matched location.
This method returns immediately and does not block.
When internal calculation is complete, callbacks are called on the main thread.
When multiple updates are triggered while processing is still running,
intermediate locations are skipped and only the last location is processed.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">update</span><span class="p">(</span><span class="nv">mapMatchedLocation</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-mapmatchedlocation">MapMatchedLocation</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>mapMatchedLocation</em>
</code>
</td>
<td>
<div>
<p>The map-matched location that defines the current vehicle position on the road network.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23ElectronicHorizonEngineC03addbC8DelegateyyAA0bcF0_pF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/addElectronicHorizonDelegate(_:)"></a>
<a class="token" href="#/s:7heresdk23ElectronicHorizonEngineC03addbC8DelegateyyAA0bcF0_pF">addElectronicHorizonDelegate(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Adds an <code><a href="sdk-for-ios-navigate-api-reference-protocols-electronichorizondelegate">ElectronicHorizonDelegate</a></code> to the subscription list.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">addElectronicHorizonDelegate</span><span class="p">(</span><span class="n">_</span> <span class="nv">electronicHorizonListener</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-electronichorizondelegate">ElectronicHorizonDelegate</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>electronicHorizonListener</em>
</code>
</td>
<td>
<div>
<p>The listener that receives electronic horizon path updates.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23ElectronicHorizonEngineC06removebC8DelegateyyAA0bcF0_pF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeElectronicHorizonDelegate(_:)"></a>
<a class="token" href="#/s:7heresdk23ElectronicHorizonEngineC06removebC8DelegateyyAA0bcF0_pF">removeElectronicHorizonDelegate(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes an <code><a href="sdk-for-ios-navigate-api-reference-protocols-electronichorizondelegate">ElectronicHorizonDelegate</a></code> from the subscription list.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">removeElectronicHorizonDelegate</span><span class="p">(</span><span class="n">_</span> <span class="nv">electronicHorizonListener</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-electronichorizondelegate">ElectronicHorizonDelegate</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>electronicHorizonListener</em>
</code>
</td>
<td>
<div>
<p>The listener that should no longer receive electronic horizon path updates.</p>
</div>
</td>
</tr>
</tbody>
</table>
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
