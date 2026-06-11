---
title: "MapContentSettings"
slug: "sdk-for-ios-explore-api-reference-classes-mapcontentsettings"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapContentSettings"></a>
<a title="MapContentSettings Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>

<a href="sdk-for-ios-explore-api-reference-maps">Maps</a>

        MapContentSettings Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>MapContentSettings</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapContentSettings</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapContentSettings</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapContentSettings</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Provides settings regarding map data which are applied globally to all map views. The settings
can already be changed before a map view instance is created.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18MapContentSettingsC25TrafficRefreshPeriodErrora"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/TrafficRefreshPeriodError"></a>
<a class="token" href="#/s:7heresdk18MapContentSettingsC25TrafficRefreshPeriodErrora">TrafficRefreshPeriodError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Traffic refresh period error exception</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">TrafficRefreshPeriodError</span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-mapcontentsettings-trafficrefreshperioderrorcode">TrafficRefreshPeriodErrorCode</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18MapContentSettingsC29TrafficRefreshPeriodErrorCodeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/TrafficRefreshPeriodErrorCode"></a>
<a class="token" href="#/s:7heresdk18MapContentSettingsC29TrafficRefreshPeriodErrorCodeO">TrafficRefreshPeriodErrorCode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Traffic refresh period error code</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-mapcontentsettings-trafficrefreshperioderrorcode">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">TrafficRefreshPeriodErrorCode</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-mapcontentsettings">MapContentSettings</a></span><span class="o">.</span><span class="kt">TrafficRefreshPeriodErrorCode</span> <span class="p">:</span> <span class="kt">Error</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18MapContentSettingsC22filterTrafficIncidents07trafficG0ySayAA0F12IncidentTypeOG_tFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/filterTrafficIncidents(trafficIncidents:)"></a>
<a class="token" href="#/s:7heresdk18MapContentSettingsC22filterTrafficIncidents07trafficG0ySayAA0F12IncidentTypeOG_tFZ">filterTrafficIncidents(trafficIncidents:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Filters the displayed traffic incidents so that only the ones applicable to the specified
criteria are shown when general display of traffic incidents is enabled.
The display of traffic incidents can be enabled using <code><a href="../Classes/MapScene.html#/s:7heresdk8MapSceneC14enableFeaturesyySDyS2SGF">MapScene.enableFeatures(...)</a></code> with
<code><a href="../Structs/MapFeatures.html#/s:7heresdk11MapFeaturesV16trafficIncidentsSSvpZ">MapFeatures.trafficIncidents</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">filterTrafficIncidents</span><span class="p">(</span><span class="nv">trafficIncidents</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-trafficincidenttype">TrafficIncidentType</a></span><span class="p">])</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>trafficIncidents</em>
</code>
</td>
<td>
<div>
<p>The traffic incidents to filter for, so that only applicable incidents are displayed.
When the list is empty, then all traffic incidents will be displayed.
If the <code>MapContentSettings.filterTrafficIncidents(...).trafficIncidents</code> contains <code><a href="../Enums/TrafficIncidentType.html#/s:7heresdk19TrafficIncidentTypeO7unknownyA2CmF">TrafficIncidentType.unknown</a></code>, then the
traffic filter will be applied ignoring this element.</p>
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
<a name="/s:7heresdk18MapContentSettingsC26resetTrafficIncidentFilteryyFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/resetTrafficIncidentFilter()"></a>
<a class="token" href="#/s:7heresdk18MapContentSettingsC26resetTrafficIncidentFilteryyFZ">resetTrafficIncidentFilter()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes all filters regarding Traffic Incidents so that all incidents will be displayed,
when the display of Traffic Incidents is enabled using <code><a href="../Classes/MapScene.html#/s:7heresdk8MapSceneC14enableFeaturesyySDyS2SGF">MapScene.enableFeatures(...)</a></code> with
<code><a href="../Structs/MapFeatures.html#/s:7heresdk11MapFeaturesV16trafficIncidentsSSvpZ">MapFeatures.trafficIncidents</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">resetTrafficIncidentFilter</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18MapContentSettingsC23setTrafficRefreshPeriodyySdKFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setTrafficRefreshPeriod(_:)"></a>
<a class="token" href="#/s:7heresdk18MapContentSettingsC23setTrafficRefreshPeriodyySdKFZ">setTrafficRefreshPeriod(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the traffic data refresh period for both <code><a href="../Structs/MapFeatures.html#/s:7heresdk11MapFeaturesV11trafficFlowSSvpZ">MapFeatures.trafficFlow</a></code> and
<code><a href="../Structs/MapFeatures.html#/s:7heresdk11MapFeaturesV16trafficIncidentsSSvpZ">MapFeatures.trafficIncidents</a></code>. By default, the traffic information
validity time and the refresh period is derived from the refresh period of HERE’s traffic server.
The period set by this function will override the server’s default setting for
upcoming traffic data requests.
Defaults to 60 seconds.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Classes/MapContentSettings.html#/s:7heresdk18MapContentSettingsC25TrafficRefreshPeriodErrora">MapContentSettings.TrafficRefreshPeriodError</a></code> <code><a href="../Classes/MapContentSettings.html#/s:7heresdk18MapContentSettingsC25TrafficRefreshPeriodErrora">MapContentSettings.TrafficRefreshPeriodError</a></code> indicates what went wrong.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">setTrafficRefreshPeriod</span><span class="p">(</span><span class="n">_</span> <span class="nv">value</span><span class="p">:</span> <span class="kt">TimeInterval</span><span class="p">)</span> <span class="k">throws</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>value</em>
</code>
</td>
<td>
<div>
<p>Traffic data refresh period in seconds. Valid range is [60, 300] seconds.
The shortest refresh period that can be set is 60 seconds. This means that the traffic
data shown on a map view will be refreshed every minute.
The longest refresh period that can be set is 300 seconds. This means that the traffic
data shown on the current map view will be refreshed every 5 minutes
if the viewport does not change.
Note that when a viewport change occurs, new traffic data may be requested
regardless of the set refresh period. For example, during turn-by-turn navigation,
frequent viewport changes can result in missing traffic data, causing new requests
to be made more often.</p>
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
<a name="/s:7heresdk18MapContentSettingsC25resetTrafficRefreshPeriodyyFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/resetTrafficRefreshPeriod()"></a>
<a class="token" href="#/s:7heresdk18MapContentSettingsC25resetTrafficRefreshPeriodyyFZ">resetTrafficRefreshPeriod()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Resets the traffic data (both flow and incidents) refresh period so the default traffic information
validity time and the refresh period derived from the refresh period of the traffic server is used.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">resetTrafficRefreshPeriod</span><span class="p">()</span></code></pre>
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
