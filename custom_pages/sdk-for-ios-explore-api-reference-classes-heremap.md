---
title: "HereMap Class Reference"
slug: "sdk-for-ios-explore-api-reference-classes-heremap"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- HereMap.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Class/HereMap"></a>
<a title="HereMap Class Reference"></a>
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
        HereMap Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public class HereMap</code></pre>
<pre><code>extension HereMap: NativeBase</code></pre>
<pre><code>extension HereMap: Hashable</code></pre>
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
<pre><code>public var style: Style { get }</code></pre>
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
<pre><code>public func addMapIdleDelegate(_ delegate: MapIdleDelegate)</code></pre>
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
<pre><code>public func removeMapIdleDelegate(_ delegate: MapIdleDelegate)</code></pre>
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



</div>
`
}</HTMLBlock>
