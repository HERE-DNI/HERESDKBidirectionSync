---
title: "onDrawingSelected abstract method"
slug: "sdk-for-flutter-navigate-venue-control-venuedrawingselectionlistener-ondrawingselected"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- onDrawingSelected.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-venue-control-venue-control-library</li>
<li>/sdk-for-flutter-navigate-venue-control-venuedrawingselectionlistener-class</li>
<li class="self-crumb">onDrawingSelected abstract method</li>
</ol>
<div class="self-name">onDrawingSelected</div>
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
<div class="main-content" data-above-sidebar="venue.control/VenueDrawingSelectionListener-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>onDrawingSelected abstract method</h1></div>
<section class="multi-line-signature">
void
onDrawingSelected(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-venue-control-venue-class venue, </li>
<li>/sdk-for-flutter-navigate-venue-data-venuedrawing-class? deselectedDrawing, </li>
<li>/sdk-for-flutter-navigate-venue-data-venuedrawing-class selectedDrawing</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Indicates that new /sdk-for-flutter-navigate-venue-data-venuedrawing-class has been selected.</p>
<ul>
<li>
<p><code>venue</code> The /sdk-for-flutter-navigate-venue-control-venue-class where a selected drawing was changed.</p>
</li>
<li>
<p><code>deselectedDrawing</code> The previously selected /sdk-for-flutter-navigate-venue-data-venuedrawing-class object or <code>null</code>
if there was no selected drawing before.</p>
</li>
<li>
<p><code>selectedDrawing</code> The new selected /sdk-for-flutter-navigate-venue-data-venuedrawing-class object.</p>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void onDrawingSelected(Venue venue, VenueDrawing? deselectedDrawing, VenueDrawing selectedDrawing);</code></pre>
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
<li>/sdk-for-flutter-navigate-venue-control-venue-control-library</li>
<li>/sdk-for-flutter-navigate-venue-control-venuedrawingselectionlistener-class</li>
<li class="self-crumb">onDrawingSelected abstract method</li>
</ol>
<h5>VenueDrawingSelectionListener class</h5>
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
