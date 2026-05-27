---
title: "Implementation"
slug: "sdk-for-flutter-explore-core-custommetadatavalue-custommetadatavalue"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- CustomMetadataValue.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../core/core-library.html">/sdk-for-flutter-explore-core-core-library</a></li>
<li><a href="../../core/CustomMetadataValue-class.html">/sdk-for-flutter-explore-core-custommetadatavalue-class</a></li>
<li class="self-crumb">CustomMetadataValue factory constructor</li>
</ol>
<div class="self-name">CustomMetadataValue</div>
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
<div class="main-content" data-above-sidebar="core/CustomMetadataValue-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>CustomMetadataValue constructor</h1></div>
<section class="multi-line-signature">
CustomMetadataValue(<wbr/><ol class="parameter-list single-line"> <li>String getTagLambda()</li>
</ol>)
    </section>
<section class="desc markdown">
<p>Abstract class for storing arbitrary metadata types.</p>
<p>By implementing this abstract class, multiple object types can be stored as
desired, simply by adding fields to the implementation that refer to those
objects and then assigning an instance of the CustomMetadataValue derived class
to a map item.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory CustomMetadataValue(
  String Function() getTagLambda,

) =&gt; CustomMetadataValue$Lambdas(
  getTagLambda,

);</code></pre>
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
<li><a href="../../core/core-library.html">/sdk-for-flutter-explore-core-core-library</a></li>
<li><a href="../../core/CustomMetadataValue-class.html">/sdk-for-flutter-explore-core-custommetadatavalue-class</a></li>
<li class="self-crumb">CustomMetadataValue factory constructor</li>
</ol>
<h5>CustomMetadataValue class</h5>
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
