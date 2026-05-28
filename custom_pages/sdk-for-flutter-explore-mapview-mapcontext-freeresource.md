---
title: "freeResource abstract method"
slug: "sdk-for-flutter-explore-mapview-mapcontext-freeresource"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- freeResource.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-mapcontext-class</li>
<li class="self-crumb">freeResource abstract method</li>
</ol>
<div class="self-name">freeResource</div>
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
<h1>freeResource abstract method</h1></div>
<section class="multi-line-signature">
void
freeResource(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-explore-mapview-mapcontextresourcetype type, </li>
<li>/sdk-for-flutter-explore-mapview-mapcontextfreeresourceseverity severity</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Frees a system resource held by the /sdk-for-flutter-explore-mapview-mapcontext-class and all entities attached to it, like /sdk-for-flutter-explore-mapview-heremapcontrollercore-class.</p>
<p>This function is intended for use when a system resource availability becomes low.
For example, some memory can be freed when the application transitions to the background state.</p>
<ul>
<li>
<p><code>type</code> Type of resource to be freed.</p>
</li>
<li>
<p><code>severity</code> Severity of the request.</p>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void freeResource(MapContextResourceType type, MapContextFreeResourceSeverity severity);</code></pre>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-mapcontext-class</li>
<li class="self-crumb">freeResource abstract method</li>
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
</div></div>
</div>
`
}</HTMLBlock>
