---
title: "MapContext class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapcontext-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapContext-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapContext-class-sidebar.html">

<div>

# <span class="kind-class">MapContext</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

MapContext is the rendering engine and the context in which virtual geographic maps get rendered.

It runs the render loop or offers the means for the user to run a custom one.

Data sources, assets and virtual maps can be attached to the context. A virtual map can only render data from sources attached to the same context.

The graphics backend to be used by the engine can be choosen by the user or a platform suitable one can be automatically selected internally. Only one graphics backend can be active and once selected it cannot be changed.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcontext-mapcontext">MapContext</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcontext-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcontext-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcontext-freeresource">freeResource</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-freeResource-param-type" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapcontextresourcetype">MapContextResourceType</a></span> <span class="parameter-name">type</span>, </span><span id="sdk-for-flutter-navigate-freeResource-param-severity" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapcontextfreeresourceseverity">MapContextFreeResourceSeverity</a></span> <span class="parameter-name">severity</span></span>) <span class="returntype parameter">→ void</span> </span>  
Frees a system resource held by the <a href="sdk-for-flutter-navigate-mapview-mapcontext-class">MapContext</a> and all entities attached to it, like <a href="sdk-for-flutter-navigate-mapview-heremapcontrollercore-class">HereMapControllerCore</a>.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcontext-getmemorymanagementoptions">getMemoryManagementOptions</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-mapview-mapcontextmemorymanagementoptions-class">MapContextMemoryManagementOptions</a></span> </span>  
Returns <a href="sdk-for-flutter-navigate-mapview-mapcontextmemorymanagementoptions-class">MapContextMemoryManagementOptions</a>. Gets the current memory management options. Returns the actual applied memory limits. If the underlying system limits exceed int32_t max value (2,147,483,647 KiB or ~2 TiB), the returned value is clamped to int32_t max.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcontext-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcontext-setmemorymanagementoptions">setMemoryManagementOptions</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setMemoryManagementOptions-param-memoryManagementOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapcontextmemorymanagementoptions-class">MapContextMemoryManagementOptions</a></span> <span class="parameter-name">memoryManagementOptions</span>, </span><span id="sdk-for-flutter-navigate-setMemoryManagementOptions-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapcontextsetmemorymanagementoptionscallback">MapContextSetMemoryManagementOptionsCallback</a>?</span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ void</span> </span>  
Sets memory management options for controlling tile cache and video memory usage.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcontext-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcontext-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
