---
title: "Untitled"
slug: "sdk-for-ios-navigate-api-reference-classes-venuegeometry"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- VenueGeometry.html -->
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/VenueGeometry"></a>
<a title="VenueGeometry Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-venues">Venues</a>
<img alt="" id="carat" src="../img/carat.png"/>
        VenueGeometry Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>VenueGeometry</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">VenueGeometry</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">VenueGeometry</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">VenueGeometry</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Represents a geometry inside the <code><a href="sdk-for-ios-navigate-api-reference-..-classes-venuelevel">VenueLevel</a></code>. The geometry can be any object
inside the level, like a room, a wall or a table. Also the geometry can represent virtual
objects, like a team area in an open space.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13VenueGeometryC19StringToPropertyMapa"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/StringToPropertyMap"></a>
<a class="token" href="#/s:7heresdk13VenueGeometryC19StringToPropertyMapa">StringToPropertyMap</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Undocumented</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">StringToPropertyMap</span> <span class="o">=</span> <span class="p">[</span><span class="kt">String</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-property">Property</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13VenueGeometryC10identifierSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/identifier"></a>
<a class="token" href="#/s:7heresdk13VenueGeometryC10identifierSSvp">identifier</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The <code>id</code> of the geometry.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">identifier</span><span class="p">:</span> <span class="kt">String</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13VenueGeometryC5levelAA0B5LevelCvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/level"></a>
<a class="token" href="#/s:7heresdk13VenueGeometryC5levelAA0B5LevelCvp">level</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The parent level of the geometry.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">level</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-venuelevel">VenueLevel</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13VenueGeometryC12geometryTypeAC0cE0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/geometryType"></a>
<a class="token" href="#/s:7heresdk13VenueGeometryC12geometryTypeAC0cE0Ovp">geometryType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The type of the geometry.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">geometryType</span><span class="p">:</span> <span class="kt">VenueGeometry</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-venuegeometry-geometrytype">GeometryType</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13VenueGeometryC6centerAA14GeoCoordinatesVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/center"></a>
<a class="token" href="#/s:7heresdk13VenueGeometryC6centerAA14GeoCoordinatesVvp">center</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The geographic coordinates of the center of the geometry.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">center</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-geocoordinates">GeoCoordinates</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13VenueGeometryC11boundingBoxAA03GeoE0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/boundingBox"></a>
<a class="token" href="#/s:7heresdk13VenueGeometryC11boundingBoxAA03GeoE0Vvp">boundingBox</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The <code><a href="sdk-for-ios-navigate-api-reference-..-structs-geobox">GeoBox</a></code> of the bounding area of the geometry.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">boundingBox</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-geobox">GeoBox</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13VenueGeometryC10propertiesSDySSAA8PropertyCGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/properties"></a>
<a class="token" href="#/s:7heresdk13VenueGeometryC10propertiesSDySSAA8PropertyCGvp">properties</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The properties of the geometry.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">properties</span><span class="p">:</span> <span class="kt">VenueGeometry</span><span class="o">.</span><span class="kt"><a href="../Classes/VenueGeometry.html#/s:7heresdk13VenueGeometryC19StringToPropertyMapa">StringToPropertyMap</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13VenueGeometryC15internalAddressAC08InternalE0CSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/internalAddress"></a>
<a class="token" href="#/s:7heresdk13VenueGeometryC15internalAddressAC08InternalE0CSgvp">internalAddress</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The internal address of the geometry.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">internalAddress</span><span class="p">:</span> <span class="kt">VenueGeometry</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-venuegeometry-internaladdress">InternalAddress</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13VenueGeometryC4nameSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/name"></a>
<a class="token" href="#/s:7heresdk13VenueGeometryC4nameSSvp">name</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The name of the geometry.
If no name has been set, returns a label name.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">name</span><span class="p">:</span> <span class="kt">String</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13VenueGeometryC9labelNameSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/labelName"></a>
<a class="token" href="#/s:7heresdk13VenueGeometryC9labelNameSSvp">labelName</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The label name of the geometry.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">labelName</span><span class="p">:</span> <span class="kt">String</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13VenueGeometryC10lookupTypeAC06LookupE0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/lookupType"></a>
<a class="token" href="#/s:7heresdk13VenueGeometryC10lookupTypeAC06LookupE0Ovp">lookupType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The lookup type of the geometry.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">lookupType</span><span class="p">:</span> <span class="kt">VenueGeometry</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-venuegeometry-lookuptype">LookupType</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13VenueGeometryC06parentC0ACvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/parentGeometry"></a>
<a class="token" href="#/s:7heresdk13VenueGeometryC06parentC0ACvp">parentGeometry</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The parent geometry.
Defaults to <code>nil</code>, if the geometry represents a base shape.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">parentGeometry</span><span class="p">:</span> <span class="kt">VenueGeometry</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13VenueGeometryC5styleAA0bC5StyleCSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/style"></a>
<a class="token" href="#/s:7heresdk13VenueGeometryC5styleAA0bC5StyleCSgvp">style</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The style of the geometry.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">style</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-venuegeometrystyle">VenueGeometryStyle</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13VenueGeometryC10labelStyleAA0b5LabelE0CSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/labelStyle"></a>
<a class="token" href="#/s:7heresdk13VenueGeometryC10labelStyleAA0b5LabelE0CSgvp">labelStyle</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The label style of the geometry.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">labelStyle</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-venuelabelstyle">VenueLabelStyle</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13VenueGeometryC7levelIDSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/levelID"></a>
<a class="token" href="#/s:7heresdk13VenueGeometryC7levelIDSSvp">levelID</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The level ID of geometry.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">levelID</span><span class="p">:</span> <span class="kt">String</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13VenueGeometryC15InternalAddressC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/InternalAddress"></a>
<a class="token" href="#/s:7heresdk13VenueGeometryC15InternalAddressC">InternalAddress</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents an internal addresses of the geometry inside the venue. The internal
address can be a number of a seat in a stadium, or a name of a classroom in a university.
One internal address can be shared between few geometries. For example, if a store in
a shopping mall is located on few floors, few different geometries will represent it.
But each of them will have the same internal address.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-..-classes-venuegeometry-internaladdress">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">InternalAddress</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-venuegeometry">VenueGeometry</a></span><span class="o">.</span><span class="kt">InternalAddress</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-venuegeometry">VenueGeometry</a></span><span class="o">.</span><span class="kt">InternalAddress</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13VenueGeometryC0C4TypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/GeometryType"></a>
<a class="token" href="#/s:7heresdk13VenueGeometryC0C4TypeO">GeometryType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Geometry types.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-..-classes-venuegeometry-geometrytype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">GeometryType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13VenueGeometryC10LookupTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/LookupType"></a>
<a class="token" href="#/s:7heresdk13VenueGeometryC10LookupTypeO">LookupType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines how the geometry will be presented.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-..-classes-venuegeometry-lookuptype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">LookupType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
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
