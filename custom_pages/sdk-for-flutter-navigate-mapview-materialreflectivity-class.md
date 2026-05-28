---
title: "MaterialReflectivity class"
slug: "sdk-for-flutter-navigate-mapview-materialreflectivity-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MaterialReflectivity-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview/MaterialReflectivity-class.html#constructors">Constructors</a></li>
<li><a href="mapview/MaterialReflectivity/MaterialReflectivity.html">MaterialReflectivity</a></li>
<li class="section-title">
<a href="mapview/MaterialReflectivity-class.html#instance-properties">Properties</a>
</li>
<li><a href="mapview/MaterialReflectivity/ambientFactor.html">ambientFactor</a></li>
<li><a href="mapview/MaterialReflectivity/diffuseFactor.html">diffuseFactor</a></li>
<li><a href="mapview/MaterialReflectivity/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="mapview/MaterialReflectivity/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="mapview/MaterialReflectivity-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="mapview/MaterialReflectivity/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="mapview/MaterialReflectivity/toString.html">toString</a></li>
<li class="section-title"><a href="mapview/MaterialReflectivity-class.html#operators">Operators</a></li>
<li><a href="mapview/MaterialReflectivity/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li class="self-crumb">MaterialReflectivity class</li>
</ol>
<div class="self-name">MaterialReflectivity</div>
<form class="search navbar-right" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-box" placeholder="Loading search..." type="text"/>
</form>
<div class="toggle" id="theme-button" title="Toggle brightness">
<label for="theme">
<input id="theme" type="checkbox" value="light-theme"/>

        dark_mode
      

        light_mode
      
</label>
</div>
</header>
<main>
<div class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MaterialReflectivity-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>MaterialReflectivity class</h1></div>
<section class="desc markdown">
<p>Material reflectivity properties are used to enable per‑pixel lighting for supported map objects
(e.g.</p>
<p><code>LocationIndicator</code> markers and their halo).</p>
<h2 id="lighting-off-vs-on">Lighting OFF vs ON</h2>
<p>By default (when no MaterialReflectivity is assigned) objects are rendered "unlit" (emissive):
their texture / color appears at a constant brightness, unaffected by scene lights. Assigning a
<code>MaterialReflectivity</code> instance to an object that supports it (e.g. <code>LocationIndicator.materialReflectivity</code>)
automatically enables lighting for this object and all its internal components. Clearing (setting the property to
<code>null</code>) disables lighting again and restores the unlit appearance.</p>
<h2 id="factors">Factors</h2>
<p>Both factors are expected to be within [0.0, 1.0]. Values outside this range are allowed but may
produce exaggerated results or be clamped by future implementations. Typical useful ranges:</p>
<ul>
<li>ambientFactor: 0.0 – 0.4 (higher values flatten the shading and reduce directional contrast)</li>
<li>diffuseFactor: 0.5 – 1.0 (lower values dim the object under directional light)</li>
</ul>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="MaterialReflectivity">
/sdk-for-flutter-navigate-mapview-materialreflectivity-materialreflectivity()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="ambientFactor">
/sdk-for-flutter-navigate-mapview-materialreflectivity-ambientfactor
↔ double
</dt>
<dd>
  The ambient factor controls how much of the object's base color is treated as
constant ambient contribution (independent of light direction) when lighting is enabled. Default value is 0.0.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="diffuseFactor">
/sdk-for-flutter-navigate-mapview-materialreflectivity-diffusefactor
↔ double
</dt>
<dd>
  The diffuse factor controls how much of the object's color contributes to
the diffuse lighting component when lighting is enabled. Default value is 1.0.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-mapview-materialreflectivity-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-mapview-materialreflectivity-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-mapview-materialreflectivity-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-mapview-materialreflectivity-tostring(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable" id="operator ==">
/sdk-for-flutter-navigate-mapview-materialreflectivity-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd>
  The equality operator.
  

</dd>
</dl>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li class="self-crumb">MaterialReflectivity class</li>
</ol>
<h5>mapview library</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>
</div></div>
</div>
`
}</HTMLBlock>
