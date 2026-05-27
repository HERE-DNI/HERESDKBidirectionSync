---
title: "Implementation"
slug: "sdk-for-flutter-explore-search-placecategory-placecategory"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- PlaceCategory.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../search/search-library.html">/sdk-for-flutter-explore-search-search-library</a></li>
<li><a href="../../search/PlaceCategory-class.html">/sdk-for-flutter-explore-search-placecategory-class</a></li>
<li class="self-crumb">PlaceCategory factory constructor</li>
</ol>
<div class="self-name">PlaceCategory</div>
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
<div class="main-content" data-above-sidebar="search/PlaceCategory-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>PlaceCategory constructor</h1></div>
<section class="multi-line-signature">
PlaceCategory(<wbr/><ol class="parameter-list single-line"> <li>String id</li>
</ol>)
    </section>
<section class="desc markdown">
<p>Creates a new instance of this class.</p>
<ul>
<li><code>id</code> Place category ID.
The HERE places category system provides three levels of granularity:</li>
</ul>
<ol>
<li>Level 1 represents high level groupings, such as "Eat and drink".
Their IDs take the form "xxx", for example "100".</li>
<li>Level 2 represents logical sub-groups or domains, such as "Eat and Drink / Restaurant".
Their IDs take the form "xxx-xxxx", for example "100-1000".</li>
<li>Level 3 provides the greatest level of granularity about place categorization,
such as "Eat and Drink / Restaurant / Casual Dining".
Their IDs take the form "xxx-xxxx-xxxx", for example "100-1000-0001".
The category ID can be provided as one of the predefined values, such as
<a href="../../search/PlaceCategory/eatAndDrinkRestaurant.html">/sdk-for-flutter-explore-search-placecategory-eatanddrinkrestaurant</a> or as a literal string that matches
one of the category IDs defined by the HERE Search service.
Only level 1 and 2 category IDs are predefined.
The complete list of supported category IDs, including level 3, can be found online:
<a href="https://www.here.com/docs/bundle/geocoding-and-search-api-v7-api-reference/page/index.html">https://www.here.com/docs/bundle/geocoding-and-search-api-v7-api-reference/page/index.html</a>.</li>
</ol>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory PlaceCategory(String id) =&gt; $prototype.make(id);</code></pre>
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
<li><a href="../../search/search-library.html">/sdk-for-flutter-explore-search-search-library</a></li>
<li><a href="../../search/PlaceCategory-class.html">/sdk-for-flutter-explore-search-placecategory-class</a></li>
<li class="self-crumb">PlaceCategory factory constructor</li>
</ol>
<h5>PlaceCategory class</h5>
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
