---
title: "Untitled"
slug: "sdk-for-flutter-explore-mapview-mapscene-disablefeatures"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- disableFeatures.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li>/sdk-for-flutter-explore-mapview-mapscene-class</li>
<li class="self-crumb">disableFeatures abstract method</li>
</ol>
<div class="self-name">disableFeatures</div>
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
<div class="main-content" data-above-sidebar="mapview/MapScene-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>disableFeatures abstract method</h1></div>
<section class="multi-line-signature">
void
disableFeatures(<wbr/><ol class="parameter-list single-line"> <li>List&lt;<wbr/>String&gt; features</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Disables specified map features.</p>
<p>Those will become inactive
after next map redraw, meaning that /sdk-for-flutter-explore-mapview-mapscene-getactivefeatures will
return updated list of active features only after the redraw happens.</p>
<p>Does not affect features that were not specified.
Unsupported features are ignored.</p>
<p>May cause the current map configuration to be reloaded.</p>
<p>See /sdk-for-flutter-explore-mapview-mapfeatures-class for feature names.</p>
<ul>
<li><code>features</code> The names of features to disable (see /sdk-for-flutter-explore-mapview-mapfeatures-class).</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void disableFeatures(List&lt;String&gt; features);</code></pre>
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
<li>/sdk-for-flutter-explore-mapview-mapscene-class</li>
<li class="self-crumb">disableFeatures abstract method</li>
</ol>
<h5>MapScene class</h5>
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
