---
title: "Untitled"
slug: "sdk-for-ios-navigate-api-reference-classes-venueengine"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- VenueEngine.html -->
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/VenueEngine"></a>
<a title="VenueEngine Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-venues">Venues</a>
<img alt="" id="carat" src="../img/carat.png"/>
        VenueEngine Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>VenueEngine</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">VenueEngine</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">VenueEngine</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">VenueEngine</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>VenueEngine is an add-on to the base map functionality with its
own content loading and cache.
VenueEngine gives access to the venue functionality, which allows you
to load and visualize venues on the map, search content inside venues etc.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11VenueEngineC8callbackACyycSg_tKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(callback:)"></a>
<a class="token" href="#/s:7heresdk11VenueEngineC8callbackACyycSg_tKcfc">init(callback:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">callback</span><span class="p">:</span> <span class="kt"><a href="../Venues.html#/s:7heresdk32VenueEngineInitCompletionHandlera">VenueEngineInitCompletionHandler</a></span><span class="p">?)</span> <span class="k">throws</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>callback</em>
</code>
</td>
<td>
<div>
<p>The optional callback that will be triggered when a venue engine initialization
will be completed. After the initialization, the <code><a href="sdk-for-ios-navigate-api-reference-..-classes-venueservice">VenueService</a></code> should
be started using one of its methods or using <code>VenueEngine.start(String)</code>.</p>
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
<a name="/s:7heresdk11VenueEngineC_8callbackAcA09SDKNativeC0C_yycSgtKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:callback:)"></a>
<a class="token" href="#/s:7heresdk11VenueEngineC_8callbackAcA09SDKNativeC0C_yycSgtKcfc">init(_:<wbr/>callback:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="n">_</span> <span class="nv">sdkEngine</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-sdknativeengine">SDKNativeEngine</a></span><span class="p">,</span> <span class="nv">callback</span><span class="p">:</span> <span class="kt"><a href="../Venues.html#/s:7heresdk32VenueEngineInitCompletionHandlera">VenueEngineInitCompletionHandler</a></span><span class="p">?)</span> <span class="k">throws</span></code></pre>
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
<p>Instance of existing SDKEngine.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>callback</em>
</code>
</td>
<td>
<div>
<p>The optional callback that will be triggered when a venue engine initialization
will be completed. After the initialization, the <code><a href="sdk-for-ios-navigate-api-reference-..-classes-venueservice">VenueService</a></code> should
be started using one of its methods or using <code>VenueEngine.start(String)</code>.</p>
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
<a name="/s:7heresdk11VenueEngineC12venueServiceAA0bE0Cvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/venueService"></a>
<a class="token" href="#/s:7heresdk11VenueEngineC12venueServiceAA0bE0Cvp">venueService</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The venue service.
Gets the <code><a href="sdk-for-ios-navigate-api-reference-..-classes-venueservice">VenueService</a></code>. This service
can be used to load the <code><a href="sdk-for-ios-navigate-api-reference-..-classes-venuemodel">VenueModel</a></code> objects.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">venueService</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-venueservice">VenueService</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11VenueEngineC8venueMapAA0bE0Cvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/venueMap"></a>
<a class="token" href="#/s:7heresdk11VenueEngineC8venueMapAA0bE0Cvp">venueMap</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The venue map.
Gets a venue map to visualize venues and control the
state of the venues on the map. You need to start the <code><a href="sdk-for-ios-navigate-api-reference-..-classes-venueservice">VenueService</a></code> to
be able to load venues.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">venueMap</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-venuemap">VenueMap</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11VenueEngineC5start8callbackyyAA19AuthenticationErrorOSg_AA0F4DataVSgtcSg_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/start(callback:)"></a>
<a class="token" href="#/s:7heresdk11VenueEngineC5start8callbackyyAA19AuthenticationErrorOSg_AA0F4DataVSgtcSg_tF">start(callback:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Authenticates asynchronously using HERE SDK credentials and uses a result token to start
the <code><a href="sdk-for-ios-navigate-api-reference-..-classes-venueservice">VenueService</a></code>. An initialization status of the venue service is
returned to objects registered as <code><a href="sdk-for-ios-navigate-api-reference-..-protocols-venueservicedelegate">VenueServiceDelegate</a></code>. If the
authentication will fail, the venue service will not be started.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">start</span><span class="p">(</span><span class="nv">callback</span><span class="p">:</span> <span class="kt"><a href="../Core.html#/s:7heresdk31AuthenticationCompletionHandlera">AuthenticationCompletionHandler</a></span><span class="p">?)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>callback</em>
</code>
</td>
<td>
<div>
<p>The optional callback that will be triggered when the authentication will be completed.
If the authentication fails, the venue service will not be started.</p>
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
<a name="/s:7heresdk11VenueEngineC5start5tokenySS_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/start(token:)"></a>
<a class="token" href="#/s:7heresdk11VenueEngineC5start5tokenySS_tF">start(token:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Authenticates asynchronously using HERE SDK credentials using a token to start
the <code><a href="sdk-for-ios-navigate-api-reference-..-classes-venueservice">VenueService</a></code>. An initialization status of the venue service is
returned to objects registered as <code><a href="sdk-for-ios-navigate-api-reference-..-protocols-venueservicedelegate">VenueServiceDelegate</a></code>. If the
authentication will fail, the venue service will not be started.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">start</span><span class="p">(</span><span class="nv">token</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>token</em>
</code>
</td>
<td>
<div>
<p>SDK project scope token to be used for authentication</p>
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
<a name="/s:7heresdk11VenueEngineC7destroyyyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/destroy()"></a>
<a class="token" href="#/s:7heresdk11VenueEngineC7destroyyyF">destroy()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Releases all internally used resources. The instance can’t be used anymore after calling
this method.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">destroy</span><span class="p">()</span></code></pre>
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

</div>
`
}</HTMLBlock>
