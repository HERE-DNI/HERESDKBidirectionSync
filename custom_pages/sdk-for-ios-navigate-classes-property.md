---
title: "Property"
slug: "sdk-for-ios-navigate-classes-property"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/Property"></a>
<a title="Property Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-index">heresdk</a>

<a href="sdk-for-ios-navigate-venues">Venues</a>

        Property Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>Property</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">Property</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Property</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Property</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Holds information of varying types, such as Boolean, Integer, String. Properties are used
in <code><a href="sdk-for-ios-navigate-classes-venuemodel">VenueModel</a></code> <code><a href="sdk-for-ios-navigate-classes-venuedrawing">VenueDrawing</a></code>, <code><a href="sdk-for-ios-navigate-classes-venuelevel">VenueLevel</a></code>
and <code><a href="sdk-for-ios-navigate-classes-venuegeometry">VenueGeometry</a></code> to describe this objects.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8PropertyC4typeAC0B4TypeOvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/type"></a>
<a class="token" href="#/s:7heresdk8PropertyC4typeAC0B4TypeOvp">type</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The type of the property.
It can be used to get type of property.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">type</span><span class="p">:</span> <span class="kt">Property</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-classes-property-propertytype">PropertyType</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8PropertyC6isBoolSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isBool"></a>
<a class="token" href="#/s:7heresdk8PropertyC6isBoolSbvp">isBool</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The Boolean value.
Converts the value of the property to a boolean.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isBool</span><span class="p">:</span> <span class="kt">Bool</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8PropertyC3ints5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/int"></a>
<a class="token" href="#/s:7heresdk8PropertyC3ints5Int32Vvp">int</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The Integer value.
Converts the value of the property to a Integer.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">int</span><span class="p">:</span> <span class="kt">Int32</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8PropertyC6stringSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/string"></a>
<a class="token" href="#/s:7heresdk8PropertyC6stringSSvp">string</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The String value.
Converts the value of the property to a boolean.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">string</span><span class="p">:</span> <span class="kt">String</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8PropertyC0B4TypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/PropertyType"></a>
<a class="token" href="#/s:7heresdk8PropertyC0B4TypeO">PropertyType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Types of properties.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-classes-property-propertytype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">PropertyType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
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
