---
title: "Toll constructor"
slug: "sdk-for-flutter-navigate-routing-toll-toll"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- Toll.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li>/sdk-for-flutter-navigate-routing-toll-class</li>
<li class="self-crumb">Toll constructor</li>
</ol>
<div class="self-name">Toll</div>
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
<div class="main-content" data-above-sidebar="routing/Toll-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>Toll constructor</h1></div>
<section class="multi-line-signature">
Toll(<wbr/><ol class="parameter-list single-line"> <li>String countryCode, </li>
<li>List&lt;<wbr/>String&gt; tollSystems, </li>
<li>List&lt;<wbr/>/sdk-for-flutter-navigate-routing-tollfare-class&gt; fares</li>
</ol>)
    </section>
<section class="desc markdown">
<p>Creates a new instance.</p>
<ul>
<li><code>countryCode</code> The country in which the toll is to be paid in ISO-3166-1 alpha-3 format, e.g. "USA".</li>
<li><code>tollSystems</code> Names of the multiple toll systems which are associated with the toll, e.g. ["ATLANDES“, "ASF", "COFIROUTE"].
When the toll information covers several toll roads and the toll system of the each road is different,
all toll system names are listed here and the last element will be one of the exit toll booth.</li>
<li><code>fares</code> The list of toll fares possible for the toll which may depend on time of day, payment method, vehicle
characteristics, etc. If there are multiple toll fares that the router cannot disambiguate, then the
list will contain more than one toll fare. Note that this list contains at least one element, i.e. it
is never empty.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">Toll(this.countryCode, this.tollSystems, this.fares);</code></pre>
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
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li>/sdk-for-flutter-navigate-routing-toll-class</li>
<li class="self-crumb">Toll constructor</li>
</ol>
<h5>Toll class</h5>
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
