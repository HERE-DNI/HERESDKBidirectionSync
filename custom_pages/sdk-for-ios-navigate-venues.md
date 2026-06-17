---
title: "Venues"
slug: "sdk-for-ios-navigate-venues"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Section/Venues"></a>
<a title="Venues  Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-index">heresdk</a>

        Venues  Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>Venues</h1>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9CrosswalkC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/Crosswalk"></a>
<a class="token" href="#/s:7heresdk9CrosswalkC">Crosswalk</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents crosswalk’s inside the <code><a href="sdk-for-ios-navigate-classes-venuelevel">VenueLevel</a></code>. A crosswalk is an area of the road surface
where pedestrians are expected to walk across the road. The area is represented as a polygon, which is often,
but not necessarily, rectangular and oriented with the shorter dimension in the vehicle’s direction of travel.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-classes-crosswalk">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">Crosswalk</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Crosswalk</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Crosswalk</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8PropertyC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/Property"></a>
<a class="token" href="#/s:7heresdk8PropertyC">Property</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Holds information of varying types, such as Boolean, Integer, String. Properties are used
in <code><a href="sdk-for-ios-navigate-classes-venuemodel">VenueModel</a></code> <code><a href="sdk-for-ios-navigate-classes-venuedrawing">VenueDrawing</a></code>, <code><a href="sdk-for-ios-navigate-classes-venuelevel">VenueLevel</a></code>
and <code><a href="sdk-for-ios-navigate-classes-venuegeometry">VenueGeometry</a></code> to describe this objects.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-classes-property">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">Property</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Property</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Property</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk5VenueC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/Venue"></a>
<a class="token" href="#/s:7heresdk5VenueC">Venue</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Controls the <code><a href="sdk-for-ios-navigate-classes-venuemodel">VenueModel</a></code> inside the <code><a href="sdk-for-ios-navigate-classes-venuemap">VenueMap</a></code> object.
The venue controls the selection of the <code><a href="sdk-for-ios-navigate-classes-venuedrawing">VenueDrawing</a></code> and the <code><a href="sdk-for-ios-navigate-classes-venuelevel">VenueLevel</a></code>
of the <code><a href="sdk-for-ios-navigate-classes-venuemodel">VenueModel</a></code>. It provides the possibility to customize styles for the <code><a href="sdk-for-ios-navigate-classes-venuegeometry">VenueGeometry</a></code>.
Objects of this class can only be created using methods
<code>VenueMap.addVenueAsync(String, VenueLoadErrorHandler)</code> and <code>VenueMap.selectVenueAsync(String, VenueLoadErrorHandler)</code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-classes-venue">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">Venue</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Venue</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Venue</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13VenueDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/VenueDelegate"></a>
<a class="token" href="#/s:7heresdk13VenueDelegateP">VenueDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The protocol for delegates for
venue loading events in <code><a href="sdk-for-ios-navigate-classes-venueservice">VenueService</a></code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-protocols-venuedelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">VenueDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12VenueDrawingC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/VenueDrawing"></a>
<a class="token" href="#/s:7heresdk12VenueDrawingC">VenueDrawing</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents a drawing inside the <code><a href="sdk-for-ios-navigate-classes-venuemodel">VenueModel</a></code>. The drawing can be
a separate building in a complex of buildings, or show a different
view of a venue. For example, in an airport, one drawing can be used
as an overview of all buildings in this venue, while other drawings
contains details for each terminal in this airport.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-classes-venuedrawing">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">VenueDrawing</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">VenueDrawing</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">VenueDrawing</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk29VenueDrawingSelectionDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/VenueDrawingSelectionDelegate"></a>
<a class="token" href="#/s:7heresdk29VenueDrawingSelectionDelegateP">VenueDrawingSelectionDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The protocol for delegates for
the <code><a href="sdk-for-ios-navigate-classes-venuedrawing">VenueDrawing</a></code> selection event. Use the <code><a href="sdk-for-ios-navigate-classes-venuemap">VenueMap</a></code>
to add and remove the <code>VenueDrawingSelectionDelegate</code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-protocols-venuedrawingselectiondelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">VenueDrawingSelectionDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11VenueEngineC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/VenueEngine"></a>
<a class="token" href="#/s:7heresdk11VenueEngineC">VenueEngine</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>VenueEngine is an add-on to the base map functionality with its
own content loading and cache.
VenueEngine gives access to the venue functionality, which allows you
to load and visualize venues on the map, search content inside venues etc.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-classes-venueengine">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">VenueEngine</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">VenueEngine</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">VenueEngine</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk32VenueEngineInitCompletionHandlera"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/VenueEngineInitCompletionHandler"></a>
<a class="token" href="#/s:7heresdk32VenueEngineInitCompletionHandlera">VenueEngineInitCompletionHandler</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This method will be called on the main thread when VenueEngine initialization is completed.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">VenueEngineInitCompletionHandler</span> <span class="o">=</span> <span class="p">()</span> <span class="o">-&gt;</span> <span class="kt">Void</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10VenueErrora"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/VenueError"></a>
<a class="token" href="#/s:7heresdk10VenueErrora">VenueError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies possible errors that may occur during loading of indoor maps</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">VenueError</span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-navigate-enums-venueerrorcode">VenueErrorCode</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14VenueErrorCodeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/VenueErrorCode"></a>
<a class="token" href="#/s:7heresdk14VenueErrorCodeO">VenueErrorCode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies possible errors that may occur during loading of indoor maps</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-enums-venueerrorcode">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">VenueErrorCode</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">VenueErrorCode</span> <span class="p">:</span> <span class="kt">Error</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13VenueGeometryC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/VenueGeometry"></a>
<a class="token" href="#/s:7heresdk13VenueGeometryC">VenueGeometry</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents a geometry inside the <code><a href="sdk-for-ios-navigate-classes-venuelevel">VenueLevel</a></code>. The geometry can be any object
inside the level, like a room, a wall or a table. Also the geometry can represent virtual
objects, like a team area in an open space.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-classes-venuegeometry">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">VenueGeometry</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">VenueGeometry</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">VenueGeometry</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23VenueGeometryFilterTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/VenueGeometryFilterType"></a>
<a class="token" href="#/s:7heresdk23VenueGeometryFilterTypeO">VenueGeometryFilterType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Filter types for the <code><a href="sdk-for-ios-navigate-classes-venuegeometry">VenueGeometry</a></code> search.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-enums-venuegeometryfiltertype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">VenueGeometryFilterType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18VenueGeometryStyleC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/VenueGeometryStyle"></a>
<a class="token" href="#/s:7heresdk18VenueGeometryStyleC">VenueGeometryStyle</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents a style of the <code><a href="sdk-for-ios-navigate-classes-venuegeometry">VenueGeometry</a></code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-classes-venuegeometrystyle">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">VenueGeometryStyle</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">VenueGeometryStyle</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">VenueGeometryStyle</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9VenueInfoC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/VenueInfo"></a>
<a class="token" href="#/s:7heresdk9VenueInfoC">VenueInfo</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents the venue info existing in a catalogs contains id and name.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-classes-venueinfo">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">VenueInfo</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">VenueInfo</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">VenueInfo</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17VenueInfoDataLista"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/VenueInfoDataList"></a>
<a class="token" href="#/s:7heresdk17VenueInfoDataLista">VenueInfoDataList</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">VenueInfoDataList</span> <span class="o">=</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-classes-venueinfo">VenueInfo</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk29VenueInfoListListenerDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/VenueInfoListListenerDelegate"></a>
<a class="token" href="#/s:7heresdk29VenueInfoListListenerDelegateP">VenueInfoListListenerDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The protocol for delegates for
the list of <code><a href="sdk-for-ios-navigate-classes-venueinfo">VenueInfo</a></code> load event. Use <code><a href="sdk-for-ios-navigate-classes-venuemap">VenueMap</a></code>
to add and remove the <code>VenueInfoListListenerDelegate</code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-protocols-venueinfolistlistenerdelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">VenueInfoListListenerDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15VenueLabelStyleC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/VenueLabelStyle"></a>
<a class="token" href="#/s:7heresdk15VenueLabelStyleC">VenueLabelStyle</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents a style of the label.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-classes-venuelabelstyle">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">VenueLabelStyle</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">VenueLabelStyle</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">VenueLabelStyle</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10VenueLevelC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/VenueLevel"></a>
<a class="token" href="#/s:7heresdk10VenueLevelC">VenueLevel</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents one level of a building or a complex of buildings inside the <code><a href="sdk-for-ios-navigate-classes-venuedrawing">VenueDrawing</a></code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-classes-venuelevel">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">VenueLevel</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">VenueLevel</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">VenueLevel</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27VenueLevelSelectionDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/VenueLevelSelectionDelegate"></a>
<a class="token" href="#/s:7heresdk27VenueLevelSelectionDelegateP">VenueLevelSelectionDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The protocol for delegates for
the <code><a href="sdk-for-ios-navigate-classes-venuelevel">VenueLevel</a></code> selection event. Use the <code><a href="sdk-for-ios-navigate-classes-venuemap">VenueMap</a></code>
to add and remove the <code>VenueLevelSelectionDelegate</code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-protocols-venuelevelselectiondelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">VenueLevelSelectionDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22VenueLifecycleDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/VenueLifecycleDelegate"></a>
<a class="token" href="#/s:7heresdk22VenueLifecycleDelegateP">VenueLifecycleDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The protocol for delegates for
the <code><a href="sdk-for-ios-navigate-classes-venue">Venue</a></code> lifecycle events. Use the <code><a href="sdk-for-ios-navigate-classes-venuemap">VenueMap</a></code>
to add and remove the <code>VenueLifecycleDelegate</code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-protocols-venuelifecycledelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">VenueLifecycleDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21VenueLoadErrorHandlera"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/VenueLoadErrorHandler"></a>
<a class="token" href="#/s:7heresdk21VenueLoadErrorHandlera">VenueLoadErrorHandler</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A method which is called on the main thread when <code>VenueMap.selectVenueAsync(String, VenueLoadErrorHandler)</code> has been completed.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">VenueLoadErrorHandler</span> <span class="o">=</span> <span class="p">(</span><span class="n">_</span> <span class="nv">error</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-enums-venueerrorcode">VenueErrorCode</a></span><span class="p">?)</span> <span class="o">-&gt;</span> <span class="kt">Void</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>error</em>
</code>
</td>
<td>
<div>
<p>Represents an error in case of a failure. It is <code>nil</code> for an operation that succeeds.</p>
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
<a name="/s:7heresdk8VenueMapC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/VenueMap"></a>
<a class="token" href="#/s:7heresdk8VenueMapC">VenueMap</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Connects a map with venues. When the <code>VenueMap</code> is started,
venues can be seen on the map as interactive models. The user can switch drawings and levels,
change a visual style of geometries and related labels inside the venue etc.
After constructing the <code>VenueMap</code>, delegates
for relevant events should be added to the object. <code>VenueMap</code> is an add-on to
the base map functionality with its own content loading and cache. For this reason, in certain
situations there may be a small delay before the venue is visible.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-classes-venuemap">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">VenueMap</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">VenueMap</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">VenueMap</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16VenueMapDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/VenueMapDelegate"></a>
<a class="token" href="#/s:7heresdk16VenueMapDelegateP">VenueMapDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The protocol for delegates for
venue loading events in <code><a href="sdk-for-ios-navigate-classes-venueservice">VenueService</a></code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-protocols-venuemapdelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">VenueMapDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25VenueMapLifecycleDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/VenueMapLifecycleDelegate"></a>
<a class="token" href="#/s:7heresdk25VenueMapLifecycleDelegateP">VenueMapLifecycleDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The protocol for delegates for
the <code><a href="sdk-for-ios-navigate-classes-venue">Venue</a></code> lifecycle events. Use the <code><a href="sdk-for-ios-navigate-classes-venuemap">VenueMap</a></code>
to add and remove the <code>VenueMapLifecycleDelegate</code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-protocols-venuemaplifecycledelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">VenueMapLifecycleDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10VenueModelC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/VenueModel"></a>
<a class="token" href="#/s:7heresdk10VenueModelC">VenueModel</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents a building or a complex of buildings, like airports or universities.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-classes-venuemodel">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">VenueModel</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">VenueModel</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">VenueModel</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22VenueSelectionDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/VenueSelectionDelegate"></a>
<a class="token" href="#/s:7heresdk22VenueSelectionDelegateP">VenueSelectionDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The protocol for delegates for
the <code><a href="sdk-for-ios-navigate-classes-venue">Venue</a></code> selection event. Use the <code><a href="sdk-for-ios-navigate-classes-venuemap">VenueMap</a></code>
to add and remove the <code>VenueSelectionDelegate</code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-protocols-venueselectiondelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">VenueSelectionDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12VenueServiceC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/VenueService"></a>
<a class="token" href="#/s:7heresdk12VenueServiceC">VenueService</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Offers methods to download venues. Use of this
object does not necessitate Map involvement.</p>
<p>
Before loading the venues, initialize the venue service
with one of the start methods.
</p>
<p>
The venue service is online only. Even if there is a cached
venue on the device, the venue service requires an online
connection to check if the venue is available for the user.
</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-classes-venueservice">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">VenueService</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">VenueService</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">VenueService</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VenueServiceDelegateP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/VenueServiceDelegate"></a>
<a class="token" href="#/s:7heresdk20VenueServiceDelegateP">VenueServiceDelegate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The protocol for delegates for
lifecycle events in <code><a href="sdk-for-ios-navigate-classes-venueservice">VenueService</a></code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-protocols-venueservicedelegate">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">VenueServiceDelegate</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22VenueServiceInitStatusO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/VenueServiceInitStatus"></a>
<a class="token" href="#/s:7heresdk22VenueServiceInitStatusO">VenueServiceInitStatus</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Initialization status types of the <code><a href="sdk-for-ios-navigate-classes-venueservice">VenueService</a></code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-enums-venueserviceinitstatus">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">VenueServiceInitStatus</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10VenueStyleC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/VenueStyle"></a>
<a class="token" href="#/s:7heresdk10VenueStyleC">VenueStyle</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents a style of the venue. Contains the information about the geometry and label styles
available for the venue.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-classes-venuestyle">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">VenueStyle</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">VenueStyle</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">VenueStyle</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13VenueTopologyC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/VenueTopology"></a>
<a class="token" href="#/s:7heresdk13VenueTopologyC">VenueTopology</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents routing topologies inside the <code><a href="sdk-for-ios-navigate-classes-venuelevel">VenueLevel</a></code>. The topologies can be paths
used for enabling routing services.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-classes-venuetopology">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">VenueTopology</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">VenueTopology</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">VenueTopology</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18VenueTransportModeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/VenueTransportMode"></a>
<a class="token" href="#/s:7heresdk18VenueTransportModeO">VenueTransportMode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Available mode of transport on indoor topology.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-enums-venuetransportmode">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">VenueTransportMode</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
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
