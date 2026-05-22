---
title: "Untitled"
slug: "sdk-for-flutter-explore-mapview-datasource-tileurlproviderfactory-fromxyzurltemplate"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- fromXyzUrlTemplate.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-datasource-mapview-datasource-library</li>
<li>/sdk-for-flutter-explore-mapview-datasource-tileurlproviderfactory-class</li>
<li class="self-crumb">fromXyzUrlTemplate static method</li>
</ol>
<div class="self-name">fromXyzUrlTemplate</div>
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
<div class="main-content" data-above-sidebar="mapview.datasource/TileUrlProviderFactory-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>fromXyzUrlTemplate static method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-explore-mapview-datasource-tileurlprovidercallback?
fromXyzUrlTemplate(<wbr/><ol class="parameter-list single-line"> <li>String urlTemplate</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Creates /sdk-for-flutter-explore-mapview-datasource-tileurlprovidercallback for the given URL template.</p>
<p>A url template should look like this 'https://TestRasterTileService.com/{z}/{x}/{y}/'
here the z parameter is the storage level, x and y define the location of the tile.
The valid range for X and Y is from 0 to 2^level − 1.</p>
<ul>
<li><code>urlTemplate</code> The url template</li>
</ul>
<p>Returns /sdk-for-flutter-explore-mapview-datasource-tileurlprovidercallback. <code>null</code> if the provided template is not valid xyz url type.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static TileUrlProviderCallback? fromXyzUrlTemplate(String urlTemplate) =&gt; $prototype.fromXyzUrlTemplate(urlTemplate);</code></pre>
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
<li>/sdk-for-flutter-explore-mapview-datasource-mapview-datasource-library</li>
<li>/sdk-for-flutter-explore-mapview-datasource-tileurlproviderfactory-class</li>
<li class="self-crumb">fromXyzUrlTemplate static method</li>
</ol>
<h5>TileUrlProviderFactory class</h5>
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
