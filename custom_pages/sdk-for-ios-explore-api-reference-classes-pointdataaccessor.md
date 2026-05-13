---
title: "PointDataAccessor Class Reference"
slug: "sdk-for-ios-explore-api-reference-classes-pointdataaccessor"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- PointDataAccessor.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Class/PointDataAccessor"></a>
<a title="PointDataAccessor Class Reference"></a>
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
        PointDataAccessor Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public class PointDataAccessor</code></pre>
<pre><code>extension PointDataAccessor: NativeBase</code></pre>
<pre><code>extension PointDataAccessor: Hashable</code></pre>
</div>
</div>
<p>Point data accessor used for manipulating points that are part of a PointDataSource.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17PointDataAccessorC14getCoordinatesAA03GeoF0VyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getCoordinates()"></a>
<a class="token" href="#/s:7heresdk17PointDataAccessorC14getCoordinatesAA03GeoF0VyF">getCoordinates()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Gets point coordinates.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func getCoordinates() -&gt; GeoCoordinates</code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>The point coordinates.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17PointDataAccessorC13getAttributesAA0cfD0CyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getAttributes()"></a>
<a class="token" href="#/s:7heresdk17PointDataAccessorC13getAttributesAA0cfD0CyF">getAttributes()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Gets point attributes accessor.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func getAttributes() -&gt; DataAttributesAccessor</code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>The point attributes accessor.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17PointDataAccessorC14setCoordinatesyyAA03GeoF0VF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setCoordinates(_:)"></a>
<a class="token" href="#/s:7heresdk17PointDataAccessorC14setCoordinatesyyAA03GeoF0VF">setCoordinates(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Updates point coordinates.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func setCoordinates(_ position: GeoCoordinates)</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>position</em>
</code>
</td>
<td>
<div>
<p>The new point coordinates.</p>
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
<a name="/s:7heresdk17PointDataAccessorC13setAttributesyyAA0cF0CF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setAttributes(_:)"></a>
<a class="token" href="#/s:7heresdk17PointDataAccessorC13setAttributesyyAA0cF0CF">setAttributes(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Replaces point attributes.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func setAttributes(_ attributes: DataAttributes)</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>attributes</em>
</code>
</td>
<td>
<div>
<p>The new point attributes.</p>
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
