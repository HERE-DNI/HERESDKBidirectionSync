---
title: "Gestures"
slug: "sdk-for-ios-explore-api-reference-classes-gestures"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/Gestures"></a>
<a title="Gestures Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>

<a href="sdk-for-ios-explore-api-reference-maps">Maps</a>

        Gestures Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>Gestures</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">Gestures</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Gestures</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Gestures</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Use this class to process touch events from the platform and detect gesture induced actions on the map view.
Please note that this class holds strong references to the gesture delegates.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8GesturesC11tapDelegateAA03TapD0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/tapDelegate"></a>
<a class="token" href="#/s:7heresdk8GesturesC11tapDelegateAA03TapD0_pSgvp">tapDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p><code><a href="sdk-for-ios-explore-api-reference-protocols-tapdelegate">TapDelegate</a></code> that notifies when a tap gesture occurs.
<code>Gestures</code> holds a strong reference to the delegate.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">weak</span> <span class="k">var</span> <span class="nv">tapDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-tapdelegate">TapDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8GesturesC17doubleTapDelegateAA06DoubledE0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/doubleTapDelegate"></a>
<a class="token" href="#/s:7heresdk8GesturesC17doubleTapDelegateAA06DoubledE0_pSgvp">doubleTapDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p><code><a href="sdk-for-ios-explore-api-reference-protocols-doubletapdelegate">DoubleTapDelegate</a></code> that notifies when a double-tap gesture occurs.
<code>Gestures</code> holds a strong reference to the delegate.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">weak</span> <span class="k">var</span> <span class="nv">doubleTapDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-doubletapdelegate">DoubleTapDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8GesturesC19pinchRotateDelegateAA05PinchdE0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/pinchRotateDelegate"></a>
<a class="token" href="#/s:7heresdk8GesturesC19pinchRotateDelegateAA05PinchdE0_pSgvp">pinchRotateDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p><code><a href="sdk-for-ios-explore-api-reference-protocols-pinchrotatedelegate">PinchRotateDelegate</a></code> that notifies when a pinch-rotate gesture occurs.
<code>Gestures</code> holds a strong reference to the delegate.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">weak</span> <span class="k">var</span> <span class="nv">pinchRotateDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-pinchrotatedelegate">PinchRotateDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8GesturesC17longPressDelegateAA04LongdE0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/longPressDelegate"></a>
<a class="token" href="#/s:7heresdk8GesturesC17longPressDelegateAA04LongdE0_pSgvp">longPressDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p><code><a href="sdk-for-ios-explore-api-reference-protocols-longpressdelegate">LongPressDelegate</a></code> that notifies when a long-press gesture occurs.
<code>Gestures</code> holds a strong reference to the delegate.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">weak</span> <span class="k">var</span> <span class="nv">longPressDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-longpressdelegate">LongPressDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8GesturesC11panDelegateAA03PanD0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/panDelegate"></a>
<a class="token" href="#/s:7heresdk8GesturesC11panDelegateAA03PanD0_pSgvp">panDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p><code><a href="sdk-for-ios-explore-api-reference-protocols-pandelegate">PanDelegate</a></code> that notifies when a pan gesture occurs.
<code>Gestures</code> holds a strong reference to the delegate.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">weak</span> <span class="k">var</span> <span class="nv">panDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-pandelegate">PanDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8GesturesC20twoFingerTapDelegateAA03TwodeF0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/twoFingerTapDelegate"></a>
<a class="token" href="#/s:7heresdk8GesturesC20twoFingerTapDelegateAA03TwodeF0_pSgvp">twoFingerTapDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p><code><a href="sdk-for-ios-explore-api-reference-protocols-twofingertapdelegate">TwoFingerTapDelegate</a></code> that notifies when a two-finger tap gesture occurs.
<code>Gestures</code> holds a strong reference to the delegate.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">weak</span> <span class="k">var</span> <span class="nv">twoFingerTapDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-twofingertapdelegate">TwoFingerTapDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8GesturesC20twoFingerPanDelegateAA03TwodeF0_pSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/twoFingerPanDelegate"></a>
<a class="token" href="#/s:7heresdk8GesturesC20twoFingerPanDelegateAA03TwodeF0_pSgvp">twoFingerPanDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p><code><a href="sdk-for-ios-explore-api-reference-protocols-twofingerpandelegate">TwoFingerPanDelegate</a></code> that notifies when a two-finger pan gesture occurs.
<code>Gestures</code> holds a strong reference to the delegate.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">weak</span> <span class="k">var</span> <span class="nv">twoFingerPanDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-twofingerpandelegate">TwoFingerPanDelegate</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8GesturesC19enableDefaultAction10forGestureyAA0G4TypeO_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/enableDefaultAction(forGesture:)"></a>
<a class="token" href="#/s:7heresdk8GesturesC19enableDefaultAction10forGestureyAA0G4TypeO_tF">enableDefaultAction(forGesture:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Enables default action to be performed for a specified
gesture.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">enableDefaultAction</span><span class="p">(</span><span class="n">forGesture</span> <span class="nv">gestureType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-gesturetype">GestureType</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>gestureType</em>
</code>
</td>
<td>
<div>
<p>The gesture type.</p>
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
<a name="/s:7heresdk8GesturesC20disableDefaultAction10forGestureyAA0G4TypeO_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/disableDefaultAction(forGesture:)"></a>
<a class="token" href="#/s:7heresdk8GesturesC20disableDefaultAction10forGestureyAA0G4TypeO_tF">disableDefaultAction(forGesture:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Disables default action for a specified gesture.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">disableDefaultAction</span><span class="p">(</span><span class="n">forGesture</span> <span class="nv">gestureType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-gesturetype">GestureType</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>gestureType</em>
</code>
</td>
<td>
<div>
<p>The gesture type.</p>
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
} </HTMLBlock>
