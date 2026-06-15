---
title: "LocationEngineBase"
slug: "sdk-for-ios-navigate-api-reference-protocols-locationenginebase"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/LocationEngineBase"></a>
<a title="LocationEngineBase Protocol Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-positioning">Positioning</a>

        LocationEngineBase Protocol Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>LocationEngineBase</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">LocationEngineBase</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
<p>Public protocol that describes the behaviour of <code><a href="sdk-for-ios-navigate-api-reference-classes-locationengine">LocationEngine</a></code>.
Implementation is platform-specific.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18LocationEngineBaseP09lastKnownB0AA0B0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/lastKnownLocation"></a>
<a class="token" href="#/s:7heresdk18LocationEngineBaseP09lastKnownB0AA0B0VSgvp">lastKnownLocation</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The last known location obtained by the <code><a href="sdk-for-ios-navigate-api-reference-classes-locationengine">LocationEngine</a></code>. It is persisted throughout the app’s lifecycle.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">lastKnownLocation</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-location">Location</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18LocationEngineBaseP9isStartedSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isStarted"></a>
<a class="token" href="#/s:7heresdk18LocationEngineBaseP9isStartedSbvp">isStarted</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Checks if the engine is in started state.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">isStarted</span><span class="p">:</span> <span class="kt">Bool</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18LocationEngineBaseP5start16locationAccuracyAA0bC6StatusOAA0bG0O_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/start(locationAccuracy:)"></a>
<a class="token" href="#/s:7heresdk18LocationEngineBaseP5start16locationAccuracyAA0bC6StatusOAA0bG0O_tF">start(locationAccuracy:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Starts the location engine with desired <code><a href="sdk-for-ios-navigate-api-reference-enums-locationaccuracy">LocationAccuracy</a></code>. Returns
<code><a href="../Enums/LocationEngineStatus.html#/s:7heresdk20LocationEngineStatusO14alreadyStartedyA2CmF">LocationEngineStatus.alreadyStarted</a></code>, if <code>start(LocationOptions)</code> is called again without <code><a href="../Protocols/LocationEngineBase.html#/s:7heresdk18LocationEngineBaseP4stopyyF">stop(...)</a></code> in between.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">start</span><span class="p">(</span><span class="nv">locationAccuracy</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-locationaccuracy">LocationAccuracy</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-locationenginestatus">LocationEngineStatus</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>locationAccuracy</em>
</code>
</td>
<td>
<div>
<p>Desired location accuracy. Requested accuracy is not guaranteed.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Engine status. Valid values are defined in <code><a href="sdk-for-ios-navigate-api-reference-enums-locationenginestatus">LocationEngineStatus</a></code></p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18LocationEngineBaseP06updateB8Accuracy08locationF0AA0bC6StatusOAA0bF0O_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/updateLocationAccuracy(locationAccuracy:)"></a>
<a class="token" href="#/s:7heresdk18LocationEngineBaseP06updateB8Accuracy08locationF0AA0bC6StatusOAA0bF0O_tF">updateLocationAccuracy(locationAccuracy:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Reconfigures the location engine with desired <code><a href="sdk-for-ios-navigate-api-reference-enums-locationaccuracy">LocationAccuracy</a></code>. This method is a faster way to change location accuracy for already started
location engine, than calling <code><a href="../Protocols/LocationEngineBase.html#/s:7heresdk18LocationEngineBaseP4stopyyF">stop(...)</a></code> and <code>start(LocationOptions)</code> in sequence. Returns <code><a href="../Enums/LocationEngineStatus.html#/s:7heresdk20LocationEngineStatusO8notReadyyA2CmF">LocationEngineStatus.notReady</a></code>,
if called for unstarted location engine.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">updateLocationAccuracy</span><span class="p">(</span><span class="nv">locationAccuracy</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-locationaccuracy">LocationAccuracy</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-locationenginestatus">LocationEngineStatus</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>locationAccuracy</em>
</code>
</td>
<td>
<div>
<p>Desired location accuracy. Requested accuracy is not guaranteed.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Engine status. Valid values are defined in <code><a href="sdk-for-ios-navigate-api-reference-enums-locationenginestatus">LocationEngineStatus</a></code></p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18LocationEngineBaseP4stopyyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/stop()"></a>
<a class="token" href="#/s:7heresdk18LocationEngineBaseP4stopyyF">stop()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Stops the location engine.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">stop</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18LocationEngineBaseP03addB8Delegate08locationF0yAA0bF0_p_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/addLocationDelegate(locationDelegate:)"></a>
<a class="token" href="#/s:7heresdk18LocationEngineBaseP03addB8Delegate08locationF0yAA0bF0_p_tF">addLocationDelegate(locationDelegate:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Adds a <code><a href="sdk-for-ios-navigate-api-reference-protocols-locationdelegate">LocationDelegate</a></code> to the engine to get notified when there is a new location
update available. Supports more than one delegate, instance is added only once.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">addLocationDelegate</span><span class="p">(</span><span class="nv">locationDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-locationdelegate">LocationDelegate</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>locationDelegate</em>
</code>
</td>
<td>
<div>
<p>The listener.</p>
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
<a name="/s:7heresdk18LocationEngineBaseP06removeB8Delegate08locationF0yAA0bF0_p_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeLocationDelegate(locationDelegate:)"></a>
<a class="token" href="#/s:7heresdk18LocationEngineBaseP06removeB8Delegate08locationF0yAA0bF0_p_tF">removeLocationDelegate(locationDelegate:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes a <code><a href="sdk-for-ios-navigate-api-reference-protocols-locationdelegate">LocationDelegate</a></code> from the engine.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">removeLocationDelegate</span><span class="p">(</span><span class="nv">locationDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-locationdelegate">LocationDelegate</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>locationDelegate</em>
</code>
</td>
<td>
<div>
<p>The listener.</p>
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
<a name="/s:7heresdk18LocationEngineBaseP03addB14StatusDelegate08locationfG0yAA0bfG0_p_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/addLocationStatusDelegate(locationStatusDelegate:)"></a>
<a class="token" href="#/s:7heresdk18LocationEngineBaseP03addB14StatusDelegate08locationfG0yAA0bfG0_p_tF">addLocationStatusDelegate(locationStatusDelegate:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Adds a <code><a href="sdk-for-ios-navigate-api-reference-protocols-locationstatusdelegate">LocationStatusDelegate</a></code> to the engine to get notified when there is an important
status change. Supports more than one delegate, instance is added only once.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">addLocationStatusDelegate</span><span class="p">(</span><span class="nv">locationStatusDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-locationstatusdelegate">LocationStatusDelegate</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>locationStatusDelegate</em>
</code>
</td>
<td>
<div>
<p>The listener.</p>
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
<a name="/s:7heresdk18LocationEngineBaseP06removeB14StatusDelegate08locationfG0yAA0bfG0_p_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeLocationStatusDelegate(locationStatusDelegate:)"></a>
<a class="token" href="#/s:7heresdk18LocationEngineBaseP06removeB14StatusDelegate08locationfG0yAA0bfG0_p_tF">removeLocationStatusDelegate(locationStatusDelegate:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes a <code><a href="sdk-for-ios-navigate-api-reference-protocols-locationstatusdelegate">LocationStatusDelegate</a></code> from the engine.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">removeLocationStatusDelegate</span><span class="p">(</span><span class="nv">locationStatusDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-locationstatusdelegate">LocationStatusDelegate</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>locationStatusDelegate</em>
</code>
</td>
<td>
<div>
<p>The listener.</p>
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
<a name="/s:7heresdk18LocationEngineBaseP013setBackgroundB7Allowed7allowedAA0bC6StatusOSb_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setBackgroundLocationAllowed(allowed:)"></a>
<a class="token" href="#/s:7heresdk18LocationEngineBaseP013setBackgroundB7Allowed7allowedAA0bC6StatusOSb_tF">setBackgroundLocationAllowed(allowed:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Enables or disables background location updates for an application.
Defaults to <code>false</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">setBackgroundLocationAllowed</span><span class="p">(</span><span class="nv">allowed</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-locationenginestatus">LocationEngineStatus</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>allowed</em>
</code>
</td>
<td>
<div>
<p>Set to <code>true</code> to allow background location updates, or <code>false</code> to disable them.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p><code><a href="../Enums/LocationEngineStatus.html#/s:7heresdk20LocationEngineStatusO2okyA2CmF">LocationEngineStatus.ok</a></code> if call succeeds. <code><a href="../Enums/LocationEngineStatus.html#/s:7heresdk20LocationEngineStatusO10notAllowedyA2CmF">LocationEngineStatus.notAllowed</a></code> if the application
does not have background location capabilities enabled.
<code><a href="../Enums/LocationEngineStatus.html#/s:7heresdk20LocationEngineStatusO12notSupportedyA2CmF">LocationEngineStatus.notSupported</a></code> on platforms which do not support controlling of background location modes.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18LocationEngineBaseP013getBackgroundB7AllowedSbyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getBackgroundLocationAllowed()"></a>
<a class="token" href="#/s:7heresdk18LocationEngineBaseP013getBackgroundB7AllowedSbyF">getBackgroundLocationAllowed()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Check if application’s background location updates are enabled. Returns <code>false</code> on platforms which do not
support controlling of background location modes using <code><a href="../Protocols/LocationEngineBase.html#/s:7heresdk18LocationEngineBaseP013setBackgroundB7Allowed7allowedAA0bC6StatusOSb_tF">setBackgroundLocationAllowed(...)</a></code> method.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">getBackgroundLocationAllowed</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p><code>True</code> if background location updates are allowed, <code>false</code> otherwise.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18LocationEngineBaseP013setBackgroundB16IndicatorVisible7visibleAA0bC6StatusOSb_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setBackgroundLocationIndicatorVisible(visible:)"></a>
<a class="token" href="#/s:7heresdk18LocationEngineBaseP013setBackgroundB16IndicatorVisible7visibleAA0bC6StatusOSb_tF">setBackgroundLocationIndicatorVisible(visible:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Controls visibility of application’s background location indicator. By default background location indicator
is visible, if application has background location capabilities.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">setBackgroundLocationIndicatorVisible</span><span class="p">(</span><span class="nv">visible</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-locationenginestatus">LocationEngineStatus</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>visible</em>
</code>
</td>
<td>
<div>
<p>Set to <code>true</code> to show background location indicator, or <code>false</code> to hide it.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p><code><a href="../Enums/LocationEngineStatus.html#/s:7heresdk20LocationEngineStatusO2okyA2CmF">LocationEngineStatus.ok</a></code> if call succeeds. <code><a href="../Enums/LocationEngineStatus.html#/s:7heresdk20LocationEngineStatusO10notAllowedyA2CmF">LocationEngineStatus.notAllowed</a></code> if the application
does not have background location capabilities enabled.
<code><a href="../Enums/LocationEngineStatus.html#/s:7heresdk20LocationEngineStatusO12notSupportedyA2CmF">LocationEngineStatus.notSupported</a></code> on platforms which do not support controlling of background location
indicator visibility.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18LocationEngineBaseP013getBackgroundB16IndicatorVisibleSbyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getBackgroundLocationIndicatorVisible()"></a>
<a class="token" href="#/s:7heresdk18LocationEngineBaseP013getBackgroundB16IndicatorVisibleSbyF">getBackgroundLocationIndicatorVisible()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Check if application’s background location indicator is visible. Returns <code>false</code> on platforms which do not
support controlling of background location indicator using <code><a href="../Protocols/LocationEngineBase.html#/s:7heresdk18LocationEngineBaseP013setBackgroundB16IndicatorVisible7visibleAA0bC6StatusOSb_tF">setBackgroundLocationIndicatorVisible(...)</a></code> method.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">getBackgroundLocationIndicatorVisible</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p><code>True</code> if background location indicator is visible, <code>false</code> otherwise.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18LocationEngineBaseP08setPauseB20UpdatesAutomatically7allowedAA0bC6StatusOSb_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setPauseLocationUpdatesAutomatically(allowed:)"></a>
<a class="token" href="#/s:7heresdk18LocationEngineBaseP08setPauseB20UpdatesAutomatically7allowedAA0bC6StatusOSb_tF">setPauseLocationUpdatesAutomatically(allowed:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Controls automatic pausing of location updates e.g. for improving device’s battery life at times when
location data is unlikely to change. By default automatic pausing of location updates is allowed.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">setPauseLocationUpdatesAutomatically</span><span class="p">(</span><span class="nv">allowed</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-locationenginestatus">LocationEngineStatus</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>allowed</em>
</code>
</td>
<td>
<div>
<p>Set to <code>true</code> to allow automatic pausing of location updates, or <code>false</code> to disable them.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p><code><a href="../Enums/LocationEngineStatus.html#/s:7heresdk20LocationEngineStatusO2okyA2CmF">LocationEngineStatus.ok</a></code> if call succeeds. <code><a href="../Enums/LocationEngineStatus.html#/s:7heresdk20LocationEngineStatusO12notSupportedyA2CmF">LocationEngineStatus.notSupported</a></code> on platforms
which do not support automatic pausing of location updates.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18LocationEngineBaseP08getPauseB20UpdatesAutomaticallySbyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getPauseLocationUpdatesAutomatically()"></a>
<a class="token" href="#/s:7heresdk18LocationEngineBaseP08getPauseB20UpdatesAutomaticallySbyF">getPauseLocationUpdatesAutomatically()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Check if automatic pausing of location updates are enabled. Returns <code>false</code> on platforms which do not
support controlling of automatic pausing of location updates using <code><a href="../Protocols/LocationEngineBase.html#/s:7heresdk18LocationEngineBaseP08setPauseB20UpdatesAutomatically7allowedAA0bC6StatusOSb_tF">setPauseLocationUpdatesAutomatically(...)</a></code>
method.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">getPauseLocationUpdatesAutomatically</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p><code>True</code> if automatic pausing of location updates is enabled, <code>false</code> otherwise.</p>
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
} </HTMLBlock>
