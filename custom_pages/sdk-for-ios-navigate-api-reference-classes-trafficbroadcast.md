---
title: "TrafficRadio / TrafficBroadcast"
slug: "sdk-for-ios-navigate-api-reference-classes-trafficbroadcast"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/TrafficBroadcast"></a>
<a title="TrafficBroadcast Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-trafficradio">TrafficRadio</a>
<img alt="" id="carat" src="../img/carat.png"/>
        TrafficBroadcast Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>TrafficBroadcast</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">TrafficBroadcast</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-locationdelegate">LocationDelegate</a></span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">TrafficBroadcast</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">TrafficBroadcast</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>A <code>TrafficBroadcast</code> is expecting the <a href="https://en.wikipedia.org/wiki/Traffic_message_channel">RDS-TMC</a>
format and it can be used when there is no internet connection, so that the <code><a href="sdk-for-ios-navigate-api-reference-..-classes-offlineroutingengine">OfflineRoutingEngine</a></code>
can utilize traffic data coming over a radio channel. The <code><a href="../Classes/TrafficBroadcast.html#/s:7heresdk16TrafficBroadcastC8activateyyF">TrafficBroadcast.activate(...)</a></code> method needs to be called to
receive traffic data events.</p>
<p><strong>Note:</strong> In order to adopt the <code><a href="../Traffic.html#/s:7heresdk19TrafficDataProviderC">TrafficDataProvider</a></code> interface special hardware is required. Talk
to your HERE representative for more details. Only by adopting the <code><a href="../Traffic.html#/s:7heresdk19TrafficDataProviderC">TrafficDataProvider</a></code> interface
you can integrate radio station signals providing traffic broadcasts. Traffic broadcasts are meant
to be used <em>independently</em> from the already included traffic on routes, on the map and from the
HERE backends (when using the <code><a href="sdk-for-ios-navigate-api-reference-..-classes-trafficengine">TrafficEngine</a></code>).</p>
<p>This class continuously reacts to new locations provided from a location source and acts as a
<code><a href="sdk-for-ios-navigate-api-reference-..-protocols-locationdelegate">LocationDelegate</a></code>. The location must be updated regardless of calling <code><a href="../Classes/TrafficBroadcast.html#/s:7heresdk16TrafficBroadcastC8activateyyF">TrafficBroadcast.activate(...)</a></code>.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16TrafficBroadcastC10parametersAcA0bC10ParametersV_tKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(parameters:)"></a>
<a class="token" href="#/s:7heresdk16TrafficBroadcastC10parametersAcA0bC10ParametersV_tKcfc">init(parameters:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance of this class.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Core.html#/s:7heresdk18InstantiationErrora">InstantiationError</a></code> when the object was not initialized properly.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">parameters</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-trafficbroadcastparameters">TrafficBroadcastParameters</a></span><span class="p">)</span> <span class="k">throws</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>parameters</em>
</code>
</td>
<td>
<div>
<p>The necessary parameters to start traffic broadcast.</p>
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
<a name="/s:7heresdk16TrafficBroadcastC_10parametersAcA15SDKNativeEngineC_AA0bC10ParametersVtKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:parameters:)"></a>
<a class="token" href="#/s:7heresdk16TrafficBroadcastC_10parametersAcA15SDKNativeEngineC_AA0bC10ParametersVtKcfc">init(_:<wbr/>parameters:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance of this class.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Core.html#/s:7heresdk18InstantiationErrora">InstantiationError</a></code> when the object was not initialized properly.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="n">_</span> <span class="nv">sdkEngine</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-sdknativeengine">SDKNativeEngine</a></span><span class="p">,</span> <span class="nv">parameters</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-trafficbroadcastparameters">TrafficBroadcastParameters</a></span><span class="p">)</span> <span class="k">throws</span></code></pre>
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
<p>Instance of an existing SDKEngine.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>parameters</em>
</code>
</td>
<td>
<div>
<p>The necessary parameters to start traffic broadcast.</p>
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
<a name="/s:7heresdk16TrafficBroadcastC19trafficDataProviderAA0beF0CSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/trafficDataProvider"></a>
<a class="token" href="#/s:7heresdk16TrafficBroadcastC19trafficDataProviderAA0beF0CSgvp">trafficDataProvider</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The traffic data provider that provides the traffic information.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">trafficDataProvider</span><span class="p">:</span> <span class="kt"><a href="../Traffic.html#/s:7heresdk19TrafficDataProviderC">TrafficDataProvider</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16TrafficBroadcastC17onLocationUpdatedyyAA0E0VF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/onLocationUpdated(_:)"></a>
<a class="token" href="#/s:7heresdk16TrafficBroadcastC17onLocationUpdatedyyAA0E0VF">onLocationUpdated(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Called each time a new location is available.
In a navigation context while using the <code><a href="sdk-for-ios-navigate-api-reference-..-classes-navigator">Navigator</a></code> or <code><a href="sdk-for-ios-navigate-api-reference-..-classes-visualnavigator">VisualNavigator</a></code>,
it’s required to set the <code><a href="../Structs/Location.html#/s:7heresdk8LocationV4time10Foundation4DateVSgvp">Location.time</a></code> parameter for each <code><a href="sdk-for-ios-navigate-api-reference-..-structs-location">Location</a></code>
object so that the HERE SDK can map-match the locations properly.
If the <code><a href="../Structs/Location.html#/s:7heresdk8LocationV4time10Foundation4DateVSgvp">Location.time</a></code> parameter is missing, the location will be ignored.
For navigation, it is also recommended to provide the <code>bearing</code> and <code>speed</code>
parameters for each <code><a href="sdk-for-ios-navigate-api-reference-..-structs-location">Location</a></code> object.
Invoked on the main thread.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">onLocationUpdated</span><span class="p">(</span><span class="n">_</span> <span class="nv">location</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-location">Location</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>location</em>
</code>
</td>
<td>
<div>
<p>Current location.</p>
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
<a name="/s:7heresdk16TrafficBroadcastC8activateyyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/activate()"></a>
<a class="token" href="#/s:7heresdk16TrafficBroadcastC8activateyyF">activate()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Activates the reception of traffic data over the radio channel.
This method is supposed to be called when the system loses internet connection,
so that traffic data can be switched from the online source to the radio channel.
When activation is done, requestTMCService is called from TMCServiceInterface</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">activate</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16TrafficBroadcastC10deactivateyyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/deactivate()"></a>
<a class="token" href="#/s:7heresdk16TrafficBroadcastC10deactivateyyF">deactivate()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Deactivates the reception of traffic data over the radio channel.
When deactivation is done, requestTMCService is called from TMCServiceInterface
With special case of countryCode parameter = 0</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">deactivate</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16TrafficBroadcastC31onTMCServiceProviderInfoUpdated018tmcServiceProdiverG0yAA0efG0V_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/onTMCServiceProviderInfoUpdated(tmcServiceProdiverInfo:)"></a>
<a class="token" href="#/s:7heresdk16TrafficBroadcastC31onTMCServiceProviderInfoUpdated018tmcServiceProdiverG0yAA0efG0V_tF">onTMCServiceProviderInfoUpdated(tmcServiceProdiverInfo:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Must be called on every TMC service prodiver info update.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">onTMCServiceProviderInfoUpdated</span><span class="p">(</span><span class="nv">tmcServiceProdiverInfo</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-tmcserviceproviderinfo">TMCServiceProviderInfo</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>tmcServiceProdiverInfo</em>
</code>
</td>
<td>
<div>
<p>Contains service prodiver info in RDS-TMC format.</p>
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
<a name="/s:7heresdk16TrafficBroadcastC16onTMCDataUpdated7tmcDatayAA0E0V_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/onTMCDataUpdated(tmcData:)"></a>
<a class="token" href="#/s:7heresdk16TrafficBroadcastC16onTMCDataUpdated7tmcDatayAA0E0V_tF">onTMCDataUpdated(tmcData:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Must be called on every TMC data update.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">onTMCDataUpdated</span><span class="p">(</span><span class="nv">tmcData</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-tmcdata">TMCData</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>tmcData</em>
</code>
</td>
<td>
<div>
<p>Contains the traffic events in RDS-TMC format.</p>
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
