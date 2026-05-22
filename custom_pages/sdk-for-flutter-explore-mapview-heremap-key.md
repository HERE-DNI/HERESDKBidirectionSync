---
title: "Untitled"
slug: "sdk-for-flutter-explore-mapview-heremap-key"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- key.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-heremap-class</li>
<li class="self-crumb">key property</li>
</ol>
<div class="self-name">key</div>
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
<div class="main-content" data-above-sidebar="mapview/HereMap-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>key property</h1></div>
<section class="multi-line-signature">
        
        Key?
        key
<div class="features">finalinherited</div>
</section>
<section class="desc markdown">
<p>Controls how one widget replaces another widget in the tree.</p>
<p>If the <code>runtimeType</code> and <code>key</code> properties of the two widgets are
<code>operator==</code>, respectively, then the new widget replaces the old widget by
updating the underlying element (i.e., by calling <code>Element.update</code> with the
new widget). Otherwise, the old element is removed from the tree, the new
widget is inflated into an element, and the new element is inserted into the
tree.</p>
<p>In addition, using a <code>GlobalKey</code> as the widget's <code>key</code> allows the element
to be moved around the tree (changing parent) without losing state. When a
new widget is found (its key and type do not match a previous widget in
the same location), but there was a widget with that same global key
elsewhere in the tree in the previous frame, then that widget's element is
moved to the new location.</p>
<p>Generally, a widget that is the only child of another widget does not need
an explicit key.</p>
<p>See also:</p>
<ul>
<li>The discussions at <code>Key</code> and <code>GlobalKey</code>.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">final Key? key;</code></pre>
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
<li>/sdk-for-flutter-explore-mapview-heremap-class</li>
<li class="self-crumb">key property</li>
</ol>
<h5>HereMap class</h5>
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
