---
title: "MapContext Class Reference"
slug: "sdk-for-ios-explore-api-reference-classes-mapcontext"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- MapContext.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Class/MapContext"></a>
<a title="MapContext Class Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="sdk-for-ios-explore-api-reference-..-index">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-maps">Maps</a>
<img alt="" id="carat" src="../img/carat.png"/>
        MapContext Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public class MapContext</code></pre>
<pre><code>extension MapContext: NativeBase</code></pre>
<pre><code>extension MapContext: Hashable</code></pre>
</div>
</div>
<p>MapContext is the rendering engine and the context in which virtual geographic maps get rendered.</p>
<p>It runs the render loop or offers the means for the user to run a custom one.</p>
<p>Data sources, assets and virtual maps can be attached to the context. A virtual map can only
render data from sources attached to the same context.</p>
<p>The graphics backend to be used by the engine can be choosen by the user or a platform suitable
one can be automatically selected internally. Only one graphics backend can be active and once
selected it cannot be changed.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10MapContextC43SetMemoryManagementOptionsCompletionHandlera"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/SetMemoryManagementOptionsCompletionHandler"></a>
<a class="token" href="#/s:7heresdk10MapContextC43SetMemoryManagementOptionsCompletionHandlera">SetMemoryManagementOptionsCompletionHandler</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Completion handler for the memory management result.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public typealias SetMemoryManagementOptionsCompletionHandler = (_ result: MapContext.MemoryManagementResult) -&gt; Void</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>result</em>
</code>
</td>
<td>
<div>
<p>The memory management result.</p>
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
<a name="/s:7heresdk10MapContextC24MemoryManagementStrategyO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/MemoryManagementStrategy"></a>
<a class="token" href="#/s:7heresdk10MapContextC24MemoryManagementStrategyO">MemoryManagementStrategy</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The memory management strategy.
Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-..-classes-mapcontext-memorymanagementstrategy">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum MemoryManagementStrategy : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10MapContextC26MemoryManagementResultCodeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/MemoryManagementResultCode"></a>
<a class="token" href="#/s:7heresdk10MapContextC26MemoryManagementResultCodeO">MemoryManagementResultCode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The memory management result code.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-..-classes-mapcontext-memorymanagementresultcode">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum MemoryManagementResultCode : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10MapContextC12ResourceTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/ResourceType"></a>
<a class="token" href="#/s:7heresdk10MapContextC12ResourceTypeO">ResourceType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Types of system resources used by <code><a href="sdk-for-ios-explore-api-reference-..-classes-mapcontext">MapContext</a></code> or any of the entities attached to it, like <code><a href="sdk-for-ios-explore-api-reference-..-classes-heremap">HereMap</a></code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-..-classes-mapcontext-resourcetype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum ResourceType : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10MapContextC20FreeResourceSeverityO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/FreeResourceSeverity"></a>
<a class="token" href="#/s:7heresdk10MapContextC20FreeResourceSeverityO">FreeResourceSeverity</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The severity of a free resource request.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-..-classes-mapcontext-freeresourceseverity">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum FreeResourceSeverity : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10MapContextC22MemoryManagementResultV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/MemoryManagementResult"></a>
<a class="token" href="#/s:7heresdk10MapContextC22MemoryManagementResultV">MemoryManagementResult</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Memory management result.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-..-classes-mapcontext-memorymanagementresult">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct MemoryManagementResult</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10MapContextC23MemoryManagementOptionsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/MemoryManagementOptions"></a>
<a class="token" href="#/s:7heresdk10MapContextC23MemoryManagementOptionsV">MemoryManagementOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Memory management options.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-..-classes-mapcontext-memorymanagementoptions">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct MemoryManagementOptions</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10MapContextC12freeResource4type8severityyAC0E4TypeO_AC04FreeE8SeverityOtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/freeResource(type:severity:)"></a>
<a class="token" href="#/s:7heresdk10MapContextC12freeResource4type8severityyAC0E4TypeO_AC04FreeE8SeverityOtF">freeResource(type:<wbr/>severity:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Frees a system resource held by the <code>MapContext</code> and all entities attached to it, like <code><a href="sdk-for-ios-explore-api-reference-..-classes-heremap">HereMap</a></code>.
This function is intended for use when a system resource availability becomes low.
For example, some memory can be freed when the application transitions to the background state.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func freeResource(type: MapContext.ResourceType, severity: MapContext.FreeResourceSeverity)</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>type</em>
</code>
</td>
<td>
<div>
<p>Type of resource to be freed.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>severity</em>
</code>
</td>
<td>
<div>
<p>Severity of the request.</p>
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
<a name="/s:7heresdk10MapContextC26getMemoryManagementOptionsAC0efG0VyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getMemoryManagementOptions()"></a>
<a class="token" href="#/s:7heresdk10MapContextC26getMemoryManagementOptionsAC0efG0VyF">getMemoryManagementOptions()</a>
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
<pre><code>public func getMemoryManagementOptions() -&gt; MapContext.MemoryManagementOptions</code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>Gets the current memory management options.
Returns the actual applied memory limits. If the underlying system limits exceed
int32_t max value (2,147,483,647 KiB or ~2 TiB), the returned value is clamped to int32_t max.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10MapContextC26setMemoryManagementOptions_10completionyAC0efG0V_yAC0eF6ResultVcSgtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setMemoryManagementOptions(_:completion:)"></a>
<a class="token" href="#/s:7heresdk10MapContextC26setMemoryManagementOptions_10completionyAC0efG0V_yAC0eF6ResultVcSgtF">setMemoryManagementOptions(_:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets memory management options for controlling tile cache and video memory usage.
In <code><a href="sdk-for-ios-explore-api-reference-..-classes-mapcontext-memorymanagementoptions">MapContext.MemoryManagementOptions</a></code> optional parameters with <code>nil</code>
or non positive values will be ignored, preserving their existing settings.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func setMemoryManagementOptions(_ memoryManagementOptions: MapContext.MemoryManagementOptions, completion: MapContext.SetMemoryManagementOptionsCompletionHandler?)</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>memoryManagementOptions</em>
</code>
</td>
<td>
<div>
<p>The memory management options to set.</p>
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
<p>Optional handler used upon
completion to pass the return value to the caller.</p>
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



</div>
`
}</HTMLBlock>
