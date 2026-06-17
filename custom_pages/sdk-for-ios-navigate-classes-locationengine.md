---
title: "LocationEngine"
slug: "sdk-for-ios-navigate-classes-locationengine"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/LocationEngine"></a>
<a title="LocationEngine Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-index">heresdk</a>

<a href="sdk-for-ios-navigate-positioning">Positioning</a>

        LocationEngine Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>LocationEngine</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">LocationEngine</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-locationenginebase">LocationEngineBase</a></span></code></pre>
</div>
</div>
<p>This class handles location updates received according to the desired LocationAccuracy.
Each instance of this class will be using internally the same client providing the actual
location updates. For that reason, only one LocationEngine can be started at a time.
Multiple delegates can be attached, either to receive location updates, see LocationUpdateDelegate,
or status updates, see LocationStatusDelegate. When a different LocationAccuracy is
desired, the LocationEngine needs to be stopped and started again.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
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
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">private(set)</span> <span class="k">var</span> <span class="nv">isStarted</span><span class="p">:</span> <span class="kt">Bool</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14LocationEngineCACyKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init()"></a>
<a class="token" href="#/s:7heresdk14LocationEngineCACyKcfc">init()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Undocumented</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="n">convenience</span> <span class="nf">init</span><span class="p">()</span> <span class="k">throws</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14LocationEngineC03sdkC0AcA09SDKNativeC0C_tKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(sdkEngine:)"></a>
<a class="token" href="#/s:7heresdk14LocationEngineC03sdkC0AcA09SDKNativeC0C_tKcfc">init(sdkEngine:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Undocumented</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">sdkEngine</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-classes-sdknativeengine">SDKNativeEngine</a></span><span class="p">)</span> <span class="k">throws</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14LocationEngineC5start16locationAccuracyAA0bC6StatusOAA0bF0O_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/start(locationAccuracy:)"></a>
<a class="token" href="#/s:7heresdk14LocationEngineC5start16locationAccuracyAA0bC6StatusOAA0bF0O_tF">start(locationAccuracy:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Starts the location engine with desired LocationAccuracy.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">start</span><span class="p">(</span><span class="nv">locationAccuracy</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-enums-locationaccuracy">LocationAccuracy</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-enums-locationenginestatus">LocationEngineStatus</a></span></code></pre>
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
<p>Determines desired location accuracy.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Location engine status.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14LocationEngineC5start15locationOptionsAA0bC6StatusOAA0bF0V_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/start(locationOptions:)"></a>
<a class="token" href="#/s:7heresdk14LocationEngineC5start15locationOptionsAA0bC6StatusOAA0bF0V_tF">start(locationOptions:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Starts the location engine with desired LocationOptions.
This method variant is not currently supported on iOS platforms.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">start</span><span class="p">(</span><span class="nv">locationOptions</span><span class="p">:</span> <span class="kt">LocationOptions</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-enums-locationenginestatus">LocationEngineStatus</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>locationOptions</em>
</code>
</td>
<td>
<div>
<p>Determines desired location options.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>LocationEngineStatus.notSupported.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14LocationEngineC06updateB8Accuracy08locationE0AA0bC6StatusOAA0bE0O_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/updateLocationAccuracy(locationAccuracy:)"></a>
<a class="token" href="#/s:7heresdk14LocationEngineC06updateB8Accuracy08locationE0AA0bC6StatusOAA0bE0O_tF">updateLocationAccuracy(locationAccuracy:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Reconfigures the location engine with desired LocationAccuracy. This method is a faster way to change location accuracy for already started
location engine, than calling <code><a href="../Classes/LocationEngine.html#/s:7heresdk14LocationEngineC4stopyyF">stop(...)</a></code> and <code>start(LocationOptions)</code> in sequence. Returns <code><a href="../Enums/LocationEngineStatus.html#/s:7heresdk20LocationEngineStatusO8notReadyyA2CmF">LocationEngineStatus.notReady</a></code>,
if called for unstarted location engine.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">updateLocationAccuracy</span><span class="p">(</span><span class="nv">locationAccuracy</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-enums-locationaccuracy">LocationAccuracy</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-enums-locationenginestatus">LocationEngineStatus</a></span></code></pre>
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
<p>Engine status. Valid values are defined in <code><a href="sdk-for-ios-navigate-enums-locationenginestatus">LocationEngineStatus</a></code></p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14LocationEngineC06updateB7Options08locationE0AA0bC6StatusOAA0bE0V_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/updateLocationOptions(locationOptions:)"></a>
<a class="token" href="#/s:7heresdk14LocationEngineC06updateB7Options08locationE0AA0bC6StatusOAA0bE0V_tF">updateLocationOptions(locationOptions:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Reconfigures the location engine with desired LocationOptions. This method is a faster way to change location options for already started
location engine, than calling <code><a href="../Classes/LocationEngine.html#/s:7heresdk14LocationEngineC4stopyyF">stop(...)</a></code> and <code>start(LocationOptions)</code> in sequence. Returns <code><a href="../Enums/LocationEngineStatus.html#/s:7heresdk20LocationEngineStatusO8notReadyyA2CmF">LocationEngineStatus.notReady</a></code>,
if called for unstarted location engine.
This method variant is not currently supported on iOS platforms. Returns <code><a href="../Enums/LocationEngineStatus.html#/s:7heresdk20LocationEngineStatusO12notSupportedyA2CmF">LocationEngineStatus.notSupported</a></code> on platforms which this method variant is not supported.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">updateLocationOptions</span><span class="p">(</span><span class="nv">locationOptions</span><span class="p">:</span> <span class="kt">LocationOptions</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-enums-locationenginestatus">LocationEngineStatus</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>locationOptions</em>
</code>
</td>
<td>
<div>
<p>Desired location options.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Engine status. Valid values are defined in <code><a href="sdk-for-ios-navigate-enums-locationenginestatus">LocationEngineStatus</a></code></p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14LocationEngineC09lastKnownB0AA0B0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/lastKnownLocation"></a>
<a class="token" href="#/s:7heresdk14LocationEngineC09lastKnownB0AA0B0VSgvp">lastKnownLocation</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Returns the last known location obtained by the engine.
Location is returned synchronously. Location object has
timestamp attribute, which reflects when data was obtained. If location
was never obtained - nil is returned.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">lastKnownLocation</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-location">Location</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14LocationEngineC4stopyyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/stop()"></a>
<a class="token" href="#/s:7heresdk14LocationEngineC4stopyyF">stop()</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">stop</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14LocationEngineC33confirmHEREPrivacyNoticeInclusionAA18ConfirmationStatusOyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/confirmHEREPrivacyNoticeInclusion()"></a>
<a class="token" href="#/s:7heresdk14LocationEngineC33confirmHEREPrivacyNoticeInclusionAA18ConfirmationStatusOyF">confirmHEREPrivacyNoticeInclusion()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This method does nothing on iOS platforms. Returns <code><a href="../Enums/ConfirmationStatus.html#/s:7heresdk18ConfirmationStatusO2okyA2CmF">ConfirmationStatus.ok</a></code> on this platform.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">confirmHEREPrivacyNoticeInclusion</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-enums-confirmationstatus">ConfirmationStatus</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14LocationEngineC33confirmHEREPrivacyNoticeExceptionAA18ConfirmationStatusOyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/confirmHEREPrivacyNoticeException()"></a>
<a class="token" href="#/s:7heresdk14LocationEngineC33confirmHEREPrivacyNoticeExceptionAA18ConfirmationStatusOyF">confirmHEREPrivacyNoticeException()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This method does nothing on iOS platforms. Returns <code><a href="../Enums/ConfirmationStatus.html#/s:7heresdk18ConfirmationStatusO2okyA2CmF">ConfirmationStatus.ok</a></code> on this platform.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">confirmHEREPrivacyNoticeException</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-enums-confirmationstatus">ConfirmationStatus</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14LocationEngineC03addB8Delegate08locationE0yAA0bE0_p_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/addLocationDelegate(locationDelegate:)"></a>
<a class="token" href="#/s:7heresdk14LocationEngineC03addB8Delegate08locationE0yAA0bE0_p_tF">addLocationDelegate(locationDelegate:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Adds a LocationDelegate to the engine to get notified when there is a new location
update available. Supports more than one delegate, instance is added only once.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">addLocationDelegate</span><span class="p">(</span><span class="nv">locationDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-locationdelegate">LocationDelegate</a></span><span class="p">)</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14LocationEngineC06removeB8Delegate08locationE0yAA0bE0_p_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeLocationDelegate(locationDelegate:)"></a>
<a class="token" href="#/s:7heresdk14LocationEngineC06removeB8Delegate08locationE0yAA0bE0_p_tF">removeLocationDelegate(locationDelegate:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes a LocationDelegate from the engine.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">removeLocationDelegate</span><span class="p">(</span><span class="nv">locationDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-locationdelegate">LocationDelegate</a></span><span class="p">)</span></code></pre>
</div>
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
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">addLocationStatusDelegate</span><span class="p">(</span><span class="nv">locationStatusDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-locationstatusdelegate">LocationStatusDelegate</a></span><span class="p">)</span></code></pre>
</div>
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
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">removeLocationStatusDelegate</span><span class="p">(</span><span class="nv">locationStatusDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-locationstatusdelegate">LocationStatusDelegate</a></span><span class="p">)</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14LocationEngineC013setBackgroundB7Allowed7allowedAA0bC6StatusOSb_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setBackgroundLocationAllowed(allowed:)"></a>
<a class="token" href="#/s:7heresdk14LocationEngineC013setBackgroundB7Allowed7allowedAA0bC6StatusOSb_tF">setBackgroundLocationAllowed(allowed:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Enables or disables application’s background location updates. By default background location updates
are enabled if application has background location capabilities.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">setBackgroundLocationAllowed</span><span class="p">(</span><span class="nv">allowed</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-enums-locationenginestatus">LocationEngineStatus</a></span></code></pre>
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
<p>Set to true to allow background location updates, or false to disable them.</p>
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
<a name="/s:7heresdk14LocationEngineC013getBackgroundB7AllowedSbyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getBackgroundLocationAllowed()"></a>
<a class="token" href="#/s:7heresdk14LocationEngineC013getBackgroundB7AllowedSbyF">getBackgroundLocationAllowed()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Check if application’s background location updates are enabled. Returns false on platforms which do not
support controlling of background location modes using <code><a href="../Protocols/LocationEngineBase.html#/s:7heresdk18LocationEngineBaseP013setBackgroundB7Allowed7allowedAA0bC6StatusOSb_tF">LocationEngineBase.setBackgroundLocationAllowed(...)</a></code> method.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getBackgroundLocationAllowed</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>True if background location updates are allowed, false otherwise.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14LocationEngineC013setBackgroundB16IndicatorVisible7visibleAA0bC6StatusOSb_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setBackgroundLocationIndicatorVisible(visible:)"></a>
<a class="token" href="#/s:7heresdk14LocationEngineC013setBackgroundB16IndicatorVisible7visibleAA0bC6StatusOSb_tF">setBackgroundLocationIndicatorVisible(visible:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">setBackgroundLocationIndicatorVisible</span><span class="p">(</span><span class="nv">visible</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-enums-locationenginestatus">LocationEngineStatus</a></span></code></pre>
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
<p>Set to true to show background location indicator, or false to hide it.</p>
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
<a name="/s:7heresdk14LocationEngineC013getBackgroundB16IndicatorVisibleSbyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getBackgroundLocationIndicatorVisible()"></a>
<a class="token" href="#/s:7heresdk14LocationEngineC013getBackgroundB16IndicatorVisibleSbyF">getBackgroundLocationIndicatorVisible()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Check if application’s background location indicator is visible. Returns false on platforms which do not
support controlling of background location indicator using <code><a href="../Protocols/LocationEngineBase.html#/s:7heresdk18LocationEngineBaseP013setBackgroundB16IndicatorVisible7visibleAA0bC6StatusOSb_tF">LocationEngineBase.setBackgroundLocationIndicatorVisible(...)</a></code> method.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getBackgroundLocationIndicatorVisible</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>True if background location indicator is visible, false otherwise.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14LocationEngineC08setPauseB20UpdatesAutomatically7allowedAA0bC6StatusOSb_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setPauseLocationUpdatesAutomatically(allowed:)"></a>
<a class="token" href="#/s:7heresdk14LocationEngineC08setPauseB20UpdatesAutomatically7allowedAA0bC6StatusOSb_tF">setPauseLocationUpdatesAutomatically(allowed:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">setPauseLocationUpdatesAutomatically</span><span class="p">(</span><span class="nv">allowed</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-enums-locationenginestatus">LocationEngineStatus</a></span></code></pre>
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
<p>Set to true to allow automatic pausing of location updates, or false to disable them.</p>
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
<a name="/s:7heresdk14LocationEngineC08getPauseB20UpdatesAutomaticallySbyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getPauseLocationUpdatesAutomatically()"></a>
<a class="token" href="#/s:7heresdk14LocationEngineC08getPauseB20UpdatesAutomaticallySbyF">getPauseLocationUpdatesAutomatically()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Check if automatic pausing of location updates are enabled. Returns false on platforms which do not
support controlling of automatic pausing of location updates using <code><a href="../Protocols/LocationEngineBase.html#/s:7heresdk18LocationEngineBaseP08setPauseB20UpdatesAutomatically7allowedAA0bC6StatusOSb_tF">LocationEngineBase.setPauseLocationUpdatesAutomatically(...)</a></code>
method.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getPauseLocationUpdatesAutomatically</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>True if automatic pausing of location updates is enabled, false otherwise.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14LocationEngineC36setCallListenerFromMainThreadEnabled7enabledySb_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setCallListenerFromMainThreadEnabled(enabled:)"></a>
<a class="token" href="#/s:7heresdk14LocationEngineC36setCallListenerFromMainThreadEnabled7enabledySb_tF">setCallListenerFromMainThreadEnabled(enabled:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Enables or disables forcing listener calls to originate from main thread.
When disabled listener calls can originate from any thread.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">setCallListenerFromMainThreadEnabled</span><span class="p">(</span><span class="nv">enabled</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>enabled</em>
</code>
</td>
<td>
<div>
<p>Set to true to force listener calls to be called from main thread.</p>
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
<a name="/s:7heresdk16LocationDelegateP02onB7UpdatedyyAA0B0VF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/onLocationUpdated(_:)"></a>
<a class="token" href="#/s:7heresdk16LocationDelegateP02onB7UpdatedyyAA0B0VF">onLocationUpdated(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">onLocationUpdated</span><span class="p">(</span><span class="n">_</span> <span class="nv">position</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-location">Location</a></span><span class="p">)</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22LocationStatusDelegateP02onC7Changed014locationEngineC0yAA0bhC0O_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/onStatusChanged(locationEngineStatus:)"></a>
<a class="token" href="#/s:7heresdk22LocationStatusDelegateP02onC7Changed014locationEngineC0yAA0bhC0O_tF">onStatusChanged(locationEngineStatus:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">onStatusChanged</span><span class="p">(</span><span class="nv">locationEngineStatus</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-enums-locationenginestatus">LocationEngineStatus</a></span><span class="p">)</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22LocationStatusDelegateP22onFeaturesNotAvailable8featuresySayAA0B7FeatureOG_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/onFeaturesNotAvailable(features:)"></a>
<a class="token" href="#/s:7heresdk22LocationStatusDelegateP22onFeaturesNotAvailable8featuresySayAA0B7FeatureOG_tF">onFeaturesNotAvailable(features:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">onFeaturesNotAvailable</span><span class="p">(</span><span class="nv">features</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-enums-locationfeature">LocationFeature</a></span><span class="p">])</span></code></pre>
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
} </HTMLBlock>
