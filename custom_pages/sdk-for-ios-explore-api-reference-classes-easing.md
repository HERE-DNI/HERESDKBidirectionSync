---
title: "Easing Class Reference"
slug: "sdk-for-ios-explore-api-reference-classes-easing"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- Easing.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Class/Easing"></a>
<a title="Easing Class Reference"></a>
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
        Easing Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public class Easing</code></pre>
<pre><code>extension Easing: NativeBase</code></pre>
<pre><code>extension Easing: Hashable</code></pre>
</div>
</div>
<p>Animation easing representing an easing function to be used during animations.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk6EasingC18InstantiationErrora"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/InstantiationError"></a>
<a class="token" href="#/s:7heresdk6EasingC18InstantiationErrora">InstantiationError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Thrown when a problem occurs while trying to create an <code>Easing</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public typealias InstantiationError = InstantiationErrorCode</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk6EasingCyAcA0B8FunctionOcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:)"></a>
<a class="token" href="#/s:7heresdk6EasingCyAcA0B8FunctionOcfc">init(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates an instance of <code>Easing</code> using a predefined easing function.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public init(_ easingFunction: EasingFunction)</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>easingFunction</em>
</code>
</td>
<td>
<div>
<p>Easing function.</p>
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
<a name="/s:7heresdk6EasingCyACSayAA7Point2DVGKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:)"></a>
<a class="token" href="#/s:7heresdk6EasingCyACSayAA7Point2DVGKcfc">init(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates an instance of customized <code>Easing</code> using a specified number of points describing an
easing function.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Classes/Easing.html#/s:7heresdk6EasingC18InstantiationErrora">Easing.InstantiationError</a></code> Instantiation error in case of invalid input parameters.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public init(_ points: [Point2D]) throws</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>points</em>
</code>
</td>
<td>
<div>
<p>List of sampled data points that define an easing function.
X describes normalized time values in the range [0, 1].
Y describes normalized animated value changes. Values can fall outside of the range [0, 1]. During
an animation run animated target value is multiplied with Y value. In case resulting animated target value
falls outside of its own supported range it will be clamped to its range (e.g. when negative values used for
color animation).
X values must increase monotonically.
There must be at least 2 data points specified. The first point’s X value must be 0, the last point’s
X value must be 1.
During an animation run for any given time value X’ from the animation engine that
satisfies the relation X(i) &lt; X’ &lt; X(i+1) for the given X data points the corresponding
Y’ value will be calculated by linearly interpolating between Y(i) and Y(i+1) data points.
The higher the sampling rate of the easing curve used for the data points the more precise the results.
In order to achieve the same animation precision for animations with different durations
(shorter vs longer) it is recommended to use a higher sampling rate for longer animation duration.</p>
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
<a name="/s:7heresdk6EasingC22InstantiationErrorCodeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/InstantiationErrorCode"></a>
<a class="token" href="#/s:7heresdk6EasingC22InstantiationErrorCodeO">InstantiationErrorCode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Describes a reason for failing to create an <code><a href="sdk-for-ios-explore-api-reference-..-classes-easing">Easing</a></code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-..-classes-easing-instantiationerrorcode">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum InstantiationErrorCode : UInt32, CaseIterable, Codable</code></pre>
<pre><code>extension Easing.InstantiationErrorCode : Error</code></pre>
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
