---
title: "Maps / MapViewLifecycleDelegate"
slug: "sdk-for-ios-navigate-api-reference-protocols-mapviewlifecycledelegate"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/MapViewLifecycleDelegate"></a>
<a title="MapViewLifecycleDelegate Protocol Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-maps">Maps</a>
<img alt="" id="carat" src="../img/carat.png"/>
        MapViewLifecycleDelegate Protocol Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>MapViewLifecycleDelegate</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">MapViewLifecycleDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
<p>Provides a mechanism for observing a lifecycle of a map view and/or implementing components
whose lifecycle needs to be linked with that of a map view.</p>
<p>Storing the map view in a strong reference is strongly discouraged, as that
will create a reference cycle and prevent map view from being released.</p>
<p>A <code><a href="sdk-for-ios-navigate-api-reference-..-classes-mapview">MapView</a></code> is using a
<a href="https://developer.apple.com/documentation/quartzcore/cametallayer">CAMetalLayer</a></p>
<p>to render its content.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24MapViewLifecycleDelegateP8onAttach2toyAA0bC4Base_p_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/onAttach(to:)"></a>
<a class="token" href="#/s:7heresdk24MapViewLifecycleDelegateP8onAttach2toyAA0bC4Base_p_tF">onAttach(to:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Called when adding <code>MapViewLifecycleDelegate</code> to the map view. If the map view does not
have render target attached at the time of adding the listener, then this method will
be called later, after render target is attached. This means that the map view it
receives is always fully initialized.</p>
<p>Can be used to implement
the logic to create and add visual components to the map view.</p>
<p>Storing the map view in a strong reference is strongly discouraged, as that
will create a reference cycle and prevent map view from being released.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">onAttach</span><span class="p">(</span><span class="n">to</span> <span class="nv">mapView</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-mapviewbase">MapViewBase</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>mapView</em>
</code>
</td>
<td>
<div>
<p>The map view to attach to.</p>
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
<a name="/s:7heresdk24MapViewLifecycleDelegateP8onDetach4fromyAA0bC4Base_p_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/onDetach(from:)"></a>
<a class="token" href="#/s:7heresdk24MapViewLifecycleDelegateP8onDetach4fromyAA0bC4Base_p_tF">onDetach(from:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Called when removing <code>MapViewLifecycleDelegate</code> from the map view. Can be used to implement
the logic to remove visual components from the map view and release resources if necessary.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">onDetach</span><span class="p">(</span><span class="n">from</span> <span class="nv">mapView</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-mapviewbase">MapViewBase</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>mapView</em>
</code>
</td>
<td>
<div>
<p>The map view to detach from.</p>
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
<a name="/s:7heresdk24MapViewLifecycleDelegateP7onPauseyyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/onPause()"></a>
<a class="token" href="#/s:7heresdk24MapViewLifecycleDelegateP7onPauseyyF">onPause()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Called when the map view to which this <code>MapViewLifecycleDelegate</code> is attached to gets paused
(usually when the app goes into background). This should be used by components that
perform continuous updates to pause those updates until <code><a href="../Protocols/MapViewLifecycleDelegate.html#/s:7heresdk24MapViewLifecycleDelegateP8onResumeyyF">onResume(...)</a></code>
is called.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">onPause</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24MapViewLifecycleDelegateP8onResumeyyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/onResume()"></a>
<a class="token" href="#/s:7heresdk24MapViewLifecycleDelegateP8onResumeyyF">onResume()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Called when the map view to which this <code>MapViewLifecycleDelegate</code> is attached to gets resumed
(usually when the app goes into foreground). This should be used by components that
perform continuous updates to resume those updates after a previous call to
<code><a href="../Protocols/MapViewLifecycleDelegate.html#/s:7heresdk24MapViewLifecycleDelegateP7onPauseyyF">onPause(...)</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">onResume</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24MapViewLifecycleDelegateP9onDestroyyyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/onDestroy()"></a>
<a class="token" href="#/s:7heresdk24MapViewLifecycleDelegateP9onDestroyyyF">onDestroy()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Called when the map view to which this is attached to is destroyed.
After this is called, no other <code>MapViewLifecycleDelegate</code> method will be invoked.
This should be used to make sure all resources are freed.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">onDestroy</span><span class="p">()</span></code></pre>
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
