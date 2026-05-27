---
title: "Implementation"
slug: "sdk-for-flutter-explore-mapview-maplayerprioritybuilder-withcategory"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- withCategory.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/MapLayerPriorityBuilder-class.html">/sdk-for-flutter-explore-mapview-maplayerprioritybuilder-class</a></li>
<li class="self-crumb">withCategory abstract method</li>
</ol>
<div class="self-name">withCategory</div>
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
<div class="main-content" data-above-sidebar="mapview/MapLayerPriorityBuilder-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>withCategory abstract method</h1></div>
<section class="multi-line-signature">
<a href="../../mapview/MapLayerPriorityBuilder-class.html">/sdk-for-flutter-explore-mapview-maplayerprioritybuilder-class</a>
withCategory(<wbr/><ol class="parameter-list single-line"> <li>String category</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Sets the layer category for which a priority could be defined with the next call to the functions
<code>renderedFirst|Last|BeforeLayer|AfterLayer</code>.</p>
<p>After a priority is defined by calling one of the aforementioned functions, the current category
is cleared and the builder refers again to the layer itself.</p>
<ul>
<li><code>category</code> The name of the layer category.</li>
</ul>
<p>Returns <a href="../../mapview/MapLayerPriorityBuilder-class.html">/sdk-for-flutter-explore-mapview-maplayerprioritybuilder-class</a>. This class instance.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">MapLayerPriorityBuilder withCategory(String category);</code></pre>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li><a href="../../mapview/MapLayerPriorityBuilder-class.html">/sdk-for-flutter-explore-mapview-maplayerprioritybuilder-class</a></li>
<li class="self-crumb">withCategory abstract method</li>
</ol>
<h5>MapLayerPriorityBuilder class</h5>
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
