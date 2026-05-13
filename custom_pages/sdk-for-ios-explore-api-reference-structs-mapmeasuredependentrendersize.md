---
title: "MapMeasureDependentRenderSize Structure Reference"
slug: "sdk-for-ios-explore-api-reference-structs-mapmeasuredependentrendersize"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- MapMeasureDependentRenderSize.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/MapMeasureDependentRenderSize"></a>
<a title="MapMeasureDependentRenderSize Structure Reference"></a>
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
        MapMeasureDependentRenderSize Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct MapMeasureDependentRenderSize : Hashable</code></pre>
</div>
</div>
<p>Represents a render size, described as map measure dependent values.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk29MapMeasureDependentRenderSizeV11measureKindAA0bC0V0H0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/measureKind"></a>
<a class="token" href="#/s:7heresdk29MapMeasureDependentRenderSizeV11measureKindAA0bC0V0H0Ovp">measureKind</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The unit used for the key in <code><a href="../Structs/MapMeasureDependentRenderSize.html#/s:7heresdk29MapMeasureDependentRenderSizeV5sizesSDyS2dGvp">MapMeasureDependentRenderSize.sizes</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public let measureKind: MapMeasure.Kind</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk29MapMeasureDependentRenderSizeV8sizeUnitAA0eF0V0H0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/sizeUnit"></a>
<a class="token" href="#/s:7heresdk29MapMeasureDependentRenderSizeV8sizeUnitAA0eF0V0H0Ovp">sizeUnit</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The unit used for the value in <code><a href="../Structs/MapMeasureDependentRenderSize.html#/s:7heresdk29MapMeasureDependentRenderSizeV5sizesSDyS2dGvp">MapMeasureDependentRenderSize.sizes</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public let sizeUnit: RenderSize.Unit</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk29MapMeasureDependentRenderSizeV5sizesSDyS2dGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/sizes"></a>
<a class="token" href="#/s:7heresdk29MapMeasureDependentRenderSizeV5sizesSDyS2dGvp">sizes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The dictionary describing the size (value) per map measure (key).</p>
<p>Units of keys and values are defined in <code><a href="../Structs/MapMeasureDependentRenderSize.html#/s:7heresdk29MapMeasureDependentRenderSizeV11measureKindAA0bC0V0H0Ovp">MapMeasureDependentRenderSize.measureKind</a></code> and <code><a href="../Structs/MapMeasureDependentRenderSize.html#/s:7heresdk29MapMeasureDependentRenderSizeV8sizeUnitAA0eF0V0H0Ovp">MapMeasureDependentRenderSize.sizeUnit</a></code>.</p>
<p><code>sizes</code> with a single entry indicates using a fixed size value across all map measures.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public let sizes: [Double : Double]</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk29MapMeasureDependentRenderSizeV11measureKind8sizeUnit5sizesAcA0bC0V0H0O_AA0eF0V0J0OSDyS2dGtKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(measureKind:sizeUnit:sizes:)"></a>
<a class="token" href="#/s:7heresdk29MapMeasureDependentRenderSizeV11measureKind8sizeUnit5sizesAcA0bC0V0H0O_AA0eF0V0J0OSDyS2dGtKcfc">init(measureKind:<wbr/>sizeUnit:<wbr/>sizes:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs a <code>MapMeasureDependentRenderSize</code> from given parameters.</p>
<p>Supplying <code><a href="../Structs/MapMeasureDependentRenderSize.html#/s:7heresdk29MapMeasureDependentRenderSizeV5sizesSDyS2dGvp">sizes</a></code> map with a single entry indicates using a fixed size value across all map measures.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Structs/MapMeasureDependentRenderSize.html#/s:7heresdk29MapMeasureDependentRenderSizeV18InstantiationErrora">MapMeasureDependentRenderSize.InstantiationError</a></code> Instantiation error if <code><a href="../Structs/MapMeasureDependentRenderSize.html#/s:7heresdk29MapMeasureDependentRenderSizeV5sizesSDyS2dGvp">sizes</a></code> map is empty or contains negative keys or values.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public init(measureKind: MapMeasure.Kind, sizeUnit: RenderSize.Unit, sizes: [Double : Double]) throws</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>measureKind</em>
</code>
</td>
<td>
<div>
<p>The unit used for the key in <code><a href="../Structs/MapMeasureDependentRenderSize.html#/s:7heresdk29MapMeasureDependentRenderSizeV5sizesSDyS2dGvp">sizes</a></code>.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>sizeUnit</em>
</code>
</td>
<td>
<div>
<p>The unit used for the value in <code><a href="../Structs/MapMeasureDependentRenderSize.html#/s:7heresdk29MapMeasureDependentRenderSizeV5sizesSDyS2dGvp">sizes</a></code>.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>sizes</em>
</code>
</td>
<td>
<div>
<p>The dictionary describing the size (value) per map measure (key).</p>
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
<a name="/s:7heresdk29MapMeasureDependentRenderSizeV8sizeUnit0G0AcA0eF0V0H0O_SdtKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(sizeUnit:size:)"></a>
<a class="token" href="#/s:7heresdk29MapMeasureDependentRenderSizeV8sizeUnit0G0AcA0eF0V0H0O_SdtKcfc">init(sizeUnit:<wbr/>size:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs a <code>MapMeasureDependentRenderSize</code> from single size value which is constant across all map measures.</p>
<p>The given <code>size</code> value is stored in <code><a href="../Structs/MapMeasureDependentRenderSize.html#/s:7heresdk29MapMeasureDependentRenderSizeV5sizesSDyS2dGvp">MapMeasureDependentRenderSize.sizes</a></code> map at key 0 and <code><a href="../Structs/MapMeasureDependentRenderSize.html#/s:7heresdk29MapMeasureDependentRenderSizeV11measureKindAA0bC0V0H0Ovp">MapMeasureDependentRenderSize.measureKind</a></code> is set to <code><a href="../Structs/MapMeasure/Kind.html#/s:7heresdk10MapMeasureV4KindO9zoomLevelyA2EmF">MapMeasure.Kind.zoomLevel</a></code>.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Structs/MapMeasureDependentRenderSize.html#/s:7heresdk29MapMeasureDependentRenderSizeV18InstantiationErrora">MapMeasureDependentRenderSize.InstantiationError</a></code> Instantiation error if <code>size</code> is negative.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public init(sizeUnit: RenderSize.Unit, size: Double) throws</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>sizeUnit</em>
</code>
</td>
<td>
<div>
<p>The unit used for the value in <code>size</code>.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>size</em>
</code>
</td>
<td>
<div>
<p>The size independent of map measure. Must not be negative.</p>
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
<a name="/s:7heresdk29MapMeasureDependentRenderSizeV22InstantiationErrorCodeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/InstantiationErrorCode"></a>
<a class="token" href="#/s:7heresdk29MapMeasureDependentRenderSizeV22InstantiationErrorCodeO">InstantiationErrorCode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Describes a reason for failing to create a <code><a href="sdk-for-ios-explore-api-reference-..-structs-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a></code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-..-structs-mapmeasuredependentrendersize-instantiationerrorcode">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum InstantiationErrorCode : UInt32, CaseIterable, Codable</code></pre>
<pre><code>extension MapMeasureDependentRenderSize.InstantiationErrorCode : Error</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk29MapMeasureDependentRenderSizeV18InstantiationErrora"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/InstantiationError"></a>
<a class="token" href="#/s:7heresdk29MapMeasureDependentRenderSizeV18InstantiationErrora">InstantiationError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Thrown when a problem occurs while trying to create <code>MapMeasureDependentRenderSize</code>.</p>
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
