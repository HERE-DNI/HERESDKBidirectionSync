---
title: "HereMap"
slug: "sdk-for-ios-navigate-api-reference-classes-heremap"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/HereMap"></a>
<a title="HereMap Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-maps">Maps</a>

        HereMap Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>HereMap</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">HereMap</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">HereMap</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">HereMap</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>The representation of a dynamic and interactive geographic map.
The map manages a collection of layers of objects and spaces, presents them in a stacked layout and offers the means to focus on a certain area.
The layers, their relation to the objects and spaces, the layout and the representation style is described through a configuration.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7HereMapC5styleAA5StyleCvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/style"></a>
<a class="token" href="#/s:7heresdk7HereMapC5styleAA5StyleCvp">style</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The style that the map uses to customize the visual appearance of rendered features.
Changes made to the map style using <code><a href="../Classes/Style.html#/s:7heresdk5StyleC6updateyyACF">Style.update(...)</a></code> are lost when new scene is loaded using
<code>MapScene.loadScene(MapScheme, MapScene.LoadSceneCompletionHandler?)</code> and its variants as well as
when map features are enabled or disabled using <code><a href="../Classes/MapScene.html#/s:7heresdk8MapSceneC14enableFeaturesyySDyS2SGF">MapScene.enableFeatures(...)</a></code> and <code><a href="../Classes/MapScene.html#/s:7heresdk8MapSceneC15disableFeaturesyySaySSGF">MapScene.disableFeatures(...)</a></code>.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">style</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-style">Style</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7HereMapC03addC12IdleDelegateyyAA0ceF0_pF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/addMapIdleDelegate(_:)"></a>
<a class="token" href="#/s:7heresdk7HereMapC03addC12IdleDelegateyyAA0ceF0_pF">addMapIdleDelegate(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Adds a delegate for receiving idle state
notifications and notifies it of the current state.</p>
<p>The first notification received is always the state at the time of registration.</p>
<p>The new delegate is appended to the set
of <code>HereMap</code> idle delegates as a strong reference.
The caller is responsible for releasing the strong reference by calling
<code><a href="../Classes/HereMap.html#/s:7heresdk7HereMapC06removeC12IdleDelegateyyAA0ceF0_pF">HereMap.removeMapIdleDelegate(...)</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">addMapIdleDelegate</span><span class="p">(</span><span class="n">_</span> <span class="nv">delegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-mapidledelegate">MapIdleDelegate</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>delegate</em>
</code>
</td>
<td>
<div>
<p>The delegate</p>
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
<a name="/s:7heresdk7HereMapC06removeC12IdleDelegateyyAA0ceF0_pF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeMapIdleDelegate(_:)"></a>
<a class="token" href="#/s:7heresdk7HereMapC06removeC12IdleDelegateyyAA0ceF0_pF">removeMapIdleDelegate(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes a delegate from receiving idle state notifications.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">removeMapIdleDelegate</span><span class="p">(</span><span class="n">_</span> <span class="nv">delegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-mapidledelegate">MapIdleDelegate</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>delegate</em>
</code>
</td>
<td>
<div>
<p>The delegate</p>
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
</body>
</html>

`
}</HTMLBlock>
