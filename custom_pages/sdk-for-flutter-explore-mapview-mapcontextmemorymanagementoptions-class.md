---
title: "MapContextMemoryManagementOptions class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapcontextmemorymanagementoptions-class"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapContextMemoryManagementOptions-class-sidebar.html">

<div>

# <span class="kind-class">MapContextMemoryManagementOptions</span> class

</div>

<div class="section desc markdown">

Memory management options.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcontextmemorymanagementoptions-mapcontextmemorymanagementoptions">MapContextMemoryManagementOptions</a></span><span class="signature">()</span>  
Creates a new instance.

## Properties

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcontextmemorymanagementoptions-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcontextmemorymanagementoptions-memorymanagementstrategy">memoryManagementStrategy</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-mapview-mapcontextmemorymanagementstrategy">MapContextMemoryManagementStrategy</a></span>  
The default setting MemoryManagementStrategy.DYNAMIC is suitable for common cases. The map data cache can adjust dynamically to fit visible data. When the visible data needs extra memory, it would increase. When it's not needed, it will reduce to a limit which is calculated internally or by using <a href="sdk-for-flutter-explore-mapview-mapcontextmemorymanagementoptions-tilecachememorylimitinkib">MapContextMemoryManagementOptions.tileCacheMemoryLimitInKiB</a> option. The MemoryManagementStrategy.FIXED would be only useful when there is very strict memory consumption requirement for the application. It potentially can have flickering visual artifacts when the map data to be visualized is very large and exceeds the cache limit.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcontextmemorymanagementoptions-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcontextmemorymanagementoptions-tilecachememorylimitinkib">tileCacheMemoryLimitInKiB</a></span> <span class="signature">↔ int?</span>  
Tile cache memory limit in kibibytes. Non positive or `null` values are ignored. Default value is `null`. Low tile cache limit will lead to eviction of tiles only if MemoryManagementStrategy is set to FIXED.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcontextmemorymanagementoptions-videomemorylimitinkib">videoMemoryLimitInKiB</a></span> <span class="signature">↔ int?</span>  
Target video memory limit in kibibytes. Non positive or `null` values are ignored. Default value is `null`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcontextmemorymanagementoptions-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcontextmemorymanagementoptions-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcontextmemorymanagementoptions-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

