---
title: "GestureType Enumeration Reference"
slug: "sdk-for-ios-explore-api-reference-enums-gesturetype"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- GestureType.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Enum/GestureType"></a>
<a title="GestureType Enumeration Reference"></a>
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
        GestureType Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public enum GestureType : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
<p>Enum that represents the type of a gesture.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11GestureTypeO12twoFingerTapyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/twoFingerTap"></a>
<a class="token" href="#/s:7heresdk11GestureTypeO12twoFingerTapyA2CmF">twoFingerTap</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Single-tap performed with two fingers. When performed on a map view, this instantly zooms
the map out by a factor of 0.5 and the map becomes twice as small.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case twoFingerTap</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11GestureTypeO9doubleTapyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/doubleTap"></a>
<a class="token" href="#/s:7heresdk11GestureTypeO9doubleTapyA2CmF">doubleTap</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Double-tap performed with one finger. When performed on a map view, this instantly zooms
the map in by a factor of 2 and the map becomes twice as big.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case doubleTap</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11GestureTypeO3panyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/pan"></a>
<a class="token" href="#/s:7heresdk11GestureTypeO3panyA2CmF">pan</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Panning gesture with a one or two fingers. When performed on a map view, this continuously moves
the map.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case pan</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11GestureTypeO12twoFingerPanyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/twoFingerPan"></a>
<a class="token" href="#/s:7heresdk11GestureTypeO12twoFingerPanyA2CmF">twoFingerPan</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Vertical panning gesture with two fingers. When performed on a map view, this continuously
tilts the map.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case twoFingerPan</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11GestureTypeO11pinchRotateyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/pinchRotate"></a>
<a class="token" href="#/s:7heresdk11GestureTypeO11pinchRotateyA2CmF">pinchRotate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Pinching and rotating gesture using two fingers. When performed on a map view, this
continuously scales, zooms or rotates the map.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case pinchRotate</code></pre>
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



</div>
`
}</HTMLBlock>
