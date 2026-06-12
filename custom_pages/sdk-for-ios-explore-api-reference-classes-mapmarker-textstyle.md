---
title: "TextStyle"
slug: "sdk-for-ios-explore-api-reference-classes-mapmarker-textstyle"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/TextStyle"></a>
<a title="TextStyle Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>

<a href="sdk-for-ios-explore-api-reference-maps">Maps</a>

<a href="sdk-for-ios-explore-api-reference-classes-mapmarker">MapMarker</a>

        TextStyle Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>TextStyle</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">TextStyle</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-mapmarker">MapMarker</a></span><span class="o">.</span><span class="kt">TextStyle</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-mapmarker">MapMarker</a></span><span class="o">.</span><span class="kt">TextStyle</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Styling options for the text of a <code><a href="sdk-for-ios-explore-api-reference-classes-mapmarker">MapMarker</a></code>.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapMarkerC9TextStyleC18InstantiationErrora"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/InstantiationError"></a>
<a class="token" href="#/s:7heresdk9MapMarkerC9TextStyleC18InstantiationErrora">InstantiationError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Thrown when a problem occurs while trying to create a <code>MapMarker.TextStyle</code> instance.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">InstantiationError</span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-mapmarker-textstyle-instantiationerrorcode">InstantiationErrorCode</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapMarkerC9TextStyleCAEycfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init()"></a>
<a class="token" href="#/s:7heresdk9MapMarkerC9TextStyleCAEycfc">init()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a default set of styling options for the text of a <code><a href="sdk-for-ios-explore-api-reference-classes-mapmarker">MapMarker</a></code> that consists of
the following values:</p>
<ul>
<li>Text size: 18 pixels</li>
<li>Text color: opaque white</li>
<li>Text outline size: 0 pixels</li>
<li>Text outline color: opaque black</li>
<li>Text placement: <code><a href="../../Classes/MapMarker/TextStyle/Placement.html#/s:7heresdk9MapMarkerC9TextStyleC9PlacementO6bottomyA2GmF">MapMarker.TextStyle.Placement.bottom</a></code></li>
</ul>
<p>Once the resulting <code>TextStyle</code> is applied to a <code><a href="sdk-for-ios-explore-api-reference-classes-mapmarker">MapMarker</a></code>, its text will be centered over its
image. The font will be 18 pixels wide, colored opaque white and will have no visible outline.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapMarkerC9TextStyleC8textSize0F5Color0f7OutlineG00fiH010placementsAESd_So7UIColorCSdALSayAE9PlacementOGtKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(textSize:textColor:textOutlineSize:textOutlineColor:placements:)"></a>
<a class="token" href="#/s:7heresdk9MapMarkerC9TextStyleC8textSize0F5Color0f7OutlineG00fiH010placementsAESd_So7UIColorCSdALSayAE9PlacementOGtKcfc">init(textSize:<wbr/>textColor:<wbr/>textOutlineSize:<wbr/>textOutlineColor:<wbr/>placements:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a set of styling options for the text of a <code><a href="sdk-for-ios-explore-api-reference-classes-mapmarker">MapMarker</a></code>.</p>
<p>List of placements is used to specify allowed placement of text relative to the icon.
When marker overlapping is allowed as set by <code><a href="../../Classes/MapMarker.html#/s:7heresdk9MapMarkerC16isOverlapAllowedSbvp">MapMarker.isOverlapAllowed</a></code>,
only first placement element is considered.
Otherwise the placement value is chosen so that the text does not overlap
with other <code><a href="sdk-for-ios-explore-api-reference-classes-mapmarker">MapMarker</a></code> instances.</p>
<p>Placement values are prioritized according
to the order in which they appear in the list. Lists with duplicate entries
as well as empty lists are not supported.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../../Classes/MapMarker/TextStyle.html#/s:7heresdk9MapMarkerC9TextStyleC18InstantiationErrora">MapMarker.TextStyle.InstantiationError</a></code> In case of invalid input parameters.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">textSize</span><span class="p">:</span> <span class="kt">Double</span><span class="p">,</span> <span class="nv">textColor</span><span class="p">:</span> <span class="kt">UIColor</span><span class="p">,</span> <span class="nv">textOutlineSize</span><span class="p">:</span> <span class="kt">Double</span><span class="p">,</span> <span class="nv">textOutlineColor</span><span class="p">:</span> <span class="kt">UIColor</span><span class="p">,</span> <span class="nv">placements</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-mapmarker">MapMarker</a></span><span class="o">.</span><span class="kt">TextStyle</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-mapmarker-textstyle-placement">Placement</a></span><span class="p">])</span> <span class="k">throws</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>textSize</em>
</code>
</td>
<td>
<div>
<p>The size of the text in pixels.
Only positive values are supported.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>textColor</em>
</code>
</td>
<td>
<div>
<p>The text color.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>textOutlineSize</em>
</code>
</td>
<td>
<div>
<p>The size of the text outline in pixels.
Only non-negative values are supported.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>textOutlineColor</em>
</code>
</td>
<td>
<div>
<p>The color of the text outline.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>placements</em>
</code>
</td>
<td>
<div>
<p>List of allowed placements of the text relative to the icon of a <code><a href="sdk-for-ios-explore-api-reference-classes-mapmarker">MapMarker</a></code>.</p>
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
<a name="/s:7heresdk9MapMarkerC9TextStyleC8textSize0F5Color0f7OutlineG00fiH010placements8fontNameAESd_So7UIColorCSdAMSayAE9PlacementOGSStKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(textSize:textColor:textOutlineSize:textOutlineColor:placements:fontName:)"></a>
<a class="token" href="#/s:7heresdk9MapMarkerC9TextStyleC8textSize0F5Color0f7OutlineG00fiH010placements8fontNameAESd_So7UIColorCSdAMSayAE9PlacementOGSStKcfc">init(textSize:<wbr/>textColor:<wbr/>textOutlineSize:<wbr/>textOutlineColor:<wbr/>placements:<wbr/>fontName:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a set of styling options for the text of a <code><a href="sdk-for-ios-explore-api-reference-classes-mapmarker">MapMarker</a></code>.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<p>List of placements is used to specify allowed placement of text relative to the icon.
When marker overlapping is allowed as set by <code><a href="../../Classes/MapMarker.html#/s:7heresdk9MapMarkerC16isOverlapAllowedSbvp">MapMarker.isOverlapAllowed</a></code>,
only first placement element is considered.
Otherwise the placement value is chosen so that the text does not overlap
with other <code><a href="sdk-for-ios-explore-api-reference-classes-mapmarker">MapMarker</a></code> instances.</p>
<p>Placement values are prioritized according
to the order in which they appear in the list. Lists with duplicate entries
as well as empty lists are not supported.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../../Classes/MapMarker/TextStyle.html#/s:7heresdk9MapMarkerC9TextStyleC18InstantiationErrora">MapMarker.TextStyle.InstantiationError</a></code> In case of invalid input parameters.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">textSize</span><span class="p">:</span> <span class="kt">Double</span><span class="p">,</span> <span class="nv">textColor</span><span class="p">:</span> <span class="kt">UIColor</span><span class="p">,</span> <span class="nv">textOutlineSize</span><span class="p">:</span> <span class="kt">Double</span><span class="p">,</span> <span class="nv">textOutlineColor</span><span class="p">:</span> <span class="kt">UIColor</span><span class="p">,</span> <span class="nv">placements</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-mapmarker">MapMarker</a></span><span class="o">.</span><span class="kt">TextStyle</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-mapmarker-textstyle-placement">Placement</a></span><span class="p">],</span> <span class="nv">fontName</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span> <span class="k">throws</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>textSize</em>
</code>
</td>
<td>
<div>
<p>The size of the text in pixels.
Only positive values are supported.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>textColor</em>
</code>
</td>
<td>
<div>
<p>The text color.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>textOutlineSize</em>
</code>
</td>
<td>
<div>
<p>The size of the text outline in pixels.
Only non-negative values are supported.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>textOutlineColor</em>
</code>
</td>
<td>
<div>
<p>The color of the text outline.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>placements</em>
</code>
</td>
<td>
<div>
<p>List of allowed placements of the text relative to the icon of a <code><a href="sdk-for-ios-explore-api-reference-classes-mapmarker">MapMarker</a></code>.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>fontName</em>
</code>
</td>
<td>
<div>
<p>Font name, registered with <code>AssetsManager.registerFont</code>.
If empty string is provided, a default font will be used.</p>
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
<a name="/s:7heresdk9MapMarkerC9TextStyleC8fontNameSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/fontName"></a>
<a class="token" href="#/s:7heresdk9MapMarkerC9TextStyleC8fontNameSSvp">fontName</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The font used in the text style.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">fontName</span><span class="p">:</span> <span class="kt">String</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapMarkerC9TextStyleC8textSizeSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/textSize"></a>
<a class="token" href="#/s:7heresdk9MapMarkerC9TextStyleC8textSizeSdvp">textSize</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The text size in pixels.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">textSize</span><span class="p">:</span> <span class="kt">Double</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapMarkerC9TextStyleC9textColorSo7UIColorCvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/textColor"></a>
<a class="token" href="#/s:7heresdk9MapMarkerC9TextStyleC9textColorSo7UIColorCvp">textColor</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The text color.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">textColor</span><span class="p">:</span> <span class="kt">UIColor</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapMarkerC9TextStyleC15textOutlineSizeSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/textOutlineSize"></a>
<a class="token" href="#/s:7heresdk9MapMarkerC9TextStyleC15textOutlineSizeSdvp">textOutlineSize</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The text outline size in pixels.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">textOutlineSize</span><span class="p">:</span> <span class="kt">Double</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapMarkerC9TextStyleC16textOutlineColorSo7UIColorCvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/textOutlineColor"></a>
<a class="token" href="#/s:7heresdk9MapMarkerC9TextStyleC16textOutlineColorSo7UIColorCvp">textOutlineColor</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The text outline color.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">textOutlineColor</span><span class="p">:</span> <span class="kt">UIColor</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapMarkerC9TextStyleC10placementsSayAE9PlacementOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/placements"></a>
<a class="token" href="#/s:7heresdk9MapMarkerC9TextStyleC10placementsSayAE9PlacementOGvp">placements</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of possible text placements relative to the icon of a <code><a href="sdk-for-ios-explore-api-reference-classes-mapmarker">MapMarker</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">placements</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-mapmarker">MapMarker</a></span><span class="o">.</span><span class="kt">TextStyle</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-mapmarker-textstyle-placement">Placement</a></span><span class="p">]</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapMarkerC9TextStyleC22InstantiationErrorCodeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/InstantiationErrorCode"></a>
<a class="token" href="#/s:7heresdk9MapMarkerC9TextStyleC22InstantiationErrorCodeO">InstantiationErrorCode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Describes a reason for failing to create a <code><a href="sdk-for-ios-explore-api-reference-classes-mapmarker-textstyle">MapMarker.TextStyle</a></code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-mapmarker-textstyle-instantiationerrorcode">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">InstantiationErrorCode</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-mapmarker">MapMarker</a></span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-mapmarker-textstyle">TextStyle</a></span><span class="o">.</span><span class="kt">InstantiationErrorCode</span> <span class="p">:</span> <span class="kt">Error</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapMarkerC9TextStyleC9PlacementO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/Placement"></a>
<a class="token" href="#/s:7heresdk9MapMarkerC9TextStyleC9PlacementO">Placement</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents text placement with respect to the icon of a <code><a href="sdk-for-ios-explore-api-reference-classes-mapmarker">MapMarker</a></code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-mapmarker-textstyle-placement">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">Placement</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
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
} </HTMLBlock>
