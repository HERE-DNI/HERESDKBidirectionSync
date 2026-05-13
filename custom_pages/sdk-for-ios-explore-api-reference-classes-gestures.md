---
title: "Gestures Class Reference"
slug: "sdk-for-ios-explore-api-reference-classes-gestures"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- Gestures.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Class/Gestures"></a>
<a title="Gestures Class Reference"></a>
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
        Gestures Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public class Gestures</code></pre>
<pre><code>extension Gestures: NativeBase</code></pre>
<pre><code>extension Gestures: Hashable</code></pre>
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
<p><code><a href="sdk-for-ios-explore-api-reference-..-protocols-tapdelegate">TapDelegate</a></code> that notifies when a tap gesture occurs.
<code>Gestures</code> holds a strong reference to the delegate.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public weak var tapDelegate: TapDelegate? { get set }</code></pre>
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
<p><code><a href="sdk-for-ios-explore-api-reference-..-protocols-doubletapdelegate">DoubleTapDelegate</a></code> that notifies when a double-tap gesture occurs.
<code>Gestures</code> holds a strong reference to the delegate.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public weak var doubleTapDelegate: DoubleTapDelegate? { get set }</code></pre>
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
<p><code><a href="sdk-for-ios-explore-api-reference-..-protocols-pinchrotatedelegate">PinchRotateDelegate</a></code> that notifies when a pinch-rotate gesture occurs.
<code>Gestures</code> holds a strong reference to the delegate.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public weak var pinchRotateDelegate: PinchRotateDelegate? { get set }</code></pre>
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
<p><code><a href="sdk-for-ios-explore-api-reference-..-protocols-longpressdelegate">LongPressDelegate</a></code> that notifies when a long-press gesture occurs.
<code>Gestures</code> holds a strong reference to the delegate.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public weak var longPressDelegate: LongPressDelegate? { get set }</code></pre>
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
<p><code><a href="sdk-for-ios-explore-api-reference-..-protocols-pandelegate">PanDelegate</a></code> that notifies when a pan gesture occurs.
<code>Gestures</code> holds a strong reference to the delegate.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public weak var panDelegate: PanDelegate? { get set }</code></pre>
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
<p><code><a href="sdk-for-ios-explore-api-reference-..-protocols-twofingertapdelegate">TwoFingerTapDelegate</a></code> that notifies when a two-finger tap gesture occurs.
<code>Gestures</code> holds a strong reference to the delegate.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public weak var twoFingerTapDelegate: TwoFingerTapDelegate? { get set }</code></pre>
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
<p><code><a href="sdk-for-ios-explore-api-reference-..-protocols-twofingerpandelegate">TwoFingerPanDelegate</a></code> that notifies when a two-finger pan gesture occurs.
<code>Gestures</code> holds a strong reference to the delegate.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public weak var twoFingerPanDelegate: TwoFingerPanDelegate? { get set }</code></pre>
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
<pre><code>public func enableDefaultAction(forGesture gestureType: GestureType)</code></pre>
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
<pre><code>public func disableDefaultAction(forGesture gestureType: GestureType)</code></pre>
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



</div>
`
}</HTMLBlock>
