---
title: "Untitled"
slug: "sdk-for-flutter-navigate-mapview-mapcontext-setmemorymanagementoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setMemoryManagementOptions.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-mapcontext-class</li>
<li class="self-crumb">setMemoryManagementOptions abstract method</li>
</ol>
<div class="self-name">setMemoryManagementOptions</div>
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
<div class="main-content" data-above-sidebar="mapview/MapContext-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>setMemoryManagementOptions abstract method</h1></div>
<section class="multi-line-signature">
void
setMemoryManagementOptions(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-mapview-mapcontextmemorymanagementoptions-class memoryManagementOptions, </li>
<li>/sdk-for-flutter-navigate-mapview-mapcontextsetmemorymanagementoptionscallback? callback</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Sets memory management options for controlling tile cache and video memory usage.</p>
<p>In /sdk-for-flutter-navigate-mapview-mapcontextmemorymanagementoptions-class optional parameters with <code>null</code>
or non positive values will be ignored, preserving their existing settings.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<ul>
<li>
<p><code>memoryManagementOptions</code> The memory management options to set.</p>
</li>
<li>
<p><code>callback</code> Optional callback used upon
completion to pass the return value to the caller.
The callback is called from an arbitrary thread.</p>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void setMemoryManagementOptions(MapContextMemoryManagementOptions memoryManagementOptions, MapContextSetMemoryManagementOptionsCallback? callback);</code></pre>
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
<li>/sdk-for-flutter-navigate-mapview-mapcontext-class</li>
<li class="self-crumb">setMemoryManagementOptions abstract method</li>
</ol>
<h5>MapContext class</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>



</div>
`
}</HTMLBlock>
