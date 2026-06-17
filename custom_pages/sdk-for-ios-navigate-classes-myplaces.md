---
title: "MyPlaces"
slug: "sdk-for-ios-navigate-classes-myplaces"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/MyPlaces"></a>
<a title="MyPlaces Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-index">heresdk</a>

<a href="sdk-for-ios-navigate-search">Search</a>

        MyPlaces Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>MyPlaces</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MyPlaces</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MyPlaces</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MyPlaces</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Provides means to populate personal places data source. Also acts as a
owner of the collection of personal places. MyPlaces is
memory-only object: nothing is persisted and/or sent over the network.
Client has full control on how to store personal places.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8MyPlacesCACycfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init()"></a>
<a class="token" href="#/s:7heresdk8MyPlacesCACycfc">init()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance of this class.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8MyPlacesC6placesSayAA8GeoPlaceVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/places"></a>
<a class="token" href="#/s:7heresdk8MyPlacesC6placesSayAA8GeoPlaceVGvp">places</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of places which currently belong to this data source. This list is
a clone of the internal list and thus changing it has no effect on the data source.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">places</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-structs-geoplace">GeoPlace</a></span><span class="p">]</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8MyPlacesC8addPlace5place8callbackAA10TaskHandle_pAA03GeoE0V_yAA0H7OutcomeOctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/addPlace(place:callback:)"></a>
<a class="token" href="#/s:7heresdk8MyPlacesC8addPlace5place8callbackAA10TaskHandle_pAA03GeoE0V_yAA0H7OutcomeOctF">addPlace(place:<wbr/>callback:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Adds a place to this data source.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">addPlace</span><span class="p">(</span><span class="nv">place</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-geoplace">GeoPlace</a></span><span class="p">,</span> <span class="nv">callback</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Core.html#/s:7heresdk21TaskCompletionHandlera">TaskCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>place</em>
</code>
</td>
<td>
<div>
<p>The place.</p>
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
<p>The callback to be called when task is completed.</p>
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
<a name="/s:7heresdk8MyPlacesC03addC06places8callbackAA10TaskHandle_pSayAA8GeoPlaceVG_yAA0G7OutcomeOctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/addPlaces(places:callback:)"></a>
<a class="token" href="#/s:7heresdk8MyPlacesC03addC06places8callbackAA10TaskHandle_pSayAA8GeoPlaceVG_yAA0G7OutcomeOctF">addPlaces(places:<wbr/>callback:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Adds a list of places to this data source.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">addPlaces</span><span class="p">(</span><span class="nv">places</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-structs-geoplace">GeoPlace</a></span><span class="p">],</span> <span class="nv">callback</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Core.html#/s:7heresdk21TaskCompletionHandlera">TaskCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>places</em>
</code>
</td>
<td>
<div>
<p>Places</p>
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
<p>The callback to be called when task is completed.</p>
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
<a name="/s:7heresdk8MyPlacesC11removePlace7placeId8callbackAA10TaskHandle_pSS_yAA0I7OutcomeOctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removePlace(placeId:callback:)"></a>
<a class="token" href="#/s:7heresdk8MyPlacesC11removePlace7placeId8callbackAA10TaskHandle_pSS_yAA0I7OutcomeOctF">removePlace(placeId:<wbr/>callback:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes a place from this data source.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">removePlace</span><span class="p">(</span><span class="nv">placeId</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">callback</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Core.html#/s:7heresdk21TaskCompletionHandlera">TaskCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>placeId</em>
</code>
</td>
<td>
<div>
<p>The place id</p>
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
<p>The callback to be called when task is completed.</p>
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
<a name="/s:7heresdk8MyPlacesC06removeC08placeIds8callbackAA10TaskHandle_pSaySSG_yAA0H7OutcomeOctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removePlaces(placeIds:callback:)"></a>
<a class="token" href="#/s:7heresdk8MyPlacesC06removeC08placeIds8callbackAA10TaskHandle_pSaySSG_yAA0H7OutcomeOctF">removePlaces(placeIds:<wbr/>callback:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes a list of places from this data source.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">removePlaces</span><span class="p">(</span><span class="nv">placeIds</span><span class="p">:</span> <span class="p">[</span><span class="kt">String</span><span class="p">],</span> <span class="nv">callback</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Core.html#/s:7heresdk21TaskCompletionHandlera">TaskCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>placeIds</em>
</code>
</td>
<td>
<div>
<p>Place ids</p>
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
<p>The callback to be called when task is completed.</p>
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
<a name="/s:7heresdk8MyPlacesC9removeAll8callbackAA10TaskHandle_pyAA0G7OutcomeOc_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeAll(callback:)"></a>
<a class="token" href="#/s:7heresdk8MyPlacesC9removeAll8callbackAA10TaskHandle_pyAA0G7OutcomeOc_tF">removeAll(callback:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes all places from this data source.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">removeAll</span><span class="p">(</span><span class="nv">callback</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Core.html#/s:7heresdk21TaskCompletionHandlera">TaskCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
<p>The callback to be called when task is completed.</p>
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
