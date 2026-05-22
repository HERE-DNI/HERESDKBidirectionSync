---
title: "Untitled"
slug: "sdk-for-flutter-navigate-navigation-visualnavigator-customlocationindicator"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- customLocationIndicator.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-visualnavigator-class</li>
<li class="self-crumb">customLocationIndicator property</li>
</ol>
<div class="self-name">customLocationIndicator</div>
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
<div class="main-content" data-above-sidebar="navigation/VisualNavigator-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>customLocationIndicator property</h1></div>
<section id="getter">
<section class="multi-line-signature">
/sdk-for-flutter-navigate-mapview-locationindicator-class?
customLocationIndicator
</section>
<section class="desc markdown">
<p>Custom location indicator /sdk-for-flutter-navigate-mapview-locationindicator-class which /sdk-for-flutter-navigate-navigation-visualnavigator-class uses instead of the default.
If set, the user is responsible for adding and removing the object to/from the mapview.
It is important to stop sending location updates to the provided /sdk-for-flutter-navigate-mapview-locationindicator-class, since
/sdk-for-flutter-navigate-navigation-visualnavigator-class will control its position when rendering is active, i.e., between startRendering() and
stopRendering() calls. By default this property is <code>null</code>,
which means the default indicator is used, and /sdk-for-flutter-navigate-navigation-visualnavigator-class automatically adds and removes it to/from
the mapview upon startRendering() and stopRendering() calls.
Gets the currently set <code>LocationIndicator</code>.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">LocationIndicator? get customLocationIndicator;</code></pre>
</section>
</section>
<section id="setter">
<section class="multi-line-signature">
void
customLocationIndicator=(<wbr/>/sdk-for-flutter-navigate-mapview-locationindicator-class? value)
</section>
<section class="desc markdown">
<p>Custom location indicator /sdk-for-flutter-navigate-mapview-locationindicator-class which /sdk-for-flutter-navigate-navigation-visualnavigator-class uses instead of the default.
If set, the user is responsible for adding and removing the object to/from the mapview.
It is important to stop sending location updates to the provided /sdk-for-flutter-navigate-mapview-locationindicator-class, since
/sdk-for-flutter-navigate-navigation-visualnavigator-class will control its position when rendering is active, i.e., between startRendering() and
stopRendering() calls. By default this property is <code>null</code>,
which means the default indicator is used, and /sdk-for-flutter-navigate-navigation-visualnavigator-class automatically adds and removes it to/from
the mapview upon startRendering() and stopRendering() calls.
Sets a custom /sdk-for-flutter-navigate-mapview-locationindicator-class, so that /sdk-for-flutter-navigate-navigation-visualnavigator-class uses the provided one instead
of the default.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set customLocationIndicator(LocationIndicator? value);</code></pre>
</section>
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
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-visualnavigator-class</li>
<li class="self-crumb">customLocationIndicator property</li>
</ol>
<h5>VisualNavigator class</h5>
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
