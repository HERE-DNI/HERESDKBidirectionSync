---
title: "Untitled"
slug: "sdk-for-ios-navigate-api-reference-classes-mapmarker-textstyle-instantiationerrorcode"
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
<a href="sdk-for-ios-navigate-api-reference-..-..-..-index">heresdk</a>
<img alt="" id="carat" src="../../../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-..-..-maps">Maps</a>
<img alt="" id="carat" src="../../../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-..-..-classes-mapmarker">MapMarker</a>
<img alt="" id="carat" src="../../../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-..-..-classes-mapmarker-textstyle">TextStyle</a>
<img alt="" id="carat" src="../../../img/carat.png"/>
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
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-..-..-classes-mapmarker">MapMarker</a></span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-..-..-classes-mapmarker-textstyle">TextStyle</a></span><span class="o">.</span><span class="kt">InstantiationErrorCode</span> <span class="p">:</span> <span class="kt">Error</span></code></pre>
</div>
</div>
<p>Describes a reason for failing to create a <code><a href="sdk-for-ios-navigate-api-reference-..-..-..-classes-mapmarker-textstyle">MapMarker.TextStyle</a></code>.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapMarkerC9TextStyleC22InstantiationErrorCodeO011nonPositiveD4SizeyA2GmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/nonPositiveTextSize"></a>
<a class="token" href="#/s:7heresdk9MapMarkerC9TextStyleC22InstantiationErrorCodeO011nonPositiveD4SizeyA2GmF">nonPositiveTextSize</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Instantiation parameters contain unsupported non positive text size.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">nonPositiveTextSize</span> <span class="o">=</span> <span class="mi">1</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapMarkerC9TextStyleC22InstantiationErrorCodeO08negativeD11OutlineSizeyA2GmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/negativeTextOutlineSize"></a>
<a class="token" href="#/s:7heresdk9MapMarkerC9TextStyleC22InstantiationErrorCodeO08negativeD11OutlineSizeyA2GmF">negativeTextOutlineSize</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Instantiation parameters contain unsupported negative text outline size.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">negativeTextOutlineSize</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapMarkerC9TextStyleC22InstantiationErrorCodeO05emptyD13PlacementListyA2GmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/emptyTextPlacementList"></a>
<a class="token" href="#/s:7heresdk9MapMarkerC9TextStyleC22InstantiationErrorCodeO05emptyD13PlacementListyA2GmF">emptyTextPlacementList</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Instantiation parameters contain unsupported empty list without any <code><a href="sdk-for-ios-navigate-api-reference-..-..-..-classes-mapmarker-textstyle-placement">MapMarker.TextStyle.Placement</a></code> entries.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">emptyTextPlacementList</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapMarkerC9TextStyleC22InstantiationErrorCodeO09duplicateD15PlacementValuesyA2GmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/duplicateTextPlacementValues"></a>
<a class="token" href="#/s:7heresdk9MapMarkerC9TextStyleC22InstantiationErrorCodeO09duplicateD15PlacementValuesyA2GmF">duplicateTextPlacementValues</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Instantiation parameters contain unsupported list with duplicate <code><a href="sdk-for-ios-navigate-api-reference-..-..-..-classes-mapmarker-textstyle-placement">MapMarker.TextStyle.Placement</a></code> entries.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">duplicateTextPlacementValues</span></code></pre>
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
