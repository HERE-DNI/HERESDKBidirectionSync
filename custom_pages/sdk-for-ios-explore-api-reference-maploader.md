---
title: "MapLoader  Reference"
slug: "sdk-for-ios-explore-api-reference-maploader"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- MapLoader.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Section/MapLoader"></a>
<a title="MapLoader  Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="sdk-for-ios-explore-api-reference-index">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>
<img alt="" id="carat" src="img/carat.png"/>
        MapLoader  Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18DataAttributesBaseP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/DataAttributesBase"></a>
<a class="token" href="#/s:7heresdk18DataAttributesBaseP">DataAttributesBase</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Interface for a collection of data attributes.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-protocols-dataattributesbase">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public protocol DataAttributesBase : AnyObject</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8LineDataC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/LineData"></a>
<a class="token" href="#/s:7heresdk8LineDataC">LineData</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents a geodetic line with custom attributes.
Can be created using a <code><a href="sdk-for-ios-explore-api-reference-classes-linedatabuilder">LineDataBuilder</a></code>.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public class LineData</code></pre>
<pre><code>extension LineData: NativeBase</code></pre>
<pre><code>extension LineData: Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16LineDataAccessorC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/LineDataAccessor"></a>
<a class="token" href="#/s:7heresdk16LineDataAccessorC">LineDataAccessor</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Line data accessor used for manipulating polylines that are part of a LineDataSource.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-linedataaccessor">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public class LineDataAccessor</code></pre>
<pre><code>extension LineDataAccessor: NativeBase</code></pre>
<pre><code>extension LineDataAccessor: Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15LineDataBuilderC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/LineDataBuilder"></a>
<a class="token" href="#/s:7heresdk15LineDataBuilderC">LineDataBuilder</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Builder of <code><a href="MapLoader.html#/s:7heresdk8LineDataC">LineData</a></code> instances.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-linedatabuilder">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public class LineDataBuilder</code></pre>
<pre><code>extension LineDataBuilder: NativeBase</code></pre>
<pre><code>extension LineDataBuilder: Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14LineDataSourceC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/LineDataSource"></a>
<a class="token" href="#/s:7heresdk14LineDataSourceC">LineDataSource</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Polyline data source allows the rendering engine access to the user provided
polylines geometry and their attributes.</p>
<p>Polyline segments are rendered following the shortest path between their end vertices.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-linedatasource">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public class LineDataSource</code></pre>
<pre><code>extension LineDataSource: NativeBase</code></pre>
<pre><code>extension LineDataSource: Hashable</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21LineDataSourceBuilderC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/LineDataSourceBuilder"></a>
<a class="token" href="#/s:7heresdk21LineDataSourceBuilderC">LineDataSourceBuilder</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Builder of lines data source.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-linedatasourcebuilder">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public class LineDataSourceBuilder</code></pre>
<pre><code>extension LineDataSourceBuilder: NativeBase</code></pre>
<pre><code>extension LineDataSourceBuilder: Hashable</code></pre>
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
