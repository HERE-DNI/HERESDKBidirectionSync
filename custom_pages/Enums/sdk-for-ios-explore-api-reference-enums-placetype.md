---
title: "PlaceType Enumeration Reference"
slug: "sdk-for-ios-explore-api-reference-enums-placetype"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- PlaceType.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Enum/PlaceType"></a>
<a title="PlaceType Enumeration Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="../index.html">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="../index.html">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="../Search.html">Search</a>
<img alt="" id="carat" src="../img/carat.png"/>
        PlaceType Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public enum PlaceType : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
<p>Specifies place type of Place result from a search query.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9PlaceTypeO3poiyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/poi"></a>
<a class="token" href="#/s:7heresdk9PlaceTypeO3poiyA2CmF">poi</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Point of interest, for example a shop, restaurant, museum.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case poi</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9PlaceTypeO7addressyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/address"></a>
<a class="token" href="#/s:7heresdk9PlaceTypeO7addressyA2CmF">address</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Address of a place. It can have different formats based on the addressing system.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case address</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9PlaceTypeO4areayA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/area"></a>
<a class="token" href="#/s:7heresdk9PlaceTypeO4areayA2CmF">area</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Geographical area, for example a country, a city or a district.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case area</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9PlaceTypeO6streetyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/street"></a>
<a class="token" href="#/s:7heresdk9PlaceTypeO6streetyA2CmF">street</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A street.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case street</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9PlaceTypeO12intersectionyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/intersection"></a>
<a class="token" href="#/s:7heresdk9PlaceTypeO12intersectionyA2CmF">intersection</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>An intersection of two, or more, streets.
Note: This type is not supported in offline search.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case intersection</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9PlaceTypeO7unknownyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/unknown"></a>
<a class="token" href="#/s:7heresdk9PlaceTypeO7unknownyA2CmF">unknown</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Unknown or missing place type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case unknown</code></pre>
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
