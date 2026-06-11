---
title: "WarnerEngine"
slug: "sdk-for-ios-navigate-api-reference-classes-warnerengine"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/WarnerEngine"></a>
<a title="WarnerEngine Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-warnerengine">WarnerEngine</a>

        WarnerEngine Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>WarnerEngine</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">WarnerEngine</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-electronichorizondelegate">ElectronicHorizonDelegate</a></span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">WarnerEngine</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">WarnerEngine</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Provides the core functionality for generating and managing navigation warnings.</p>
<p><code>WarnerEngine</code> processes Electronic Horizon data and determines when various types
of warnings should be issued. It is used with <code><a href="sdk-for-ios-navigate-api-reference-protocols-electronichorizondelegate">ElectronicHorizonDelegate</a></code>,
which supply the road topology and positional updates required for warning evaluation.</p>
<p>The engine monitors enabled warning types and notifies registered listeners when new warnings become available.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12WarnerEngineC15enabledWarningsACSayAA11WarningTypeOG_tKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(enabledWarnings:)"></a>
<a class="token" href="#/s:7heresdk12WarnerEngineC15enabledWarningsACSayAA11WarningTypeOG_tKcfc">init(enabledWarnings:<wbr/>)</a>
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
<code><a href="../Core.html#/s:7heresdk18InstantiationErrora">InstantiationError</a></code> Indicates what went wrong when the instantiation was attempted.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">enabledWarnings</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-warningtype">WarningType</a></span><span class="p">])</span> <span class="k">throws</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>enabledWarnings</em>
</code>
</td>
<td>
<div>
<p>The list of warning types that should be monitored and processed
by the engine. Only warnings of these types will be generated.</p>
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
<a name="/s:7heresdk12WarnerEngineC03sdkC015enabledWarningsAcA09SDKNativeC0C_SayAA11WarningTypeOGtKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(sdkEngine:enabledWarnings:)"></a>
<a class="token" href="#/s:7heresdk12WarnerEngineC03sdkC015enabledWarningsAcA09SDKNativeC0C_SayAA11WarningTypeOGtKcfc">init(sdkEngine:<wbr/>enabledWarnings:<wbr/>)</a>
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
<code><a href="../Core.html#/s:7heresdk18InstantiationErrora">InstantiationError</a></code> Indicates what went wrong when the instantiation was attempted.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">sdkEngine</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-sdknativeengine">SDKNativeEngine</a></span><span class="p">,</span> <span class="nv">enabledWarnings</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-warningtype">WarningType</a></span><span class="p">])</span> <span class="k">throws</span></code></pre>
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
<p>A <code>SDKEngine</code> instance.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>enabledWarnings</em>
</code>
</td>
<td>
<div>
<p>The list of warning types that should be monitored and processed
by the engine. Only warnings of these types will be generated.</p>
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
<a name="/s:7heresdk12WarnerEngineC03sdkC09wallClock15enabledWarningsAcA09SDKNativeC0C_AA04WallF0_pSayAA11WarningTypeOGtKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(sdkEngine:wallClock:enabledWarnings:)"></a>
<a class="token" href="#/s:7heresdk12WarnerEngineC03sdkC09wallClock15enabledWarningsAcA09SDKNativeC0C_AA04WallF0_pSayAA11WarningTypeOGtKcfc">init(sdkEngine:<wbr/>wallClock:<wbr/>enabledWarnings:<wbr/>)</a>
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
<code><a href="../Core.html#/s:7heresdk18InstantiationErrora">InstantiationError</a></code> Indicates what went wrong when the instantiation was attempted.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">sdkEngine</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-sdknativeengine">SDKNativeEngine</a></span><span class="p">,</span> <span class="nv">wallClock</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-wallclock">WallClock</a></span><span class="p">,</span> <span class="nv">enabledWarnings</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-warningtype">WarningType</a></span><span class="p">])</span> <span class="k">throws</span></code></pre>
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
<p>A <code>SDKEngine</code> instance.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>wallClock</em>
</code>
</td>
<td>
<div>
<p>A <code><a href="sdk-for-ios-navigate-api-reference-protocols-wallclock">WallClock</a></code> instance.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>enabledWarnings</em>
</code>
</td>
<td>
<div>
<p>The list of warning types that should be monitored and processed
by the engine. Only warnings of these types will be generated.</p>
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
<a name="/s:7heresdk12WarnerEngineC14warningOptionsAA07WarningE0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/warningOptions"></a>
<a class="token" href="#/s:7heresdk12WarnerEngineC14warningOptionsAA07WarningE0Vvp">warningOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Options that define warning behavior for all the warners.
Provides configuration parameters for all the warners.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">warningOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-warningoptions">WarningOptions</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12WarnerEngineC13timingProfileAA06TimingE0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/timingProfile"></a>
<a class="token" href="#/s:7heresdk12WarnerEngineC13timingProfileAA06TimingE0Ovp">timingProfile</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The timing profile that defines when navigation warnings should be triggered.
Configures the base notification thresholds used for delivering
navigation warnings. The effective thresholds depend on the selected
<code><a href="sdk-for-ios-navigate-api-reference-enums-timingprofile">TimingProfile</a></code> and may adjust automatically according to
the current speed limit:</p>
<ul>
<li>For <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9fastSpeedyA2CmF">TimingProfile.fastSpeed</a></code>, thresholds apply when the current
speed limit is above 100 km/h (62 mph).</li>
<li>For <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO12regularSpeedyA2CmF">TimingProfile.regularSpeed</a></code>, thresholds apply when the current
speed limit is above 60 km/h (37 mph).</li>
<li>For <code><a href="../Enums/TimingProfile.html#/s:7heresdk13TimingProfileO9slowSpeedyA2CmF">TimingProfile.slowSpeed</a></code>, thresholds apply when the current
speed limit is 60 km/h (37 mph) or below.</li>
</ul>
<p><strong>Note:</strong> Custom threshold values can be set, but these timing-profile rules will still apply.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">timingProfile</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-timingprofile">TimingProfile</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12WarnerEngineC26onElectronicHorizonUpdated9errorCode6updateyAA0ef5ErrorI0OSg_AA0eF6UpdateVSgtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/onElectronicHorizonUpdated(errorCode:update:)"></a>
<a class="token" href="#/s:7heresdk12WarnerEngineC26onElectronicHorizonUpdated9errorCode6updateyAA0ef5ErrorI0OSg_AA0eF6UpdateVSgtF">onElectronicHorizonUpdated(errorCode:<wbr/>update:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Called whenever the electronic horizon subsystem produces:</p>
<ul>
<li>a new update,</li>
<li>an error,</li>
</ul>
<p>The client must inspect <code>error_code</code> to determine whether the call
represents an error or a valid update.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">onElectronicHorizonUpdated</span><span class="p">(</span><span class="nv">errorCode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-electronichorizonerrorcode">ElectronicHorizonErrorCode</a></span><span class="p">?,</span> <span class="nv">update</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-electronichorizonupdate">ElectronicHorizonUpdate</a></span><span class="p">?)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>errorCode</em>
</code>
</td>
<td>
<div>
<p>The error associated with the horizon computation.
<code>nil</code> means no error.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>update</em>
</code>
</td>
<td>
<div>
<p>The update describing the current electronic horizon state.
May be <code>nil</code> if an update could not be produced.</p>
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
<a name="/s:7heresdk12WarnerEngineC18addEnabledWarnings12warningTypesySayAA11WarningTypeOG_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/addEnabledWarnings(warningTypes:)"></a>
<a class="token" href="#/s:7heresdk12WarnerEngineC18addEnabledWarnings12warningTypesySayAA11WarningTypeOG_tF">addEnabledWarnings(warningTypes:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Adds the given warning types to the set of warnings monitored by the engine.</p>
<p>After this call, the engine will begin generating warnings for all
types included in <code>WarnerEngine.addEnabledWarnings(...).warningTypes</code>, in addition to those that are already enabled.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">addEnabledWarnings</span><span class="p">(</span><span class="nv">warningTypes</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-warningtype">WarningType</a></span><span class="p">])</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>warningTypes</em>
</code>
</td>
<td>
<div>
<p>Warning types to be added to the engine’s active monitoring set.</p>
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
<a name="/s:7heresdk12WarnerEngineC21removeEnabledWarnings12warningTypesySayAA11WarningTypeOG_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeEnabledWarnings(warningTypes:)"></a>
<a class="token" href="#/s:7heresdk12WarnerEngineC21removeEnabledWarnings12warningTypesySayAA11WarningTypeOG_tF">removeEnabledWarnings(warningTypes:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes the given warning types from the set of warnings monitored by the engine.</p>
<p>After this call, the engine will stop generating warnings for all
types included in <code>WarnerEngine.removeEnabledWarnings(...).warningTypes</code>, while other enabled types remain unaffected.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">removeEnabledWarnings</span><span class="p">(</span><span class="nv">warningTypes</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-warningtype">WarningType</a></span><span class="p">])</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>warningTypes</em>
</code>
</td>
<td>
<div>
<p>Warning types to be removed from the engine’s active monitoring set.</p>
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
<a name="/s:7heresdk12WarnerEngineC18setEnabledWarnings12warningTypesySayAA11WarningTypeOG_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setEnabledWarnings(warningTypes:)"></a>
<a class="token" href="#/s:7heresdk12WarnerEngineC18setEnabledWarnings12warningTypesySayAA11WarningTypeOG_tF">setEnabledWarnings(warningTypes:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Replaces the current set of enabled warning types with the provided list.</p>
<p>After this call, the engine will monitor and generate warnings
only for types included in <code>WarnerEngine.setEnabledWarnings(...).warningTypes</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">setEnabledWarnings</span><span class="p">(</span><span class="nv">warningTypes</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-warningtype">WarningType</a></span><span class="p">])</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>warningTypes</em>
</code>
</td>
<td>
<div>
<p>The complete new set of warning types the engine should track.</p>
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
<a name="/s:7heresdk12WarnerEngineC18getEnabledWarningsSayAA11WarningTypeOGyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getEnabledWarnings()"></a>
<a class="token" href="#/s:7heresdk12WarnerEngineC18getEnabledWarningsSayAA11WarningTypeOGyF">getEnabledWarnings()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Returns the current list of enabled warning types.
If the WarnerEngine was retrieved from the <code><a href="sdk-for-ios-navigate-api-reference-classes-navigator">Navigator</a></code>, it will also contain
all the warnings enabled for which listeners are set.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getEnabledWarnings</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-warningtype">WarningType</a></span><span class="p">]</span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>The currect list instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12WarnerEngineC18addWarningDelegateyyAA0eF0_pF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/addWarningDelegate(_:)"></a>
<a class="token" href="#/s:7heresdk12WarnerEngineC18addWarningDelegateyyAA0eF0_pF">addWarningDelegate(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Registers a listener that will receive warning notifications.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">addWarningDelegate</span><span class="p">(</span><span class="n">_</span> <span class="nv">warningListener</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-warningdelegate">WarningDelegate</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>warningListener</em>
</code>
</td>
<td>
<div>
<p>The listener instance that should be notified when new warnings are generated.</p>
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
<a name="/s:7heresdk12WarnerEngineC21removeWarningDelegateyyAA0eF0_pF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeWarningDelegate(_:)"></a>
<a class="token" href="#/s:7heresdk12WarnerEngineC21removeWarningDelegateyyAA0eF0_pF">removeWarningDelegate(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Unregisters a previously added warning listener.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">removeWarningDelegate</span><span class="p">(</span><span class="n">_</span> <span class="nv">warningListener</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-warningdelegate">WarningDelegate</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>warningListener</em>
</code>
</td>
<td>
<div>
<p>The listener instance that should no longer receive warning notifications.</p>
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
<a name="/s:7heresdk12WarnerEngineC19getWarningsRegistryAA0eF0CyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getWarningsRegistry()"></a>
<a class="token" href="#/s:7heresdk12WarnerEngineC19getWarningsRegistryAA0eF0CyF">getWarningsRegistry()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Returns the centralized access point for retrieving full metadata of any supported
warning category (e.g., safety cameras, truck restrictions, etc.).
<code><a href="sdk-for-ios-navigate-api-reference-classes-warningsregistry">WarningsRegistry</a></code> class exposes getter methods, each returning the detailed warning object for the given identifier.
Use this getter to look up complete warning information by its id, as provided through <code>WarningListener.onWarning</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getWarningsRegistry</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-warningsregistry">WarningsRegistry</a></span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>The centralized <code><a href="sdk-for-ios-navigate-api-reference-classes-warningsregistry">WarningsRegistry</a></code> instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12WarnerEngineC31getWarningNotificationDistances11warningTypeAA0efG0VAA0eI0O_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getWarningNotificationDistances(warningType:)"></a>
<a class="token" href="#/s:7heresdk12WarnerEngineC31getWarningNotificationDistances11warningTypeAA0efG0VAA0eI0O_tF">getWarningNotificationDistances(warningType:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Returns the warning notification distances for the requested warning type.</p>
<p><strong>Note</strong>: <code><a href="../Enums/WarningType.html#/s:7heresdk11WarningTypeO6customyA2CmF">WarningType.custom</a></code> is not a valid value for this method.
Use <code><a href="../Classes/WarnerEngine.html#/s:7heresdk12WarnerEngineC37getCustomWarningNotificationDistances06customF4TypeAA0fgH0Vs5Int32V_tF">WarnerEngine.getCustomWarningNotificationDistances(...)</a></code> to retrieve distances for a specific
custom warning type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getWarningNotificationDistances</span><span class="p">(</span><span class="nv">warningType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-warningtype">WarningType</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-warningnotificationdistances">WarningNotificationDistances</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>warningType</em>
</code>
</td>
<td>
<div>
<p>The warning type for which the notification distances will be returned.
Must not be <code><a href="../Enums/WarningType.html#/s:7heresdk11WarningTypeO6customyA2CmF">WarningType.custom</a></code>.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The warning notification distances for the given <code>WarnerEngine.getWarningNotificationDistances(...).warningType</code>.
If <code>WarnerEngine.getWarningNotificationDistances(...).warningType</code> is <code><a href="../Enums/WarningType.html#/s:7heresdk11WarningTypeO6customyA2CmF">WarningType.custom</a></code>, a default
<code><a href="sdk-for-ios-navigate-api-reference-structs-warningnotificationdistances">WarningNotificationDistances</a></code> value is returned.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12WarnerEngineC31setWarningNotificationDistances11warningType0hfG0SbAA0eI0O_AA0efG0VtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setWarningNotificationDistances(warningType:warningNotificationDistances:)"></a>
<a class="token" href="#/s:7heresdk12WarnerEngineC31setWarningNotificationDistances11warningType0hfG0SbAA0eI0O_AA0efG0VtF">setWarningNotificationDistances(warningType:<wbr/>warningNotificationDistances:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the warning notification distances for the specified warning type.</p>
<p><strong>Note</strong>: <code><a href="../Enums/WarningType.html#/s:7heresdk11WarningTypeO6customyA2CmF">WarningType.custom</a></code> is not a valid value for this method.
Use <code><a href="../Classes/WarnerEngine.html#/s:7heresdk12WarnerEngineC37setCustomWarningNotificationDistances06customF4Type07warninggH0Sbs5Int32V_AA0fgH0VtF">WarnerEngine.setCustomWarningNotificationDistances(...)</a></code> to configure distances for a specific
custom warning type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">setWarningNotificationDistances</span><span class="p">(</span><span class="nv">warningType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-warningtype">WarningType</a></span><span class="p">,</span> <span class="nv">warningNotificationDistances</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-warningnotificationdistances">WarningNotificationDistances</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>warningType</em>
</code>
</td>
<td>
<div>
<p>The warning type for which the warning notification distances will be set.
Must not be <code><a href="../Enums/WarningType.html#/s:7heresdk11WarningTypeO6customyA2CmF">WarningType.custom</a></code>.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>warningNotificationDistances</em>
</code>
</td>
<td>
<div>
<p>The warning notification distances to be set for the specified warning type.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>True if the distances were successfully set; false if <code>WarnerEngine.setWarningNotificationDistances(...).warningType</code> is
<code><a href="../Enums/WarningType.html#/s:7heresdk11WarningTypeO6customyA2CmF">WarningType.custom</a></code> or the options could not be applied.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12WarnerEngineC37getCustomWarningNotificationDistances06customF4TypeAA0fgH0Vs5Int32V_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getCustomWarningNotificationDistances(customWarningType:)"></a>
<a class="token" href="#/s:7heresdk12WarnerEngineC37getCustomWarningNotificationDistances06customF4TypeAA0fgH0Vs5Int32V_tF">getCustomWarningNotificationDistances(customWarningType:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Returns the warning notification distances for the specified custom warning type.</p>
<p>Unlike <code><a href="../Classes/WarnerEngine.html#/s:7heresdk12WarnerEngineC31getWarningNotificationDistances11warningTypeAA0efG0VAA0eI0O_tF">WarnerEngine.getWarningNotificationDistances(...)</a></code>, which operates on a <code><a href="sdk-for-ios-navigate-api-reference-enums-warningtype">WarningType</a></code>,
this method targets a specific custom warning category identified by <code>WarnerEngine.getCustomWarningNotificationDistances(...).customWarningType</code>,
as defined in <code><a href="../Structs/CustomWarning.html#/s:7heresdk13CustomWarningV06customC4Types5Int32Vvp">CustomWarning.customWarningType</a></code> and <code><a href="../Structs/Warning.html#/s:7heresdk7WarningV06customB4Types5Int32VSgvp">Warning.customWarningType</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getCustomWarningNotificationDistances</span><span class="p">(</span><span class="nv">customWarningType</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-warningnotificationdistances">WarningNotificationDistances</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>customWarningType</em>
</code>
</td>
<td>
<div>
<p>The identifier of the custom warning type for which the
notification distances are requested.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The warning notification distances configured for the given <code>WarnerEngine.getCustomWarningNotificationDistances(...).customWarningType</code>.
If no distances have been explicitly set for this type, a default
<code><a href="sdk-for-ios-navigate-api-reference-structs-warningnotificationdistances">WarningNotificationDistances</a></code> value is returned.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12WarnerEngineC37setCustomWarningNotificationDistances06customF4Type07warninggH0Sbs5Int32V_AA0fgH0VtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setCustomWarningNotificationDistances(customWarningType:warningNotificationDistances:)"></a>
<a class="token" href="#/s:7heresdk12WarnerEngineC37setCustomWarningNotificationDistances06customF4Type07warninggH0Sbs5Int32V_AA0fgH0VtF">setCustomWarningNotificationDistances(customWarningType:<wbr/>warningNotificationDistances:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the warning notification distances for the specified custom warning type.</p>
<p>Unlike <code><a href="../Classes/WarnerEngine.html#/s:7heresdk12WarnerEngineC31setWarningNotificationDistances11warningType0hfG0SbAA0eI0O_AA0efG0VtF">WarnerEngine.setWarningNotificationDistances(...)</a></code>, which applies settings to a <code><a href="sdk-for-ios-navigate-api-reference-enums-warningtype">WarningType</a></code>,
this method allows configuring notification distances independently for each custom warning
category identified by <code>WarnerEngine.setCustomWarningNotificationDistances(...).customWarningType</code>, as defined in
<code><a href="../Structs/CustomWarning.html#/s:7heresdk13CustomWarningV06customC4Types5Int32Vvp">CustomWarning.customWarningType</a></code> and <code><a href="../Structs/Warning.html#/s:7heresdk7WarningV06customB4Types5Int32VSgvp">Warning.customWarningType</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">setCustomWarningNotificationDistances</span><span class="p">(</span><span class="nv">customWarningType</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">,</span> <span class="nv">warningNotificationDistances</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-warningnotificationdistances">WarningNotificationDistances</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>customWarningType</em>
</code>
</td>
<td>
<div>
<p>The identifier of the custom warning type for which the
notification distances should be set.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>warningNotificationDistances</em>
</code>
</td>
<td>
<div>
<p>The warning notification distances to be applied
for the specified <code>WarnerEngine.setCustomWarningNotificationDistances(...).customWarningType</code>.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>True if the distances were successfully set; false otherwise.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12WarnerEngineC21finalizeGivenWarningsyyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/finalizeGivenWarnings()"></a>
<a class="token" href="#/s:7heresdk12WarnerEngineC21finalizeGivenWarningsyyF">finalizeGivenWarnings()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Marks all currently active warnings as passed (<code>DistanceType.PASSED</code>), notifies all
registered <code><a href="sdk-for-ios-navigate-api-reference-protocols-warningdelegate">WarningDelegate</a></code> instances on the main thread, and then clears these
warnings from their corresponding registries by invoking the appropriate<code>WarningsRegistry.clear&lt;Type&gt;</code> methods.</p>
<p>This method triggers notifications only for enabled warners. Warning processing may
occur asynchronously unless synchronous mode is enabled.</p>
<p><strong>Note</strong>: Although each warning type can also be cleared manually via the respective
<code>WarningsRegistry.clear&lt;Type&gt;()</code> methods, <code>finalizeGivenWarnings()</code> provides a
unified way to flush all active warnings after they have been reported as
passed. If this method is not invoked, warnings will continue to accumulate in the
registry according to the configured warning-generation options.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">finalizeGivenWarnings</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12WarnerEngineC24addCustomWarningProvider06customfG024segmentDataLoaderOptionsyAA0efG0_p_AA07SegmentjkL0VtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/addCustomWarningProvider(customWarningProvider:segmentDataLoaderOptions:)"></a>
<a class="token" href="#/s:7heresdk12WarnerEngineC24addCustomWarningProvider06customfG024segmentDataLoaderOptionsyAA0efG0_p_AA07SegmentjkL0VtF">addCustomWarningProvider(customWarningProvider:<wbr/>segmentDataLoaderOptions:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Registers a custom warning provider.</p>
<p>The registered provider participates in warning evaluation and is invoked
to generate custom warnings based on the current vehicle position.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">addCustomWarningProvider</span><span class="p">(</span><span class="nv">customWarningProvider</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-customwarningprovider">CustomWarningProvider</a></span><span class="p">,</span> <span class="nv">segmentDataLoaderOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-segmentdataloaderoptions">SegmentDataLoaderOptions</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>customWarningProvider</em>
</code>
</td>
<td>
<div>
<p>A provider responsible for generating custom warnings.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>segmentDataLoaderOptions</em>
</code>
</td>
<td>
<div>
<p>Specifies which data should be loaded by the <code><a href="sdk-for-ios-navigate-api-reference-classes-segmentdataloader">SegmentDataLoader</a></code>.</p>
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
<a name="/s:7heresdk12WarnerEngineC27removeCustomWarningProvider06customfG0yAA0efG0_p_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeCustomWarningProvider(customWarningProvider:)"></a>
<a class="token" href="#/s:7heresdk12WarnerEngineC27removeCustomWarningProvider06customfG0yAA0efG0_p_tF">removeCustomWarningProvider(customWarningProvider:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Unregisters a custom warning provider.</p>
<p>After removal, the provider will no longer participate in warning evaluation
and will not generate custom warnings.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">removeCustomWarningProvider</span><span class="p">(</span><span class="nv">customWarningProvider</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-customwarningprovider">CustomWarningProvider</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>customWarningProvider</em>
</code>
</td>
<td>
<div>
<p>The provider to be removed.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
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
<a name="/s:7heresdk12WarnerEngineC27clearCustomWarningProvidersyyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/clearCustomWarningProviders()"></a>
<a class="token" href="#/s:7heresdk12WarnerEngineC27clearCustomWarningProvidersyyF">clearCustomWarningProviders()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Unregisters all custom warning providers.</p>
<p>After this call, no custom warning providers will participate in warning
evaluation until new providers are registered.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">clearCustomWarningProviders</span><span class="p">()</span></code></pre>
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
