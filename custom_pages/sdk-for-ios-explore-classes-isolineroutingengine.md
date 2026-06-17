---
title: "IsolineRoutingEngine"
slug: "sdk-for-ios-explore-classes-isolineroutingengine"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/IsolineRoutingEngine"></a>
<a title="IsolineRoutingEngine Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-index">heresdk</a>

<a href="sdk-for-ios-explore-routing">Routing</a>

        IsolineRoutingEngine Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>IsolineRoutingEngine</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">IsolineRoutingEngine</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">IsolineRoutingEngine</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">IsolineRoutingEngine</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Use the IsolineRoutingEngine to calculate a reachable area from a center point.
The calculation is done asynchronously and requires an
online connection.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20IsolineRoutingEngineCACyKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init()"></a>
<a class="token" href="#/s:7heresdk20IsolineRoutingEngineCACyKcfc">init()</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">()</span> <span class="k">throws</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20IsolineRoutingEngineC18connectionSettingsAcA0c10ConnectionF0V_tKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(connectionSettings:)"></a>
<a class="token" href="#/s:7heresdk20IsolineRoutingEngineC18connectionSettingsAcA0c10ConnectionF0V_tKcfc">init(connectionSettings:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance of RoutingEngine.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Core.html#/s:7heresdk18InstantiationErrora">InstantiationError</a></code> Indicates what went wrong when the instantiation was attempted.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">connectionSettings</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-structs-routingconnectionsettings">RoutingConnectionSettings</a></span><span class="p">)</span> <span class="k">throws</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>connectionSettings</em>
</code>
</td>
<td>
<div>
<p>Settings for the route calculation.</p>
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
<a name="/s:7heresdk20IsolineRoutingEngineC_18connectionSettingsAcA09SDKNativeD0C_AA0c10ConnectionF0VtKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:connectionSettings:)"></a>
<a class="token" href="#/s:7heresdk20IsolineRoutingEngineC_18connectionSettingsAcA09SDKNativeD0C_AA0c10ConnectionF0VtKcfc">init(_:<wbr/>connectionSettings:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance of RoutingEngine.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Core.html#/s:7heresdk18InstantiationErrora">InstantiationError</a></code> Indicates what went wrong when the instantiation was attempted.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="n">_</span> <span class="nv">sdkEngine</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-classes-sdknativeengine">SDKNativeEngine</a></span><span class="p">,</span> <span class="nv">connectionSettings</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-structs-routingconnectionsettings">RoutingConnectionSettings</a></span><span class="p">)</span> <span class="k">throws</span></code></pre>
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
<p>An SDKEngine instance.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>connectionSettings</em>
</code>
</td>
<td>
<div>
<p>Settings for the route calculation.</p>
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
<a name="/s:7heresdk20IsolineRoutingEngineCyAcA09SDKNativeD0CKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:)"></a>
<a class="token" href="#/s:7heresdk20IsolineRoutingEngineCyAcA09SDKNativeD0CKcfc">init(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance of IsolineRoutingEngine.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Core.html#/s:7heresdk18InstantiationErrora">InstantiationError</a></code> Indicates what went wrong when the instantiation was attempted.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="n">_</span> <span class="nv">sdkEngine</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-classes-sdknativeengine">SDKNativeEngine</a></span><span class="p">)</span> <span class="k">throws</span></code></pre>
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
<p>An SDKEngine instance.</p>
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
<a name="/s:7heresdk20IsolineRoutingEngineC09calculateB06center14isolineOptions10completionAA10TaskHandle_pAA8WaypointV_AA0bH0VyAA0C5ErrorOSg_SayAA0B0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/calculateIsoline(center:isolineOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk20IsolineRoutingEngineC09calculateB06center14isolineOptions10completionAA10TaskHandle_pAA8WaypointV_AA0bH0VyAA0C5ErrorOSg_SayAA0B0CGSgtctF">calculateIsoline(center:<wbr/>isolineOptions:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously calculates isolines to indicate the reachable area from a center point.
This finds all destinations that can be reached in a specific amount of time,
a maximum travel distance, or even the charge level available in an electric vehicle.
The result is a polygon area where each point is reachable within the provided limit.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">calculateIsoline</span><span class="p">(</span><span class="nv">center</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-structs-waypoint">Waypoint</a></span><span class="p">,</span> <span class="nv">isolineOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-structs-isolineoptions">IsolineOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk33CalculateIsolineCompletionHandlera">CalculateIsolineCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>center</em>
</code>
</td>
<td>
<div>
<p>Center point from which isolines are calculated.
At minimum, the waypoint must contain the coordinates as point of origin.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>isolineOptions</em>
</code>
</td>
<td>
<div>
<p>Options for isoline calculation.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>completion</em>
</code>
</td>
<td>
<div>
<p>Callback object that will be invoked after isoline calculation.
It is always invoked on the main thread.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Handle that will be used to manipulate the execution of the task.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20IsolineRoutingEngineC15setCustomOption4name5valueAA0C5ErrorOSgSS_SSSgtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setCustomOption(name:value:)"></a>
<a class="token" href="#/s:7heresdk20IsolineRoutingEngineC15setCustomOption4name5valueAA0C5ErrorOSgSS_SSSgtF">setCustomOption(name:<wbr/>value:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets a custom option for routing backend queries.
The custom option is applied to all the queries that <code>IsolineRoutingEngine</code> performs.
For a complete list of available parameter names and their valid values, refer to
<a href="https://www.here.com/docs/bundle/batch-api-developer-guide/page/topics/constructing-request.html">HERE Routing API v8</a>.
<strong>Note:</strong> It’s easy to set a wrong option that makes queries invalid,
so make sure you read and understand the backend documentation.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">setCustomOption</span><span class="p">(</span><span class="nv">name</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">value</span><span class="p">:</span> <span class="kt">String</span><span class="p">?)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-enums-routingerror">RoutingError</a></span><span class="p">?</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>name</em>
</code>
</td>
<td>
<div>
<p>An option name. If the engine already has an option with the same name, the option will be overwritten. The option name must be a non-empty string.
The option name should’t duplicate option names that SDK creates by itself for usage in the query,
otherwise the query will callback with the error <code>RoutingError.INTERNAL_ERROR</code>.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>value</em>
</code>
</td>
<td>
<div>
<p>An option value. If the value is <code>nil</code>, the option will be removed. The option value must be a non-empty string.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>An optional error of setting the option. It’s <code>nil</code> if the option has been set successfully.
It’s <code>RoutingError.INVALID_PARAMETER</code> if the input name and/or value haven’t passed internal validation.</p>
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
