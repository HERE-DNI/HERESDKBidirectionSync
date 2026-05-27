---
title: "getMemoryManagementOptions abstract method"
slug: "sdk-for-flutter-explore-mapview-mapcontext-getmemorymanagementoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getMemoryManagementOptions.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-mapcontext-class</li>
<li class="self-crumb">getMemoryManagementOptions abstract method</li>
</ol>
<div class="self-name">getMemoryManagementOptions</div>
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
<h1>getMemoryManagementOptions abstract method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-explore-mapview-mapcontextmemorymanagementoptions-class
getMemoryManagementOptions(<wbr/>)

      

    </section>
<section class="desc markdown">
<p>Returns /sdk-for-flutter-explore-mapview-mapcontextmemorymanagementoptions-class. Gets the current memory management options.
Returns the actual applied memory limits. If the underlying system limits exceed
<code>int32_t</code> max value (2,147,483,647 KiB or ~2 TiB), the returned value is clamped to <code>int32_t</code> max.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">MapContextMemoryManagementOptions getMemoryManagementOptions();</code></pre>
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
<li class="self-crumb">getMemoryManagementOptions abstract method</li>
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
