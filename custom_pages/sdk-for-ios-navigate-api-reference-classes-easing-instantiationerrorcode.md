---
title: "Untitled"
slug: "sdk-for-ios-navigate-api-reference-classes-easing-instantiationerrorcode"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- InstantiationErrorCode.html -->
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Enum/InstantiationErrorCode"></a>
<a title="InstantiationErrorCode Enumeration Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-..-index">heresdk</a>
<img alt="" id="carat" src="../../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-..-maps">Maps</a>
<img alt="" id="carat" src="../../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-..-classes-easing">Easing</a>
<img alt="" id="carat" src="../../img/carat.png"/>
        InstantiationErrorCode Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>InstantiationErrorCode</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">InstantiationErrorCode</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-..-classes-easing">Easing</a></span><span class="o">.</span><span class="kt">InstantiationErrorCode</span> <span class="p">:</span> <span class="kt">Error</span></code></pre>
</div>
</div>
<p>Describes a reason for failing to create an <code><a href="sdk-for-ios-navigate-api-reference-..-..-classes-easing">Easing</a></code>.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk6EasingC22InstantiationErrorCodeO29sampledDataPointCountTooSmallyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/sampledDataPointCountTooSmall"></a>
<a class="token" href="#/s:7heresdk6EasingC22InstantiationErrorCodeO29sampledDataPointCountTooSmallyA2EmF">sampledDataPointCountTooSmall</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Number of sampled data points in the list that defines an easing function is too small (i.e. less than 2).</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">sampledDataPointCountTooSmall</span> <span class="o">=</span> <span class="mi">1</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk6EasingC22InstantiationErrorCodeO35sampledDataPointsFirstXValueInvalidyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/sampledDataPointsFirstXValueInvalid"></a>
<a class="token" href="#/s:7heresdk6EasingC22InstantiationErrorCodeO35sampledDataPointsFirstXValueInvalidyA2EmF">sampledDataPointsFirstXValueInvalid</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Invalid first value of X in the list of sampled data points that define an easing function. First value of X must be 0.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">sampledDataPointsFirstXValueInvalid</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk6EasingC22InstantiationErrorCodeO34sampledDataPointsLastXValueInvalidyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/sampledDataPointsLastXValueInvalid"></a>
<a class="token" href="#/s:7heresdk6EasingC22InstantiationErrorCodeO34sampledDataPointsLastXValueInvalidyA2EmF">sampledDataPointsLastXValueInvalid</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Invalid last value of X in the list of sampled data points that define an easing function. Last value of X must be 1.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">sampledDataPointsLastXValueInvalid</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk6EasingC22InstantiationErrorCodeO27sampledDataXValueOutOfRangeyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/sampledDataXValueOutOfRange"></a>
<a class="token" href="#/s:7heresdk6EasingC22InstantiationErrorCodeO27sampledDataXValueOutOfRangeyA2EmF">sampledDataXValueOutOfRange</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sampled data point X values that define an easing function are out of range [0, 1].</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">sampledDataXValueOutOfRange</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk6EasingC22InstantiationErrorCodeO30sampledDataXValuesNonMonotonicyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/sampledDataXValuesNonMonotonic"></a>
<a class="token" href="#/s:7heresdk6EasingC22InstantiationErrorCodeO30sampledDataXValuesNonMonotonicyA2EmF">sampledDataXValuesNonMonotonic</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sampled data point X values in the list that defines an easing function don’t increase monotonically.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">sampledDataXValuesNonMonotonic</span></code></pre>
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
