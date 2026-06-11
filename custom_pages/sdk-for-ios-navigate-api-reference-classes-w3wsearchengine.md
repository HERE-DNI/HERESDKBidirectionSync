---
title: "sdk-for-ios-navigate-api-reference-classes-w3wsearchengine"
slug: "sdk-for-ios-navigate-api-reference-classes-w3wsearchengine"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/W3WSearchEngine"></a>
<a title="W3WSearchEngine Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-search">Search</a>
<img alt="" id="carat" src="/carat.png"/>
        W3WSearchEngine Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>W3WSearchEngine</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">W3WSearchEngine</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">W3WSearchEngine</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">W3WSearchEngine</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>what3words is an alternative geocode system designed to identify any location on the planet.
The system divides the world into a grid of 57 trillion 3-by-3-metre squares, each of which
has a three-word address. For example, the front door of HERE’s Berlin office is identified by
“///wage.mere.heap”.
<code>W3WSearchEngine</code> allows you to convert 3 word addresses to coordinates and also coordinates
to 3 word addresses.</p>
<p><strong>Note:</strong> Using W3WSearchEngine requires a licence to access HERE what3words APIs.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15W3WSearchEngineCACyKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init()"></a>
<a class="token" href="#/s:7heresdk15W3WSearchEngineCACyKcfc">init()</a>
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
<a name="/s:7heresdk15W3WSearchEngineCyAcA09SDKNativeD0CKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:)"></a>
<a class="token" href="#/s:7heresdk15W3WSearchEngineCyAcA09SDKNativeD0CKcfc">init(_:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="n">_</span> <span class="nv">sdkEngine</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-sdknativeengine">SDKNativeEngine</a></span><span class="p">)</span> <span class="k">throws</span></code></pre>
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
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15W3WSearchEngineC6search5words10completionAA10TaskHandle_pSS_yAA0bC5ErrorOSg_AA0B7WSquareVSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/search(words:completion:)"></a>
<a class="token" href="#/s:7heresdk15W3WSearchEngineC6search5words10completionAA10TaskHandle_pSS_yAA0bC5ErrorOSg_AA0B7WSquareVSgtctF">search(words:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Performs an asynchronous request to search for a <code><a href="sdk-for-ios-navigate-api-reference-structs-w3wsquare">W3WSquare</a></code> that corresponds to
the given 3 words.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">search</span><span class="p">(</span><span class="nv">words</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Search.html#/s:7heresdk26W3WSearchCompletionHandlera">W3WSearchCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>words</em>
</code>
</td>
<td>
<div>
<p>A 3 word address as a string. It must be three words separated with dots or
a japanese middle dot character (・). Words separated by spaces will be rejected.
Optionally, the 3 word address can be prefixed with ///.</p>
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
<p>Callback which receives the result on the main thread.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Handle that can be used to manipulate the execution of the task.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15W3WSearchEngineC6search11coordinates8language10completionAA10TaskHandle_pAA14GeoCoordinatesV_SSSgyAA0bC5ErrorOSg_AA0B7WSquareVSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/search(coordinates:language:completion:)"></a>
<a class="token" href="#/s:7heresdk15W3WSearchEngineC6search11coordinates8language10completionAA10TaskHandle_pAA14GeoCoordinatesV_SSSgyAA0bC5ErrorOSg_AA0B7WSquareVSgtctF">search(coordinates:<wbr/>language:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Performs an asynchronous request to search for a <code><a href="sdk-for-ios-navigate-api-reference-structs-w3wsquare">W3WSquare</a></code>, which includes
the 3 word address, that corresponds to the given coordinates.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">search</span><span class="p">(</span><span class="nv">coordinates</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geocoordinates">GeoCoordinates</a></span><span class="p">,</span> <span class="nv">language</span><span class="p">:</span> <span class="kt">String</span><span class="p">?,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Search.html#/s:7heresdk26W3WSearchCompletionHandlera">W3WSearchCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>coordinates</em>
</code>
</td>
<td>
<div>
<p>The coordinates where to search.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>language</em>
</code>
</td>
<td>
<div>
<p>A supported 3 word address language as an ISO 639-1 2 letter code.
For Bosnian-Croatian-Montenegrin-Serbian use “oo”. Defaults to “en” (English).</p>
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
<p>Callback which receives the result on the main thread.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Handle that can be used to manipulate the execution of the task.</p>
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
