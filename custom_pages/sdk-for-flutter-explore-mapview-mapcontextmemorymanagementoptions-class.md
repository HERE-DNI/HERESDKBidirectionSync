---
title: "Constructors"
slug: "sdk-for-flutter-explore-mapview-mapcontextmemorymanagementoptions-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- MapContextMemoryManagementOptions-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview/MapContextMemoryManagementOptions-class.html#constructors">Constructors</a></li>
<li><a href="mapview/MapContextMemoryManagementOptions/MapContextMemoryManagementOptions.html">MapContextMemoryManagementOptions</a></li>
<li class="section-title">
<a href="mapview/MapContextMemoryManagementOptions-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="mapview/MapContextMemoryManagementOptions/hashCode.html">hashCode</a></li>
<li><a href="mapview/MapContextMemoryManagementOptions/memoryManagementStrategy.html">memoryManagementStrategy</a></li>
<li class="inherited"><a href="mapview/MapContextMemoryManagementOptions/runtimeType.html">runtimeType</a></li>
<li><a href="mapview/MapContextMemoryManagementOptions/tileCacheMemoryLimitInKiB.html">tileCacheMemoryLimitInKiB</a></li>
<li><a href="mapview/MapContextMemoryManagementOptions/videoMemoryLimitInKiB.html">videoMemoryLimitInKiB</a></li>
<li class="section-title inherited"><a href="mapview/MapContextMemoryManagementOptions-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="mapview/MapContextMemoryManagementOptions/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="mapview/MapContextMemoryManagementOptions/toString.html">toString</a></li>
<li class="section-title inherited"><a href="mapview/MapContextMemoryManagementOptions-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapview/MapContextMemoryManagementOptions/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li class="self-crumb">MapContextMemoryManagementOptions class</li>
</ol>
<div class="self-name">MapContextMemoryManagementOptions</div>
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
<div class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapContextMemoryManagementOptions-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>MapContextMemoryManagementOptions class</h1></div>
<section class="desc markdown">
<p>Memory management options.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="MapContextMemoryManagementOptions">
<a href="../mapview/MapContextMemoryManagementOptions/MapContextMemoryManagementOptions.html">/sdk-for-flutter-explore-mapview-mapcontextmemorymanagementoptions-mapcontextmemorymanagementoptions</a>()
</dt>
<dd>
          Creates a new instance.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
<a href="../mapview/MapContextMemoryManagementOptions/hashCode.html">/sdk-for-flutter-explore-mapview-mapcontextmemorymanagementoptions-hashcode</a>
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="memoryManagementStrategy">
<a href="../mapview/MapContextMemoryManagementOptions/memoryManagementStrategy.html">/sdk-for-flutter-explore-mapview-mapcontextmemorymanagementoptions-memorymanagementstrategy</a>
↔ <a href="../mapview/MapContextMemoryManagementStrategy.html">/sdk-for-flutter-explore-mapview-mapcontextmemorymanagementstrategy</a>
</dt>
<dd>
  The default setting MemoryManagementStrategy.DYNAMIC is suitable for common cases. The map
data cache can adjust dynamically to fit visible data. When the visible data needs extra
memory, it would increase. When it's not needed, it will reduce to a limit which is
calculated internally or by using <a href="../mapview/MapContextMemoryManagementOptions/tileCacheMemoryLimitInKiB.html">/sdk-for-flutter-explore-mapview-mapcontextmemorymanagementoptions-tilecachememorylimitinkib</a> option.
The MemoryManagementStrategy.FIXED would be only useful when there is very
strict memory consumption requirement for the application. It potentially can have
flickering visual artifacts when the map data to be visualized is very large and exceeds
the cache limit.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../mapview/MapContextMemoryManagementOptions/runtimeType.html">/sdk-for-flutter-explore-mapview-mapcontextmemorymanagementoptions-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="tileCacheMemoryLimitInKiB">
<a href="../mapview/MapContextMemoryManagementOptions/tileCacheMemoryLimitInKiB.html">/sdk-for-flutter-explore-mapview-mapcontextmemorymanagementoptions-tilecachememorylimitinkib</a>
↔ int?
</dt>
<dd>
  Tile cache memory limit in kibibytes. Non positive or <code>null</code> values are ignored.
Default value is <code>null</code>.
Low tile cache limit will lead to eviction of tiles only if MemoryManagementStrategy is set to FIXED.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="videoMemoryLimitInKiB">
<a href="../mapview/MapContextMemoryManagementOptions/videoMemoryLimitInKiB.html">/sdk-for-flutter-explore-mapview-mapcontextmemorymanagementoptions-videomemorylimitinkib</a>
↔ int?
</dt>
<dd>
  Target video memory limit in kibibytes. Non positive or <code>null</code> values are ignored.
Default value is <code>null</code>.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
<a href="../mapview/MapContextMemoryManagementOptions/noSuchMethod.html">/sdk-for-flutter-explore-mapview-mapcontextmemorymanagementoptions-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../mapview/MapContextMemoryManagementOptions/toString.html">/sdk-for-flutter-explore-mapview-mapcontextmemorymanagementoptions-tostring</a>(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable inherited" id="operator ==">
<a href="../mapview/MapContextMemoryManagementOptions/operator_equals.html">/sdk-for-flutter-explore-mapview-mapcontextmemorymanagementoptions-operator-equals</a>(<wbr/>Object other)
    → bool

</dt>
<dd class="inherited">
  The equality operator.
  <div class="features">inherited</div>
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
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li class="self-crumb">MapContextMemoryManagementOptions class</li>
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
</HTMLBlock>
