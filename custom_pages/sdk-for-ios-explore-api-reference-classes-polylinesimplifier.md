---
title: "Untitled"
slug: "sdk-for-ios-explore-api-reference-classes-polylinesimplifier"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- PolylineSimplifier.html -->
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/PolylineSimplifier"></a>
<a title="PolylineSimplifier Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-core">Core</a>
<img alt="" id="carat" src="../img/carat.png"/>
        PolylineSimplifier Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>PolylineSimplifier</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">PolylineSimplifier</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">PolylineSimplifier</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">PolylineSimplifier</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>PolylineSimplifier helps to reduce the number of points
in the polyline by removing redundant elements using
Douglas–Peucker algorithm, so that result stays
within <code><a href="sdk-for-ios-explore-api-reference-..-classes-polylinesimplifier-options">PolylineSimplifier.Options</a></code>.</p>
<p>Typical use case is to perform input preparation step
before invoking computationally heavy API. Such API
have an upper limit on the input collection size
and is subject to reduced performance when collection
is huge. Examples of such API are:</p>
<ul>
<li><code><a href="sdk-for-ios-explore-api-reference-..-classes-trafficengine">TrafficEngine</a></code> methods which accept a <code><a href="sdk-for-ios-explore-api-reference-..-structs-geocorridor">GeoCorridor</a></code>;</li>
<li><code>RoutePrefetcher.prefetchGeoCorridor</code>.</li>
</ul>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18PolylineSimplifierCACyKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init()"></a>
<a class="token" href="#/s:7heresdk18PolylineSimplifierCACyKcfc">init()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance of <code>PolylineSimplifier</code>.</p>
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
<a name="/s:7heresdk18PolylineSimplifierC7OptionsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/Options"></a>
<a class="token" href="#/s:7heresdk18PolylineSimplifierC7OptionsV">Options</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Controls the strategy of <code><a href="../Classes/PolylineSimplifier.html#/s:7heresdk18PolylineSimplifierC8simplify8polyline24simplificationParameters10completionAA10TaskHandle_pSayAA14GeoCoordinatesVG_AC7OptionsVyAA0B19SimplificationErrorOSg_AKSgtctF">PolylineSimplifier.simplify(...)</a></code>
when reducing a size of polyline.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-..-classes-polylinesimplifier-options">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">Options</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18PolylineSimplifierC8simplify8polyline24simplificationParameters10completionAA10TaskHandle_pSayAA14GeoCoordinatesVG_AC7OptionsVyAA0B19SimplificationErrorOSg_AKSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/simplify(polyline:simplificationParameters:completion:)"></a>
<a class="token" href="#/s:7heresdk18PolylineSimplifierC8simplify8polyline24simplificationParameters10completionAA10TaskHandle_pSayAA14GeoCoordinatesVG_AC7OptionsVyAA0B19SimplificationErrorOSg_AKSgtctF">simplify(polyline:<wbr/>simplificationParameters:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Reduces the number of points in the input polyline.
Does this by removing points which are not significant
according to the passed <code><a href="sdk-for-ios-explore-api-reference-..-classes-polylinesimplifier-options">PolylineSimplifier.Options</a></code>.
Simplification process is performed on the device without
connecting to the network and is computationally intensive.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">simplify</span><span class="p">(</span><span class="nv">polyline</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-geocoordinates">GeoCoordinates</a></span><span class="p">],</span> <span class="nv">simplificationParameters</span><span class="p">:</span> <span class="kt">PolylineSimplifier</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-polylinesimplifier-options">Options</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Core.html#/s:7heresdk39PolylineSimplificationCompletionHandlera">PolylineSimplificationCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>polyline</em>
</code>
</td>
<td>
<div>
<p>Input polyline that should be reduced in size.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>simplificationParameters</em>
</code>
</td>
<td>
<div>
<p>Strategy, that controls the behavior of the underlying algorithm.</p>
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
<p>Callback, which will be invoked on the main thread,
when operation is finished.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Controls an asynchronous operation.</p>
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

</div>
`
}</HTMLBlock>
