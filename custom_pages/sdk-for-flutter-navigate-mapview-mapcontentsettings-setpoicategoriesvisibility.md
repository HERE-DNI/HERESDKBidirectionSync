---
title: "setPoiCategoriesVisibility static method"
slug: "sdk-for-flutter-navigate-mapview-mapcontentsettings-setpoicategoriesvisibility"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setPoiCategoriesVisibility.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-mapcontentsettings-class</li>
<li class="self-crumb">setPoiCategoriesVisibility static method</li>
</ol>
<div class="self-name">setPoiCategoriesVisibility</div>
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
<div class="main-content" data-above-sidebar="mapview/MapContentSettings-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>setPoiCategoriesVisibility static method</h1></div>
<section class="multi-line-signature">
void
setPoiCategoriesVisibility(<wbr/><ol class="parameter-list single-line"> <li>List&lt;<wbr/>String&gt; categoryIds, </li>
<li>/sdk-for-flutter-navigate-mapview-visibilitystate visibility</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Sets visibility for embedded carto POI categories (points of interest that are visible on the
map, by default).</p>
<p>For HERE standard map schemes all available POI categories are visible by
default for each selected map scheme. Note that not all POI categories are available for
all map schemes.</p>
<p>Based on the given list of categories the number of shown carto POIs can be reduced.
To find all possible POI category strings look into <code>here.sdk.search.PlaceCategory</code>.
Note that it is enough to hide a main category like "100" (eat-and-drink) to also affect
sub categories such as "100-1000" (eat-and-drink-restaurant)
and "100-1100" (eat-and-drink-coffee-tea). To enable a sub category, also the related
main categories need have the <code>VISIBLE</code> state.</p>
<p>The POI visibility is a property of the map data itself. Once set it will be applied to
all HERE standard map schemes and the selected categories will remain even when
switching a map scheme.</p>
<ul>
<li>
<p><code>categoryIds</code> A list of POI categories that a visibility state is set for.</p>
</li>
<li>
<p><code>visibility</code> A selected visibility for specified POI categories.</p>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static void setPoiCategoriesVisibility(List&lt;String&gt; categoryIds, VisibilityState visibility) =&gt; $prototype.setPoiCategoriesVisibility(categoryIds, visibility);</code></pre>
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
<li>/sdk-for-flutter-navigate-mapview-mapcontentsettings-class</li>
<li class="self-crumb">setPoiCategoriesVisibility static method</li>
</ol>
<h5>MapContentSettings class</h5>
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
